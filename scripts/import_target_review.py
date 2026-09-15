"""Import one numbered target-review submission after verifying its ledger hashes."""
import argparse
import csv
import json
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.labeling.manual_queue import write_rows
from src.utils.hashing import file_hash, stable_hash
from src.utils.io import atomic_write, project_path, write_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", required=True)
    parser.add_argument("--batch", type=int, required=True)
    args = parser.parse_args()
    folder = project_path(args.folder)
    review_path = folder / f"batch_{args.batch:02}_user_review.json"
    review = json.loads(review_path.read_text(encoding="utf-8"))
    manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    with (folder / "queue.csv").open(encoding="utf-8", newline="") as stream:
        queue = list(csv.DictReader(stream))
    assert stable_hash([(row["request_id"], row["response_sha256"]) for row in queue]) == manifest["queue_sha256"]
    numbers = review["correct_numbers"] + review["incorrect_numbers"] + review["invalid_numbers"]
    assert len(numbers) == len(set(numbers)) and numbers
    labels_path = project_path("data/labels/reviewed_labels.csv")
    with labels_path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        fields, existing = reader.fieldnames, list(reader)
    lookup = {row["request_id"]: row for row in existing}
    assert len(lookup) == len(existing)
    db = sqlite3.connect(f"file:{project_path('artifacts/groq/private/requests.sqlite3')}?mode=ro", uri=True)
    added, invalid = [], []
    notes = review.get("user_notes", {})
    for number in sorted(numbers):
        row = queue[number - 1]
        item = manifest["numbered_requests"][number - 1]
        assert item["number"] == number and item["request_id"] == row["request_id"] and item["response_sha256"] == row["response_sha256"]
        stored = db.execute("SELECT record FROM attempts WHERE request_key=? AND state='success'", (row["request_id"],)).fetchone()
        assert stored and json.loads(stored[0])["response_sha256"] == row["response_sha256"]
        note = f"User review; {folder.name} batch {args.batch} item {number}; entire response evaluated. " + (notes.get(str(number), "") if isinstance(notes, dict) else str(notes))
        if number in review["invalid_numbers"]:
            assert not json.loads(stored[0])["valid_response"]
            invalid.append(dict(number=number, request_id=row["request_id"], response_sha256=row["response_sha256"], review_label=None,
                                review_status="human_confirmed_invalid", reviewer=review["reviewer"], review_notes=note))
            continue
        label = "1" if number in review["correct_numbers"] else "0"
        if row["request_id"] in lookup:
            old = lookup[row["request_id"]]
            assert old["response_sha256"] == row["response_sha256"] and old["review_label"] == label
        else:
            added.append(dict(row, review_label=label, reviewer=review["reviewer"], review_notes=note))
    backup = folder / f"reviewed_labels_before_batch_{args.batch:02}.csv"
    if not backup.exists():
        atomic_write(backup, labels_path.read_text(encoding="utf-8-sig"))
    write_rows(labels_path, existing + added, fields)
    if invalid:
        write_json(folder / f"batch_{args.batch:02}_invalid_reviews.json", invalid)
    audit = dict(added=len(added), reviewed=len(numbers), correct=len(review["correct_numbers"]),
                 incorrect=len(review["incorrect_numbers"]), invalid=len(invalid), submission_sha256=file_hash(review_path),
                 reviewed_labels_sha256=file_hash(labels_path), numbered_requests=[manifest["numbered_requests"][i - 1] for i in sorted(numbers)])
    write_json(folder / f"batch_{args.batch:02}_import_audit.json", audit)
    print(json.dumps(audit, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
