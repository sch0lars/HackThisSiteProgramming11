# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                             #
#   Solution to Hack This Site Programming Mission 11         #
#                                                             #
#   Author: Tyler Hooks                                       #
#                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import requests
import re

url = "https://www.hackthissite.org/missions/prog/11/"
referer = "https://www.hackthissite.org/missions/programming/"
# Insert PHP Session ID
cookies = {'PHPSESSID':'InsertPHPSessionIDHere'}
session = requests.Session()
session.headers.update({'referer':referer})
site = session.post(url, cookies = cookies)
code = re.search("String: .*", site.text)[0].split()[1].strip('<br')
shift = int(re.search("Shift: .*", site.text)[0].split()[1].strip("<br"))
answer = ""
for d in re.findall("\d+", code):
    d = (int(d) - shift)%127
    answer += chr(d)

url = "https://www.hackthissite.org/missions/prog/11/index.php"
payload = {'solution':answer}    
site = session.post(url, data = payload, cookies = cookies)
