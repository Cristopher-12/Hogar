import sys 
import os
import requests
import json
import urllib
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = "1775871252:AAE-503J0CK3y5Yf0pjdvC0Kd_Xt0_PjlBs"

def start(bot,update):
    try:

        username = update.message.from_user.username
        message = "Hola " + username
        update.message.reply_text(message)

    except Exception as e:
        print ("Error001: {}".format(error.args[0]))

def classify(text):
    key = "5fa87800-a2c7-11eb-9e86-fdccf43bc69d434cef89-f8e4-4580-8bed-8d97e9f3a3ef"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def echo(bot,update):
    try:

        text = update.message.text
        demo = classify(text)
        label = demo["class_name"]

        message = "El objeto que ingresaste corresponde a : %s" %(label)
        update.message.reply_text(message)

    except Exception as e:
        print ("Error002: "+type(e).__name__)

def help(bot,update):
    try:

        message = """Tambien puedo reconocer Objetos del Hogar:
            Autos
            Sala
            Cocina
            Dormitorio"""
        update.message.reply_text(message)

    except Exception as e:
        print ("Error003: "+type(e).__name__)

def getImage(bot,update):
    try:

        message = "Analizando imagen"
        update.message.reply_text(message)

        file = bot.getFile(update.message.photo[-1].file_id)
        id = file.file_id
            
        filename = os.path.join("src/","{}.jpg".format(id))

        file.download(filename)

        r = enviar(id)

        update.message.reply_text(r)

    except Exception as e:
        print ("Error007: "+type(e).__name__)

def enviar(id):
    data2 = {'myfile': open('src/{}.jpg'.format(id), 'rb')}

    url = "https://8080-red-crow-k3ybte9c.ws-us03.gitpod.io/upload?"

    result = requests.post(url, files = data2)

    res = result.json()

    respuesta = res["resultado"]

    return respuesta

def error (bot, update, error):
    try:

        print(error)

    except Exception as e:
        print ("Error004: "+type(e).__name__)


    
def main():
    try:
        token = "1775871252:AAE-503J0CK3y5Yf0pjdvC0Kd_Xt0_PjlBs"

        updater = Updater(token)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))

        dp.add_handler(MessageHandler(Filters.text, echo))
        dp.add_handler(MessageHandler(Filters.photo, getImage))

        dp.add_error_handler(error)

        updater.start_polling()
        updater.idle()

    except Exception as e:
        print ("Error005: "+type(e).__name__)
    
if __name__ == "__main__":
    try: 
        main()
    except Exception as e:
        print ("Error006: "+type(e).__name__)
