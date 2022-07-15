import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "6435225"))
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
BOT_USERNAME = getenv("BOT_USERNAME", "@misscuitebot")
ARQ_API_KEY = getenv("ARQ_API_KEY", "SBQCPG-YJEYHI-RGOJXR-NLBQMH-ARQ")
BOT_TOKEN = getenv("BOT_TOKEN", "5532932947:AAE5cteaMxyVcgq8ITSn0GXYpXAowVF66oE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
SESSION_NAME = getenv("SESSION_NAME", "AQAt_UpOXUi6aiWcR8_cEhWDC1D5Wye5rGJKoxwiR989bxaVQDJDUgNvOSs_MdleAoqMY-wGdXOmOiOPFRZniTlX5hb9uK4Cr_fFGe917JijetTbC9OFNMZhVPJDH1patcnTWsEhyBAtZWWisGUMe9DPUiRjX5jNAiqsE1jxUjljGLaIlTiJd4CsvXax21aps_rI-3pz8kBMrEQNd8sTw5m-Dtf3-GCrSbydmD38pYH52lam4hFm3vAv2N7hbMaBsrLSom0BE9qJdlSWKaXUq7LwaPOI2ito9TPZ03psdRExu833LXIDUzkVlasb4J5UXcDg1y_wuRQ7gzbBWf6acfqMAAAAATUNt44A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5308191867").split()))
aiohttpsession = aiohttp.ClientSession()
