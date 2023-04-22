from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/block/{blockchain}/{block_id}")
def get_block(blockchain: str, block_id: str):
    pass  # Implementação futura

@app.get("/transaction/{blockchain}/{transaction_id}")
def get_transaction(blockchain: str, transaction_id: str):
    pass  # Implementação futura

@app.get("/address/{blockchain}/{address}")
def get_address(blockchain: str, address: str):
    pass  # Implementação futura

@app.get("/stats/{blockchain}")
def get_stats(blockchain: str):
    pass  # Implementação futura
