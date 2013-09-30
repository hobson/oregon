# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render



def graph(request):
    nodes = ["node 1", 'node2', 'node3', 'node4']
    edges = [{'from': 1, 'to': 2},{'from': 2, 'to': 3},{'from': 3, 'to': 4}, {'from': 1, 'to': 3},{'from': 2, 'to': 4}]
    return render(request, 'home/base.html', {'data': {'nodes': nodes, 'edges': edges}})

def index(request):
    return HttpResponse("This is the index page for storydecoder.com in the oregon.home app.")
def home(request):
    return HttpResponse("This is the home page for storydecoder.com in the oregon.home app.")
