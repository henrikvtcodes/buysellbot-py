# This script simplifies the reading of yaml files

import yaml

def openYaml(yml='config.yaml'):
    f = open(yml, 'r')
    config = yaml.load_all(f, Loader=yaml.Loader)
    return config

global baseConfig
global coin
baseConfig = 'Empty'
coins = 'Empty'

config = openYaml()
for doc in config:
    print()
    print(doc.items())
    # baseConfig = doc.get('baseConfig')
    # print(baseConfig)

def baseConfig():    
    config=openYaml()
    
    for doc in config:      
        baseConfig = doc.get('baseConfig')
        if baseConfig!=None:
            break
    return baseConfig

def coinConfig():    
    config=openYaml()
    
    for doc in config:      
        coinConfig = doc.get('coinConfig')
        if coinConfig!=None:
            break
    return coinConfig
  


print(coinConfig())
print()
print(baseConfig())