from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app2_string(request):
    return HttpResponse('this is my app2_string as response')
def app2_html(request):
    return render(request,'app2_string.html')

