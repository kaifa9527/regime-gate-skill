import json, pathlib
def parse_regime(p='regime.json'):
    return json.loads(pathlib.Path(p).read_text()) if pathlib.Path(p).exists() else {'allowed':'none'}
