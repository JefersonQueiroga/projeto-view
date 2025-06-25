from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'variavel': 'Olá mundo'}
    return render(request, 'index.html',context)


def list_user(request):
    usuarios_banco = [
        {
            'id': 1,
            'nome': 'Ana Silva',
            'email': 'ana.silva@email.com',
            'cpf': '123.456.789-00',
            'status': 'ativo'
        },
        {
            'id': 2,
            'nome': 'Bruno Costa',
            'email': 'bruno.costa@email.com',
            'cpf': '987.654.321-00',
            'status': 'ativo'
        },
        {
            'id': 3,
            'nome': 'Carla Dias',
            'email': 'carla.dias@email.com',
            'cpf': '111.222.333-44',
            'status': 'inativo'
        },
        {
            'id': 4,
            'nome': 'Daniel Souza',
            'email': 'daniel.souza@email.com',
            'cpf': '555.666.777-88',
            'status': 'ativo'
        },
        {
            'id': 5,
            'nome': 'Eduardo Lima',
            'email': 'eduardo.lima@email.com',
            'cpf': '222.333.444-55',
            'status': 'ativo'
        },
        {
            'id': 6,
            'nome': 'Fernanda Oliveira',
            'email': 'fernanda.oliveira@email.com',
            'cpf': '666.777.888-99',
            'status': 'inativo'
        },
    ]
    context= {"usuarios": usuarios_banco}

    return render(request,'usuarios.html',context)

def setup(request,name):
    return render(request,'configuracao.html',{'name':name})