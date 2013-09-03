# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("This is the home page for storydecoder.com in the oregon.home app.")

def index(request):
    return HttpResponse("This is the idnex page for storydecoder.com in the oregon.home app.")