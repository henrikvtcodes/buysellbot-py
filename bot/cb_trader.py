from envs import env

from coinbase.wallet.client import Client

import ryaml as r

baseConf = r.baseConfig()
coinConf = r.coinConfig()
cur = baseConf[0]
fiat = cur.get('currency')

try:
    key = env('COINBASE_KEY')
    secret = env('COINBASE_SECRET')
except:
    print("API Key Not Found.")
else:
    try:
        client = Client(key, secret)
    except:
        print('API Key Error')
        print('Invalid Key:',key)
        print('Invalid Secret:',secret)

def getCurrentUserData(returnType): #get the properties of the user from their API Key
    userObj = json.loads(client.get_current_user())

def getPrice(crypto):
    priceObj = (str(crypto)+'-'+str(fiat))
    
    try:
        spotPrice = json.loads(client.get_spot_price(currency_pair = priceObj))
    except:
        spotPrice = 'OP_FAILED'
    
    try:
        buyPrice = json.loads(client.get_buy_price(currency_pair = priceObj))
    except:
        spotPrice = 'OP_FAILED'
    
    try:
        sellPrice = json.loads(client.get_sell_price(currency_pair = priceObj))
    except:
        spotPrice = 'OP_FAILED'
    
    priceList = list()
    priceList.append(spotPrice)
    priceList.append(buyPrice)
    priceList.append(sellPrice)
    return priceList

# def validateOrder(isBuy, orderValue):#make sure that an buy or sell order is within parameters
    
    
# def buy(coin, amount):
