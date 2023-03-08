from django.db import models

# Create your models here.
class edittor(models.Model):
    sitepages     = (
        ('1', u'Sport'),
        ('2', u'Education'),
        ('3', u'politics'),
    )

    eitName = models.CharField(max_length=200)
    eitPassword = models.CharField(max_length=140)
    accPage = models.CharField(max_length=32, choices=sitepages, null=True, blank=True)

    def __str__(self):
        template = '{0.eitName} {0.eitPassword}'
        return template.format(self)