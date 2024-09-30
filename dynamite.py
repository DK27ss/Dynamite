#   Copyright 2024. SUPERPOSE INT. All rights reserved.
#   ___    A
#   | |   {*}       This vulnerability recognition software, including all source code, documentation and associated files, is the exclusive property of @makaki22. Any unauthorized
#   | |  __V__      reproduction, distribution or modification of this software is strictly prohibited.
#   |_|o_|%%%|0_    This software is provided "as is" without warranty of any kind, either express or implied, including, but not limited to, the implied warranties of merchantability, 
#      |       |    fitness for a particular purpose and non-infringement. In no event shall @makaki22 be liable for any direct, indirect, incidental, special or consequential damages arising 
#      |       |    out of the use or inability to use this software, even if advised of the possibility of such damages.
#      |_______|
#                   Use of this software is subject to the terms and conditions of the applicable license agreement provided with the software.
#                   By using this software, you agree to be bound by the terms of this license.
#
#                   If you have any questions about this software or require additional permissions, please contact @makaki22 on telegram.
#

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import os
import subprocess
import argparse
import colorama
import requests
import re
import threading
from colorama import Fore
import time

################

ETHERSCAN_API_KEY = '9VWN8UD5TVYKAVMN1IVXJ2QRVR3HHDAFSB'
BASE_API_KEY = 'VUNI3HKC7VDBRRAJEUAJWA5ABDIKFF9AIS'
BSC_API_KEY = 'M41SV3B61NEEH55ZZ421ABE7CHWND7SWTW'
CRO_API_KEY = 'UF9N1SZS5PCB647XVBE7AQ2XJVXQH7ZPSP'
AVAX_API_KEY = 'J9BG6RAZB3R3W114MCTXP439D547SRNZGY'
POLYGON_API_KEY = 'XUM9KC73EVNM682515IUCQJKC8TFW2GXMI'

################

######################################################################################################
######################################################################################################

