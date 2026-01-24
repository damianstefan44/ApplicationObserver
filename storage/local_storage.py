import json
from pathlib import Path

class JsonlStorage:
    """
    Provides simple append-only storage of snapshots in JSON Lines (JSONL) format.
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, snapshot: dict):
        with self.file_path.open("a") as f:
            f.write(json.dumps(snapshot) + "\n")

    def read_last_n(self, n: int) -> list[dict]:
        if not self.file_path.exists():
            return []

        with self.file_path.open("r") as f:
            lines = f.readlines()

        return [json.loads(line) for line in lines[-n:]]