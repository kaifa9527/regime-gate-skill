import json, pathlib, sys
sys.path.append(str(pathlib.Path(__file__).parent.parent/'patches'))
from onchain_agent import OnChainAgent
from derivatives_agent import DerivativesAgent
def main():
    o=OnChainAgent().evaluate(); d=DerivativesAgent().evaluate();
    regime={'regime':o['regime'],'bias':o['bias'],'allowed':'long_only' if o['score']>0 else 'short_only' if o['score']<0 else 'both','close_mode':'SOFT_CLOSE','ttl_hours':26,'price':o['price'],'components':{'onchain':o,'derivatives':d}}
    pathlib.Path('regime.json').write_text(json.dumps(regime, indent=2))
    print(json.dumps(regime, indent=2))
if __name__=='__main__':
    main()
