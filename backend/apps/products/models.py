from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products/", blank=True, null=True, help_text="Main thumbnail image")
    video = models.FileField(upload_to="products/videos/", blank=True, null=True, help_text="Product showcase video")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/gallery/")
    alt_text = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} Gallery Image"