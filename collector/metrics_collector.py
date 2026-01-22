import psutil
import time


class MetricsCollector:
    def __init__(self, pid):
        self.pid = pid
        self.process = psutil.Process(pid)
        self.snapshots = []

    def collect_once(self):
        cpu = self.process.cpu_percent(interval=1)
        rss = self.process.memory_info().rss / (1024*1024)
        threads = self.process.num_threads()
        snapshot = {
            "timestamp": time.time(),
            "pid": self.pid,
            "cpu": cpu,
            "ram": rss,
            "threads": threads
        }
        self.snapshots.append(snapshot)
        return snapshot

    def run(self):
        while True:
            snap = self.collect_once()
            print(snap)


current_proc = psutil.Process()
current_pid = current_proc.pid
print(f"Starting metrics collecting for PID: {current_pid}")

collector = MetricsCollector(current_pid)
collector.run()

