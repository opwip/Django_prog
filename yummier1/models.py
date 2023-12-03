from django.db import models


# Create your models here.
class DishCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Dish categories"
        ordering = ("order",)

    def __iter__(self):
        dishes = self.dishes.filter(is_visible=True)
        for dish in dishes:
            yield dish

    def __str__(self):
        return f"{self.name}"


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')
    ingredients = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.PositiveSmallIntegerField(blank=True)
    photo = models.ImageField(upload_to="dishes/", blank=True)
    is_visible = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField()

    category = models.ForeignKey(DishCategory, on_delete=models.PROTECT, related_name='dishes')

    class Meta:
        verbose_name_plural = "Dishes"
        ordering = ("order",)
        constraints = [
            models.UniqueConstraint(fields=['order', 'category'], name='unique_order_each_category')
        ]
        unique_together = ['id', 'slug']

    def __str__(self):
        return f"{self.name}"


class Photo(models.Model):
    title = models.CharField(max_length=255, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(True)
    image = models.ImageField(upload_to="photos/")
