import re
import os
from os import environ
from Script import script
from collections import defaultdict
from pyrogram import Client
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '4770590'))
API_HASH = environ.get('API_HASH', 'e33bf9032335b874acb9c6406f044836')
BOT_TOKEN = environ.get('BOT_TOKEN', '7072168719:AAFtSZT02BErD7WCVi73r3a4whlfUTdEs1Q')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1654334233').split()]
USERNAME = environ.get('USERNAME', "https://telegram.me/IAmVenomStone")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002113810572'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/VenomStoneNetwork')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002038220265 -1002026830023').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://biyerax927:5RRqhXAbDR2P8luy@cluster0.lv1shat.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://sipox67538:21r6EUhj5x5pJgzV@cluster0.vwua2s9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'cluster0')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002113810572'))
QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/55749b0d3eaee3a5b958b.jpg')
START_IMG = environ.get('START_IMG', 'https://telegra.ph/file/eb119179b4d2a13e71163.jpg')
#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL','-1002113810572'))
URL = environ.get('URL', 'file-to-linkbot-d0729a6fc938.herokuapp.com')
EARNFORLINK = 'earn4link.in'
ADRINOLINKS = 'adrinolinks.in'
STICKERS_IDS = ('CAACAgUAAxkBAAJpY2alJkmLwjC0KFjQh310HOV4SQNRAAL1DwACOZkoVevVYW-YUYNKNQQ').split()

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002113810572'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/VenomStoneMovies/2533")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://telegra.ph/file/7a0860885a8c5942c8192.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "7ebeacbdb05bb5e25802b31fa256f421defb5633")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", EARNFORLINK)
SHORTENER_API2 = environ.get("SHORTENER_API2", "a4245c57312ff9942e8b3bbd0a8283aa2a57e38d")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", ADRINOLINKS)
SHORTENER_API3 = environ.get("SHORTENER_API3", "")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", )
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
auth_channel = environ.get('AUTH_CHANNEL', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002155879591'))

# hastags request features
request_channel = environ.get('REQUEST_CHANNEL', '-1002241752271')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
UPI_PAY_LOGS = int(environ.get('UPI_PAY_LOGS', '-1002113810572'))
# bot settings
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', True)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 300))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', False)
