from django.shortcuts import render
from .models import Client


def register_client(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'hw_table.html', context)


def detail_client(request, id):
    client = Client.objects.get(id=id)
    context = {
        'client': client
    }
    return render(request, 'client.html', context)