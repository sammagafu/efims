from django.db import models
from pages.models import Client

# Create your models here.
class BiologyPF180(models.Model):
    """Model definition for Biology."""
    ref = models.CharField(verbose_name="REF C F", max_length=100,blank=False,null=False)
    date = models.DateTimeField(verbose_name="Date Created",auto_now_add=True)
    casecf = models.CharField(verbose_name="Exhibits in Case CF", max_length=100,null=False,blank=False)
    united = models.CharField(verbose_name="United Republic V", max_length=100,null=False,blank=False)
    venue = models.CharField(verbose_name="The case will be held on", max_length=100,null=False,blank=False)
    brief = models.TextField()
    receicer = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name="receiving_officer",verbose_name="receiving officer")
    deliver = models.ForeignKey(Client,on_delete=models.CASCADE,related_name="delivering_officer",verbose_name="delivering officer")
    # back page details
    exihibit_marked = models.CharField(verbose_name="Exihibit Marked", max_length=50)
    exihibit_description = models.CharField(verbose_name="Description of exihibit", max_length=160)
    points = models.CharField(verbose_name="Points of which Opinions is required", max_length=160)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Biology."""

        verbose_name = 'Biology or DNA PF180'
        verbose_name_plural = 'Biology or DNA PF180'

    def __str__(self):
        """Unicode representation of Biology."""
        return self.ref

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('dna:detail', kwargs={'pk': self.pk})

class PoliceForm113(models.Model):
    """Model definition for PoliceForm114."""
    date = models.DateTimeField(verbose_name="date",auto_now_add=True)
    Station = models.CharField(verbose_name="Station", max_length=160,null=False,blank=False)
    receicer = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name="checked_by",verbose_name="Checkd and Received by")
    correspondin = models.CharField(verbose_name="Correspondence in", max_length=100,null=False,blank=False)
    correspondout = models.CharField(verbose_name="Correspondence Out", max_length=100,null=False,blank=False)
    articles = models.TextField(verbose_name="Articles Received")
    articlesrtn = models.TextField(verbose_name="Articles Returned")
    brief = models.TextField(verbose_name="Brief Particulars of Case")
    purpose = models.TextField(verbose_name="Purpose Of Examination")
    eximiner = models.ForeignKey(Client,on_delete=models.CASCADE,related_name="eximiner",verbose_name="Eximined by")
    # file = models.FileField(, upload_to='uploads', max_length=100)
    # photo = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)





    # TODO: Define fields here

    class Meta:
        """Meta definition for PoliceForm114."""

        verbose_name = 'Police Form 113'
        verbose_name_plural = 'Police Form113'

    def __str__(self):
        """Unicode representation of PoliceForm114."""
        return self.brief

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('police-detail', kwargs={'pk': self.pk})
