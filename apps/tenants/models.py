from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse


class TenantManager(models.Manager):
    def all(self):
        qs = super(TenantManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(TenantManager, self).filter(content_type=content_type, object_id=obj_id).filter(parent=None)
        return qs


class Tenant(models.Model):
    name = models.CharField(max_length=16)
    subdomain_prefix = models.CharField(max_length=16, blank=True, null=True, unique=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    tenant_object = GenericForeignKey('content_type', 'object_id')

    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return str(f"Tenant <{self.name}>")

    def get_absolute_url(self):
        return reverse("tenants:detail", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("tenants:delete", kwargs={"id": self.id})

    def get_update_url(self):
        return reverse("tenants:update", kwargs={"id": self.id})

    def children(self):  # child tenants
        return Tenant.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True


class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        abstract = True
