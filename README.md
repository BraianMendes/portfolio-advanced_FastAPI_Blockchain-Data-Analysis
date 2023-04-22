<h1 align="center">Welcome to FastAPI NLP API 👋</h1>
<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://twitter.com/braian_dev" target="_blank">
    <img alt="Twitter: 'braian_dev'" src="https://img.shields.io/twitter/follow/braian_dev.svg?style=social" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20With-FastAPI-009688?logo=fastapi&style=for-the-badge">
</p>

> The project is 

<p align="center">
  <img src="img.png" alt="Preview">
</p>

<h2>Installation</h2>

Follow these steps to install and run the project locally:


* Create a Python virtual environment (recommended):

```
python -m venv venv
```

* Activate the virtual environment:

On Windows:

```
venv\Scripts\activate
```

On macOS/Linux:

```
source venv/bin/activate
```

  * Install the dependencies:

``` 
pip install -r requirements.txt
``` 

* Start the FastAPI server:

```
uvicorn main:app --reload
```

## Requirements

1. **Retrieve block information**: Obtain information about a specific block (block height, hash, transactions, etc.)
2. **Retrieve transaction information**: Obtain information about a specific transaction (hash, sender, recipient, value, fee, etc.)
3. **Retrieve address information**: Obtain information about a specific address (balance, transaction history, etc.)
4. **Calculate basic network statistics**: Calculate basic network statistics (hash rate, difficulty, number of transactions, etc.)

Based on these requirements, we created the following API endpoints:

- `/block/{blockchain}/{block_id}`
- `/transaction/{blockchain}/{transaction_id}`
- `/address/{blockchain}/{address}`
- `/stats/{blockchain}`

## Libraries and External Services

1. **web3.py**: Python library for interacting with the Ethereum blockchain. It will allow us to obtain information about blocks, transactions, and addresses.
   Documentation: https://web3py.readthedocs.io/en/stable/

2. **bitcoinrpc**: Python library for interacting with the Bitcoin blockchain via its RPC interface. It will allow us to obtain information about blocks, transactions, and addresses.
   Documentation: https://github.com/jgarzik/python-bitcoinrpc

3. **requests**: Library for making HTTP requests. It may be useful for obtaining information from external APIs, in case we need to supplement our data.
   Documentation: https://docs.python-requests.org/en/master/


## Future Features

1. **Real-time transaction tracking**: Provide real-time updates for new transactions on the network, enabling users to monitor transactions as they occur.
2. **Token tracking**: Support for tracking ERC-20 and other custom tokens on the Ethereum network, providing information about token balances and transactions.
3. **Smart contract interaction**: Allow users to interact with smart contracts on the Ethereum network, such as querying contract data or sending transactions to execute contract functions.
4. **Advanced analytics**: Perform advanced analytics on the blockchain data, such as detecting patterns, trends, and anomalies, and providing insights on network usage and user behavior.
5. **Data export**: Enable users to export blockchain data and analysis results in various formats (CSV, JSON, etc.), facilitating integration with other tools and platforms.
6. **Multi-chain support**: Extend the API to support additional blockchains, increasing the range of use cases and applications.
7. **User authentication and authorization**: Implement user authentication and authorization features to ensure the security and privacy of API usage and user data.

## Author

<h5>Thank you very much for reading so far. I'm open for everything, and I really hope to see you next time. Best Regards, Braian.</h5>

👤 **Braian Mendes**

* Instagram [@braian.tech](https://www.instagram.com/braian.tech)
* Twitter: [@braian_dev](https://twitter.com/braian_dev)
* Github: [@BraianMendes](https://github.com/BraianMendes)
* LinkedIn: [@braianmendes](https://linkedin.com/in/braianmendes)

## Show your support

Give a ⭐️ if this project helped you!

<a href="https://www.patreon.com/braian_dev">
  <img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>