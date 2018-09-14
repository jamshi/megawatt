from django.db import models
from .managers import SiteManager

class Site(models.Model):

    objects = SiteManager()

    def __str__(self):
        return u'%s' % self.name

    name = models.CharField(max_length=50, unique=True, verbose_name='Site Name')


# Create your models here.
class SiteDetail(models.Model):

    def __str__(self):
        return u'%s-%s' % (self.site, self.date)

    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    date = models.DateField()
    a_value = models.FloatField()
    b_value = models.FloatField()

    
    
