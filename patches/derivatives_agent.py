
import requests
class DerivativesAgent:
    def evaluate(self):
        try:
            r=requests.get('https://fapi.binance.com/fapi/v1/premiumIndex?symbol=BTCUSDT', timeout=5)
            f=float(r.json().get('lastFundingRate',0))
        except:
            f=0.0001
        return {'funding_rate':f,'score':-1 if f>0.0005 else 1 if f<-0.0002 else 0}
