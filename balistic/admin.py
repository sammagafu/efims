from django.contrib import admin
from . models import Ballistic,BallisticReport
# Register your models here.

admin.site.register(Ballistic)
admin.site.register(BallisticReport)

# @admin.register(Ballistic)
class BallisticAdmin(admin.ModelAdmin):
    list_display = ('ourref','yourref')
