import psutil


class ProcessDiscovery:
    """
    Process discovery module.
    Holds configuration for the target process and returns its PID.
    """

    def find_target_pid(self) -> int:
        return psutil.Process().pid