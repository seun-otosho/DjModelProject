from dotenv import load_dotenv

load_dotenv()

from model_pro.settings.base import *
from model_pro.settings.users import *
from model_pro.settings.admin import *
from model_pro.settings.jazzmin import *
# from model_pro.settings.ra_erp import *

# from model_pro.settings.unicorn import *

from model_pro.settings.tenants import *
from model_pro.settings.institutions import *
from model_pro.settings.files import *
from model_pro.settings.aws import *
# print(f"{DEFAULT_FILE_STORAGE=}")
