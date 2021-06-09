from django.shortcuts import render,redirect

# Create your views here.
def products_grid(request):
    
    return render(request,'product-grid.html',{})