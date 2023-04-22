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

> The project is a comprehensive blockchain data analysis platform built using FastAPI. It provides a RESTful API for interacting with and analyzing data from multiple blockchains, including Ethereum and Bitcoin. By utilizing powerful libraries such as web3.py and third-party services like Infura and BlockCypher, this platform offers users a unified and efficient way to gather essential information from different blockchain networks.

> With its well-documented and easy-to-use API endpoints, users can access crucial data about blocks, transactions, addresses, and overall network statistics. The project is designed to be highly modular and can easily be extended to support additional blockchain networks in the future. Furthermore, the use of FastAPI ensures excellent performance, automatic validation of request and response data, and interactive API documentation through SwaggerUI.

> This platform can serve a wide range of use cases, from developers building blockchain-based applications to researchers, analysts, and enthusiasts who require in-depth information about various blockchain networks. Overall, this project aims to simplify blockchain data analysis and offer a powerful tool for users to access and understand the complex world of distributed ledger technology.

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

### Infura

Infura is a hosted Ethereum and IPFS (InterPlanetary File System) infrastructure service that provides developers with a scalable and reliable API to access Ethereum and IPFS networks. It eliminates the need to set up, maintain, and synchronize a full Ethereum node, making it easier and faster to build decentralized applications (dApps) and interact with the Ethereum blockchain.

We are using Infura because it offers the following advantages:

    Scalability: Infura can handle a large number of requests and scales automatically as your application grows, reducing the need for infrastructure management.
    Reliability: Infura provides a high-availability service with multiple redundancies, ensuring consistent access to the Ethereum network.
    Ease of use: By using Infura, we can quickly access Ethereum data and interact with smart contracts without setting up and maintaining our own Ethereum node.

In addition to the basic Ethereum API, Infura also provides several advanced features:

    Real-time event notifications: Infura supports Websockets for real-time updates on events, such as new blocks, transactions, and contract events.
    IPFS integration: Infura provides a gateway to the IPFS network, which is a distributed file storage system. This can be useful for storing and retrieving large files in a decentralized manner.
    Ethereum archive data: Infura offers access to historical Ethereum data, enabling deeper analysis and insights into the Ethereum blockchain.
    Custom solutions: Infura provides custom infrastructure solutions tailored to specific business needs, such as dedicated nodes and private Ethereum networks.

By using Infura in our project, we can easily interact with the Ethereum blockchain and focus on building our application instead of managing the underlying infrastructure.

### BlockCypher

BlockCypher is a cloud-optimized blockchain infrastructure that provides API services for developers and enterprises to interact with various blockchains like Bitcoin, Ethereum, and Litecoin. It offers robust, scalable, and secure APIs, making it easier for developers to build and deploy blockchain applications without the need to maintain their own full nodes.

We are using BlockCypher because:

    Ease of use: BlockCypher provides simple RESTful APIs to interact with multiple blockchains, making it easy to integrate into our application.
    Scalability: BlockCypher's infrastructure is designed to handle high volumes of requests, ensuring our application performs well under load.
    Security: BlockCypher is built with security in mind, offering features such as address validation and transaction signing to help protect our application from common security threats.
    Reduced overhead: By using BlockCypher, we can avoid the need to maintain and sync our own full nodes, reducing the overhead and complexity of our application.

With BlockCypher, we can do much more than just querying block and transaction data. Some additional features include:

    WebHooks and WebSockets: Receive real-time notifications about events happening on the blockchain, such as new transactions or blocks.
    Transaction API: Create, sign, and broadcast transactions on the blockchain, allowing our application to send and manage funds.
    Address API: Generate new addresses and manage existing ones, enabling our application to create and monitor multiple wallets.
    Analytics API: Access blockchain analytics and insights, such as transaction volume, address distribution, and more.

For more information, visit the BlockCypher documentation.

## Important Sites
1. https://www.infura.io/
2. https://www.blockcypher.com/

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