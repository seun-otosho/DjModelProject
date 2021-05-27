"""model_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

# try:
#     if settings.RA_ERP:
#         from ra.admin.admin import ra_admin_site
#         urlpatterns += [
#             path('erp', ra_admin_site.urls),
#         ]
# except:
#     pass

try:
    if settings.PONIES:
        from apps.ponies import urls as ponies_urls
        urlpatterns += [
            # other urls
            path("unicorn/", include("django_unicorn.urls")),
            path("", include(ponies_urls)),
        ]
except:
    pass