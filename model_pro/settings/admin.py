from typing import Dict, Any

from model_pro.settings import INSTALLED_APPS

INSTALLED_APPS = [
    'jazzmin',
] + INSTALLED_APPS

JAZZMIN_SETTINGS: Dict[str, Any] = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Osher Admin",
    # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Osher",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to Osher",
    # Copyright on the footer
    "copyright": "Osher Labs",

    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "users.MyUser",

    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Admin", "url": "admin:index", "permissions": ["auth.view_user"]},

        # # SWAG Links
        # {"name": "CMS", "url": "wagtailadmin_home", "permissions": ["auth.view_user"]},
        # {"name": "Pages", "url": "wagtailadmin_explore_root", "permissions": ["auth.view_user"]},
        # {"name": "Documents", "url": "wagtailadmin_home", "permissions": ["auth.view_user"]},
        # {"name": "Images", "url": "wagtailadmin_home", "permissions": ["auth.view_user"]},

        # # external url that opens in a new window (Permissions can be added)
        # {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        # model admin to link to (Permissions checked against model)
        {"model": "users.MyUser"},
        # # App with dropdown menu to all its models pages (Permissions checked against models)
        # {"app": "books"},
        # {"app": "loans"},
    ],


# Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # # Add a language dropdown into the admin
    # "language_chooser": True,


}

JAZZMIN_UI_TWEAKS = {
    # "navbar_small_text": False,
    # "footer_small_text": False,
    # "body_small_text": False,
    # "brand_small_text": False,
    # "brand_colour": False,
    # "accent": "accent-primary",
    # "navbar": "navbar-white navbar-light",
    # "no_navbar_border": False,
    "navbar_fixed": True,
    # "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,
    # "sidebar": "sidebar-dark-primary",
    # "sidebar_nav_small_text": False,
    # "sidebar_disable_expand": False,
    # "sidebar_nav_child_indent": False,
    # "sidebar_nav_compact_style": False,
    # "sidebar_nav_legacy_style": False,
    # "sidebar_nav_flat_style": False,
    # "theme": "default",
    # "dark_mode_theme": None,
    # "button_classes": {
    #     "primary": "btn-outline-primary",
    #     "secondary": "btn-outline-secondary",
    #     "info": "btn-outline-info",
    #     "warning": "btn-outline-warning",
    #     "danger": "btn-outline-danger",
    #     "success": "btn-outline-success",
    # },
}
