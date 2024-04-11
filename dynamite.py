

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

import os
import subprocess
import colorama
from colorama import Fore

def call_network_eth(OxETH):
    OxETH_path = os.path.join("network", OxETH)
    if os.path.exists(OxETH_path):
        subprocess.run(["python", OxETH_path])
    else:
        print(f"'{OxETH}' was not found in the 'network' folder.")

def call_network_avax(OxAVAX):
    OxAVAX_path = os.path.join("network", OxAVAX)
    if os.path.exists(OxAVAX_path):
        subprocess.run(["python", OxAVAX_path])
    else:
        print(f"'{OxAVAX}' was not found in the 'network' folder.")

def call_network_base(OxBASE):
    OxBASE_path = os.path.join("network", OxBASE)
    if os.path.exists(OxBASE_path):
        subprocess.run(["python", OxBASE_path])
    else:
        print(f"'{OxBASE}' was not found in the 'network' folder.")

def call_network_bsc(OxBSC):
    OxBSC_path = os.path.join("network", OxBSC)
    if os.path.exists(OxBSC_path):
        subprocess.run(["python", OxBSC_path])
    else:
        print(f"'{OxBSC}' was not found in the 'network' folder.")

def call_network_cro(OxCRO):
    OxCRO_path = os.path.join("network", OxCRO)
    if os.path.exists(OxCRO_path):
        subprocess.run(["python", OxCRO_path])
    else:
        print(f"'{OxCRO}' was not found in the 'network' folder.")

def call_network_poly(OxPOLY):
    OxPOLY_path = os.path.join("network", OxPOLY)
    if os.path.exists(OxPOLY_path):
        subprocess.run(["python", OxPOLY_path])
    else:
        print(f"'{OxPOLY}' was not found in the 'network' folder.")



def call_ethereum_network():
    #subprocess.run(["python", "network/0xEth.py"])
    call_network_eth("0xEth.py")
def call_avax_network():
    #subprocess.run(["python", "network/0xAvax.py"])
    call_network_eth("0xAvax.py")
def call_base_network():
    #subprocess.run(["python", "network/0xBase.py"])
    call_network_eth("0xBase.py")
def call_bsc_network():
    #subprocess.run(["python", "network/0xBsc.py"])
    call_network_eth("0xBsc.py")
def call_cronos_network():
    #subprocess.run(["python", "network/0xCro.py"])
    call_network_eth("0xCro.py")
def call_polygon_network():
    #subprocess.run(["python", "network/0xPoly.py"])
    call_network_eth("0xPoly.py")




def main():
    os.system('cls')
    print("""
 |___  | |___  | |___  | |___  | |___  | |___  | |___  | |___  | |___ 
    _|_|    _|_|    _|_|    _|_|    _|_|    _|_|    _|_|    _|_|    _|     ┳┓┓┏┳┓┏┓┳┳┓┳┏┳┓┏┓ 🐋
_  | |___  | |___  | |___  | |___  | |___  | |___  | |___  | |___  | |     ┃┃┗┫┃┃┣┫┃┃┃┃ ┃ ┣  
_|_|    _|_|    _|_|    _|_|    _|_|    _|_|    _|_|    _|_|    _|_|       ┻┛┗┛┛┗┛┗┛ ┗┻ ┻ ┗┛
 |___  | |___  | |___  | |___  | |___  | |___  | |___  | |___  | |___         By @makaki22
    _|_|    _|_|    _|_|    _|_|    _|_|    _|_|    _|_|    _|_|    _|
_  | |___  | |___  | |___  | |___  | |___  | |___  | |___  | |___  | |     [ Auto Smart-Contract Recon & Analyze ]
_|_|    _|_|    _|_|    _|_|    _|_|    _|_|    _|_|    _|_|    _|_|       [ 1. ETHEREUM | 2. AVAX | 3. BASE | 4. BSC | 5. CRONOS | 6. POLYGON ]
          
""")
    
    makakcall0x = input("select network : ")
    print("")
    
    if makakcall0x == '1':
        print("🦥 you have chosen the ETHEREUM network.")
        call_ethereum_network()
    elif makakcall0x == '2':
        print("🐦 you have chosen the AVAX network.")
        call_avax_network()
    elif makakcall0x == '3':
        print("🐬 you have chosen the BASE network.")
        call_base_network()
    elif makakcall0x == '4':
        print("🦘 you have chosen the BSC network.")
        call_bsc_network()
    elif makakcall0x == '5':
        print("🦏 you have chosen the CRONOS network.")
        call_cronos_network()
    elif makakcall0x == '6':
        print("🦑 you have chosen the POLYGON network.")
        call_polygon_network()
    else:
        print(Fore.WHITE + "[" + Fore.RED + "ERROR" + Fore.WHITE + "]" + " Invalid choice ! please retry.")

if __name__ == "__main__":
    main()