def get_contract_source_code_ether(contract_address):
    url = f"https://api.etherscan.io/api"
    params = {
        'module': 'contract',
        'action': 'getsourcecode',
        'address': contract_address,
        'apiKey': ETHERSCAN_API_KEY
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == '1':
        return data['result'][0]['SourceCode']
    else:
        raise Exception("Erreur lors de la récupération du code source : " + data['message'])

def extract_function_names_ether(contract_code):
    function_pattern = r'\bfunction\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
    function_names = re.findall(function_pattern, contract_code)
    return function_names


######################################################################################################
######################################################################################################

def get_contract_source_code_base(contract_address):
    url = f"https://api.basescan.org/api"
    params = {
        'module': 'contract',
        'action': 'getsourcecode',
        'address': contract_address,
        'apiKey': BASE_API_KEY
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == '1':
        return data['result'][0]['SourceCode']
    else:
        raise Exception("Erreur lors de la récupération du code source : " + data['message'])

def extract_function_names_base(contract_code):
    function_pattern = r'\bfunction\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
    function_names = re.findall(function_pattern, contract_code)
    return function_names


######################################################################################################
######################################################################################################

def get_contract_source_code_bsc(contract_address):
    url = f"https://api.bscscan.com/api"
    params = {
        'module': 'contract',
        'action': 'getsourcecode',
        'address': contract_address,
        'apiKey': BSC_API_KEY
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == '1':
        return data['result'][0]['SourceCode']
    else:
        raise Exception("Erreur lors de la récupération du code source : " + data['message'])

def extract_function_names_bsc(contract_code):
    function_pattern = r'\bfunction\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
    function_names = re.findall(function_pattern, contract_code)
    return function_names

######################################################################################################
######################################################################################################

def get_contract_source_code_cronos(contract_address):
    url = f"https://api.cronoscan.com/api"
    params = {
        'module': 'contract',
        'action': 'getsourcecode',
        'address': contract_address,
        'apiKey': CRO_API_KEY
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == '1':
        return data['result'][0]['SourceCode']
    else:
        raise Exception("Erreur lors de la récupération du code source : " + data['message'])

def extract_function_names_cronos(contract_code):
    function_pattern = r'\bfunction\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
    function_names = re.findall(function_pattern, contract_code)
    return function_names


######################################################################################################
######################################################################################################

def get_contract_source_code_avax(contract_address):
    url = f"https://api.snowscan.xyz/api"
    params = {
        'module': 'contract',
        'action': 'getsourcecode',
        'address': contract_address,
        'apiKey': AVAX_API_KEY
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == '1':
        return data['result'][0]['SourceCode']
    else:
        raise Exception("Erreur lors de la récupération du code source : " + data['message'])

def extract_function_names_avax(contract_code):
    function_pattern = r'\bfunction\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
    function_names = re.findall(function_pattern, contract_code)
    return function_names

######################################################################################################
######################################################################################################

def get_contract_source_code_polygon(contract_address):
    url = f"https://api.polygonscan.com/api"
    params = {
        'module': 'contract',
        'action': 'getsourcecode',
        'address': contract_address,
        'apiKey': POLYGON_API_KEY
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == '1':
        return data['result'][0]['SourceCode']
    else:
        raise Exception("Erreur lors de la récupération du code source : " + data['message'])

def extract_function_names_polygon(contract_code):
    function_pattern = r'\bfunction\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
    function_names = re.findall(function_pattern, contract_code)
    return function_names

######################################################################################################
######################################################################################################



def loading_animation():
    chars = ['▖', '▘', '▝', '▗']  
    while not stop_loading:
        for char in chars:
            print(Fore.YELLOW + f"\r[{char}] forge PoC creation ..", end="")
            time.sleep(0.2)





def call_network(network_file):
    network_path = os.path.join("network", network_file)
    if os.path.exists(network_path):
        subprocess.run(["python", network_path])
    else:
        print(Fore.RED + "[CRITICAL]" + Fore.WHITE + f"'{network_file}' was not found in the 'network' folder.")




def analyze_func_with_mistral(functions):
    global stop_loading

    MISTRAL_API_URL = "https://codestral.mistral.ai/v1/chat/completions"  
    mistral_api_key = "SPVhQvPY2313gzVXeDVKYANdeIbSWDfZ"  # Remplace par ta clé d'API Mistral
    
    headers = {
        "Authorization": "Bearer " + f"{mistral_api_key}",
        "Content-Type": "application/json"
    }

    while True:
        user_prompt_choice = input("Interact with Mistral API ? (Y/n) ")

        if user_prompt_choice.lower() == 'n':
            print(Fore.MAGENTA + "[API] " + Fore.YELLOW + "[MISTRAL] Interruption." + Fore.WHITE)
            break

        user_prompt = input(Fore.MAGENTA + "[API] " + Fore.YELLOW + "[MISTRAL] (press 'exit' to quit) " + Fore.WHITE + "\nDIRECT REQUEST # ")

        if user_prompt.lower() == 'exit':
            print(Fore.MAGENTA + "[API] " + Fore.YELLOW + "[MISTRAL] Interruption." + Fore.WHITE)
            break
        
        prompt = (
            "Tu es un expert en analyse de smart contrats. Voici les fonctions que je souhaite analyser à nouveau :\n\n"
            + "\n".join(functions) + "\n"
            "Voici ma question : " + user_prompt
        )

        data = {
            "model": "codestral-latest",
            "messages": [{"role": "user", "content": prompt}]
        }

        # Lancer l'animation de chargement dans un autre thread
        stop_loading = False
        loading_thread = threading.Thread(target=loading_animation)
        loading_thread.start()

        try:
            # Appel de l'API Mistral
            response = requests.post(MISTRAL_API_URL, headers=headers, json=data)

            # Stopper l'animation une fois l'appel terminé
            stop_loading = True
            loading_thread.join()  # Attendre la fin du thread d'animation

            # Affichage de l'analyse ou de l'erreur
            if response.status_code == 200:
                analysis = response.json()['choices'][0]['message']['content']
                print(Fore.MAGENTA + "\n[API] " + Fore.YELLOW + "[MISTRAL RESULT] " + Fore.CYAN + analysis + Fore.WHITE)
            else:
                print(Fore.RED + "[ERROR]" + Fore.WHITE + " failed to call Mistral API :", response.text)
        except Exception as e:
            stop_loading = True
            loading_thread.join()  # Attendre la fin du thread d'animation
            print(Fore.RED + "[ERROR]" + Fore.WHITE + f" Exception occurred: {str(e)}")

###########################################################################################################################################
###########################################################################################################################################

def call_catf_program_ether_network(contract_address):
    try:
        # Récupérer le code source du contrat
        contract_code = get_contract_source_code_ether(contract_address)
        # Extraire les noms de fonctions
        function_names = extract_function_names_ether(contract_code)
        
        # Afficher les fonctions dumpées
        print(Fore.GREEN + "[#]" + Fore.WHITE + " Dumped functions for " + Fore.MAGENTA + f"{contract_address}:" + Fore.WHITE)
        for name in function_names:
            print(name)

        # Appeler l'analyse avec Mistral
        analyze_func_with_mistral(function_names)

    except Exception as e:
        print(Fore.RED + "[ERROR]" + Fore.WHITE + f" {str(e)}")

###########################################################################################################################################
###########################################################################################################################################

def call_catf_program_base_network(contract_address):
    try:
        # Récupérer le code source du contrat
        contract_code = get_contract_source_code_base(contract_address)
        # Extraire les noms de fonctions
        function_names = extract_function_names_base(contract_code)
        
        # Afficher les fonctions dumpées
        print(Fore.GREEN + "[#]" + Fore.WHITE + " Dumped functions for " + Fore.MAGENTA + f"{contract_address}:" + Fore.WHITE)
        for name in function_names:
            print(name)

        # Appeler l'analyse avec Mistral
        analyze_func_with_mistral(function_names)

    except Exception as e:
        print(Fore.RED + "[ERROR]" + Fore.WHITE + f" {str(e)}")



###########################################################################################################################################
###########################################################################################################################################

def call_catf_program_bsc_network(contract_address):
    try:
        # Récupérer le code source du contrat
        contract_code = get_contract_source_code_bsc(contract_address)
        # Extraire les noms de fonctions
        function_names = extract_function_names_bsc(contract_code)
        
        # Afficher les fonctions dumpées
        print(Fore.GREEN + "[#]" + Fore.WHITE + " Dumped functions for " + Fore.MAGENTA + f"{contract_address}:" + Fore.WHITE)
        for name in function_names:
            print(name)

        # Appeler l'analyse avec Mistral
        analyze_func_with_mistral(function_names)

    except Exception as e:
        print(Fore.RED + "[ERROR]" + Fore.WHITE + f" {str(e)}")




###########################################################################################################################################
###########################################################################################################################################

def call_catf_program_cronos_network(contract_address):
    try:
        # Récupérer le code source du contrat
        contract_code = get_contract_source_code_cronos(contract_address)
        # Extraire les noms de fonctions
        function_names = extract_function_names_cronos(contract_code)
        
        # Afficher les fonctions dumpées
        print(Fore.GREEN + "[#]" + Fore.WHITE + " Dumped functions for " + Fore.MAGENTA + f"{contract_address}:" + Fore.WHITE)
        for name in function_names:
            print(name)

        # Appeler l'analyse avec Mistral
        analyze_func_with_mistral(function_names)

    except Exception as e:
        print(Fore.RED + "[ERROR]" + Fore.WHITE + f" {str(e)}")



###########################################################################################################################################
###########################################################################################################################################


def call_catf_program_avax_network(contract_address):
    try:
        # Récupérer le code source du contrat
        contract_code = get_contract_source_code_avax(contract_address)
        # Extraire les noms de fonctions
        function_names = extract_function_names_avax(contract_code)
        
        # Afficher les fonctions dumpées
        print(Fore.GREEN + "[#]" + Fore.WHITE + " Dumped functions for " + Fore.MAGENTA + f"{contract_address}:" + Fore.WHITE)
        for name in function_names:
            print(name)

        # Appeler l'analyse avec Mistral
        analyze_func_with_mistral(function_names)

    except Exception as e:
        print(Fore.RED + "[ERROR]" + Fore.WHITE + f" {str(e)}")



###########################################################################################################################################
###########################################################################################################################################

def call_catf_program_polygon_network(contract_address):
    try:
        # Récupérer le code source du contrat
        contract_code = get_contract_source_code_polygon(contract_address)
        # Extraire les noms de fonctions
        function_names = extract_function_names_polygon(contract_code)
        
        # Afficher les fonctions dumpées
        print(Fore.GREEN + "[#]" + Fore.WHITE + " Dumped functions for " + Fore.MAGENTA + f"{contract_address}:" + Fore.WHITE)
        for name in function_names:
            print(name)

        # Appeler l'analyse avec Mistral
        analyze_func_with_mistral(function_names)

    except Exception as e:
        print(Fore.RED + "[ERROR]" + Fore.WHITE + f" {str(e)}")



###########################################################################################################################################
###########################################################################################################################################


## ETH MYTHRIL SCAN CONTRACT FUNCTION
#######################
#######################
def eth_myth_scan_contract(contract_address):
    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " perform to Myth attack")
    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " dynamite looks for contract datas .. " + Fore.WHITE)
    print("")

    api_key = '9VWN8UD5TVYKAVMN1IVXJ2QRVR3HHDAFSB'
    account_address = contract_address

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
            print(Fore.GREEN + "[CONTRACT FOUND!]" + Fore.WHITE)
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
                print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " CONTRACT CODE" + Fore.CYAN)
                print("")
                print("")
                print(source_code)
                print("")
                print("")

                if not os.path.exists("eth_check"):
                    os.makedirs("eth_check")

                filename = os.path.join("eth_check", contract_address + ".sol")

                if os.path.exists(filename):
                    print(Fore.WHITE + "[" + Fore.RED + "avoided" + Fore.WHITE + "]" + Fore.YELLOW + " .sol already exists." + Fore.WHITE)
                else:
                    with open(filename, "w") as f:
                        f.write(source_code)
                    print(Fore.CYAN + "Contract source code saved at " + Fore.CYAN + f"{filename}" + Fore.WHITE)

                # Nouvelle commande: Utilisation de Mythril pour analyser le contrat
                print(Fore.YELLOW + "[INFO] Running Mythril analysis..." + Fore.WHITE)
                subprocess.run(["myth", "a", filename])  # Commande "myth a" pour analyser le contrat
                print(Fore.GREEN + "[200 OK] Mythril analysis completed." + Fore.WHITE)

                # Analyse par Mystral
                analyze_with_mistral(source_code)

            else:
                print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " No pragma solidity declaration found in the contract source code.")
        else:
            print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Error retrieving contract details:", data_contract_details['message'])
    else:
        print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Data retrieval error:", data_transfers['message'])


## MISTRAL ANALYSE & GEN POC FUNCTION
#######################
#######################

def analyze_with_mistral(source_code):
    global stop_loading  # Déclare stop_loading comme global

    MISTRAL_API_URL = "https://codestral.mistral.ai/v1/chat/completions"  
    mistral_api_key = "SPVhQvPY2313gzVXeDVKYANdeIbSWDfZ"  # Remplace par ta clé d'API Mistral
    
    headers = {
        "Authorization": "Bearer " + f"{mistral_api_key}",
        "Content-Type": "application/json"
    }

    prompt = (
        "Tu es un expert en analyse de smart contrats et j'aimerais que tu identifie les vulnérabilités de Slither pour le contrat et propose un PoC de test pour Foundry afin de vérifier les vulnérabilités :\n\n"
        f"{source_code}\n"
    )

    user_input = input("Build foundry Mistral PoC ? (Y/n) ").strip().lower()

    if user_input != 'y':
        print(Fore.RED + "[EXIT] " + Fore.YELLOW + "Process canceled." + Fore.WHITE)
        return
    
    mistral_model = "codestral-latest"
    data = {
        "model": f"{mistral_model}",
        "messages": [{"role": "user", "content": prompt}]
    }

    stop_loading = False
    loading_thread = threading.Thread(target=loading_animation)
    loading_thread.start()

    try:
        response2 = requests.post(MISTRAL_API_URL, headers=headers, json=data)

        stop_loading = True
        loading_thread.join()  # Attendre la fin du thread d'animation

        # Affichage de l'analyse ou de l'erreur
        if response2.status_code == 200:
            analysis = response2.json()['choices'][0]['message']['content']
            print(Fore.MAGENTA + "\n[API] " + Fore.YELLOW + "[MISTRAL RESULT] " + Fore.CYAN + analysis + Fore.WHITE)
        else:
            print(Fore.RED + "[ERROR]" + Fore.WHITE + " failed to call " + Fore.YELLOW + f"[{mistral_model}]" + " Mistral API :", response2.text)
    
        # Interaction continue avec Mistral
        while True:
            user_prompt_choice = input("Interact with Mistral API ? (Y/n) ")

            if user_prompt_choice.lower() == 'n':
                print(Fore.MAGENTA + "[API] " + Fore.YELLOW + "[MISTRAL] Interruption." + Fore.WHITE)
                break

            user_prompt = input(Fore.MAGENTA + "[API] " + Fore.YELLOW + "[MISTRAL] (press 'exit' to quit) " + Fore.WHITE + "\nDIRECT REQUEST # " + Fore.GREEN)

            if user_prompt.lower() == 'exit':
                print(Fore.MAGENTA + "[API] " + Fore.YELLOW + "[MISTRAL] Interruption." + Fore.WHITE)
                break

            prompt2 = (
                "Tu es un expert en analyse de smart contrats avec Foundry et j'aimerais que tu m'aide :\n\n"
                + "\n" + user_prompt
            )

            data2 = {
                "model": "codestral-latest",
                "messages": [{"role": "user", "content": prompt2}]
            }

            # Lancer l'animation de chargement dans un autre thread
            stop_loading = False
            loading_thread = threading.Thread(target=loading_animation)
            loading_thread.start()

            try:
                # Appel de l'API Mistral
                response = requests.post(MISTRAL_API_URL, headers=headers, json=data2)

                # Stopper l'animation une fois l'appel terminé
                stop_loading = True
                loading_thread.join()  # Attendre la fin du thread d'animation

                # Affichage de l'analyse ou de l'erreur
                if response.status_code == 200:
                    analysis = response.json()['choices'][0]['message']['content']
                    print(Fore.MAGENTA + "\n[API] " + Fore.YELLOW + "[MISTRAL RESULT] " + Fore.CYAN + analysis + Fore.WHITE)
                else:
                    print(Fore.RED + "[ERROR]" + Fore.WHITE + " failed to call Mistral API :", response.text)
            except Exception as e:
                stop_loading = True
                loading_thread.join()  # Attendre la fin du thread d'animation
                print(Fore.RED + "[ERROR]" + Fore.WHITE + f" Exception occurred: {str(e)}")
    
    except Exception as e:
        stop_loading = True
        loading_thread.join()  # Attendre la fin du thread d'animation
        print(Fore.RED + "[ERROR]" + Fore.WHITE + f" Exception occurred: {str(e)}")

## ETH SCAN CONTRACT FUNCTION
#######################
#######################

def eth_scan_contract(contract_address):
    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " perform to Slither attack")
    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " dynamite looks for contract datas .. " + Fore.WHITE)
    print("")

    api_key = '9VWN8UD5TVYKAVMN1IVXJ2QRVR3HHDAFSB'
    account_address = contract_address

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
            print(Fore.GREEN + "[CONTRACT FOUND!]" + Fore.WHITE)
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
                print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " CONTRACT CODE" + Fore.CYAN)
                print("")
                print("")
                print(source_code)
                print("")
                print("")

                if not os.path.exists("eth_check"):
                    os.makedirs("eth_check")

                filename = os.path.join("eth_check", contract_address + ".sol")

                if os.path.exists(filename):
                    print(Fore.WHITE + "[" + Fore.RED + "avoided" + Fore.WHITE + "]" + Fore.YELLOW + " .sol already exists." + Fore.WHITE)
                else:
                    with open(filename, "w") as f:
                        f.write(source_code)
                    print(Fore.CYAN + "Contract source code saved at " + Fore.CYAN + f"{filename}" + Fore.WHITE)

                solidity_version_numbers = re.findall(r'\d+\.\d+\.\d+', solidity_version)
                if solidity_version_numbers:
                    solidity_version = solidity_version_numbers[0]
                    subprocess.run(["solc-select", "install", solidity_version])
                    print(Fore.YELLOW + f"{solidity_version}" + Fore.CYAN + " Solidity compiler successfully downloaded." + Fore.WHITE)
                    subprocess.run(["solc-select", "use", solidity_version])
                    print(Fore.YELLOW + f"{solidity_version}" + Fore.CYAN + " Solidity compiler successfully added." + Fore.WHITE)
                    subprocess.run(["slither", filename])
                    print(Fore.GREEN + "[200 OK] " + Fore.YELLOW + "Slither analysis completed." + Fore.WHITE)

                    # Analyse par Mystral
                    analyze_with_mistral(source_code)

                else:
                    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + Fore.RED + " Invalid Solidity compiler version")
            else:
                print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " No pragma solidity declaration found in the contract source code.")
        else:
            print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Error retrieving contract details:", data_contract_details['message'])
    else:
        print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Data retrieval error:", data_transfers['message'])

