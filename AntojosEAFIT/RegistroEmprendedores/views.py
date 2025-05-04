from django.shortcuts import render, redirect, get_object_or_404
from .forms import EntrepreneurForm, ProductForm
from .models import Entrepreneur, Product
from django.http import HttpResponse

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
    entrepreneurs = Entrepreneur.objects.prefetch_related('products')  # Use the correct related name
    return render(request, 'entrepreneur_list.html', {'entrepreneurs': entrepreneurs})



def add_product(request, pk):
    entrepreneur = get_object_or_404(Entrepreneur, pk=pk)

    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            description = request.POST.get('description')
            price = request.POST.get('price')
            image = request.FILES.get('image')
            category_id = request.POST.get('category')

            category_mapping = {
                "1": "Dulcesito",
                "2": "Saladito",
                "3": "Accesorios",
                "4": "Bebidas",
                "5": "Servicios",
                "6": "Candies",
            }
            category_name = category_mapping.get(category_id, "")

            if not name or not description or not price or not image or not category_name:
                return HttpResponse("Error: All fields are required.")

            Product.objects.create(
                name=name,
                description=description,
                price=price,
                image=image,
                category=category_name,
                entrepreneur=entrepreneur
            )
            return redirect('product_success', pk=entrepreneur.pk)  # Redirección con pk
        except Exception as e:
            return HttpResponse(f"Error: {e}")
    return render(request, 'add_product.html', {'entrepreneur': entrepreneur})


def view_products(request, pk):
    entrepreneur = get_object_or_404(Entrepreneur, pk=pk)
    products = Product.objects.filter(entrepreneur=entrepreneur)
    return render(request, 'view_products.html', {'entrepreneur': entrepreneur, 'products': products})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    entrepreneur = product.entrepreneur  # Get the associated entrepreneur

    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            description = request.POST.get('description')
            price = request.POST.get('price')
            image = request.FILES.get('image')
            category_id = request.POST.get('category')

            category_mapping = {
                "1": "Dulcesito",
                "2": "Saladito",
                "3": "Accesorios",
                "4": "Bebidas",
                "5": "Servicios",
                "6": "Candies",
            }
            category_name = category_mapping.get(category_id, "")

            if not name or not description or not price or not category_name:
                return HttpResponse("Error: All fields except image are required.")

            # Update the product fields
            product.name = name
            product.description = description
            product.price = price
            product.category = category_name

            if image:  # Update the image only if a new one is provided
                product.image = image

            product.save()
            return redirect('view_products', pk=entrepreneur.pk)  # Redirect to the product list
        except Exception as e:
            return HttpResponse(f"Error: {e}")

    return render(request, 'edit_product.html', {'product': product, 'entrepreneur': entrepreneur})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('view_products', pk=product.entrepreneur.pk)  # Redirect to the product list
    return render(request, 'confirm_delete_product.html', {'product': product})



def product_success(request, pk):
    entrepreneur = get_object_or_404(Entrepreneur, pk=pk)
    return render(request, 'product_success.html', {'entrepreneur': entrepreneur})


def catalogo(request):
    # Group products by category
    categories = Product.objects.values_list('category', flat=True).distinct()
    categorized_products = {category: Product.objects.filter(category=category) for category in categories}

    return render(request, 'catalogo.html', {'categorized_products': categorized_products})