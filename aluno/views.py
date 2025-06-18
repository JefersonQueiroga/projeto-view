from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'variavel': 'Olá mundo'}
    return render(request, 'index.html',context)


def list_user(request):
    return render(request,'usuarios.html')

