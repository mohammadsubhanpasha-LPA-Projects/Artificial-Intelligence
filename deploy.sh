#!/bin/bash
echo "⚔️ Pulling Excalibur..."
echo "👑 King Arthur awakening..."
python3 10-quantum/qiskit/cost_qaoa.py
python3 5-security/pqc_vault.py
echo "🏰 12 Knights of Round Table assembling..."
kubectl apply -f 5-security/knights-policies/
kubectl apply -f 4-k8s/manifests/
echo "✅ EXCALIBUR SOVEREIGN PLANE DEPLOYED - ONE SWORD RULES ALL CLOUDS - GOVERNED BY 12 KNIGHTS - 4050.1.0"
