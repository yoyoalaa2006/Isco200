from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/9cd60e6de8355a8866eda.jpg")
START_IMG = getenv("https://telegra.ph/file/9cd60e6de8355a8866eda.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Xu_Mz")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Xu_Mz")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5045401884").split()))


FAILED = "https://telegra.ph/file/9cd60e6de8355a8866eda.jpg"
