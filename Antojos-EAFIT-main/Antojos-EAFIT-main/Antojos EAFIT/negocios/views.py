from django.shortcuts import render

# Create your views here.
def catalogo_view(request):
    return render(request, 'catalogo.html', {
        'emprendimientos': range(1, 21)
    })
