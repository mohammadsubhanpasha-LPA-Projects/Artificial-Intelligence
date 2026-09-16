Context: DB failover 10s 0 loss need
Decision: Patroni 3 nodes auto failover 10s
Why X: 10s failover 3 nodes 0 loss 99.999%
Why NOT Y: Single DB 45min outage 2AM
Trade-off: Setup 1 day split-brain 3AM fixed etcd quorum 3
