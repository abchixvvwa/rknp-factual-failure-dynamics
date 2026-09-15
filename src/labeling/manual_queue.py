import csv
import io

from src.utils.io import atomic_write


def write_rows(path, rows, columns):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=columns, extrasaction="ignore", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    atomic_write(path, stream.getvalue())


def manual_queue(path, rows):
    columns = ["request_id", "response_sha256", "fact_id", "language", "model_id", "question",
               "canonical_answer", "acceptable_aliases", "target_response", "auto_reason",
               "review_label", "review_notes", "reviewer"]
    write_rows(path, [dict(row, review_label="") for row in rows if row["label_status"] == "unresolved"], columns)
