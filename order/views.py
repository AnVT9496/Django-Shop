from product.models import Category
from django.contrib import messages
from order.models import ShopCart, ShopCartForm
from django.http.response import  HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('order page')

# @login_required(login_url='/login') # Check login
def addToShopCart(request,id):
    url =  request.META.get('HTTP_REFERER') #get last url
    current_user = request.user #access user session information

    checkproduct = ShopCart.objects.filter(product_id = id) #ccheck product in shopcart
    if checkproduct:
        control = 1 #the product is in cart
    else:
        control = 0 #the product is not in cart

    if request.method == 'POST': #if there is a POST  (for product detail)
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save() #save data
            else: #insert to shopcart
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Product added to Cart")
        return HttpResponseRedirect(url)

    else: #if no POST ( just add one product)
        if control ==1 : #update shopcart
            data = ShopCart.objects.get(product_id = id)
            data.quantity += 1
            data.save()
        else: #insert to shopcart
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
        messages.success(request, "Product added to Cart")
        return HttpResponseRedirect(url)

def shopcart(request):
    category = Category.objects.all()
    current_user = request.user #access user session information
    shopcart = ShopCart.objects.filter(user_id = current_user.id)

    total = 0
    for rs in shopcart:
        total += rs.product.price * rs.quantity
    # return HttpResponse(str(total))
    
    context = {'shopcart': shopcart,
                'category':category,
                'total':total}
    return render(request, 'order/shopcart_products.html', context)

# @login_required(login_url='/login') # Check login
def deletefromcart(request, id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Your item deleted from Shop Cart")
    return HttpResponseRedirect("/shopcart")

