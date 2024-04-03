from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from admins.models.branch import Branch  # nega branch adminni ichida


class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='category', default='default_category.png')
    slug = models.SlugField(unique=True)  # !!!!!!!!!!!!!

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product')


class Product(models.Model):
    category = models.ForeignKey(Category, models.CASCADE)
    name = models.CharField(max_length=100)
    liter = models.FloatField()
    description = models.CharField(max_length=400)
    image = models.ManyToManyField(ProductImage, related_name='product_image')
    price = models.FloatField()
    weight = models.FloatField()
    branches = models.ManyToManyField(Branch, related_name='branch_product')
    tax_code = models.IntegerField(null=True, blank=True)
    warehouse = models.ImageField(null=True, blank=True)
    is_stock = models.BooleanField(default=True)


@receiver(pre_save, sender=Category)
def category_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