## AVAX SCAN CONTRACT FUNCTION
#######################
#######################

def avax_scan_contract(contract_address):
    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " perform to Slither attack")
    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " dynamite looks for contract datas .. " + Fore.WHITE)
    print("")

    api_key = 'J9BG6RAZB3R3W114MCTXP439D547SRNZGY'
    account_address = contract_address

    url_transfers = f'https://api.snowscan.xyz/api?module=account&action=tokentx&contractaddress={contract_address}&address={account_address}&page=1&offset=100&sort=asc&apikey={api_key}'
    response_transfers = requests.get(url_transfers)

    try:
        data_transfers = response_transfers.json()
    except ValueError:
        print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Failed to decode JSON response from Snowscan.xyz API")
        return

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

        print("Check" + Fore.YELLOW + " >> ", account_address, ":" + Fore.WHITE)
        for symbol, balance in token_balances.items():
            print(Fore.GREEN + "[CONTRACT FOUND!]" + Fore.WHITE)
            print("Symbol: " + Fore.CYAN + f"{symbol}" + Fore.WHITE + " | " + Fore.WHITE + "Token Balance: " + Fore.CYAN + f"{balance}" + Fore.WHITE)

        # Get contract source code from Snowscan.xyz
        url_contract_details = f'https://api.snowscan.xyz/api?module=contract&action=getsourcecode&address={contract_address}&apikey={api_key}'
        response_contract_details = requests.get(url_contract_details)

        try:
            data_contract_details = response_contract_details.json()
        except ValueError:
            print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Failed to decode JSON response from Snowscan.xyz API for contract details")
            return

        if data_contract_details['status'] == "1":
            source_code = data_contract_details['result'][0]['SourceCode']
            match = re.search(r"pragma solidity\s+([^\s]+);", source_code)
            if match:
                solidity_version = match.group(1)
                print("Solidity Compiler:", solidity_version)

                time.sleep(2)

                print("")
                print("")
                print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " CONTRACT CODE" + Fore.CYAN)
                print("")
                print("")
                print(source_code)
                print("")
                print("")

                if not os.path.exists("avax_check"):
                    os.makedirs("avax_check")

                filename = os.path.join("avax_check", contract_address + ".sol")
                if os.path.exists(filename):
                    print(Fore.WHITE + "[" + Fore.RED + "avoided" + Fore.WHITE + "]" + Fore.YELLOW + " .sol already exists." + Fore.WHITE)
                else:
                    with open(filename, "w") as f:
                        f.write(source_code)
                    print(Fore.CYAN + "Contract source code saved at " + Fore.CYAN + f"{filename}" + Fore.WHITE)

                solidity_version_numbers = re.findall(r'\d+\.\d+\.\d+', solidity_version)
                if solidity_version_numbers:
                    solidity_version = solidity_version_numbers[0]
                    subprocess.run(["solc-select", "install", solidity_version])
                    print(Fore.YELLOW + f"{solidity_version}" + Fore.CYAN + " solidity compiler successfully downloaded." + Fore.WHITE)
                    subprocess.run(["solc-select", "use", solidity_version])
                    print(Fore.YELLOW + f"{solidity_version}" + Fore.CYAN + " solidity compiler successfully added." + Fore.WHITE)
                    subprocess.run(["slither", filename])
                    print(Fore.GREEN + "[PASSED] " + Fore.WHITE)

                    analyze_with_mistral(source_code)
                else:
                    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + Fore.RED + " Invalid Solidity compiler version")
            else:
                print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " No pragma solidity declaration found in the contract source code.")
        else:
            print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Error retrieving contract details:", data_contract_details['message'])
    else:
        print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + "Data retrieval error:", data_transfers['message'])

