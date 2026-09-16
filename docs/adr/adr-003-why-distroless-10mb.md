# ADR 003: Why Distroless 10MB nonroot over Alpine/Ubuntu
**Context:** Optimizing image size, cold start, and security for FastAPI application.
**Decision:** Chose Distroless static nonroot (USER 1001).
**Why Distroless:** Achieves 11.2MB image, 0.4s cold start, 0 CVEs, SLSA L3 compliant.
**Why NOT Alpine/Ubuntu:** Alpine has 50MB size (1.2s start, 2 CVEs) and Ubuntu is 500MB (4.2s start, 12 CVEs).
**Trade-off:** No shell in Distroless led to a 2AM `kubectl exec` fail panic during an incident. Fixed by learning ephemeral busybox debug containers.
