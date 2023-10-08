from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("23493686"))
API_HASH = getenv("5062e37c3c064eaaf95b3d01318dae96")

BOT_TOKEN = getenv("6579209541:AAHkD3K0JbW1Cco5rqOAqao390sKFbLKxsc")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("5045401884"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/9cd60e6de8355a8866eda.jpg")
START_IMG = getenv("https://telegra.ph/file/9cd60e6de8355a8866eda.jpg")

SESSION = getenv("BACFvzifpja7WBVqV8-rm0Nvy8jVvVUmqU9RQLOUZchLVDgbo09bcpSL_Opbq7jy2UTyZvOIFMsKWKmzR4rOSyXEWQRsYWv_oaDgCZeS5wn3_raO8wYySkuNeF7um3juHHt-CAwmh77sXizB8ABanrU-MvzT5M4tXs7KUBQpuh6pGqGn5ce0CPk3MZLKWDNXYeSA6r9Q6uksp67Qq6XmJLa1Wwm3fGEHYe3AiegKI4UUutipQT0EnRJ1oZyDyu8Tj8pfpdaSRaOsKyXHuMeXE_m9eFK_VPlkveea6BWU3jWkQNUQXhjRaVNf5uECW9Zwxvkhciw14GR_D0TQPXJkpD8bAAAAAWSbXW4A")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Y_AlAA2")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PV_ISCO")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5045401884").split()))


FAILED = "https://telegra.ph/file/9cd60e6de8355a8866eda.jpg"
