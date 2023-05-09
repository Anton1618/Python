from django.db import models
from django.core.urlresolvers import reverse
from django.http import Http404


class MenuCategories(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    explicit_url = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    def children(self):
        return self.menucategories_set.all()

    def get_elder_ids(self):
        if self.parent:
            return self.parent.get_elder_ids() + [self.parent.id]
        else:
            return []
