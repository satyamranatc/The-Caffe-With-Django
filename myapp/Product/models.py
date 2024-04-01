from django.db import models

def dish_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/products/assets/<filename>
    return f'products/assets/{filename}'

class Dish(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(max_length=100, upload_to=dish_image_path)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
