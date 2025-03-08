from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    # Here 'today' is a variable that we are passing to the template welcome.html
    return render(request, 'home/welcome.html', {'today': datetime.today()})