## BASE SCAN CONTRACT FUNCTION
#######################
#######################

def base_scan_contract(contract_address):
    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " perform to Slither attack")
    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " dynamite looks for contract datas .. " + Fore.WHITE)
    print("")

    api_key = 'VUNI3HKC7VDBRRAJEUAJWA5ABDIKFF9AIS'

    account_address = (contract_address)

    url_transfers = f'https://api.basescan.org/api?module=account&action=tokentx&contractaddress={contract_address}&address={account_address}&page=1&offset=100&sort=asc&apikey={api_key}'

    response_transfers = requests.get(url_transfers)
    
    try:
        data_transfers = response_transfers.json()
    except ValueError:
        print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Failed to decode JSON response from BaseScan API")
        return

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
            print(Fore.GREEN + "[CONTRACT FOUND!]" + Fore.WHITE)
            print("Symbol: " + Fore.CYAN + f"{symbol}" + Fore.WHITE + " | " + Fore.WHITE + "Token Balance: " + Fore.CYAN + f"{balance}" + Fore.WHITE)

        # Get contract source code from BaseScan
        url_contract_details = f'https://api.basescan.org/api?module=contract&action=getsourcecode&address={contract_address}&apikey={api_key}'
        response_contract_details = requests.get(url_contract_details)

        try:
            data_contract_details = response_contract_details.json()
        except ValueError:
            print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Failed to decode JSON response from BaseScan API for contract details")
            return

        if data_contract_details['status'] == "1":
            source_code = data_contract_details['result'][0]['SourceCode']
            match = re.search(r"pragma solidity\s+([^\s]+);", source_code)
            if match:
                solidity_version = match.group(1)
                print("Solidity Compiler:", solidity_version)

                time.sleep(2)

                print("")
                print("")
                print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " CONTRACT CODE" + Fore.CYAN)
                print("")
                print("")
                print(source_code)
                print("")
                print("")

                if not os.path.exists("base_check"):
                    os.makedirs("base_check")

                filename = os.path.join("base_check", contract_address + ".sol")


                if os.path.exists(filename):
                    print(Fore.WHITE + "[" + Fore.RED + "avoided" + Fore.WHITE + "]" + Fore.YELLOW + " .sol already exists." + Fore.WHITE)
                else:
                    with open(filename, "w") as f:
                        f.write(source_code)
                    print(Fore.CYAN + "Contract source code saved at " + Fore.CYAN + f"{filename}" + Fore.WHITE)

                solidity_version_numbers = re.findall(r'\d+\.\d+\.\d+', solidity_version)
                if solidity_version_numbers:
                    solidity_version = solidity_version_numbers[0]
                    subprocess.run(["solc-select", "install", solidity_version])
                    print(Fore.YELLOW + f"{solidity_version}" + Fore.CYAN + " solidity compiler successfully downloaded." + Fore.WHITE)
                    subprocess.run(["solc-select", "use", solidity_version])
                    print(Fore.YELLOW + f"{solidity_version}" + Fore.CYAN + " solidity compiler successfully added." + Fore.WHITE)
                    subprocess.run(["slither", filename])
                    print(Fore.GREEN + "[PASSED] " + Fore.WHITE)

                    analyze_with_mistral(source_code)
                else:
                    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + Fore.RED + " Invalid Solidity compiler version")
            else:
                print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " No pragma solidity declaration found in the contract source code.")
        else:
            print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Error retrieving contract details:", data_contract_details['message'])

    else:
        print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + "Data retrieval error:", data_transfers['message'])

