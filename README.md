# Dynamite
Dynamite - For Automatic Analysis of Ethereum Smart Contracts

Dynamite is a simple tool coded in Python that automatically analyzes a smart contract using slither and the Etherscan API.

> it automatically detects tokens symbols, tokens balances and the smart contract solidity compiler version.

> it automatically adapts the compiler version to the smart contract compiler version, so that the slither scan can be performed as quickly as possible

                 ____
         '-..-'    Dynamite     .-.
        ___||___  @makaki22  .-/ /-.   Beta Version
       /_______/|           / / / /    Buy me a Coffee ! --> 0x6117A78a0122639E61f03eB518be6626b00886a3
       |       ||          / / / /
       |   o   |/         / / / / 
       '---`(--' 0x1     />>=<

# Requirements - solc
// Install solc with Node.js
 
    npm install -g solc

    docker run -v /local/path:/sources ethereum/solc:stable -o /sources/output --abi --bin /sources/Contract.sol

    docker run ethereum/solc:stable --standard-json < input.json > output.json

// Install with Linux Packages

    sudo add-apt-repository ppa:ethereum/ethereum
    sudo apt-get update
    sudo apt-get install solc

    sudo add-apt-repository ppa:ethereum/ethereum
    sudo add-apt-repository ppa:ethereum/ethereum-dev
    sudo apt-get update
    sudo apt-get install solc
    

// Install solc with Snap

    sudo snap install solc
    sudo snap install solc --edge

# Usage
// Simple Run

       python dynamite.py




