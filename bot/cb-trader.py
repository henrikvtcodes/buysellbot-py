from envs import env

from coinbase.wallet.client import Client

global client

try:
    key = env('COINBASE_KEY')
    secret = env('COINBASE_SECRET')
except:
    print("API Key Not Found.")
else:
    client = Client(key, secret)