## BSC SCAN CONTRACT FUNCTION
#######################
#######################

def bsc_scan_contract(contract_address):
    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " perform to Slither attack")
    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " dynamite looks for contract datas .. " + Fore.WHITE)
    print("")

    api_key = 'M41SV3B61NEEH55ZZ421ABE7CHWND7SWTW'

    account_address = (contract_address)

    url_transfers = f'https://api.bscscan.com/api?module=account&action=tokentx&contractaddress={contract_address}&address={account_address}&page=1&offset=100&sort=asc&apikey={api_key}'

    response_transfers = requests.get(url_transfers)
    
    try:
        data_transfers = response_transfers.json()
    except ValueError:
        print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Failed to decode JSON response from BscScan API")
        return

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
            print(Fore.GREEN + "[CONTRACT FOUND!]" + Fore.WHITE)
            print("Symbol: " + Fore.CYAN + f"{symbol}" + Fore.WHITE + " | " + Fore.WHITE + "Token Balance: " + Fore.CYAN + f"{balance}" + Fore.WHITE)

        # Get contract source code from BscScan
        url_contract_details = f'https://api.bscscan.com/api?module=contract&action=getsourcecode&address={contract_address}&apikey={api_key}'
        response_contract_details = requests.get(url_contract_details)

        try:
            data_contract_details = response_contract_details.json()
        except ValueError:
            print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Failed to decode JSON response from BscScan API for contract details")
            return

        if data_contract_details['status'] == "1":
            source_code = data_contract_details['result'][0]['SourceCode']
            match = re.search(r"pragma solidity\s+([^\s]+);", source_code)
            if match:
                solidity_version = match.group(1)
                print("Solidity Compiler:", solidity_version)

                time.sleep(2)

                print("")
                print("")
                print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " CONTRACT CODE" + Fore.CYAN)
                print("")
                print("")
                print(source_code)
                print("")
                print("")

                if not os.path.exists("bsc_check"):
                    os.makedirs("bsc_check")

                filename = os.path.join("bsc_check", contract_address + ".sol")
                if os.path.exists(filename):
                    print(Fore.WHITE + "[" + Fore.RED + "avoided" + Fore.WHITE + "]" + Fore.YELLOW + " .sol already exists." + Fore.WHITE)
                else:
                    with open(filename, "w") as f:
                        f.write(source_code)
                    print(Fore.CYAN + "Contract source code saved at " + Fore.CYAN + f"{filename}" + Fore.WHITE)

                solidity_version_numbers = re.findall(r'\d+\.\d+\.\d+', solidity_version)
                if solidity_version_numbers:
                    solidity_version = solidity_version_numbers[0]
                    subprocess.run(["solc-select", "install", solidity_version])
                    print(Fore.YELLOW + f"{solidity_version}" + Fore.CYAN + " solidity compiler successfully downloaded." + Fore.WHITE)
                    subprocess.run(["solc-select", "use", solidity_version])
                    print(Fore.YELLOW + f"{solidity_version}" + Fore.CYAN + " solidity compiler successfully added." + Fore.WHITE)
                    subprocess.run(["slither", filename])
                    print(Fore.GREEN + "[PASSED] " + Fore.WHITE)

                    analyze_with_mistral(source_code)
                else:
                    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + Fore.RED + " Invalid Solidity compiler version")
            else:
                print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " No pragma solidity declaration found in the contract source code.")
        else:
            print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Error retrieving contract details:", data_contract_details['message'])

    else:
        print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + "Data retrieval error:", data_transfers['message'])

