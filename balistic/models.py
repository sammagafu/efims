from django.db import models

from pages.models import Client

# Create your models here.

class Ballistic(models.Model):
    """Model definition for Ballistic."""
    ourref = models.CharField(verbose_name="Our REF", max_length=100,unique=True,null=False)
    yourref = models.CharField(verbose_name="Your REF", max_length=100,unique=True,null=False)
    station = models.CharField(help_text="Enter Police Station", max_length=160,null=False,blank=False,verbose_name="Police Station")
    article = models.TextField(verbose_name="Article or Exhibits Received")
    examination = models.TextField(verbose_name="Type of Examination")
    addition = models.TextField(verbose_name="Addition Information")
    received_date = models.DateTimeField(verbose_name="Date Received", auto_now=True, auto_now_add=False)
    receicer = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name="receiver",verbose_name="receiving officer")
    deliver = models.ForeignKey(Client,on_delete=models.CASCADE,related_name="deliver",verbose_name="delivering officer")
    viewed  = models.BooleanField(default=False)



    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Ballistic."""
        verbose_name = 'Ballistic'
        verbose_name_plural = 'Ballistics'

    def __str__(self):
        return self.ourref
        
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('ballistic:details', args=[str(self.id)])

    # TODO: Define custom methods here

class BallisticReport(models.Model):
    case = models.OneToOneField(Ballistic,on_delete=models.CASCADE,related_name="case",verbose_name="case")
    report = models.TextField()
    # approved = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name="approval",verbose_name="approved by")
    reported_by = models.OneToOneField('auth.User',on_delete=models.CASCADE,related_name="officer_report",verbose_name="reported by")
    approve  = models.BooleanField(default=False)
    approved = models.OneToOneField('auth.User',on_delete=models.CASCADE,related_name="officer_approval",verbose_name="approved by",null=True,blank=True)


    class Meta:
        verbose_name = "Ballistic Report"
        verbose_name_plural ="Ballistic Reports"

    def __str__(self):
        return self.report

    def get_absolute_url(self):
        return reverse("ballistic:detail", kwargs={"pk": self.case})
