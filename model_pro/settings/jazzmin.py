from model_pro.settings import JAZZMIN_SETTINGS, JAZZMIN_UI_TWEAKS

JAZZMIN_SETTINGS.update({
    'navigation_expanded': False,
    "changeform_format": "single",
})

JAZZMIN_UI_TWEAKS.update({
    "navbar": "navbar-primary navbar-dark",
    "no_navbar_border": True,
    "body_small_text": False,
    "navbar_small_text": False,
    "sidebar_nav_small_text": False,
    "accent": "accent-primary",
    "sidebar": "sidebar-dark-primary",
    "brand_colour": "navbar-primary",
    "brand_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "footer_small_text": False
})
