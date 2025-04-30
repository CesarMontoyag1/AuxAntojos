from django.shortcuts import render, redirect, get_object_or_404
from .forms import EntrepreneurForm
from .models import Entrepreneur

# Create your views here.
def create_entrepreneur(request):
    if request.method == "POST":
        form = EntrepreneurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = EntrepreneurForm()
    return render(request, 'create_entrepreneur.html', {'form': form})

def delete_entrepreneur(request, pk):
    entrepreneur = get_object_or_404(Entrepreneur, pk=pk)
    if request.method == 'POST':
        entrepreneur.delete()
        return redirect('entrepreneur_list')
    return render(request, 'confirm_delete.html', {'entrepreneur': entrepreneur})

def success(request):
    return render(request, 'success.html')

def entrepreneur_list(request):
    entrepreneurs = Entrepreneur.objects.all()
    return render(request, 'entrepreneur_list.html', {'entrepreneurs': entrepreneurs})