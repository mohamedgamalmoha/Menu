from django.db import models


class CategoryManager(models.Manager):

    def available(self):
        return self.filter(active=True)


class ProductManager(models.Manager):

    def available(self):
        return self.filter(active=True)

    def recent_add(self, days=30):
        return self.available().filter(created_at__day__lte=days)

    def featured(self):
        return self.filter(featured=True)


class GalleryManager(models.Manager):

    def available(self):
        return self.filter(active=True)
