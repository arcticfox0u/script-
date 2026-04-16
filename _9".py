cat << 'EOF' > bixo.py
import os, time, sys, random

# -----------------------------------------
# [ ENCRYPTION CORE v7.1 ]
# [ by healingboy85 ]
# [ STATUS: GHOST PROTOCOL ACTIVE ]
# -----------------------------------------

t = {
    "1":"Q","2":"W","3":"E","4":"R","5":"T","6":"Y","7":"U","8":"I","9":"O","0":"P",
    "@":"A","#":"S","$":"D","_":"F","&":"G","+":"H","(":"J",")":"K","/":"L","*":"Z",
    "\"":"X","'":"C",":":"V",";":"B","!":"N","?":"M","-":" ","¿":"?","[":"!",
    "<":",",">":".","°":"-","‰":"%","≠":"=","±":"+","×":"*",
    "£":"Ã","§":"Õ","©":"Ç","€":"É","Ö":"Ô","Ø":"Ó","Į":"Í",
    "⁹":"1","⁸":"2","⁷":"3","⁶":"4","⁵":"5","⁴":"6","³":"7","²":"8","¹":"9","⁰":"0"
}
ti = {v: k for k, v in t.items()}

def efeito_typing(texto, vel=0.02):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(vel)

def fake_loading(texto_status, cor_status="\033[1;30m"):
    os.system("clear")
    print(f"{cor_status}[!] ALTERANDO PROTOCOLO DE TRANSMISSÃO...")
    time.sleep(0.6)
    chars = "0123456789@#$_&+( )/*\"':;!?¿[<>°‰≠±×£§©€ÖØĮ⁹⁸⁷⁶⁵⁴³²¹⁰ABCÇDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(20):
        linha = "".join(random.choice(chars) for _ in range(45))
        print(f"\033[1;30m{linha}")
        time.sleep(0.03)
    os.system("clear")
    print(f"\033[1;32m[+] {texto_status}")
    print("\033[1;30m---------------------------------------------")
    time.sleep(0.8)

while True:
    os.system("clear")
    print("\033[1;32m  ┌" + "─"*45 + "┐")
    print(f"  \033[1;32m│ \033[1;37m(@4'58'-_9\") \033[1;30m| \033[1;32mELITE SYSTEM v7.1 \033[1;32m     │")
    print(f"  \033[1;32m│ \033[1;30mby healingboy85                            \033[1;32m│")
    print("  \033[1;32m└" + "─"*45 + "┘\033[0m")
    
    print("\n\033[1;30m  [ MODO PADRÃO: CÓDIGO -> PORTUGUÊS ]")
    e = input("\033[1;32m  └─\033[1;37m[SYSTEM@BIXO]\033[1;32m# \033[1;37m")
    
    if e.upper() == "SAIR": break
    
    if e == "✦":
        fake_loading("MODO INVERSO ATIVADO (PORT -> BIXO)")
        while True:
            os.system("clear")
            print("\033[1;31m  ┌" + "─"*45 + "┐")
            print(f"  \033[1;31m│ \033[1;37m(@4'58'-_9\") \033[1;30m| \033[1;31mINVERSO PROTOCOL \033[1;31m      │")
            print(f"  \033[1;31m│ \033[1;30mby healingboy85                            \033[1;31m│")
            print("  \033[1;31m└" + "─"*45 + "┘\033[0m")
            
            print("\n\033[1;31m  ◢ \033[1;37mDIGITE EM PORTUGUÊS...")
            e_inv = input("\033[1;31m  └─\033[1;31m[INVERSO]\033[1;37m# \033[1;37m")
            
            if e_inv == "✦" or e_inv.upper() == "VOLTAR":
                fake_loading("MODO PADRÃO REESTABELECIDO", "\033[1;32m")
                break
            
            res_inv = ""
            for char in e_inv.upper(): res_inv += ti.get(char, char)
            
            print(f"\n\033[1;31m  ┏━━━━[ SEQUÊNCIA ENCRIPTADA ]━━━━┓")
            sys.stdout.write("  \033[1;31m┃ \033[1;37m")
            efeito_typing(res_inv, 0.01)
            print(f"\n\033[1;31m  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            input("\n\033[1;30m  [ ENTER PARA CONTINUAR / ✦ PARA VOLTAR ]")
    
    else:
        codigos = "1234567890@#$_&+( )/*\"':;!?¿[<>°‰≠±×£§©€ÖØĮ⁹⁸⁷⁶⁵⁴³²¹⁰"
        if any(c in codigos for c in e):
            res = ""
            for char in e: res += t.get(char, char)
            print(f"\n\033[1;32m  ┏━━━━[ RESULTADO_DECRIPTADO ]━━━━┓")
            sys.stdout.write("  \033[1;32m┃ \033[1;37m")
            efeito_typing(res)
            print(f"\n\033[1;32m  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            input("\n\033[1;30m  [ ENTER PARA REPETIR ]")
EOF
python bixo.py
