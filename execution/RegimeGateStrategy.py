
from freqtrade.strategy import IStrategy
from pathlib import Path
import json, datetime

class RegimeGateStrategy(IStrategy):
    """
    GPLv3 - RegimeGate single-brain gate
    Reads ../../regime.json or ./regime.json with TTL 26h
    """
    timeframe = "1h"
    can_short = True

    def load_regime(self):
        for p in [Path("regime.json"), Path("../regime.json"), Path("../../regime.json"), Path.home()/ "Desktop"/"regime-gate-skill"/"regime.json"]:
            if p.exists():
                try:
                    data = json.loads(p.read_text())
                    ts = datetime.datetime.fromisoformat(data.get("timestamp","1970-01-01"))
                    age_h = (datetime.datetime.utcnow() - ts).total_seconds()/3600
                    expired = age_h > data.get("ttl_hours", 26)
                    data["expired"] = expired
                    data["age_hours"] = age_h
                    return data
                except Exception as e:
                    continue
        return {"bias":"neutral","allowed":"none","close_mode":"HARD_CLOSE","expired":True,"regime":"unknown"}

    def populate_entry_trend(self, dataframe, metadata):
        regime = self.load_regime()
        # Direction lock - core of RegimeGate
        if regime.get("expired"):
            # TTL expired -> HARD_CLOSE no new entries
            dataframe["enter_long"] = 0
            dataframe["enter_short"] = 0
            return dataframe

        allowed = regime.get("allowed","both")
        if allowed == "long_only":
            dataframe.loc[:, "enter_short"] = 0
        elif allowed == "short_only":
            dataframe.loc[:, "enter_long"] = 0
        elif allowed == "none":
            dataframe["enter_long"] = 0
            dataframe["enter_short"] = 0
        # both -> keep FreqAI signals
        return dataframe

    def populate_exit_trend(self, dataframe, metadata):
        regime = self.load_regime()
        close_mode = regime.get("close_mode","SOFT_CLOSE")
        if regime.get("expired") and close_mode == "HARD_CLOSE":
            # Force close all
            dataframe["exit_long"] = 1
            dataframe["exit_short"] = 1
        elif regime.get("allowed") == "none" and close_mode == "SOFT_CLOSE":
            # SOFT_CLOSE: don't open new, but let existing close by FreqAI logic
            pass
        return dataframe
