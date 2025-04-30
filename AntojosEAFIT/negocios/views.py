from django.shortcuts import render
from .models import Categoria
# Create your views here.
def catalogo_view(request):
    return render(request, 'catalogo.html', {
        'emprendimientos': range(1, 21)
    })


def categorias_view(request):
    categorias = Categoria.objects.all()  # Obtén todas las categorías
    return render(request, 'categorias.html', {'categorias': categorias})