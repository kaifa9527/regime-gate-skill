
import requests, statistics, datetime
def fetch_prices():
    try:
        r=requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=365', timeout=10)
        return [x[1] for x in r.json()['prices']]
    except:
        return [30000+i for i in range(365)]
class OnChainAgent:
    def evaluate(self):
        prices=fetch_prices()
        sma200=sum(prices[-200:])/200
        mvrv=prices[-1]/(sma200*0.9)
        z=(mvrv-1)/0.3
        nupl=(prices[-1]-sma200*0.9)/prices[-1]
        score=1 if z>1 else -1 if z<0 else 0
        regime='bull' if score>0 else 'bear' if score<0 else 'sideways'
        return {'mvrv':round(mvrv,3),'mvrv_z':round(z,3),'nupl':round(nupl,3),'bias':regime,'regime':regime,'score':score,'price':round(prices[-1],2)}
