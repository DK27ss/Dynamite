# Dynamite - For Automatic Analysis of Ethereum Smart Contracts

Bêta version 0.5
Developped and maintained by [@DK27ss](https://github.com/DK27ss)

En maintenance.. 

## Description:

Dynamite is a tool for automatically analyzes a smart contract using auto solc adapt; external modules (slither / mythril / echidna) and APIs.

## Features:

- automatically DETECTS tokens symbols, tokens balances and the smart contract solidity compiler version.
- automatically ADAPTS the compiler version to the smart contract compiler version, so that the slither scan can be performed as quickly as possible
- performs static analysis with Slither
- performs exploit analysis & generation with MistralAI
  
>> - performs static analysis & symbolic execution with Mythril [SOON]
>> - performs static analysis with Echidna [SOON]




# Requirements - Solc
// Install solc with Node.js
 
    npm install -g solc

    docker run -v /local/path:/sources ethereum/solc:stable -o /sources/output --abi --bin /sources/Contract.sol

    docker run ethereum/solc:stable --standard-json < input.json > output.json

// Install solc with Linux Packages

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

# Requirements - Slither
// Install slither with Pip

    python3 -m pip install slither-analyzer

// Install slither with Git

    git clone https://github.com/crytic/slither.git && cd slither
    python3 -m pip install .

// Install slither with Docker

    docker pull trailofbits/eth-security-toolbox
    docker run -it -v /home/share:/share trailofbits/eth-security-toolbox

# Dynamite Usage
// Simple Dynamite Run

>> Once all the requirements have been installed, or if you already have the requirements on your system, you can type the following command to launch the dynamite.

    python dynamite.py [help / -h]

https://github.com/user-attachments/assets/be051f22-0c67-48e3-9f11-5585bff29992

// Mistral PoC

https://github.com/user-attachments/assets/c968bb9e-f44a-41d2-89e3-588d677e76dd


>> if by mistake you encounter problems with the compiler version, please execute the commands shown in the following screenshot to guide you and solve your problems for future analysis.
![solve](https://github.com/DK27ss/Dynamite/assets/134336163/a713d69f-03e7-4f59-8385-08235f952482)
// install manually solidity compiler (X.X.X = compiler version)

    solc-select install X.X.X

// set manually solidity compiler (X.X.X = compiler version)

    solc-select use X.X.X
    
>> then launch the slither scan manually, which requires adding slither to your PATH so that you can call it from anywhere.
![solve2](https://github.com/DK27ss/Dynamite/assets/134336163/61b5b88b-b3df-4779-bc8b-43bfb592907b)

// run slither manually (0x000000000000 = token smart contract source code)

    slither 0x000000000000.sol



