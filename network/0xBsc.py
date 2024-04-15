

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
#                   If you have any questions about this software or require additional permissions, please contact @makaki22.
#

import re
import os
import requests
import colorama
from colorama import Fore
import subprocess
import time

def test_address():
    print("""
          ____
         '-..-'  @makaki22    .-.
        ___||___           .-/ /-.   
       /_______/|         / / / /   (network) BSC 🔗
       |       ||        / / / /
       |   o   |/       / / / / 
       '---`(--' 0x1   />>=<
      
    * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
      """)

    api_key = 'M41SV3B61NEEH55ZZ421ABE7CHWND7SWTW'

    contract_address = input(Fore.RED + "[BSC ADDRESSES ONLY]" + Fore.WHITE + " TARGET CONTRACT >> ")

    account_address = (contract_address)

    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + " dynamite looks for contract datas .. 🔍" + Fore.WHITE)
    print("")

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
                    print(Fore.GREEN + "[200 OK] " + Fore.WHITE)
                else:
                    print(Fore.WHITE + "[" + Fore.YELLOW + "INFO" + Fore.WHITE + "]" + Fore.RED + " Invalid Solidity compiler version")
            else:
                print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " No pragma solidity declaration found in the contract source code.")
        else:
            print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + " Error retrieving contract details:", data_contract_details['message'])

    else:
        print(Fore.WHITE + "[" + Fore.RED + "CRITICAL" + Fore.WHITE + "]" + "Data retrieval error:", data_transfers['message'])

    test_address()

test_address()
