import requests
import json
import sys
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from PIL import Image, ImageOps
import numpy as np


token = "1775871252:AAE-503J0CK3y5Yf0pjdvC0Kd_Xt0_PjlBs"

def start(bot, update):
    try:
        username = update.message.from_user.username
        message = "Hola " + username
        update.message.reply_text(message)
    except Exception as error:
        print("Error 001: {}".format(error.args[0]))

def classify(text):
    key = "dd1fb1a0-a18b-11eb-9d21-0188bc1272ec3c0a7a03-be22-45fe-8d89-65d66b2fc6ae"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

    message = params

def echo(bot,update):
    try:

        text = update.message.text
        demo = classify(text)
        label = demo["class_name"]

        message = "El genero de pelicula con el que se relaciona el texto es : %s" %(label)
        update.message.reply_text(message)

    except Exception as e:
        print ("Error002: "+type(e).__name__)


def help(bot, update):
    try:
        message = "Puedes enviar texto o imagenes."
        update.message.reply_text(message)
    except Exception as error:
        print("Error 003 {}".format(error.args[0]))

def error(bot, update, error):
    try:
        print(error)
    except Exception as e:
        print("Error 004 {}".format(e.args[0]))

def getImage(bot, update):
    try:
        message = "Recibiendo imagen"
        update.message.reply_text(message)

        file = bot.getFile(update.message.photo[-1].file_id)
        id = file.file_id

        filename = os.path.join("descargas/", "{}.jpg".format(id))
        file.download(filename)
        
        message = "Imagen guardada"
        update.message.reply_text(message)

        files = { "myfile": open(filename, "rb") }
        message = "Procesando imagen"
        update.message.reply_text(message)
        result = requests.post("https://8080-black-primate-h5eh4yq1.ws-us03.gitpod.io/upload", files = files)
                                
        
        update.message.reply_text(r.text)


    except Exception as e:
        print("Error 007: {}".format(e.args[0]))

def evaluar(bot,filename):
    try:
        message="Verificando la imagen..."
        update.message.reply_text(message)       
        params = {'myfile':filename}
        r = requests.post("https://8080-black-primate-h5eh4yq1.ws-us03.gitpod.io/upload", myfile=files)
        print(r.text)
        update.message.reply_text(r.text)
    except Exception as error:
        print("Error 027 {}".format(e.args[0]))

def main():
    try:
        updater = Updater(token)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))

        dp.add_handler(MessageHandler(Filters.text, echo))
        dp.add_handler(MessageHandler(Filters.photo, getImage))

        dp.add_error_handler(error)

        updater.start_polling()
        updater.idle()
        print("Bot listo")
    except Exception as e:
        print("Error 005: {}".format(e.args[0]))
        
if __name__ == "__main__":

    try:
        main()
    except Exception as error:
        print("Error 006 {}".format(error.args[0]))