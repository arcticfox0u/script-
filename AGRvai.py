cat << 'EOF' > bixo.py
import os, sys, time

t = {
    "1":"Q","2":"W","3":"E","4":"R","5":"T","6":"Y","7":"U","8":"I","9":"O","0":"P",
    "@":"A","#":"S","$":"D","_":"F","&":"G","+":"H","(":"J",")":"K","/":"L","*":"Z",
    "\"":"X","'":"C",":":"V",";":"B","!":"N","?":"M","-":" ","¿":"?","[":"!",
    "<":",",">":".","°":"-","‰":"%","≠":"=","±":"+","×":"*",
    "£":"Ã","§":"Õ","©":"Ç","€":"É","Ö":"Ô","Ø":"Ó","Į":"Í",
    "⁹":"1","⁸":"2","⁷":"3","⁶":"4","⁵":"5","⁴":"6","³":"7","²":"8","¹":"9","⁰":"0"
}
ti = {v: k for k, v in t.items()}

def processar(linhas, dicionario):
    resultado = []
    for linha in linhas:
        if linha.strip() == "":
            resultado.append("-----------------------------------")
        else:
            res = "".join([dicionario.get(char.upper() if dicionario == ti else char, char) for char in linha])
            resultado.append(res)
    return resultado

def mostrar_resultado(lista_res, cor, titulo):
    os.system("clear")
    print(f"{cor}  ◢◤  {titulo}  ◥◣")
    print(f"{cor}  ┏" + "━"*45 + "┓")
    for l in lista_res:
        print(f"{cor}  ┃ \033[1;37m{l}")
    print(f"{cor}  ┗" + "━"*45 + "┛")
    print("\n\033[1;33m  [ COPIE O TEXTO ABAIXO ]\n\033[1;37m")
    print("\n".join(lista_res))
    print("\033[1;30m\n  " + "."*45)
    input(f"\n{cor}  [ ENTER PARA VOLTAR ]")

modo_inverso = False

while True:
    os.system("clear")
    cor_menu = "\033[1;31m" if modo_inverso else "\033[1;32m"
    
    print(f"{cor_menu}  ╔" + "═"*45 + "╗")
    print(f"  {cor_menu}║ \033[1;37mBY: HEALINGBOY85 \033[1;30m| \033[1;32mv10.6 \033[1;32m       {cor_menu}║")
    print(f"  {cor_menu}║ \033[1;30m[ ✦ ]= Mudar Modo  |  [ ♰ ]= Traduzir Texto {cor_menu}║")
    print(f"{cor_menu}  ╚" + "═"*45 + "╝\033[0m")
    
    try:
        msg = input(f"\n{cor_menu}  └─> \033[1;37m")
    except EOFError: break
    
    if msg.upper() == "SAIR": break
    if msg == "✦":
        modo_inverso = not modo_inverso
        continue

    if msg == "♰":
        while True:
            os.system("clear")
            tit_criacao = "MODO DE CRIAÇÃO (VERMELHO)" if modo_inverso else "TRADUÇÃO DE TEXTO (VERDE)"
            print(f"{cor_menu}  ◢◤  {tit_criacao}  ◥◣")
            print(f"\033[1;30m  (Digite ♰ sozinho e dê CTRL+D para SAIR)\n")
            try:
                entrada_longa = sys.stdin.read().splitlines()
            except EOFError: break
            if len(entrada_longa) == 1 and entrada_longa[0] == "♰": break
            if entrada_longa:
                res_lista = processar(entrada_longa, ti if modo_inverso else t)
                mostrar_resultado(res_lista, cor_menu, "TEXTO PROCESSADO")
            else: break
        continue

    if msg.strip() != "":
        res_lista = processar([msg], ti if modo_inverso else t)
        mostrar_resultado(res_lista, cor_menu, "RESPOSTA RÁPIDA")
EOF
python b
ixo.py
