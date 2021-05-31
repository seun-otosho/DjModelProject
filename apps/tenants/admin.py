from django.contrib import admin

from .models import Tenant


class TenantAdmin(admin.ModelAdmin):
    list_display = ("name", "subdomain_prefix", "tenant_object", "parent", )
    # list_filter = ["parent", ]

    class Meta:
        model = Tenant


admin.site.register(Tenant, TenantAdmin)
