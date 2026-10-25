#!/bin/bash
set -e
cd "$(dirname "$0")/.."
echo "[RegimeGate] Generating regime.json..."
python3 gate/runner.py
echo "[RegimeGate] Starting freqtrade dry-run..."
echo "Make sure freqtrade is installed: git clone https://github.com/freqtrade/freqtrade.git"
echo "docker-compose run --rm freqtrade trade --config configs/dry_run_config.json --strategy RegimeGateStrategy --dry-run"
