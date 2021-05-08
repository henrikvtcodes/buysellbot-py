# This script simplifies the reading of yaml files

import yaml

def openYaml(yml='config.yaml'):
    f = open(yml, "r")
    config = yaml.load_all(f, Loader=yaml.Loader)
    return config

global baseConfig
global coin
baseConfig = 'Empty'
coins = 'Empty'

# def baseConfig():    
#     config=openYaml()
#     vrs()
#     
#     for doc in config:
#         if  vrs.baseConfig=='Empty':
#             baseConfig=doc
#             break
#         
#     return baseConfig
# 
# def coinConfig():    
#     config=openYaml()
#     vrs()
#     
#     for doc in config:
#         if vrs.baseConfig=='Empty':
#             baseConfig=doc
#             break
#         elif vrs.coins=='Empty':
#             coins=doc
#             break
#         
#     return coins
# 
# print(coinConfig())
# print()
# print(baseConfig())