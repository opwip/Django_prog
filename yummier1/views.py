from django.shortcuts import render
from .models import Dish, DishCategory


# Create your views here.
def main(request):
    category = DishCategory.objects.filter(is_visible=True)
    dishes_for_category = Dish.objects.filter(is_visible=True)
    return render(request, "yummier1_main.html", {"categories": category, "starter": category[0],
                                                  "dishes": dishes_for_category})
