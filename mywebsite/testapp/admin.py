from django.contrib import admin
from testapp.models import Website
# Register your models here.
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile_number','message']
admin.site.register(Website,WebsiteAdmin)
