from tronapi import Tron
from solc import compile_source

full_node = 'https://api.trongrid.io'
solidity_node = 'https://api.trongrid.io'
event_server = 'https://api.trongrid.io'

tron = Tron(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)


result = tron.trx.get_transaction(
    "17fa5b1b4bad3dd2d37cb350941bbd6bedda72488a460efba7c5e05b84a8328e")
print(result)
