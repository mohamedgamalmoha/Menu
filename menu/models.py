from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CategoryManager, ProductManager, GalleryManager


class Category(models.Model):
    name = models.CharField(max_length=120, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(verbose_name=_("Image"), upload_to="categories//%y/%m/%d")
    create_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_('Creation Date'))
    update_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_('Update Date'))
    active = models.BooleanField(default=True, verbose_name=_('Active'))

    objects = CategoryManager()

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['-create_at']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    category = models.ManyToManyField(Category,  related_name='products', verbose_name=_('Category'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True, null=True, verbose_name=_('Image'))
    featured = models.BooleanField(default=False, null=True, verbose_name=_('Featured'))
    create_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_('Creation Date'))
    update_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_('Update Date'))
    active = models.BooleanField(default=True, verbose_name=_('Active'))

    objects = ProductManager()

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ['-create_at']

    def __str__(self):
        return self.name


class Gallery(models.Model):
    product = models.ForeignKey(Product, related_name='galleries', null=True, on_delete=models.CASCADE, verbose_name=_('Product'))
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True, null=True, verbose_name=_('Image'))
    alt = models.CharField(max_length=100, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_('Creation Date'))
    update_at = models.DateTimeField(auto_now=True, null=True, verbose_name=_('Update Date'))
    active = models.BooleanField(default=True, verbose_name=_('Active'))

    objects = GalleryManager()

    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Galleries")
        ordering = ['-create_at']

    def __str__(self):
        return self.product.name
