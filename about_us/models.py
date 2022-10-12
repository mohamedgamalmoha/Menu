from django.db import models
from django.core.validators import RegexValidator


PhoneNumberValidator = RegexValidator(r'^[0-9]{10}$', 'Invalid Phone Number')


class MainInfo(models.Model):
    facebook = models.URLField('Facebook link')
    instagram = models.URLField('Instagram link')
    email = models.EmailField('Email')
    phone_number = models.CharField('Whatsapp number', max_length=11, validators=[PhoneNumberValidator, ])

    class Meta:
        verbose_name = 'Website Main Info'
        verbose_name_plural = 'Website Main Info'

    def __str__(self):
        return self.email
