import os
import requests

BLOCKCYPHER_API_KEY = os.environ.get("BLOCKCYPHER_API_KEY")
BASE_URL = f"https://api.blockcypher.com/v1/btc/main"


def get_block(block_id):
    try:
        url = f"{BASE_URL}/blocks/{block_id}?token={BLOCKCYPHER_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        block = response.json()
        return block
    except Exception as e:
        raise ValueError(f"Error fetching block data: {e}")


def get_transaction(transaction_id):
    try:
        url = f"{BASE_URL}/txs/{transaction_id}?token={BLOCKCYPHER_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        transaction = response.json()
        return transaction
    except Exception as e:
        raise ValueError(f"Error fetching transaction data: {e}")


def get_address(address):
    try:
        url = f"{BASE_URL}/addrs/{address}/full?token={BLOCKCYPHER_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        address_info = response.json()
        balance = address_info["final_balance"]
        transactions = address_info["txs"]
        return {"balance": balance, "transactions": transactions}
    except Exception as e:
        raise ValueError(f"Error fetching address data: {e}")


def get_stats():
    try:
        url = f"{BASE_URL}?token={BLOCKCYPHER_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        blockchain_info = response.json()
        stats = {
            "hash_rate": blockchain_info["hashrate"],
            "difficulty": blockchain_info["difficulty"],
            "transaction_count": blockchain_info["n_tx"],
            "protocol_version": blockchain_info["version"],
            "time_offset": None,  # BlockCypher API does not provide time_offset
        }
        return stats
    except Exception as e:
        raise ValueError(f"Error fetching stats data: {e}")
