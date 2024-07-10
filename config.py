import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6728704718:AAHbgt-igQ0pfqderXjQtG2IdYNPQw-Wj7I")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25912801"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f14e8717578935103e2774559184a345")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://pranchal1419:<password>@cluster0.gicdshq.mongodb.net/")
