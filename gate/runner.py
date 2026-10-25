
import json, datetime, pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parent))
from atomic_writer import atomic_write

def generate_regime():
    # TODO: Replace with TradingAgents daily analysis
    # For now: simple placeholder that you can edit
    # In v0.2.0 this will call OnChainAgent + DerivativesAgent
    return {
        "regime": "bull",
        "bias": "long",
        "allowed": "long_only",
        "max_position": 0.5,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "ttl_hours": 26,
        "close_mode": "SOFT_CLOSE",
        "source": "TradingAgents_daily_placeholder"
    }

def main():
    regime = generate_regime()
    out = pathlib.Path(__file__).parent.parent / "regime.json"
    atomic_write(out, json.dumps(regime, indent=2))
    print(f"[RegimeGate] regime.json written to {out}")
    print(json.dumps(regime, indent=2))

if __name__ == "__main__":
    main()
