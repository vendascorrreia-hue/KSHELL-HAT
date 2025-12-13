import os
def sistema1(apt, uni):
    sistema = f"""
cat <<EOF > .kshell/kshell-hat.py
import subprocess
import os
os.system("clear")
print ("obrigado por instalar o kshell-hat, mas devo repetir, qual é seu editor de texto?")
editor = input (" ")
os.system("clear")
print ("bem vindo ao kshell-hat, espero que se divirta!")
while True:
    print ("1.  terminal  2.  loja  3.  editor de texto  4.  gerenciador de arquivos(/) ")
    # Definimos APT_CMD e UNI_CMD como variáveis globais no script gerado:
    APT_CMD = "{apt}"
    UNI_CMD = "{uni}"
    p = input (": ")
    if "1" == p:
        print ("terminal, digite backk para sair, mas aqui é limitado para pastas e arquivos")
        while True:
            t = input (">>> ")
            if "backk" == t:
                break
            else:
                subprocess.run(t, shell=True)
                continue
    if "2" == p:
        print ("digite backk para sair ou [nome do pacote] -u para desistalar algo")
        while True:
            loop = input(": ")
            if "backk" == loop:
                break
            if "-u" in loop:
                    # Use {{ }} para que a f-string seja processada APENAS quando kshell-hat.py rodar
                os.system(f"{{UNI_CMD}} {{loop}}")
            else:
                    # Use {{ }} aqui também
                os.system (f"{{APT_CMD}} {{loop}}")
    if "3" == p:
        os.system(editor)
    if "4" == p:
        os.system("ls -a")
        while True:
            arquivo = input ("qual arquivo que deseja usar/alterar (backk para sair)? ")
            print ("1. mover")
            print ("2. copiar")
            print ("3. deletar")
            while True:
                escolha = input (": ")
                if "1" == escolha:
                    mover = input ("para onde (digite o caminho)? ")
                    os.system(f"mv {{arquivo}} {{mover}}") # Escapando aqui também
                    break
                if "2" == escolha:
                    mover = input ("para a onde (digite o caminho)? ")
                    os.system(f"cp {{arquivo}} {{mover}}") # Escapando aqui também
                if "3" == escolha:
                    os.system (f"rm -rf {{arquivo}}") # Escapando aqui também
                if "backk" == escolha
                    break
                else:
                    print ("erro, comando não encontrado")
                    continue
    else:
        print ("opção invalida, clique enter para repetir")
        input()
EOF
"""
    os.system(sistema)



os.system("mkdir .kshell")
print ("ola amigo(a), essa é a instalação do kshell-hat!!!!")
print ("digite enter para começar: ")


print ("otimo, mas qual é sua distro?")
print ("1.baseadas em BSD")
print ("2.baseadas em arch")
print ("3.baseadas em fedora")
print ("4.baseadas em ubuntu")
while True:
    distro = input ("")

    if "1" == distro:
        sistema1("pkg install ","pkg remove ")
        break
    if "2" == distro:
        sistema1("sudo pacman -S ","sudo pacman -Rns ")
        break
    if "3" == distro:
        sistema1("sudo dnf install","sudo dnf remove")
        break
    if "4" == distro:
        sistema1("sudo apt install","sudo apt remove")
    else:
        print ("opção não encontrada")
        continue
