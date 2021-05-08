import cb_trader as cb
import ryaml as r

coinConf = ryaml.coinConf()

def main(cryp,int(cryp_id)):
    coin = coinConf.get(cryp_id) # Initialize all the variables
    cid = coin.get('coin')
    buyAt = coin.get('buyAt')
    buyAmt = coin.get('buyAmt')
    sellAtHigh = coin.get('sellAtHigh')
    sellAmtHigh = coin.get('sellAmtHigh')
    sellAtLow = coin.get('sellAtLow')
    sellAmtLow = coin.get('sellAmtLow')
    
    