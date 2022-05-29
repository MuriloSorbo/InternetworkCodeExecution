import requests
import json
import os
import time
import subprocess

loadArr = ['|', '/', '--', '\\']
index = 0
mainProcess = None

configFile = open('config.json')
config = json.load(configFile)

url = config['host']

def download_file(req):

    try:
        with open('output/main.py', 'wb') as f:
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
            
        return True, 'Download succeeded!'

    except Exception as ex:
        print(ex)
        return False, 'Download failed :('


while True:

    req = requests.get(url)

    if req.status_code == 204:
        os.system('cls||clear')

        if index >= len(loadArr):
            index = 0

        print(loadArr[index])
        index += 1

    elif req.status_code == 200:
        downloaded, message = download_file(req)
        os.system('cls||clear')

        print(message)

    elif req.status_code == 202:
        downloaded, message = download_file(req)
        os.system('cls||clear')

        print(message)

        if downloaded:
            mainProcess = subprocess.Popen('exec python output/main.py', shell=True)

    elif req.status_code == 409:
        if mainProcess:
            mainProcess.kill()
            print('process terminated!')

    else:
        print('status not recognized')

    time.sleep(2)

