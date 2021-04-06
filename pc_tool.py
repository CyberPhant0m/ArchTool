
import os
import subprocess
import time
from colorama import Fore, Back, Style

def menu():
    try:
        os.system("clear")
        menu = int(input(Back.RED +"""
        Menú de utilidades sobre el sistema Arch - CyberPhantom."""+Back.RESET+
        Back.BLACK + """

        1) Controlar brillo.
        2) Porcentaje de Batería.
        3) Conectar a WPA2.
        4) Bajar-Subir volumen.
        5) Personalizar menú [BlackArch].
        6) Salir
        """+Fore.RED+"""--->:"""+ Back.RESET+Fore.RESET)) 
        return menu
    except ValueError:
        print("Llena los campos.")

def main():
    try:
        opcion = menu()
        if opcion == 1:
            os.chdir("/sys/class/backlight/")
            ubicacion = subprocess.check_output("ls")

            cantidad = int(input(Back.BLACK + """Ingresa el brillo a aplicar [50 (min)- 250 (max)]: """ + Back.RESET))
            archivo = open(f"/sys/class/backlight/{ubicacion.decode('utf-8').strip()}/brightness","w")
            archivo.write(str(cantidad))
            main()

        if opcion == 2:
            bateria = open("/sys/class/power_supply/BAT0/capacity")
            porcentaje = bateria.read()
            print(Back.BLACK+f"Porcentaje de bateria está en {porcentaje.strip()}%"+Back.RESET)
        
        if opcion == 3:
            opcion1 = int(input(Back.BLACK+"""
        1) Conectar a red WPA2.
        2) Crear archivo de configuración y conectar
        :"""+Back.RESET))
            if opcion1 == 1:
                configuracion = str(input(Back.BLACK +"Ingresa la ubicación del archivo de configuración [Ej: /etc/archivo.conf]: "+Back.RESET))
                interfaz1 = str(input(Back.BLACK +"Ingresa la interfáz de red: "+Back.RESET))
                print(Back.BLACK +"Intentando Conectar a red"+ Back.RESET)
                os.system("killall wpa_supplicant")
                os.system(f"wpa_supplicant -B -c {configuracion} -i {interfaz1}")
                os.system(f"dhclient {interfaz1}")
                print(Back.BLACK +"Verifica si ya tienes conexión."+ Back.RESET)
            if opcion1 == 2:
                nombre = str(input(Back.BLACK +"SSID: "+ Back.RESET))
                passwd = str(input(Back.BLACK +"Contraseña: "+ Back.RESET))
                interfaz = str(input(Back.BLACK +"Interfáz de red: "+ Back.RESET))
                archivo1 = str(input(Back.BLACK +"Nombre de archivo de configuración: "+ Back.RESET))
                if interfaz == "" or nombre == "" or passwd == "" or archivo1 == "":
                    print(Back.RED +"Llena los campos, por favor."+ Back.RESET)
                else:
                    print(Back.RED +"Asegurate de que tengas instalado wpa_supplicant [pacman -S wpa_supplicant]"+ Back.RESET)
                    os.system(f"killall wpa_supplicant")
                    os.system(f"wpa_passphrase '{nombre}' '{passwd}' | tee /etc/{archivo1}.conf")
                    os.system(f"wpa_supplicant -B -c /etc/{archivo1} -i {interfaz}")
                    os.system("dhclient")
                    print(Back.BLACK +"Verifica si ya tienes conexión"+Back.RESET)
            else:
                main()
        if opcion == 4:
            porcentaje1 = str(input(Back.BLACK + """Ingresa la cantidad de volumen [Ejemplo: 5- / 5+]:""" + Back.RESET))

            if porcentaje1 != "":
                os.system(f"amixer sset Master playback {porcentaje1}")
            else: 
                main()
        if opcion == 5:
            verificacion = str(input(Back.BLACK +"Está seguro de que desea continuar? Y/n: "+Back.RESET))
            if verificacion == "Y" or verificacion == "y":
                if os.path.exists("sublime-text-3"):
                    os.system("rm -rf sublime-text-3")
                usuario = str(input(Back.BLACK +"Ingresa tu usuario no-root: "+Back.RESET))
                if usuario == "":
                    main()
                os.system("git clone https://aur.archlinux.org/sublime-text-3.git")
                time.sleep(3)
                os.system("rm -rf /var/lib/pacman/db.lck")
                os.system("pacman -S code")
                os.system("pacman -S discord")
                os.system("pacman -S telegram-desktop")
                os.system("pacman -S nautilus")
                os.system("pacman -S flameshot")
                os.system("pacman -S simplescreenrecorder")
                os.system("cp -rf rc.lua /etc/xdg/awesome/")
                print(Back.BLACK+"Entra a la carpeta sublime-text-3 y escribe 'makepkg -si'"+Back.RESET)
                print(Back.BLACK+"Reinicia la sesión gráfica y verifica."+Back.RESET)
            else:
                main()

        if opcion == 6:
            exit()
    except ValueError:
        print("Ingresa un valor.") 
        main()  
    except KeyboardInterrupt:
        print("Cerrado.") 
if __name__ == "__main__":
    main()
