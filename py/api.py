import requests
import base64
from time import sleep

class rudalleClient:
    def __init__(self):
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryb6ZrB1LvoGELHGVQ',
            'Origin': 'https://fusionbrain.ai',
            'Pragma': 'no-cache',
            'Referer': 'https://fusionbrain.ai/diffusion',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
        }
    def ask(self,prompt='cat', style=''):
        data = \
f'''------WebKitFormBoundaryb6ZrB1LvoGELHGVQ\r
Content-Disposition: form-data; name="queueType"\r
\r
generate\r
------WebKitFormBoundaryb6ZrB1LvoGELHGVQ\r
Content-Disposition: form-data; name="query"\r
\r
{prompt.strip()}
\r
------WebKitFormBoundaryb6ZrB1LvoGELHGVQ\r
Content-Disposition: form-data; name="preset"\r
\r
1
\r
------WebKitFormBoundaryb6ZrB1LvoGELHGVQ\r
Content-Disposition: form-data; name="style"\r
\r
{style.strip()}
\r
------WebKitFormBoundaryb6ZrB1LvoGELHGVQ--\r
    '''

        resp = requests.post('https://fusionbrain.ai/api/v1/text2image/run', headers=self.headers, data=data)
        json = resp.json()
        if json['success'] == True:
            return True, json['result']['pocketId']
        return False, ''
    def check(self,id):
        response = requests.get(
            f'https://fusionbrain.ai/api/v1/text2image/generate/pockets/{id}/status',
            headers=self.headers,
        )
        if response.json()['success'] != True:return False, False
        if response.json()['result'] in ['INITIAL','PROCESSING']: return False, True
        if response.json()['result'] == 'SUCCESS': return True, True
    def load(self,id,path):
        result = requests.get(
            f'https://fusionbrain.ai/api/v1/text2image/generate/pockets/{id}/entities',
            headers=self.headers,
        )
        newjpgtxt = result.json().get('result', [{}])[0].get('response', [None])[0]
        # Если есть код, то декодируем его в изображение и сохраняем в файл
        if newjpgtxt:
            image_64_decode = base64.b64decode(newjpgtxt) 
            image_result = open(f'{path}/0.png', 'wb')
            image_result.write(image_64_decode)
            return True # Возвращаем True, если все прошло успешно


def generate(prompt, path='', style=''):
    client = rudalleClient()
    status, id = client.ask(prompt,style)
    if status != True:return False
    x = client.check(id)[0]
    while x != True:
        sleep(0.5)
        x = client.check(id)[0]
    return client.load(id,path)