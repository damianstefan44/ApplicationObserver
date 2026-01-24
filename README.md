# Application Observer
Application Observer is an observability tool written in Python, designed to monitor running backend applications (e.g. FastAPI) without requiring any modifications to their source code. The project focuses on runtime observation, analysis of application behavior over time, and detection of gradual performance degradation.

# Architecture Overview
Application Observer is designed as a service-centric observability tool. The system is structured around clear architectural boundaries, where each component has a single, well-defined responsibility. The architecture is planned upfront and implemented incrementally, reflecting a real-world engineering workflow rather than a collection of unrelated features.

The observer runs as an independent service that monitors a target application at runtime without requiring any changes to the application’s code. Instead of relying on internal instrumentation, it interacts with the operating system and process-level metrics to understand how the application behaves over time.

At a high level, the target application and the observer remain fully decoupled. The observer is responsible for discovering the process, collecting runtime signals, storing historical data, analyzing trends, and exposing insights through a simple API.

The discovery module is responsible for identifying and validating the process to be monitored. This includes resolving the process identifier using different strategies, such as ports or process names, and verifying that the process is alive and accessible. Isolating this logic prevents environment-specific details from leaking into other parts of the system.

The collector module is responsible for gathering raw runtime metrics from the target process. It operates on a fixed sampling interval and produces factual, uninterpreted data such as CPU usage, memory consumption, and thread count. The collector does not perform any analysis and has no knowledge of how the data will be stored or used later.

Collected metrics are persisted by the storage module. Storage acts as the system’s source of truth and maintains a time-ordered history of observations. In the MVP, this is implemented using an append-only JSON Lines file, allowing the system to reconstruct historical behavior and perform time-based analysis. The storage layer intentionally contains no business logic.

The analyzer module consumes historical metric data and transforms it into higher-level signals. Rather than focusing on individual spikes, the analyzer operates on sliding time windows and detects trends such as gradual memory growth or sustained resource saturation. The output of the analyzer is structured analytical data, not alerts or decisions.

Interpretation of analytical signals is handled by the rules or decision engine. This module translates detected patterns into meaningful conclusions, such as identifying potential memory leaks or CPU saturation scenarios. Separating decision logic from analysis improves clarity and makes the system easier to reason about and extend.

The API module provides a thin interface for exposing observer insights to users or external systems. It allows access to recent metrics, detected anomalies, and summary views of the monitored application’s state. The API layer does not contain core logic and serves purely as an integration surface.

Finally, the orchestrator manages the lifecycle of the system. It coordinates startup sequencing, schedules periodic tasks, and ensures graceful shutdown of all components. The orchestrator connects otherwise independent modules into a cohesive running service.

The project is currently under active development. The architecture is intentionally defined before full implementation, allowing each module to be developed, tested, and extended independently. This approach mirrors how observability and platform tooling is typically built in production environments.
