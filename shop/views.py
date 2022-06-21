from django.shortcuts import render, get_object_or_404
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from cart.forms import AddProductForm
from .forms import CheckPasswordForm
from django.contrib.auth.models import User
from django.contrib import messages
from .decorators import login_message_required

# Create your views here.
def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(request, 'shop/list.html', {'current_category': current_category, 'categories': categories, 'products': products})


def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial={'quantity':1})
    return render(request, 'shop/detail.html', {'product':product, 'add_to_cart':add_to_cart})


@login_message_required
def profile_view(request):
    if request.method == 'GET':
        return render(request, 'shop/profile.html')

@login_message_required
def profile_delete_view(request):
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)

        if password_form.is_valid():
            request.user.delete()
            logout(request)
            messages.success(request, "회원탈퇴가 완료되었습니다.")
            return redirect('login')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'shop/profile_delete.html', {'password_form': password_form})