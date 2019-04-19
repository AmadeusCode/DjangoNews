from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index/index.html')

def contacts(request):
    return render(request, 'index/contacts.html', {'values': ['Do You Have Any Questions for Me?', '(068) 077-88-99']})
