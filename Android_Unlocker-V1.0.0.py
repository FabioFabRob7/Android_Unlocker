import subprocess
import webbrowser

print("\n//////////////////////////////////////////////////////\n/                                                    /\n/     Android_Unlocker-V1.1.0____By FabioFabRob7     /\n/                                                    /\n//////////////////////////////////////////////////////")
print("---------------------------------------------------------------------------------------\n-I am not responsible for any problems with your smartphone so proceed with caution!!!-\n---------------------------------------------------------------------------------------\n")
       
#SELECT OS(OPERATING SYSTEM)
       
def OS():
    OS_select = input("Select your PC OS:\n1) Windows\n2) Linux\n")
    if OS_select == "1":
        BrandW()
    elif OS_select == "2":
        ADB_FASTBOOT_L()
    else:
        OS()

#INSTALL ADB AND FASTBOOT FOR LINUX

def ADB_FASTBOOT_L():
    ADB_FASTBOOT_value = input("Welcome to the universal bootloader unlocking tool for almost all Android smartphones. ADB (Android Debug Bridge) and Fastboot will be downloaded for restarting and unlocking the bootloader, you want to continue Y/N:")
    if ADB_FASTBOOT_value == "y" or ADB_FASTBOOT_value == "Y":
        subprocess.call(["sudo","apt","install","adb","fastboot"])
        BrandL()
    elif ADB_FASTBOOT_value == "n" or ADB_FASTBOOT_value == "N":
        exit
    else:
        ADB_FASTBOOT_L()


#FOR WINDOWS

def BrandW():
    BRAND_select = input("Select Brand Smartphone:\n1) Google Pixel\n2) Huawei\n3) Nokia-ONLY_8\n4) Samsung\n5) Sony\n6) Xiaomi\n7) General Devices New\n8) General Devices Old\n")
    if BRAND_select == "1":
        GOOGLE_unlock_W()
    elif BRAND_select == "2":
        HUAWEI_unlock_W()
    elif BRAND_select == "3":
        NOKIA_unlock_W()
    elif BRAND_select == "4":
        SAMSUNG_unlock_W()
    elif BRAND_select == "5":
        SONY_unlock_W()
    elif BRAND_select == "6":
        XIAOMI_unlock_W()
    elif BRAND_select == "7":
        GENERAL_N_unlock_W()
    elif BRAND_select == "8":
        GENERAL_O_unlock_W()
    else:
        BrandW()
def GOOGLE_unlock_W():
    subprocess.call(["adb.exe","devices"])
    subprocess.call(["adb.exe","reboot","bootloader"])
    subprocess.call(["fastboot.exe","devices"])
    subprocess.call(["fastboot.exe","flashing","unlock"])
    input("Follow the procedure on your smartphone and press on unlock bootloader. After the procedure on your smartphone, press enter on your PC to restart the smartphone. . .")
    subprocess.call(["fastboot.exe","reboot"])
def HUAWEI_unlock_W():
    subprocess.call(["adb.exe","devices"])
    subprocess.call(["adb.exe","reboot","bootloader"])
    webbrowser.open("https://hwid5.vmall.com/CAS/portal/loginAuth.html?lang=en-us&validated=true&themeName=red&service=http%3A%2F%2Femui.huawei.com%2Fen%2Fplugin%2Fhwlogin%2Fvalidate%3Fru%3Dhttp%253A%252F%252Femui.huawei.com%252Fen&loginChannel=22000000&reqClientType=2023")
    input("Open web page! Log in and follow the procedures on the official Huawei website! Write down the code they sent to you, YOU WILL NEED IT LATER!\nHit enter when you have the unlock code. . .")
    code = input("Enter the code sent by Huawei: ")
    subprocess.call(["fastboot.exe","devices"])
    subprocess.call(["fastboot.exe","oem","unlock",code])
    input("Follow the procedure on your smartphone and press on unlock bootloader. After the procedure on your smartphone, press enter on your PC to restart the smartphone. . .")
    subprocess.call(["fastboot.exe","reboot"])
