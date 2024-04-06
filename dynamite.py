import re
import requests
import colorama
from colorama import Fore
import subprocess

print("""
          ____
         '-..-'  @makaki22    .-.
        ___||___           .-/ /-.
       /_______/|         / / / /   
       |       ||        / / / /
       |   o   |/       / / / / 
       '---`(--' 0x1   />>=<
      """)

# Clé API Etherscan (Remplacez par votre propre clé)
api_key = '9VWN8UD5TVYKAVMN1IVXJ2QRVR3HHDAFSB'

# Adresse du contrat ERC20 (exemple)
contract_address = input("ERC20 CONTRAT >> ")

# Adresse du compte pour lequel vous voulez vérifier les jetons (exemple)
account_address = (contract_address)

# Point d'extrémité de l'API Etherscan pour obtenir les transferts de jetons
url_transfers = f'https://api.etherscan.io/api?module=account&action=tokentx&contractaddress={contract_address}&address={account_address}&page=1&offset=100&sort=asc&apikey={api_key}'

response_transfers = requests.get(url_transfers)
data_transfers = response_transfers.json()

if data_transfers['status'] == "1":
    token_transfers = data_transfers['result']

    # Créer un dictionnaire pour stocker les balances des tokens et leurs symboles
    token_balances = {}

    # Boucler à travers les transferts de jetons pour calculer la balance de chaque jeton et stocker son symbole
    for tx in token_transfers:
        token_symbol = tx['tokenSymbol']
        token_amount = int(tx['value']) / (10 ** int(tx['tokenDecimal']))

        # Ajouter le montant au solde existant si le symbole existe déjà, sinon créer une nouvelle entrée
        if token_symbol in token_balances:
            token_balances[token_symbol] += token_amount
        else:
            token_balances[token_symbol] = token_amount

    # Afficher les balances des tokens et leurs symboles
    print("Check" + Fore.MAGENTA + " >> ", account_address, ":" + Fore.WHITE)

    # Afficher la balance des tokens et leurs symboles
    for symbol, balance in token_balances.items():
        print("Symbol: " + Fore.CYAN + f"{symbol}" + Fore.WHITE + " | " + Fore.WHITE + "Token Balance: " + Fore.CYAN + f"{balance}" + Fore.WHITE)

    # Récupérer les détails du contrat pour obtenir la version du compilateur Solidity et le code source complet
    url_contract_details = f'https://api.etherscan.io/api?module=contract&action=getsourcecode&address={contract_address}&apikey={api_key}'
    response_contract_details = requests.get(url_contract_details)
    data_contract_details = response_contract_details.json()

    if data_contract_details['status'] == "1":
        # Utiliser une expression régulière pour extraire la version du compilateur Solidity
        source_code = data_contract_details['result'][0]['SourceCode']
        match = re.search(r"pragma solidity\s+([^\s]+);", source_code)
        if match:
            solidity_version = match.group(1)
            print("Solidity Compiler:", solidity_version)

            # Afficher le code source complet du contrat
            print("")
            print("")
            print(Fore.MAGENTA + "[+] " + Fore.YELLOW + "CONTRAT SOURCE CODE" + Fore.CYAN)
            print("")
            print("")
            print(source_code)
            print("")
            print("")

            # Demander à l'utilisateur s'il souhaite enregistrer le code source localement
            save_choice = input(Fore.YELLOW + "Save contrat source code [.sol] ? (Y/n) ")
            if save_choice.lower() == 'y':
                filename = contract_address + ".sol"
                with open(filename, "w") as f:
                    f.write(source_code)
                print(Fore.CYAN + "contrat source code saved at " + Fore.CYAN + f"{filename}" + Fore.WHITE)
            else:
                print(Fore.RED + "[ERROR] " + Fore.YELLOW + "contrat source code not saved !")

            # Demander à l'utilisateur s'il souhaite installer la version du compilateur Solidity
            solidity_version_numbers = re.findall(r'\d+\.\d+\.\d+', solidity_version)
            if solidity_version_numbers:
                solidity_version = solidity_version_numbers[0]
                install_choice = input(Fore.YELLOW + f"Download solidity compiler {solidity_version}? (Y/n) " + Fore.WHITE)
                if install_choice.lower() == 'y':
                    subprocess.run(["solc-select", "install", solidity_version])
                    print(Fore.YELLOW + f"{solidity_version}" + Fore.CYAN + " solidity compiler successfully download." + Fore.WHITE)
                else:
                    print(Fore.RED + "[ERROR] " + Fore.YELLOW + "solidity compiler not download !")

                # Demander à l'utilisateur s'il souhaite utiliser la version du compilateur Solidity
                use_choice = input(Fore.YELLOW + "Use solidity compiler " + Fore.CYAN + f"{solidity_version} " + Fore.WHITE +"? (Y/n) ")
                if use_choice.lower() == 'y':
                    subprocess.run(["solc-select", "use", solidity_version])
                    print(Fore.YELLOW + f"{solidity_version}" + Fore.CYAN + " solidity compiler successfully added." + Fore.WHITE)
                else:
                    print(Fore.RED + "[ERROR] " + Fore.YELLOW + "solidity compiler not added !")

                # Demander à l'utilisateur s'il souhaite exécuter Slither sur le fichier .sol enregistré localement
                slither_choice = input("Run" + Fore.MAGENTA + " slither analyzer " + Fore.MAGENTA + "on the locally saved .sol file? (Y/n) ")
                if slither_choice.lower() == 'y':
                    subprocess.run(["slither", filename])
                    print(Fore.GREEN + "[200 OK] " + Fore.WHITE)
                else:
                    print(Fore.RED + "[ERROR] " + Fore.YELLOW + "slither not executed!")

            else:
                print("La version du compilateur Solidity extraite est invalide.")
        else:
            print("Aucune déclaration pragma solidity trouvée dans le code source du contrat.")
    else:
        print("Erreur lors de la récupération des détails du contrat:", data_contract_details['message'])

else:
    print("Erreur lors de la récupération des données:", data_transfers['message'])
