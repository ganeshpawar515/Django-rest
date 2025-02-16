from django.shortcuts import render,redirect
from .models import Product,Cart,CartItem
from django.contrib.auth.decorators import login_required
# Create your views here.

# @login_required(login_url="login")
def home(request):
    pizzas = Product.objects.all()
    return render(request, "pizza/home.html",{"products":pizzas})
@login_required(login_url="login")
def cart(request,product_id=None):
    if request.method=="GET":
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.items.all()
        total_price=cart.get_total_cost()
        return render(request, "pizza/getCart.html", {"cart_items": cart_items, "total_price": total_price})
    if request.method=="POST":
        u_product=Product.objects.get(id=product_id)
        u_cart,created = Cart.objects.get_or_create(user=request.user)
        print("quant:",request.POST)
        # cart_item, created = CartItem.objects.get_or_create(cart=u_cart,product=u_product,quantity=request.POST["quantity"])
        cart_item_exists = CartItem.objects.filter(cart=u_cart,product=u_product).exists()
        if cart_item_exists:
            cart_item = CartItem.objects.get(cart=u_cart,product=u_product)
            cart_item.quantity+=int(request.POST["quantity"])
            cart_item.save()
            return redirect('get_cart')
        else:
            cart_item = CartItem.objects.create(cart=u_cart,product=u_product,quantity=request.POST["quantity"])
            cart_item.save()
            return redirect('get_cart')
        
def cart_remove_all(request):
    print("delete request received")
    u_id = request.user.id
    cart=Cart.objects.get(user=u_id)
    cart.items.all().delete()
    return redirect("get_cart")
