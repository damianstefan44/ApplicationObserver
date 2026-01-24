class RulesEngine:
    """
    Rules engine for evaluating metrics against thresholds.
    """

    def __init__(self, memory_threshold: float = 50.0, cpu_threshold: float = 80.0):
        self.memory_threshold = memory_threshold
        self.cpu_threshold = cpu_threshold

    def is_memory_growth_excessive(self, growth: float) -> bool:
        return growth > self.memory_threshold

    def is_cpu_overloaded(self, avg_cpu: float) -> bool:
        return avg_cpu > self.cpu_threshold