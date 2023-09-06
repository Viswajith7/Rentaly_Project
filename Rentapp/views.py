from django.shortcuts import render, redirect
from backapp.models import categorydb, Productdb, Contactdb
from Rentapp.models import user_reg,Booking,Payment
from django.db.models import Sum
from django.contrib import messages



# Create your views here.

def Homepage(request):
    data = categorydb.objects.all()
    return render(request, "Home_page.html", {"data": data})


def About_page(request):
    return render(request, "About_page.html")


def Product_page(request, catg):
    products = Productdb.objects.filter(Category_names=catg)
    return render(request, "Product_page.html", {'products': products})


def Single_product(request, dataid):
    data = Productdb.objects.get(id=dataid)
    return render(request, "Single_product.html", {'data': data})

def news(request):
    return render(request,"News_page.html")

def BLog_single(request):
    return render(request,"Blog_single.html")


def Contact_page(request):

    return render(request, "Contact_page.html")




def Save_contact(request):
    if request.method == "POST":
        na = request.POST.get('Name')
        em = request.POST.get('Email')
        ph = request.POST.get('phone')
        mes = request.POST.get('message')
        obj = Contactdb(Name=na, Email=em, Number=ph, Message=mes)
        obj.save()
        return redirect(Contact_page)



def User_loginpage(request):

    return render(request, "User_loginpage.html")


def Savereg(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        pas = request.POST.get('password')
        cpa = request.POST.get('cpassword')
        obj = user_reg(Name=na, Email=em, Password=pas, Cpassword=cpa)
        obj.save()
        return redirect(User_loginpage)


def user_login(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if user_reg.objects.filter(Name=username_r, Password=password_r).exists():
            request.session['usernamel'] = username_r
            request.session['passwordl'] = password_r
            messages.success(request, "Login  succesfully")



            return redirect(Homepage)
        else:
            return redirect(User_loginpage)
    return redirect(User_loginpage)



def user_logout(request):
    del request.session['usernamel']
    del request.session['passwordl']
    return redirect(User_loginpage)



def Savebooking(request):
    if request.method == "POST":
        pl = request.POST.get('PickupLocation')
        dl = request.POST.get('DropoffLocation')
        pd = request.POST.get('PickUpDate')
        pt = request.POST.get('PickUpTime')
        nd = request.POST.get('Qty')
        tp = request.POST.get('totalprice')
        car=request.POST.get('car')
        us= request.POST.get('user')
        pr=request.POST.get('price')
        data_id=request.POST.get('image')
        pimage=Productdb.objects.get(id=data_id)
        img=pimage.P_Image1
        obj = Booking(PickupLocation=pl, DropoffLocation=dl, PickUpDate=pd, PickUpTime=pt,No_days=nd,Totalprice=tp,Car=car,User=us,P_image=img,Price=pr)
        obj.save()
        return redirect(Cart)



def Cart(request):
    data=Booking.objects.filter(User=request.session['usernamel'])
    grand_total=data.aggregate(Sum("Totalprice"))["Totalprice__sum"]
    return render(request,"Cart_page.html",{'data':data,"grand_total":grand_total})


def Delete_cart(request, dataid):
    data = Booking.objects.filter(id=dataid)
    data.delete()

    return redirect(Cart)



def Checkout(request):
    data=Booking.objects.filter(User=request.session['usernamel'])
    return render(request, "Checkout_page.html",{'data':data})

def saveCheckout(request):
    if request.method == "POST":
        fn=request.POST.get('fname')
        sn=request.POST.get('sname')
        cu=request.POST.get('country')
        ad=request.POST.get('address')
        ci=request.POST.get('city')
        pi=request.POST.get('pin')
        ph=request.POST.get('phone')
        em=request.POST.get('email')
        op=request.POST.get('optradio')
        obj=Payment(Fname=fn,sname=sn,Country=cu,Address=ad,City=ci,Pin=pi,Phone=ph,Email=em,Payment=op)
        obj.save()
        messages.success(request, "Order Placed Succesfully")

        return redirect(Checkout)



