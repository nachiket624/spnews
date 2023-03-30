from django.db import models

# Create your models here.


class edittor(models.Model):
    sitepages = (
        ('1', u'Sport'),
        ('2', u'Education'),
        ('3', u'politics'),
    )

    eitName = models.CharField(max_length=200)
    eitPassword = models.CharField(max_length=140)
    accPage = models.CharField(
        max_length=32, choices=sitepages, null=True, blank=True)

    def __str__(self):
        template = '{0.eitName} {0.eitPassword}'
        return template.format(self)


class draft(models.Model):
    sitepages = (
        ('1', u'Sport'),
        ('2', u'Education'),
        ('3', u'Politics'),
    )
    newspage =  models.CharField(max_length=32, choices=sitepages, null=True, blank=False)
    newsthumbnail = models.ImageField(upload_to='images') 
    newstitle = models.CharField(max_length=250,blank=False)
    newspara1 = models.TextField(max_length=800, blank=False)
    newspara2 = models.TextField(max_length=800,blank=False)
    newstime = models.DateTimeField()
    newsauthor = models.CharField(max_length=200,blank=False)
    status = models.CharField(max_length=15,blank=False,default='draft',editable=False)

    def __str__(self):
        template = '{0.newspage} {0.newstitle}'
        return template.format(self)
