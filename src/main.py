from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()#connecting to API

r=cg.get_coins_markets(vs_currency='usd')#getting information with API
n =int(input()) #number of currencies

ans=[]
i=int(0)
for x in r:
	i=i+1
	ans.append(x['name'])
	if i==n:
		break
	
print(ans)
