## 08/12
Today’s learnings — short summary
Capacity planning: In design, estimate resource footprints; in ops, monitor usage to predict issues early.

Performance goals: Make “fast” objective—set SLOs (e.g., avg latency or p95/p99). Core metrics: latency, utilization, saturation.

Latency: Time to complete any operation (req, query, I/O, etc.); analyze full distributions, not just averages—BPF-based tools make this practical.

Observability: Understand systems via metrics (counters), profiling (sampling), and tracing (event events/flows). Benchmarks are separate.

Instrumentation:

Static (kernel tracepoints, user-space USDT).

Dynamic (modify running code to insert probes)—enables custom, on-the-fly telemetry.

Methodologies: USE, RED, workload characterization, latency analysis, Method R, drill-down, baseline stats, queueing theory, static tuning. Avoid anti-methods (streetlight, random change, blame).

Workload analysis: Characterize apps by latency, request rate/throughput, completions; contrast workload vs. resource perspectives.

I/O concepts:

Scheduling orders requests to reduce wait/turnaround.

Buffering (speed mismatch, size adaptation, copy semantics).

Caching (fast copies of hot data).

Spooling (serialize device use, e.g., printers).

Error handling & protection to contain faults and prevent misuse.

OS fundamentals: Processes & PCBs (process table); scheduling (preemptive vs non-preemptive); context switches (interrupts, multitasking, user/kernel); threads (stack, registers, program counter).

Practice mindset: Know time scales (ns→s), weigh tuning trade-offs and stop when benefits taper, quantify gains, baseline & monitor continuously, and plan capacity proactively.

