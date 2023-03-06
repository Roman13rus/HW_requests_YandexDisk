import requests
import json
class YaUploader:   # определяем класс загрузчика
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):  #функция получения ссылки для получения заголовков
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
            }
    def get_upload_link(self, file_path):  #функция получения ссылки для загрузки
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path: str): #функция загрузчика  
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self.get_upload_link(file_path='my first resume.md').get("href","")
        response = requests.put(href, data=open('my first resume.md', 'rb'))
        
        print(response.status_code) #для проверки статуса обработки запроса



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    file_path = 'my first resume.md'
    token = '....'
    uploader = YaUploader(token)
    result = uploader.upload('my first resume.md')
   
