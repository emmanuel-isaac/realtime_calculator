from django.shortcuts import render

from .models import CalculatorData

# Create your views here.
def home(request):
    results = CalculatorData.objects.order_by("-timestamp")[:10]
    operators = ["-", "*", "/", "+"]
    numbers = ["{}".format(num) for num in range(10)]
    calc_elements = operators + numbers

    return render(request, "home.html", {
        'results': results,
        'elements': calc_elements,
    })
