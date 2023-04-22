from fastapi import FastAPI, APIRouter, Path, HTTPException
from dotenv import load_dotenv
import os

from blockchain.ethereum import get_block as eth_get_block, get_transaction as eth_get_transaction, get_address as eth_get_address, get_stats as eth_get_stats
from blockchain.bitcoin import get_block as btc_get_block, get_transaction as btc_get_transaction, get_address as btc_get_address, get_stats as btc_get_stats


# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Agora você pode acessar as variáveis de ambiente usando os.environ
ETHEREUM_PROVIDER = os.environ.get("ETHEREUM_PROVIDER")
BITCOIN_RPC_USER = os.environ.get("BITCOIN_RPC_USER")
BITCOIN_RPC_PASSWORD = os.environ.get("BITCOIN_RPC_PASSWORD")
BITCOIN_RPC_HOST = os.environ.get("BITCOIN_RPC_HOST")
BITCOIN_RPC_PORT = os.environ.get("BITCOIN_RPC_PORT")

app = FastAPI()

eth_router = APIRouter(prefix="/ethereum")
btc_router = APIRouter(prefix="/bitcoin")

@eth_router.get("/block/{block_id}")
def block(block_id: int):
    try:
        return eth_get_block(block_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@eth_router.get("/transaction/{transaction_id}")
def transaction(transaction_id: str):
    try:
        return eth_get_transaction(transaction_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@eth_router.get("/address/{address}")
def address(address: str):
    try:
        return eth_get_address(address)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@eth_router.get("/stats")
def stats():
    try:
        return eth_get_stats()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@btc_router.get("/block/{block_id}")
def block(block_id: int):
    try:
        return btc_get_block(block_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@btc_router.get("/transaction/{transaction_id}")
def transaction(transaction_id: str):
    try:
        return btc_get_transaction(transaction_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@btc_router.get("/address/{address}")
def address(address: str):
    try:
        return btc_get_address(address)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@btc_router.get("/stats")
def stats():
    try:
        return btc_get_stats()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

app.include_router(eth_router)
app.include_router(btc_router)

