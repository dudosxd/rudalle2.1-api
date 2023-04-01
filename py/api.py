import requests
import base64
from time import sleep 

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

# Определяем функцию для генерации изображения по тексту
def generate(prompt,path):

    # Отправляем запрос на генерацию и получаем идентификатор задачи
    req = requests.post('https://fusionbrain.ai/api/v1/text2image/run', headers=headers ,json = {
        'queueType': 'generate',
        'query': prompt,
        'preset': 1,
        'style': ''
    })
    id = req.json().get('result', {}).get('pocketId', None)

    # Если запрос успешен и есть идентификатор, то ждем результат
    if req.status_code == 201 and id:
        # Пока задача не выполнена, проверяем статус
        while requests.get(f'https://fusionbrain.ai/api/v1/text2image/generate/pockets/{id}/status', headers=headers).json().get('result', '') != 'SUCCESS':
            sleep(0.2)
        # Получаем результат в виде base64-кода
        result = requests.get(f'https://fusionbrain.ai/api/v1/text2image/generate/pockets/{id}/entities', headers=headers)
        newjpgtxt = result.json().get('result', [{}])[0].get('response', [None])[0]
        # Если есть код, то декодируем его в изображение и сохраняем в файл
        if newjpgtxt:
            image_64_decode = base64.b64decode(newjpgtxt) 
            image_result = open(f'{path}/0.png', 'wb')
            image_result.write(image_64_decode)
            return True # Возвращаем True, если все прошло успешно
    return False # Возвращаем False, если что-то пошло не так

