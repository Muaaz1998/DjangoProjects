from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request) -> HttpResponse:
    num1, num2 = int(request.GET.get('number1')), int(request.GET.get('number2'))

    if request.GET.get('add') == "":
        ans = num1 + num2
    elif request.GET.get('subtract') == "":    
        ans = num1 - num2
    elif request.GET.get('multiply') == "":    
        ans = num1 * num2
    else:
        ans = num1 / num2
        
    return render(request, 'home.html', {'ans': ans})
    

    