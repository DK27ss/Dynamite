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

> Once all the requirements have been installed, or if you already have the requirements on your system, you can type the following command to launch the dynamite.

    python dynamite.py
    
![dyn](https://github.com/DK27ss/Dynamite/assets/134336163/5e745780-729e-4088-b3b8-ebe3276b0fb7)

> if by mistake you encounter problems with the compiler version, please execute the commands shown in the following screenshot to guide you and solve your problems for future analysis.
![solve](https://github.com/DK27ss/Dynamite/assets/134336163/a713d69f-03e7-4f59-8385-08235f952482)
> install the solidity compiler (X.X.X = compiler version)

    solc-select install X.X.X

> set the solidity compiler (X.X.X = compiler version)

    solc-select use X.X.X
    
> then launch the slither scan manually, which requires adding slither to your PATH so that you can call it from anywhere.
![solve2](https://github.com/DK27ss/Dynamite/assets/134336163/61b5b88b-b3df-4779-bc8b-43bfb592907b)

> run slither manually (0x000000000000 = token smart contract source code)

    slither 0x000000000000.sol



