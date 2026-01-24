import time
from discovery.process_discovery import ProcessDiscovery
from collector.metrics_collector import MetricsCollector
from analyzer.trend_analyzer import TrendAnalyzer
from rules.rule_engine import RulesEngine
from storage.local_storage import JsonlStorage

class Orchestrator:
    """
    Orchestrates the Application Observer pipeline:
    - discovers PID
    - collects metrics
    - stores snapshots
    - analyzes trends
    - applies rules
    """

    def __init__(
        self,
        interval: int = 5, # seconds between snapshots
        window_size: int = 60, # number of snapshots for trend analysis
        memory_threshold: float = 50.0, # maximum allowed increase in memory over the analysis window in MB
        cpu_threshold: float = 80.0,  # CPU usage percent
        storage_path: str = "snapshots.jsonl"
    ):
        self.interval = interval
        self.discovery = ProcessDiscovery()
        self.storage = JsonlStorage(file_path=storage_path)
        self.analyzer = TrendAnalyzer(window_size=window_size)
        self.rules = RulesEngine(
            memory_threshold=memory_threshold,
            cpu_threshold=cpu_threshold
        )

    def run(self):
        pid = self.discovery.find_target_pid()
        print(f"Discovered PID: {pid}")

        collector = MetricsCollector(pid)

        while True:
            snapshot = collector.collect_once()
            self.storage.append(snapshot)
            snapshots = self.storage.read_last_n(self.analyzer.window_size)

            mem_growth = self.analyzer.get_memory_growth(snapshots)
            avg_cpu = self.analyzer.get_average_cpu(snapshots)

            if self.rules.is_memory_growth_excessive(mem_growth):
                print(f"Memory growth too high: {mem_growth:.2f} MB")

            if self.rules.is_cpu_overloaded(avg_cpu):
                print(f"CPU overloaded: {avg_cpu:.2f}%")

            time.sleep(self.interval)