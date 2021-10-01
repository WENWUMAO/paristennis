import requests
import re
import time
import json
import sys
import pause, datetime

#********************************************************
# 'Pause' will put script in sleep mode until setted time.
# This part is by default commented.
#********************************************************
# dt = datetime.datetime(2021, 4, 11, 8, 0, 0, 0)
# print('sleep until 8am !')
# pause.until(dt)

#********************************************************
#****************** PARAMETERS to set *******************
#********************************************************
login = 'yourname@gmail.com'         # your username
password = '1234abcd'           # your password
equipmentId = '120', # tennis elisabeth 14e
courtId = '1109', # court No 4
startingDate = '2021/04/24 15:00:00', # starting time, SHOULD keep the same date format YYYY/MM/DD HH:MM:SS 
endingDate = '2021/04/24 16:00:00', # ending time, one hour after starting time. SHOULD keep same format YYYY/MM/DD HH:MM:SS.
#********************************************************
#************** Parameter Section END *******************
#********************************************************

#********************************************************
#********************************************************
#****      EXECUTION SECTION. SHOULD NOT MODIFY      ****
#********************************************************
#********************************************************

print('let\'s go!', datetime.datetime.now())

homepage = 'https://tennis.paris.fr/tennis/jsp/site/Portal.jsp?page=recherche&view=recherche_creneau#!'
authPage = 'https://v70-auth.paris.fr/auth/realms/paris/protocol/openid-connect/auth?client_id=moncompte_modal&response_type=code&redirect_uri=https%3A%2F%2Fmoncompte.paris.fr%2Fmoncompte%2Fjsp%2Fsite%2FPortal.jsp%3Fpage%3Dmyluteceusergu%26view%3DcreateAccountModal%26close_modal%3Dtrue&scope=openid&state=3375e317818fd&nonce=2da59198e6dc8&back_url=https%3A%2F%2Ftennis.paris.fr%2Ftennis%2F';

session = requests.Session()

# print('--------- go to search court page -----------')
homeHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,fr;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'https://moncompte.paris.fr/'
}

defaultHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,fr;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Upgrade-Insecure-Requests': '1',
}

defaultPostHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,fr;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Upgrade-Insecure-Requests': '1',
}

print('--------- go to auth page -----------')
firstHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
formResponse = session.get(url=authPage, headers=firstHeaders)
print('first request status', formResponse.status_code)

print('--------- auth -----------')
loginUrl = re.search(r'action="(.+)" role=', formResponse.text).group(1).replace('amp;', '')

loginPayload = {'username': login, 'password': password, 'Submit': ''}
authHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,fr;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Upgrade-Insecure-Requests': '1',
    'Referer': formResponse.url
}
loginResponse = session.post(url=loginUrl, data=loginPayload, headers=authHeaders)

session.get(url='https://moncompte.paris.fr/moncompte/jsp/site/Portal.jsp?page=mydashboard&panel=accueil', headers=defaultHeaders)

homepageAgainResponse = session.get(url=homepage, headers=defaultHeaders)

print('--------- openid redirecting -----------')
openidUrl = 'https://v70-auth.paris.fr/auth/realms/paris/protocol/openid-connect/auth?response_type=code&scope=openid&client_id=moncompte_bandeau&nonce=gazersdf&prompt=none&redirect_uri=https://v70-auth.paris.fr/banner/AccessCode.js'
openidResponse = session.get(url=openidUrl, headers=defaultHeaders)

errorUrl = openidResponse.url

openidResponse = session.get(url=errorUrl.replace('js?', 'jsp?'), headers=defaultHeaders)
openidForm = {
    'code': openidResponse.text.replace('\n',''),
    'grant_type': 'authorization_code',
    'client_id': 'moncompte_bandeau',
    'redirect_uri': 'https://v70-auth.paris.fr/banner/AccessCode.jsp'
}

openidTokenUrl = 'https://v70-auth.paris.fr/auth/realms/paris/protocol/openid-connect/token'
openidTokenResponse = session.post(url=openidTokenUrl, data=openidForm, headers=defaultPostHeaders)

validateSessionUrl = 'https://moncompte.paris.fr/moncompte//rest/banner/api/1/validateSession'
validateSessionForm = {
    'login': 'maowenwu2010@gmail.com'
}
validateSessionResponse = session.post(url=validateSessionUrl, data=validateSessionForm, headers=defaultPostHeaders)

print('-------------select a court-------------')
time.sleep(1)
selectElisabethCourtForm = {
    'equipmentId': equipmentId,
    'courtId': courtId,
    'dateDeb': startingDate,
    'dateFin': endingDate,
    'annulation': 'false'
}
selectCourtUrl = 'https://tennis.paris.fr/tennis/jsp/site/Portal.jsp?page=reservation&view=reservation_creneau'

selectCourtResponse = session.post(
    url=selectCourtUrl,
    data=selectElisabethCourtForm,
    headers= defaultPostHeaders,
    allow_redirects=True)

if selectCourtResponse.text.find('1 / 3 - Validation du court') == -1 :
    print('error while selecting a court')
    sys.exit()

print('-------------validating a court by adding a partner-------------')
time.sleep(1)
validationUrl = 'https://tennis.paris.fr/tennis/jsp/site/Portal.jsp?page=reservation&action=validation_court'
validationForm = {
    'player1': ['OU', 'ZHIHUI', ''],
    'counter': '',
    'submitControle': 'submit'
}

validationCourtResponse = session.post(
    url=validationUrl,
    data=validationForm,
    headers=defaultPostHeaders,
    allow_redirects=True)
my_data_file = open('step2.html', 'w')
my_data_file.write(validationCourtResponse.text)
my_data_file.close()

if validationCourtResponse.text.find('2 / 3 - Mode de paiement') == -1 :
    print('error while validating a partner')
    sys.exit()


print('-------------paying by a ticket-------------')
time.sleep(1)
paymentUrl = 'https://tennis.paris.fr/tennis/jsp/site/Portal.jsp'
paymentForm = {
    'page': 'reservation',
    'action': 'selection_methode_paiement',
    'paymentMode': 'existingTicket',
    'nbTickets': 1
}
validationCourtResponse = session.post(url=paymentUrl, data=paymentForm, headers=defaultPostHeaders)
print('-------------finished-------------')
