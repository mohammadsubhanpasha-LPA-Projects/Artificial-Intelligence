#!/bin/bash
# Running Litmus experiments
kubectl apply -f pod-delete.yaml
kubectl apply -f node-cpu-hog.yaml
kubectl apply -f network-latency.yaml
