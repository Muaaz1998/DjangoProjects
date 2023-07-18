from django.shortcuts import redirect, render

def register(request):
    if request.method == 'POST':
        return redirect('register')
    else:
        return render(request, 'login.html')

