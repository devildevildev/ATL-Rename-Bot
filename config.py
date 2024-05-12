import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27972068")
API_HASH = os.environ.get("API_HASH", "6e7e2f5cdddba536b8e603b3155223c1")
#BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
TOKEN_ONE = os.environ.get("TOKEN_ONE", "7085546403:AAF7XlHsy2Zin1gs8YL4Y6ronaJK2McaZ_A")

CHANNEL = os.environ.get("CHANNEL", "the_hell_king_updates") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","The_Hell_King_Renamer_BOt") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","the_hell_king_updates") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","Developer_Devil_01")
STRING = os.environ.get("STRING", "")

DB_NAME = os.environ.get("DB_NAME","Cluster0")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://porn:porn@cluster0.yhugro9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

FLOOD = int(os.environ.get("FLOOD", "90"))
LAZY_PIC = os.environ.get("LAZY_PIC", "")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6075512585').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002041484396"))