## CRO SCAN CONTRACT FUNCTION
#######################
#######################

def cro_scan_contract(contract_address):
    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " perform to Slither attack")
    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " dynamite looks for contract datas .. " + Fore.WHITE)
    print("")

    api_key = 'UF9N1SZS5PCB647XVBE7AQ2XJVXQH7ZPSP'

    account_address = (contract_address)

    url_transfers = f'https://api.cronoscan.com/api?module=account&action=tokentx&contractaddress={contract_address}&address={account_address}&page=1&offset=100&sort=asc&apikey={api_key}'

    response_transfers = requests.get(url_transfers)
    
    try:
        data_transfers = response_transfers.json()
    except ValueError:
        print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Failed to decode JSON response from CronoScan API")
        return

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
            print(Fore.GREEN + "[CONTRACT FOUND!]" + Fore.WHITE)
            print("Symbol: " + Fore.CYAN + f"{symbol}" + Fore.WHITE + " | " + Fore.WHITE + "Token Balance: " + Fore.CYAN + f"{balance}" + Fore.WHITE)

        # Get contract source code from CronoScan
        url_contract_details = f'https://api.cronoscan.com/api?module=contract&action=getsourcecode&address={contract_address}&apikey={api_key}'
        response_contract_details = requests.get(url_contract_details)

        try:
            data_contract_details = response_contract_details.json()
        except ValueError:
            print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Failed to decode JSON response from CronoScan API for contract details")
            return

        if data_contract_details['status'] == "1":
            source_code = data_contract_details['result'][0]['SourceCode']
            match = re.search(r"pragma solidity\s+([^\s]+);", source_code)
            if match:
                solidity_version = match.group(1)
                print("Solidity Compiler:", solidity_version)

                time.sleep(2)

                print("")
                print("")
                print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " CONTRACT CODE" + Fore.CYAN)
                print("")
                print("")
                print(source_code)
                print("")
                print("")

                if not os.path.exists("cro_check"):
                    os.makedirs("cro_check")

                filename = os.path.join("cro_check", contract_address + ".sol")
                if os.path.exists(filename):
                    print(Fore.WHITE + "[" + Fore.RED + "avoided" + Fore.WHITE + "]" + Fore.YELLOW + " .sol already exists." + Fore.WHITE)
                else:
                    with open(filename, "w") as f:
                        f.write(source_code)
                    print(Fore.CYAN + "Contract source code saved at " + Fore.CYAN + f"{filename}" + Fore.WHITE)

                solidity_version_numbers = re.findall(r'\d+\.\d+\.\d+', solidity_version)
                if solidity_version_numbers:
                    solidity_version = solidity_version_numbers[0]
                    subprocess.run(["solc-select", "install", solidity_version])
                    print(Fore.YELLOW + f"{solidity_version}" + Fore.CYAN + " solidity compiler successfully downloaded." + Fore.WHITE)
                    subprocess.run(["solc-select", "use", solidity_version])
                    print(Fore.YELLOW + f"{solidity_version}" + Fore.CYAN + " solidity compiler successfully added." + Fore.WHITE)
                    subprocess.run(["slither", filename])
                    print(Fore.GREEN + "[PASSED] " + Fore.WHITE)

                    analyze_with_mistral(source_code)
                else:
                    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + Fore.RED + " Invalid Solidity compiler version")
            else:
                print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " No pragma solidity declaration found in the contract source code.")
        else:
            print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Error retrieving contract details:", data_contract_details['message'])

    else:
        print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + "Data retrieval error:", data_transfers['message'])

