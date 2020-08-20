from django.db import models

# Create your models here.
class Client(models.Model):
    """Model definition for Client."""
    ir = models.CharField(help_text="Enter IR", max_length=160,null=False,blank=False, verbose_name="IR")
    casetype = models.CharField(help_text="Enter Case Type", max_length=160,null=False,blank=False,verbose_name="Case Type")
    status = models.CharField(help_text="Enter Exhibit Type or Status", max_length=160,null=False,blank=False,verbose_name="Exhibit Type or Status")
    region = models.CharField(help_text="Enter Region or region", max_length=160,null=False,blank=False,verbose_name="Region or District")
    client = models.CharField(help_text="Enter Clients Name", max_length=160,null=False,blank=False,verbose_name="Client Name")
    # Model to register clients to the database

    class Meta:
        """Meta definition for Client."""
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        """Unicode representation of Client."""
        return self.client

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('list-detail', args=[str(self.id)])

    # TODO: Define custom methods here
