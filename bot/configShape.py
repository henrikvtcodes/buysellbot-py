# THIS SCRIPT IS NOT USED IN OPERATION OF THIS PROGRAM

{
'baseConfig': 
    [
    {'currency': 'USD'}, 
    {'notifications': 
        [
        {'checking': True}, 
        {'buy': True}, 
        {'sell': True}, 
        {'error': True}, 
        {'misc': True}
        ]
        }, 
    {'maxHold': 100}, 
    {'maxBuy': 20}, 
    {'maxSell': None}
    ],
     
'coins': 
    {'example': 
        [
        {'announceName': 'Bitcoin'}, 
        {'coin': 'BTC'}, 
        {'maxHold': 69}, 
        {'buy': True}, 
        {'buyAt': 42000}, 
        {'buyAmt': 10}, 
        {'sell': True}, 
        {'sellAtHigh': 69000}, 
        {'sellAmtHigh': '15%'}, 
        {'sellAtLow': 40000}, 
        {'sellAmtLow': '100%'}
        ]
    }
}


dict_items([
    ('baseConfig', [
      {'currency': 'USD'}, 
      {'notifications': [
          {'checking': True}, 
          {'buy': True}, 
          {'sell': True}, 
          {'error': True}, 
          {'misc': True}
          ]
       }, 
      {'maxHold': 100}, 
      {'maxBuy': 20}, 
      {'maxSell': None}
      ]
     )
    ]
)

dict_items([('coins', {'example': [{'announceName': 'Bitcoin'}, {'coin': 'BTC'}, {'maxHold': 69}, {'buy': True}, {'buyAt': 42000}, {'buyAmt': 10}, {'sell': True}, {'sellAtHigh': 69000}, {'sellAmtHigh': '15%'}, {'sellAtLow': 40000}, {'sellAmtLow': '100%'}]})])