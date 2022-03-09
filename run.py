from web3 import Web3

if __name__ == "__main__":
    w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed1.binance.org:443"))

    print(w3.eth.get_transaction("0x87f2954f829cba53cb1b7b7edfe5a6af3f9dbbf1053ba84260274c915f16c7cb"))
