from django.shortcuts import render
from store.models import Customer

def say_hello(request):
    query_set = Customer.objects.get(pk=1)
    return render(request, 'hello.html', {"name": "Elias", "customers": query_set})
