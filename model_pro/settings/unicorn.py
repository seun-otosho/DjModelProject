from model_pro.settings import INSTALLED_APPS

PONIES = True

INSTALLED_APPS = INSTALLED_APPS + [
    "django_unicorn",
    "apps.ponies",
    "unicorn",
]
