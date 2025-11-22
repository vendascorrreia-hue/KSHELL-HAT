import os
import webbrowser
def sistema(a, e, au, poweroff, reboot,navegador):
    os.system("clear")
    while True:
        os.system("clear")
        print ("ai embaixo está oque vocẽ pode fazer, divirta-se com o kshell!!")
        print (f"1. editor de texto   2. terminal77   3. loja   4. {navegador}")
        menu = input ("selecione uma opção(ou digite rbt para reiniciar e dsl para desligar) ")
        if "dsl" in menu:
            os.system(f"{poweroff}")
        elif "rbt" in menu:
            os.system(f"{reboot}")
        elif "1" in menu:
            os.system(f"{e} ")
        elif "4" in menu:
            os.system(f"{navegador}")
        elif "3" in menu:
            while True:
                os.system("clear")
                pa = input ("digite o nome do pacote ou backk para voltar(para desistalar,digite o nome do pacote -u): ")
                if "backk" in pa:
                    break
                elif "-u" in pa:
                    os.system(f"{au} {pa}")
                else:
                    os.system(f"{a} {pa}")
        elif "2" in menu:
            os.system("clear")
            print ("terminal. digite backk para voltar")
            while True:
                print (">_<")
                ter = input(">>> ")
                if "backk" in ter:
                    break
                elif "neofetch" or "fastfetch" or "screenfetch" in ter:
                    logo = r'''
                              >>>>>>
                            >>>>>>>>>>            "OS": KSHELL HAT
                        >>>>>>>>>>>>>>>>>>         TIPO: ORIGINAL
                  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    COMPATIBILIDADE: legal :)
                        >>              >>           INTERFACE: NENHUMA
                        >>    >  _  <    >>
                        >>              >>
                          >>>>>>>>>>>>>>
                            >>>>>>>>>>
                        >>>>>>>>>>>>>>>>>>
                        >>>>>>>>>>>>>>>>>>
                         >>>>>>>>>>>>>>>>
                          >>>>>>>>>>>>>>
                           >>>>>>>>>>>>
                            >>>>>>>>>>
                            >        >
                            >        >
                            >        >
                            >        >
                            >>>>     >>>>
'''
                    print(logo)
                elif "pfetch" in ter:
                    print (" - ")
                    print ("---")
                    print (">_<")
                else:
                    os.system(ter)
        else:
            print ("hum, opção invalida, pressione ENTER para voltar")
            input()
os.system("clear")
print ("KSH >_< ELL")
print ("olá, poderia nos dizer qual é o seu sistema (ou baseado em algum desses)")
print ("1. archlinux")
print ("2. ubuntu")
print ("3. Freebsd")
print ("4. Windows")
while True:
    p = input (": ")
    if "1" in p:
        print ("você tem uma instalação simples ou completa(com navegador e etc...)? digite 1 para simples e 2 para completa")
        while True:
           boot = input (" ")
           if "1" in boot:
                editor = input ("editor de texto: ")
                navegador = "lynx"
                os.system(f"sudo pacman -S  --noconfirm {editor} {navegador}")
                os.system("clear")
                input ("otimo, pressione enter para começar a usar o sistema")
                sistema("sudo pacman -S --noconfirm",editor, "sudo pacman -Rns --noconfirm","shutdown now","reboot","lynx")
           elif "2" in boot:
               editor = input ("qual é seu editor de texto? ")
               sistema("sudo pacman -S --noconfirm",editor, "sudo pacman -Rns --noconfirm","shutdown now","reboot","lynx")
    elif "2" in p:
        editor = input ("qual é seu editor de texto? ")
        sistema("sudo apt install -y",editor, "sudo apt remove -y","shutdown now","reboot","lynx")
    elif "3" in p:
        print ("você tem uma instalação simples ou completa(com navegador e etc...)? digite 1 para simples e 2 para completa")
        while True:
           boot = input (" ")
           if "1" in boot:
                editor = input ("editor de texto: ")
                navegador = "lynx"
                os.system(f"sudo pacman -S  --noconfirm {editor} {navegador}")
                os.system("clear")
                input ("otimo, pressione enter para começar a usar o sistema")
                sistema("pkg install",editor, "pkg install","poweroff","reboot","lynx")
           elif "2" in boot:
               editor = input ("qual é seu editor de texto? ")
               sistema("pkg install",editor, "pkg install","poweroff","reboot","lynx")
    elif "4" in p:
        editor = input ("editor de texto: ")
        navegado = input ("navegador: ")
        sistema("winget install",editor, "winget uninstall","shutdown /s /t 00","shutdown /r /t 0",navegado)






