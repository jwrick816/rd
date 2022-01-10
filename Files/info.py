import os
import requests
import string
stream = os.popen('tasklist | find /i "ngrok.exe" >Nul && curl -s localhost:4040/api/tunnels | jq -r .tunnels[0].public_url')
output = stream.read()

sample_str = output
# Get last 3 character
last_chars = sample_str[-21:]

#url1= 'https://api.telegram.org/bot1718187783:AAGLVyeXsl0xWFhMM4fjYrV3ij7pE04HSt4/sendMessage?chat_id=-418475197&text=Windows-RDP'
url2= 'https://api.telegram.org/bot5017232812:AAG6ts8KVAqVymo4ULN9UdXEj45svM_rS1w/sendMessage?chat_id=-1001734502672&text={}'.format(last_chars)
#requests.get(url1)
requests.get(url2)
