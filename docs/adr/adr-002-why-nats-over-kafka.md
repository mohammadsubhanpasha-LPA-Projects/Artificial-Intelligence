# ADR 002: Why NATS JetStream over Kafka
**Context:** Need ultra-fast event streaming for deploy pipeline coordination.
**Decision:** Selected NATS JetStream over Apache Kafka.
**Why NATS:** Lightweight (5MB), fast (1ms latency), and quick to set up (60s).
**Why NOT Kafka:** Too heavy (500MB), higher latency (20ms), and complex setup with Zookeeper (2hrs).
**Trade-off:** NATS has at-least-once delivery, leading to duplicate payment double processing initially. Fixed by adding 50 lines of idempotency key logic.
