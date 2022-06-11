import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "6435225"))
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
BOT_USERNAME = getenv("BOT_USERNAME", "Techno_x_Robot")
ARQ_API_KEY = getenv("ARQ_API_KEY", "PQKVDY-NXSGJC-CIXQUY-BNKUKE-ARQ")
BOT_TOKEN = getenv("BOT_TOKEN", "5289196395:AAFwgLobxKhXpm6Zk8KxNych00bKnSTpeDM")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
SESSION_NAME = getenv("SESSION_NAME", "BQCqg8plECpv_3IBQWXdqhFPvJac4gAtsmiFgGoWLfOJmYkLzJeYpCFM31kG_f3JxQNax5MC27EKktGsvKee7OfwIoLtrUtIxHHrMGp-bm1ecaf1s5G467GDbtJ-4PhAdiHfJjozJp1uFK8Lroq0HW6MVyoaTbJyBLBhkAP_x0k5CPpzNqQciwHKOnUJ0oRGWV3-PBTgVdbX7MiWrDdxJP9Ebxa-KYSRsn9Pqk2TBwpuHo5y5kj6mn1oqKSLaJ0Vu5xqEQxPQXInxso2BOdQqbhlzPh36X6XYXEcP50lYq7O9lAvMx1satIeBiWV2XsHSqapTEw3G-hcC7USb0MnteSRAAAAATxgHa4A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5307899310").split()))
aiohttpsession = aiohttp.ClientSession()
