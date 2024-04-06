import re
import requests
import colorama
from colorama import Fore
import subprocess
import time

print("""
          ____
         '-..-'  @makaki22    .-.
        ___||___           .-/ /-.
       /_______/|         / / / /   
       |       ||        / / / /
       |   o   |/       / / / / 
       '---`(--' 0x1   />>=<
      """)

api_key = '9VWN8UD5TVYKAVMN1IVXJ2QRVR3HHDAFSB'

contract_address = input("TARGET CONTRACT >> ")

account_address = (contract_address)

url_transfers = f'https://api.etherscan.io/api?module=account&action=tokentx&contractaddress={contract_address}&address={account_address}&page=1&offset=100&sort=asc&apikey={api_key}'

response_transfers = requests.get(url_transfers)
data_transfers = response_transfers.json()

if data_transfers['status'] == "1":
    token_transfers = data_transfers['result']

    token_balances = {}

    for tx in token_transfers:
        token_symbol = tx['tokenSymbol']
        token_amount = int(tx['value']) / (10 ** int(tx['tokenDecimal']))

        if token_symbol in token_balances:
            token_balances[token_symbol] += token_amount
        else:
            token_balances[token_symbol] = token_amount

    print("Check" + Fore.MAGENTA + " >> ", account_address, ":" + Fore.WHITE)

    for symbol, balance in token_balances.items():
        print("Symbol: " + Fore.CYAN + f"{symbol}" + Fore.WHITE + " | " + Fore.WHITE + "Token Balance: " + Fore.CYAN + f"{balance}" + Fore.WHITE)

    url_contract_details = f'https://api.etherscan.io/api?module=contract&action=getsourcecode&address={contract_address}&apikey={api_key}'
    response_contract_details = requests.get(url_contract_details)
    data_contract_details = response_contract_details.json()

    if data_contract_details['status'] == "1":
        source_code = data_contract_details['result'][0]['SourceCode']
        match = re.search(r"pragma solidity\s+([^\s]+);", source_code)
        if match:
            solidity_version = match.group(1)
            print("Solidity Compiler:", solidity_version)

            time.sleep(2)

            print("")
            print("")
            print(Fore.MAGENTA + "[+] " + Fore.YELLOW + "CONTRACT SOURCE CODE" + Fore.CYAN)
            print("")
            print("")
            print(source_code)
            print("")
            print("")

            save_choice = input(Fore.YELLOW + "Save contract source code [.sol] ? (Y/n) ").strip().lower() or 'y'
            if save_choice == 'y':
                filename = contract_address + ".sol"
                with open(filename, "w") as f:
                    f.write(source_code)
                print(Fore.CYAN + "contract source code saved at " + Fore.CYAN + f"{filename}" + Fore.WHITE)
            else:
                print(Fore.RED + "[ERROR] " + Fore.YELLOW + "contract source code not saved !")

            solidity_version_numbers = re.findall(r'\d+\.\d+\.\d+', solidity_version)
            if solidity_version_numbers:
                solidity_version = solidity_version_numbers[0]
                install_choice = input(Fore.YELLOW + f"Download solidity compiler {solidity_version}? (Y/n) ").strip().lower() or 'y'
                if install_choice == 'y':
                    subprocess.run(["solc-select", "install", solidity_version])
                    print(Fore.YELLOW + f"{solidity_version}" + Fore.CYAN + " solidity compiler successfully download." + Fore.WHITE)
                else:
                    print(Fore.RED + "[ERROR] " + Fore.YELLOW + "solidity compiler not download !")

                use_choice = input(Fore.YELLOW + "Use solidity compiler " + Fore.CYAN + f"{solidity_version} " + Fore.WHITE +"? (Y/n) ").strip().lower() or 'y'
                if use_choice == 'y':
                    subprocess.run(["solc-select", "use", solidity_version])
                    print(Fore.YELLOW + f"{solidity_version}" + Fore.CYAN + " solidity compiler successfully added." + Fore.WHITE)
                else:
                    print(Fore.RED + "[ERROR] " + Fore.YELLOW + "solidity compiler not added !")

                slither_choice = input("Run" + Fore.MAGENTA + " slither analyzer " + Fore.MAGENTA + "on the locally saved .sol file? (Y/n) ").strip().lower() or 'y'
                if slither_choice == 'y':
                    subprocess.run(["slither", filename])
                    print(Fore.GREEN + "[200 OK] " + Fore.WHITE)
                else:
                    print(Fore.RED + "[ERROR] " + Fore.YELLOW + "slither not executed!")

            else:
                print("Invalid Solidity compiler version")
        else:
            print("No pragma solidity declaration found in the contract source code.")
    else:
        print("Error retrieving contract details:", data_contract_details['message'])

else:
    print("Data recovery error:", data_transfers['message'])
