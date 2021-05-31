from model_pro.settings import INSTALLED_APPS

INSTITUTIONS = True

INSTALLED_APPS += [
    'apps.institutions',
    'apps.addresses',
    'apps.contacts',
    'apps.comments',
]
