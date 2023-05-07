import requests
from PIL import Image
from io import BytesIO



def sendPhoto(TOKEN: str, CHAT_ID: int, caption: str, pathToPhoto: str):


    photo = Image.open(pathToPhoto).convert('RGB')
    SEND_PHOTO = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'

    with BytesIO() as output:
        photo.save(output, format='JPEG')
        output.seek(0)
        send = requests.post(SEND_PHOTO, data={'chat_id': CHAT_ID,'caption':caption}, files={'photo': output.read()}, timeout=10)

    return send



def sendMessage(TOKEN: str, CHAT_ID: int, text: str):

    SEND_MESSAGE = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    send = requests.post(SEND_MESSAGE, data={'chat_id': CHAT_ID,'text':text}, timeout=10)

    return send


