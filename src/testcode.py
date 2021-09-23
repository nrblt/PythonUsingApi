
from pycoingecko import CoinGeckoAPI


def f(n):
        cg = CoinGeckoAPI()#connecting to API

        r=cg.get_coins_markets(vs_currency='usd')#getting information with API
        #n =int(input()) #number of currencies

        ans=[]
        i=int(0)
        for x in r:
                i=i+1
                ans.append(x['name'])
                if i==n:
                        break
        return ans
                

 


print(f(6))
print(f(8))
