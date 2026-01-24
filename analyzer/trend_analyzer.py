from domain.metric_snapshot import MetricSnapshot

class TrendAnalyzer:
    """
    Simple trend analyzer for resource metrics.
    """

    def __init__(self, window_size: int = 60):
        self.window_size = window_size

    def get_memory_growth(self, snapshots: list[MetricSnapshot | dict]) -> float:
        if not snapshots or len(snapshots) < 2:
            return 0.0

        first = snapshots[0]
        last = snapshots[-1]

        first_mem = first.memory_mb if isinstance(first, MetricSnapshot) else first["memory_mb"]
        last_mem = last.memory_mb if isinstance(last, MetricSnapshot) else last["memory_mb"]

        return last_mem - first_mem

    def get_average_cpu(self, snapshots: list[MetricSnapshot | dict]) -> float:
        if not snapshots:
            return 0.0

        cpu_values = [
            s.cpu if isinstance(s, MetricSnapshot) else s["cpu"]
            for s in snapshots
        ]
        return sum(cpu_values) / len(cpu_values)