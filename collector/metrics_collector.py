import psutil
import time


class MetricsCollector:
    """
    Collects runtime metrics for a given process identified by its PID.
    """

    def __init__(self, pid: int):
        self.pid = pid
        self.process = psutil.Process(pid)

    def collect_once(self) -> dict:
        return {
            "timestamp": time.time(),
            "pid": self.pid,
            "cpu": self.process.cpu_percent(interval=1),
            "memory_mb": self.process.memory_info().rss / (1024 * 1024),
            "threads": self.process.num_threads(),
        }