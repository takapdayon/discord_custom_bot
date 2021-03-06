import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get("ENV_TOKEN")
RIOT_API = os.environ.get("ENV_RIOT_API")
