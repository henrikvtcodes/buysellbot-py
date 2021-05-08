import ryaml as r


def buyOrder(coin, price, amount):
    bc=r.baseConfig()
    notif=bc.get('notifications')
    if notif.get('buy') == True:
        print('The Bot is buying',amount,'of',coin,'at',price)
    
def sellOrder(coin, price, amount):
    bc=r.baseConfig()
    notif=bc.get('notifications')
    if notif.get('sell') == True:
        print('The Bot is selling',amount,'of',coin,'at',str(price)+'.','Your profit is')