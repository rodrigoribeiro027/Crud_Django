from django.shortcuts import render
from .models import Pessoa
from django.shortcuts import redirect

# Create your views here.
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "index.html" , {'pessoas': pessoas})

def salvar(request):
    nome = request.POST.get("nome")
    Pessoa.objects.create(nome=nome)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html" , {'pessoas': pessoas})


def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html" , {'pessoa': pessoa})

def update(request, id):
    NovoNome = request.POST.get("nome")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = NovoNome
    pessoa.save()
    return redirect(home)

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)