def NOKIA_unlock_W():
    subprocess.call(["adb.exe","devices"])
    subprocess.call(["adb.exe","reboot","bootloader"])
    webbrowser.open("https://www.nokia.com/phones/en_int/bootloader")
    input("Open web page! Log in and follow the steps to receive the unlock.key file. Save it in a place where you can find it because you will be prompted for the directory in the next step. Hit enter when you have your bootloader unlock file. . .")
    directory = input("Enter the directory of the unlock.key file sent by Nokia (remember to write unlock.key): ")
    subprocess.call(["fastboot.exe","devices"])
    subprocess.call(["fastboot.exe","flash","unlock",directory])
    subprocess.call(["fastboot.exe","oem","unlock"])
    input("Follow the procedure on your smartphone and press on unlock bootloader. After the procedure on your smartphone, press enter on your PC to restart the smartphone. . .")
    subprocess.call(["fastboot.exe","reboot"])
def SAMSUNG_unlock_W():
    subprocess.call(["adb.exe","devices"])
    subprocess.call(["adb.exe","reboot","bootloader"])
    subprocess.call(["fastboot.exe","devices"])
    subprocess.call(["fastboot.exe","oem","unlock"])
    input("Follow the procedure on your smartphone and press on unlock bootloader. After the procedure on your smartphone, press enter on your PC to restart the smartphone. . .")
    subprocess.call(["fastboot.exe","reboot"])
def SONY_unlock_W():
    subprocess.call(["adb.exe","devices"])
    subprocess.call(["adb.exe","reboot","bootloader"])
    webbrowser.open("https://developer.sony.com/develop/open-devices/get-started/unlock-bootloader/")
    input("Open web page! Select the device you are using at the bottom of the web page and write down the unlock code. YOU WILL NEED IT LATER! If you have the unlock code, press enter. . .")
    code = input("Enter the unlock code sent by Sony: ")
    subprocess.call(["fastboot.exe","devices"])
    subprocess.call(["fastboot.exe","oem","unlock","0x" + code])
    input("Follow the procedure on your smartphone and press on unlock bootloader. After the procedure on your smartphone, press enter on your PC to restart the smartphone. . .")
    subprocess.call(["fastboot.exe","reboot"])
def XIAOMI_unlock_W():
    subprocess.call(["adb.exe","devices"])
    subprocess.call(["adb.exe","reboot","fastboot"])
    webbrowser.open("https://en.miui.com/unlock/download_en.html")
    input("Open web page! Once the download is finished, extract the .zip file and start miflash_unlock.exe and log in. After logging in, press unlock from your PC. . .")
        

def GENERAL_N_unlock_W():
    subprocess.call(["adb.exe","devices"])
    subprocess.call(["adb.exe","reboot","bootloader"])
    subprocess.call(["fastboot.exe","devices"])
    subprocess.call(["fastboot.exe","flashing","unlock"])
    input("Follow the procedure on your smartphone and press on unlock bootloader. After the procedure on your smartphone, press enter on your PC to restart the smartphone. . .")
    subprocess.call(["fastboot.exe","reboot"])
def GENERAL_O_unlock_W():
    subprocess.call(["adb.exe","devices"])
    subprocess.call(["adb.exe","reboot","bootloader"])
    subprocess.call(["fastboot.exe","devices"])
    subprocess.call(["fastboot.exe","oem","unlock"])
    input("Follow the procedure on your smartphone and press on unlock bootloader. After the procedure on your smartphone, press enter on your PC to restart the smartphone. . .")
    subprocess.call(["fastboot.exe","reboot"])


#FOR LINUX


def BrandL():
    BRAND_select = input("Select Brand Smartphone:\n1) Google Pixel\n2) Huawei\n3) Nokia-ONLY_8\n4) Samsung\n5) Sony\n6) Xiaomi\n7) General Devices New\n8) General Devices Old\n")
    if BRAND_select == "1":
        GOOGLE_unlock_L()
    elif BRAND_select == "2":
        HUAWEI_unlock_L()
    elif BRAND_select == "3":
        NOKIA_unlock_L()
    elif BRAND_select == "4":
        SAMSUNG_unlock_L()
    elif BRAND_select == "5":
        SONY_unlock_L()
    elif BRAND_select == "6":
        XIAOMI_unlock_L()
    elif BRAND_select == "7":
        GENERAL_N_unlock_L()
    elif BRAND_select == "8":
        GENERAL_O_unlock_L()
    else:
        BrandL()
def GOOGLE_unlock_L():
    subprocess.call(["adb","devices"])
    subprocess.call(["adb","reboot","bootloader"])
    subprocess.call(["fastboot","devices"])
    subprocess.call(["fastboot","flashing","unlock"])
    input("Follow the procedure on your smartphone and press on unlock bootloader. After the procedure on your smartphone, press enter on your PC to restart the smartphone. . .")
    subprocess.call(["fastboot","reboot"])
