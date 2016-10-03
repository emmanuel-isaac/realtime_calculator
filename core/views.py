from django.shortcuts import render

from .models import CalculatorData

# Create your views here.
def home(request):
    results = CalculatorData.objects.order_by("-timestamp")[:10]
    operators = ["-", "*", "/", "+"]

    return render(request, "home.html", {
        'results': results,
        'operators': operators,
    })
