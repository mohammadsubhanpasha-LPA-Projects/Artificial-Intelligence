# Architecture

## Flow
User -> Istio Ambient -> Multi-Region -> Litmus -> Argo -> 5ms Failover -> 99.999%

## Why Litmus over ChaosMesh
Litmus was chosen over ChaosMesh because it is CNCF backed, has 100+ ready experiments, a 60s setup time, is Go native, and supports K8s 1.28 better.
ChaosMesh only had 50 experiments and complex CRDs. Litmus requires a privileged SA which is a security risk, but we fixed this using 12 OPA policies (took 2 days to debug at 2AM).
