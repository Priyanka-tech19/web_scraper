from django.contrib import admin
from .models import Link

# Register your models here.
admin.site.register(Link)

admin.site.site_header = "Scraper's Control Room"
admin.site.site_title = "Scraper Admin"
admin.site.index_title = "Welcome to the Scraper's Hub"
