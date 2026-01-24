from dataclasses import dataclass

@dataclass
class MetricSnapshot:
    timestamp: float
    pid: int
    cpu: float
    memory_mb: float
    threads: int

    def to_dict(self) -> dict[str, float | int]:
        return {
            "timestamp": self.timestamp,
            "pid": self.pid,
            "cpu": self.cpu,
            "memory_mb": self.memory_mb,
            "threads": self.threads,
        }

    @staticmethod
    def from_dict(data: dict[str, float | int]) -> "MetricSnapshot":
        return MetricSnapshot(**data)