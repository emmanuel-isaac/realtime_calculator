from django.shortcuts import render

from .models import CalculatorData

# Create your views here.
def home(request):
    results = reversed(CalculatorData.objects.order_by("-timestamp")[:10])

    print(results)

    return render(request, "home.html", {
        'results': results,
    })