## POLYGON SCAN CONTRACT FUNCTION
#######################
#######################

def polygon_scan_contract(contract_address):
    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " perform to Slither attack")
    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " dynamite looks for contract datas .. " + Fore.WHITE)
    print("")

    api_key = 'XUM9KC73EVNM682515IUCQJKC8TFW2GXMI'

    account_address = (contract_address)

    url_transfers = f'https://api.polygonscan.com/api?module=account&action=tokentx&contractaddress={contract_address}&address={account_address}&page=1&offset=100&sort=asc&apikey={api_key}'

    response_transfers = requests.get(url_transfers)
    
    try:
        data_transfers = response_transfers.json()
    except ValueError:
        print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Failed to decode JSON response from Polygonscan API")
        return

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
            print(Fore.GREEN + "[CONTRACT FOUND!]" + Fore.WHITE)
            print("Symbol: " + Fore.CYAN + f"{symbol}" + Fore.WHITE + " | " + Fore.WHITE + "Token Balance: " + Fore.CYAN + f"{balance}" + Fore.WHITE)

        # Get contract source code from Polygonscan
        url_contract_details = f'https://api.polygonscan.com/api?module=contract&action=getsourcecode&address={contract_address}&apikey={api_key}'
        response_contract_details = requests.get(url_contract_details)

        try:
            data_contract_details = response_contract_details.json()
        except ValueError:
            print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Failed to decode JSON response from Polygonscan API for contract details")
            return

        if data_contract_details['status'] == "1":
            source_code = data_contract_details['result'][0]['SourceCode']
            match = re.search(r"pragma solidity\s+([^\s]+);", source_code)
            if match:
                solidity_version = match.group(1)
                print("Solidity Compiler:", solidity_version)

                time.sleep(2)

                print("")
                print("")
                print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " CONTRACT CODE" + Fore.CYAN)
                print("")
                print("")
                print(source_code)
                print("")
                print("")

                if not os.path.exists("poly_check"):
                    os.makedirs("poly_check")

                filename = os.path.join("poly_check", contract_address + ".sol")
                if os.path.exists(filename):
                    print(Fore.WHITE + "[" + Fore.RED + "avoided" + Fore.WHITE + "]" + Fore.YELLOW + " .sol already exists." + Fore.WHITE)
                else:
                    with open(filename, "w") as f:
                        f.write(source_code)
                    print(Fore.CYAN + "Contract source code saved at " + Fore.CYAN + f"{filename}" + Fore.WHITE)

                solidity_version_numbers = re.findall(r'\d+\.\d+\.\d+', solidity_version)
                if solidity_version_numbers:
                    solidity_version = solidity_version_numbers[0]
                    subprocess.run(["solc-select", "install", solidity_version])
                    print(Fore.YELLOW + f"{solidity_version}" + Fore.CYAN + " solidity compiler successfully downloaded." + Fore.WHITE)
                    subprocess.run(["solc-select", "use", solidity_version])
                    print(Fore.YELLOW + f"{solidity_version}" + Fore.CYAN + " solidity compiler successfully added." + Fore.WHITE)
                    subprocess.run(["slither", filename])
                    print(Fore.GREEN + "[PASSED] " + Fore.WHITE)

                    analyze_with_mistral(source_code)
                else:
                    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + Fore.RED + " Invalid Solidity compiler version")
            else:
                print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " No pragma solidity declaration found in the contract source code.")
        else:
            print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Error retrieving contract details:", data_contract_details['message'])

    else:
        print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Data retrieval error:", data_transfers['message'])

## MAIN
#######################
#######################

def display_help():
    help_message = """
    [ - @ A . M s g 0 a - / / - ? - x - = A - ? - ! > - q 9 s x r - < # - C # \ a - a / L ^ s Q t R & ]
    
     27 770 
    x  x   x    | * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    x  x   x    | * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,   
    x  .   x    | * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    x  .   x    | * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    x  .   x    | * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    x  .   .    | * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
            
    # DYNAMITE  | 2.0 Release.

    [ - @ A . M s g 0 a - / / - ? - x - = A - ? - ! > - 7 s 6 2 a - < # - C # \ a - a / L ^ s Q t R & ]
      
    |-----------------------------------------------------------------------------------------------------------------------

    Basic usage:
    
    |                                            (etest > Analyze with Echidna framework) / Soon ...
    | * mtest <chain_name> <contract_address>    (mtest > Analyze with Mythril framework)
    | * stest <chain_name> <contract_address>    (stest > Analyze with Slither framework)
    | * catf <chain_name> <contract_address>     (catf  > Cat functions to target contract)
    |                                           
    |
    | Available chains:  
    |
    | * * * * * * * ETH 
    | * * * * * * * AVAX
    | * * * * * * * BASE
    | * * * * * * * BSC 
    | * * * * * * * CRO
    | * * * * * * * POLYGON
    |
    |
    | * Examples:
    |
    |   > To analyze an Ethereum contract: `python dynamite.py catf ether 0xabcdefghijklmnopq`
    |   > To analyze an Avalanche contract: `python dynamite.py scan avax 0xabcdefghijklmnopq`
    |
    |  [!] ALWAYS MAKE SURE TO SELECT THE CORRECT CHAIN ACCORDING TO YOUR CONTRACT.
    
    |-----------------------------------------------------------------------------------------------------------------------
    
    Mistral PoC:

    | * IN THIS VERSION, DYNAMITE INTEGRATES MISTRAL'S ARTIFICIAL INTELLIGENCE MODELS.
    | * THE ANALYSIS AND PoC GENERATION ARE AUTOMATED BASED ON VULNERABILITIES
    | * IDENTIFIED IN THE CONTRACT, FIRST BY SLITHER TOOLS,
    | * THEN A SECOND TIME BY MISTRAL MODELS WHICH COMBINE BOTH THE CONTRACT'S SOURCE CODE
    | * AND THE VULNERABILITIES FOUND BY SLITHER TO GENERATE AN OPTIMAL POC
    | * USABLE IN FOUNDRY OR HARDHAT ENVIRONMENTS.
    |
    | ### USAGE
    |
    |   > Once the contract analysis is completed by Slither, Dynamite will offer to generate the Mistral PoC.
    |   > Press ENTER and wait for Mistral's models to handle the analysis and PoC generation.
    |
    |   [!] MISTRAL MODELS MAY VARY IN SPEED DEPENDING ON THE CONTRACT SIZE.
    |
    |
    |
    --------------------------------------------- D Y N A M I T E - 2 -----------------------------------------------------
    """
    print(help_message)

