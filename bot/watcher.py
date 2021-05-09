import cb_trader as cb
import ryaml as r

coinConf = ryaml.coinConf()

def main(cryp, crypid):
    coin = coinConf.get(crypid) # Initialize all the variables
    cid = coin.get('coin')
    buyAt = coin.get('buyAt')
    buyAmt = coin.get('buyAmt')
    sellAtHigh = coin.get('sellAtHigh')
    sellAmtHigh = coin.get('sellAmtHigh')
    sellAtLow = coin.get('sellAtLow')
    sellAmtLow = coin.get('sellAmtLow')
    
    print(coin)
    print(cid)
    print(buyAt)
    print(buyAmt)
    print(sellAtHigh)
    print(sellAmtHigh)
    print(sellAtLow)
    print(sellAmtLow)
    