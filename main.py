from orchestrator.orchestrator import Orchestrator

def main():
    orchestrator = Orchestrator(
        interval=2,
        window_size=10,
        memory_threshold=100.0,
        cpu_threshold=90.0,
        storage_path="snapshots.jsonl"
    )
    orchestrator.run()

if __name__ == "__main__":
    main()