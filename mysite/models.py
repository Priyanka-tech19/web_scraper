from django.db import models

class Link(models.Model):
    site = models.URLField()  # Field to store the site URL
    address = models.URLField(unique=True)  # Ensure the address is unique
    name = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"{self.name or 'No Name'} - {self.address or 'No Address'}"
        