def handle_chain_selection(chain):
    chain_map = {
        'eth': ("0xEth.py", "ETHEREUM"),
        'avax': ("0xAvax.py", "AVAX"),
        'base': ("0xBase.py", "BASE"),
        'bsc': ("0xBsc.py", "BSC"),
        'cro': ("0xCro.py", "CRONOS"),
        'poly': ("0xPoly.py", "POLYGON"),
    }

    if chain in chain_map:
        network_file, network_name = chain_map[chain]
        print(Fore.GREEN + "[#]" + Fore.WHITE + " you have chosen the " + Fore.MAGENTA + f"{network_name}" + Fore.WHITE + " network.")
        call_network(network_file)
    else:
        print(Fore.WHITE + "[" + Fore.RED + "ERROR" + Fore.WHITE + "]" + " Invalid chain name! Please retry.")

def main():
    colorama.init(autoreset=True)

    parser = argparse.ArgumentParser(description="Auto Smart-Contract Recon & Analyze Tool")
    parser.add_argument('command', help="Command to execute, e.g., 'chain' or 'catf' or 'stest'")
    parser.add_argument('chain', nargs='?', help="Blockchain network (eth, avax, base, bsc, cro, polygon) or nothing for 'catf' command")
    parser.add_argument('contract_address', nargs='?', help="Contract address to analyze (required for 'catf' command with 'ether' or 'stest' with 'avax')")

    args = parser.parse_args()

    if args.command == 'help':
        display_help()
        return

    if args.command == 'chain':
        if args.chain:
            handle_chain_selection(args.chain)
        else:
            print(Fore.WHITE + "[" + Fore.RED + "ERROR" + Fore.WHITE + "]" + " You must provide a chain name for the 'chain' command.")




    elif args.command == 'mtest':
        if args.contract_address and args.chain == 'eth':
            print("[!] you have chosen to run the mtest program with Etherscan API.")
            eth_myth_scan_contract(args.contract_address)  
        else:
            print(Fore.WHITE + "[" + Fore.RED + "ERROR" + Fore.WHITE + "]" + " You must provide a contract address for the 'mtest' command with 'ether'.")





    elif args.command == 'catf':
        if args.contract_address and args.chain == 'eth':
            print("[!] you have chosen to run the catf program with Etherscan API.")
            call_catf_program_ether_network(args.contract_address)
        elif args.contract_address and args.chain == 'base':
            print("[!] you have chosen to run the scan program with Base API.")
            call_catf_program_base_network(args.contract_address) 
        elif args.contract_address and args.chain == 'bsc':
            print("[!] you have chosen to run the scan program with Bsc API.")
            call_catf_program_bsc_network(args.contract_address)
        elif args.contract_address and args.chain == 'cronos':
            print("[!] you have chosen to run the scan program with Cronos API.")
            call_catf_program_cronos_network(args.contract_address)
        elif args.contract_address and args.chain == 'avax':
            print("[!] you have chosen to run the scan program with Avax API.")
            call_catf_program_avax_network(args.contract_address)
        elif args.contract_address and args.chain == 'polygon':
            print("[!] you have chosen to run the scan program with Polygon API.")
            call_catf_program_polygon_network(args.contract_address)
        else:
            print(Fore.WHITE + "[" + Fore.RED + "ERROR" + Fore.WHITE + "]" + " You must provide a contract address for the 'catf' command with 'ether'.")



    elif args.command == 'stest':
        if args.contract_address and args.chain == 'avax':
            print("[!] you have chosen to run the scan program with Avalanche API.")
            avax_scan_contract(args.contract_address)
        elif args.contract_address and args.chain == 'eth':
            print("[!] you have chosen to run the scan program with Etherscan API.")
            eth_scan_contract(args.contract_address)
        elif args.contract_address and args.chain == 'base':
            print("[!] you have chosen to run the scan program with Base API.")
            base_scan_contract(args.contract_address)
        elif args.contract_address and args.chain == 'bsc':
            print("[!] you have chosen to run the scan program with Bsc API.")
            bsc_scan_contract(args.contract_address)
        elif args.contract_address and args.chain == 'cronos':
            print("[!] you have chosen to run the scan program with Cronos API.")
            cro_scan_contract(args.contract_address)
        elif args.contract_address and args.chain == 'polygon':
            print("[!] you have chosen to run the scan program with Polygon API.")
            polygon_scan_contract(args.contract_address)
        else:
            print(Fore.WHITE + "[" + Fore.RED + "ERROR" + Fore.WHITE + "]" + " You must provide a contract address for the 'scan' command with 'avax'.")
    else:
        print(Fore.WHITE + "[" + Fore.RED + "ERROR" + Fore.WHITE + "]" + " Invalid command! Use 'dyna chain <chain>', 'dyna catf <CONTRACT_ADDRESS> ether', or 'dyna scan <CONTRACT_ADDRESS> avax'.")
        display_help()

if __name__ == "__main__":
    main()
