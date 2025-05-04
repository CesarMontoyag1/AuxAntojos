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
    entrepreneurs = Entrepreneur.objects.all()
    return render(request, 'entrepreneur_list.html', {'entrepreneurs': entrepreneurs})


def add_product(request, pk):
    entrepreneur = get_object_or_404(Entrepreneur, pk=pk)

    # Map category IDs to category names
    category_mapping = {
        "1": "Dulcesito",
        "2": "Saladito",
        "3": "Accesorios",
        "4": "Bebidas",
        "5": "Servicios",
        "6": "Candies",
    }

    if request.method == 'POST':
        try:
            # Retrieve form data
            name = request.POST.get('name')
            description = request.POST.get('description')
            price = request.POST.get('price')
            image = request.FILES.get('image')
            category_id = request.POST.get('category')  # Get category ID from form

            # Map category ID to category name
            category_name = category_mapping.get(category_id, "")  # Default to empty string if not found

            # Debugging prints
            print(f"Name: {name}")
            print(f"Description: {description}")
            print(f"Price: {price}")
            print(f"Image: {image}")
            print(f"Category ID: {category_id}")
            print(f"Category Name: {category_name}")
            print(f"Entrepreneur: {entrepreneur}")

            # Ensure all required fields are provided
            if not name or not description or not price or not image or not category_name:
                print("Error: Missing required fields.")
                return HttpResponse("Error: All fields are required.")

            # Create the product
            product = Product.objects.create(
                name=name,
                description=description,
                price=price,
                image=image,
                category=category_name,  # Save category name
                entrepreneur=entrepreneur
            )
            print(f"Product created: {product}")
            return render(request, 'product_success.html')  # Redirect to the catalog
        except Exception as e:
            print(f"Error: {e}")
            return HttpResponse(f"Error: {e}")
    return render(request, 'add_product.html', {'entrepreneur': entrepreneur})


def catalogo(request):
    # Group products by category
    categories = Product.objects.values_list('category', flat=True).distinct()
    categorized_products = {category: Product.objects.filter(category=category) for category in categories}

    # Debugging: Print the categorized products
    for category, products in categorized_products.items():
        print(f"Category: {category}, Products: {list(products)}")

    return render(request, 'catalogo.html', {'categorized_products': categorized_products})