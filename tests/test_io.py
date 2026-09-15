from src.utils.io import atomic_write


def test_atomic_write_retries_transient_windows_lock(tmp_path, monkeypatch):
    import os
    real_replace = os.replace
    calls = []
    def transient(source, destination):
        calls.append(1)
        if len(calls) == 1:
            raise PermissionError("Simulated file reader")
        real_replace(source, destination)
    monkeypatch.setattr("src.utils.io.os.replace", transient)
    monkeypatch.setattr("src.utils.io.time.sleep", lambda _: None)
    path = tmp_path / "progress.json"
    atomic_write(path, "new content")
    assert path.read_text() == "new content" and len(calls) == 2
