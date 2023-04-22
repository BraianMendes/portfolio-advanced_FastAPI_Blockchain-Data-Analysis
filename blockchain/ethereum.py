import os
from web3 import Web3

# Substitua o valor da variável pelo seu próprio provedor Ethereum (ex: Infura)
ETHEREUM_PROVIDER = os.environ.get("ETHEREUM_PROVIDER")
w3 = Web3(Web3.HTTPProvider(ETHEREUM_PROVIDER))

def get_block(block_id: str):
    block = w3.eth.getBlock(block_id)
    if not block:
        return None

    return {
        'number': block.number,
        'hash': block.hash.hex(),
        'parentHash': block.parentHash.hex(),
        'nonce': block.nonce,
        'size': block.size,
        'timestamp': block.timestamp,
        'transactions': [tx.hex() for tx in block.transactions],
    }

def get_transaction(transaction_id: str):
    tx = w3.eth.getTransaction(transaction_id)
    if not tx:
        return None

    return {
        'hash': tx.hash.hex(),
        'nonce': tx.nonce,
        'blockHash': tx.blockHash.hex(),
        'blockNumber': tx.blockNumber,
        'transactionIndex': tx.transactionIndex,
        'from': tx['from'],
        'to': tx.to,
        'value': tx.value,
        'gas': tx.gas,
        'gasPrice': tx.gasPrice,
    }

def get_address(address: str):
    if not w3.isAddress(address):
        return None

    balance = w3.eth.getBalance(address)
    transaction_count = w3.eth.getTransactionCount(address)

    return {
        'address': address,
        'balance': balance,
        'transactionCount': transaction_count,
    }

def get_stats():
    block_number = w3.eth.blockNumber
    gas_price = w3.eth.gasPrice
    hash_rate = w3.eth.hashrate

    return {
        'blockNumber': block_number,
        'gasPrice': gas_price,
        'hashRate': hash_rate,
    }