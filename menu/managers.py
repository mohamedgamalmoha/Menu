from django.db import models


class CategoryManager(models.Manager):

    def available(self):
        return self.filter(active=True)


class ProductManager(models.Manager):

    def available(self):
        return self.filter(active=True)

    def recent_add(self, days=30):
        return self.available().filter(create_at__day__lte=days).order_by('-create_at')

    def featured(self):
        return self.filter(featured=True).order_by('-create_at')

    def newest(self):
        return self.available().order_by('-create_at')


class GalleryManager(models.Manager):

    def available(self):
        return self.filter(active=True)
