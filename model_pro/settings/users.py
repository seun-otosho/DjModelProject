from model_pro.settings import INSTALLED_APPS


INSTALLED_APPS = ["users"] + INSTALLED_APPS

AUTH_USER_MODEL = 'users.MyUser'
