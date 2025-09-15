# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "14495099"))
API_HASH = getenv("API_HASH", "2c54ae09ead43077fe57b7ce84cc0f18")
BOT_TOKEN = getenv("BOT_TOKEN", "8262040943:AAEWDhKDFgXtxvafmDxwgNpzlU0CAFrdQ1g")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6335792242").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://windows11joiya_db_user:Dd4968l3TDA1TJHx@cluster0.g15vx1l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "https://t.me/urldec")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003010233505"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "100"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("BQDdLXsAIFZmJOFQ0gnKrCJVF15k4XnLsqyJFAtx7zQFF5ed5Gw3LVEyKM-o_dV4Vzl6L9FA5vOh9wDf3YwMYsSjkJghvWJbVnAQZTB5xzhVAWrCZlyWbsMywhqqHbRVNXLiK0LGwtYTxAHseaRgoFt0Hy7_j4ekLnbhONfRZtIHFR6LBq3As-lOUO47SGNCaqc2BRcH5LUm1kzfhm2c-WHEGsuF6AS2WLb_f6raXTfy5PxmYG6DFau4aZ1SAbXMrlZ0MGFnVpFxHiy_5COQ0e7r1Rd0YnKepSyMST7-6VbiLKsIsLG6euiaqhB8FaPGoJcvpXzKamhaFAuwNoJ_vL1oIRx5cgAAAAF5pIRyAA", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
