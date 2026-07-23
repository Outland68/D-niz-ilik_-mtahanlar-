from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    icon_name = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    category = models.ForeignKey(Category, related_name='certificates', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    # Relative path to the JSON file under static/questions/
    # Example: "certdip/colreg_72.json"
    json_file = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