def HUAWEI_unlock_L():
    subprocess.call(["adb","devices"])
    subprocess.call(["adb","reboot","bootloader"])
    webbrowser.open("https://hwid5.vmall.com/CAS/portal/loginAuth.html?lang=en-us&validated=true&themeName=red&service=http%3A%2F%2Femui.huawei.com%2Fen%2Fplugin%2Fhwlogin%2Fvalidate%3Fru%3Dhttp%253A%252F%252Femui.huawei.com%252Fen&loginChannel=22000000&reqClientType=2023")
    input("Open web page! Log in and follow the procedures on the official Huawei website! Write down the code they sent to you, YOU WILL NEED IT LATER!\nHit enter when you have the unlock code. . .")
    code = input("Enter the code sent by Huawei: ")
    subprocess.call(["fastboot","devices"])
    subprocess.call(["fastboot","oem","unlock",code])
    input("Follow the procedure on your smartphone and press on unlock bootloader. After the procedure on your smartphone, press enter on your PC to restart the smartphone. . .")
    subprocess.call(["fastboot","reboot"])
def NOKIA_unlock_L():
    subprocess.call(["adb","devices"])
    subprocess.call(["adb","reboot","bootloader"])
    webbrowser.open("https://www.nokia.com/phones/en_int/bootloader")
    input("Open web page! Log in and follow the steps to receive the unlock.key file. Save it in a place where you can find it because you will be prompted for the directory in the next step. Hit enter when you have your bootloader unlock file. . .")
    directory = input("Enter the directory of the unlock.key file sent by Nokia (remember to write unlock.key): ")
    subprocess.call(["fastboot","devices"])
    subprocess.call(["fastboot","flash","unlock",directory])
    subprocess.call(["fastboot","oem","unlock"])
    input("Follow the procedure on your smartphone and press on unlock bootloader. After the procedure on your smartphone, press enter on your PC to restart the smartphone. . .")
    subprocess.call(["fastboot","reboot"])
def SAMSUNG_unlock_L():
    subprocess.call(["adb","devices"])
    subprocess.call(["adb","reboot","bootloader"])
    subprocess.call(["fastboot","devices"])
    subprocess.call(["fastboot","oem","unlock"])
    input("Follow the procedure on your smartphone and press on unlock bootloader. After the procedure on your smartphone, press enter on your PC to restart the smartphone. . .")
    subprocess.call(["fastboot","reboot"])
def SONY_unlock_L():
    subprocess.call(["adb","devices"])
    subprocess.call(["adb","reboot","bootloader"])
    webbrowser.open("https://developer.sony.com/develop/open-devices/get-started/unlock-bootloader/")
    input("Open web page! Select the device you are using at the bottom of the web page and write down the unlock code. YOU WILL NEED IT LATER! If you have the unlock code, press enter. . .")
    code = input("Enter the unlock code sent by Sony: ")
    subprocess.call(["fastboot","devices"])
    subprocess.call(["fastboot","oem","unlock","0x" + code])
    input("Follow the procedure on your smartphone and press on unlock bootloader. After the procedure on your smartphone, press enter on your PC to restart the smartphone. . .")
    subprocess.call(["fastboot","reboot"])
def XIAOMI_unlock_L():
    subprocess.call(["adb","devices"])
    subprocess.call(["adb","reboot","fastboot"])
    webbrowser.open("http://miuirom.xiaomi.com/rom/u1106245679/4.5.813.51/miflash_unlock-en-4.5.813.51.zip")
    input("Download started! Once the download is finished, extract the .zip file and start miflash_unlock.exe and log in. After logging in, press unlock from your PC. . .")
def GENERAL_N_unlock_L():
    subprocess.call(["adb","devices"])
    subprocess.call(["adb","reboot","bootloader"])
    subprocess.call(["fastboot","devices"])
    subprocess.call(["fastboot","flashing","unlock"])
    input("Follow the procedure on your smartphone and press on unlock bootloader. After the procedure on your smartphone, press enter on your PC to restart the smartphone. . .")
    subprocess.call(["fastboot","reboot"])
def GENERAL_O_unlock_L():
    subprocess.call(["adb","devices"])
    subprocess.call(["adb","reboot","bootloader"])
    subprocess.call(["fastboot","devices"])
    subprocess.call(["fastboot","oem","unlock"])
    input("Follow the procedure on your smartphone and press on unlock bootloader. After the procedure on your smartphone, press enter on your PC to restart the smartphone. . .")
    subprocess.call(["fastboot","reboot"])

OS()