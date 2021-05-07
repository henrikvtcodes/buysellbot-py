from envs import env
import json

from coinbase.wallet.client import Client

global client

try:
    key = env('COINBASE_KEY')
    secret = env('COINBASE_SECRET')
except:
    print("API Key Not Found.")
else:
    client = Client(key, secret)

def getCurrentUserData(returnType):
    userObj = json.loads(client.get_current_user())
    print(userObj)

# def buy(coin, amount):
    