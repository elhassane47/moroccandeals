from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils import timezone
from django.conf import settings


def path(instance, filename):
    return '%s/%s' % (instance.__class__.__name__, filename)


class Location(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        app_label = 'core'
        db_table = 'locations'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, null=False)
    icon = models.ImageField(
        upload_to=path,
        null=True
    )
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Deal(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)

    title = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(
        null=True, blank=True,
        help_text=_('Link to deal')
    )
    thumbnail = models.ImageField(
        upload_to=path,
        blank=True, null=True
    )
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True,
        help_text=_('Price after Deal')
    )
    crossed_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True,
        help_text=_('Price before Deal')
    )

    description = models.TextField(null=True, blank=True)

    start_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('Degree starting date')
    )
    end_date = models.DateField(
        null=True,
        blank=True,
        help_text=_('Degree ending deadline')
    )

    created_at = models.DateTimeField(
        _('created at'),
        auto_now_add=True,
        help_text=_('Used on the certificate as issuing date')
    )
    updated_at = models.DateTimeField(
        _('Updated at'),
        auto_now=True
    )

    category = models.ForeignKey(Category, null=True, related_name='deals',on_delete=models.SET_NULL)

    # add foreign key
    location = models.ForeignKey(Location, default=1, on_delete=models.CASCADE)

    @property
    def slug(self):
        return self.title.replace(" ", "-")[:50]

    @property
    def get_absolute_url(self):
        return reverse(
            'deals:deal-detail',
            kwargs={'slug': self.slug, 'deal_id': self.id})

    @property
    def get_image_url(self):
        if self.thumbnail and hasattr(self.thumbnail, 'url'):
            return self.thumbnail.url
        else:
            return "{}deals/{}".format(settings.MEDIA_URL, "img-2.jpg")

    @property
    def get_reduction(self):
        if self.price and self.crossed_price:
            return 100 - int(self.price/self.crossed_price * 100)

    def clean(self):
        super(Deal, self).clean()
        if not(timezone.now().date() <= self.start_date <= self.end_date):
            raise ValidationError('Invalid start and end datetime')

    class Meta:
        ordering = ['-created_at']
        app_label = 'core'
        db_table = 'Deals'


