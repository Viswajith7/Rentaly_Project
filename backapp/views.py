from django.shortcuts import render, redirect
from backapp.models import categorydb, Productdb,Contactdb
from Rentapp.models import user_reg,Booking,Payment
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def adminpage(request):
    return render(request, "adminpage.html")


def addcategory(request):
    return render(request, "addcategory.html")


def savecategory(request):
    if request.method == "POST":
        cn = request.POST.get('Cname')
        dis = request.POST.get('C_discription')
        img = request.FILES['C_image']
        obj = categorydb(Category_Name=cn, Discription=dis, C_Image=img)
        obj.save()
        messages.success(request, "Category added  succesfully")
        return redirect(addcategory)


def displaycategory(request):
    data = categorydb.objects.all
    return render(request, "displaycategory.html", {'data': data})



def editcategory(request, dataid):
    data = categorydb.objects.get(id=dataid)
    return render(request, "editcategory.html", {'data': data})


def updatecategory(request, dataid):
    if request.method == "POST":
        CN = request.POST.get('Cname')
        DIS = request.POST.get('C_discription')

        try:
            img = request.FILES['C_image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)

        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).C_Image

        categorydb.objects.filter(id=dataid).update(Category_Name=CN, Discription=DIS, C_Image=file)
        return redirect(displaycategory)


def deletecategory(request, dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    messages.error(request,"Category deleted")

    return redirect(displaycategory)


def Add_product(request):
    data = categorydb.objects.all()
    return render(request, "Add_product.html", {'data': data})


def Save_product(request):
    if request.method == "POST":
        cate = request.POST.get('category')
        car = request.POST.get('car')
        mo = request.POST.get('model')
        hp = request.POST.get('power')
        ce = request.POST.get('ceat')
        bo = request.POST.get('body')
        pr = request.POST.get('price')
        im = request.FILES['image1']
        imm = request.FILES['image2']
        immm = request.FILES['image3']
        di = request.POST.get('discription')
        ti = request.POST.get('transmission')
        ai = request.POST.get('airbag')
        co = request.POST.get('colour')
        obj = Productdb(Category_names=cate, Car_name=car, Model=mo, Hpower=hp, Ceat=ce, Body=bo, Price=pr,
                        Transmission=ti, Airbag=ai,
                        Discriptions=di, Colour=co,P_Image1=im,P_Image2=imm,P_Image3=immm)
        obj.save()
        messages.success(request, "Product saved succesfully")
        return redirect(Add_product)


def Display_product(request):
    data = Productdb.objects.all()
    return render(request, "Display_product.html", {'data': data})


def Edit_product(request, dataid):
    data = Productdb.objects.get(id=dataid)
    da = categorydb.objects.all()

    return render(request, "Edit_Product.html", {'data': data, "da": da})


def Update_product(request, dataid):
    if request.method == "POST":
        cate = request.POST.get('category')
        car = request.POST.get('car')
        mo = request.POST.get('model')
        hp = request.POST.get('power')
        ce = request.POST.get('ceat')
        bo = request.POST.get('body')
        pr = request.POST.get('price')
        ar = request.POST.get('airbag')
        di = request.POST.get('discription')
        co = request.POST.get('colour')
        tr = request.POST.get('transmission')

        try:
            im = request.FILES['image1']

            fs = FileSystemStorage()
            file = fs.save(im.name, im)

        except MultiValueDictKeyError:
            file = Productdb.objects.get(id=dataid).P_Image1

        Productdb.objects.filter(id=dataid).update(Category_names=cate, Car_name=car, Model=mo, Hpower=hp, Ceat=ce,
                                                   Body=bo, Price=pr, Airbag=ar, Transmission=tr,
                                                   Discriptions=di, Colour=co, P_Image1=file, )

        return redirect(Display_product)


def Delete_product(request, dataid):
    data = Productdb.objects.filter(id=dataid)
    data.delete()
    messages.error(request,"Car details deleted")

    return redirect(Display_product)


def Admin_login_page(request):
    return render(request, "Admin_login_page.html")


def Admin_login(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['username'] = username_r
                request.session['password'] = password_r
                return redirect(adminpage)
            else:
                return redirect(Admin_login_page)
        else:
            return redirect(Admin_login_page)


def Admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Admin_login_page)

def View_contact(request):
    data=Contactdb.objects.all()
    return render(request,"View_contact.html",{'data': data})

def Delete_contact(request,dataid):
    data=Contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(View_contact)

def View_user(request):
    data=user_reg.objects.all()
    return render(request,"View_user.html",{'data': data})

def Delete_user(request,dataid):
    data=user_reg.objects.filter(id=dataid)
    data.delete()
    return redirect(View_contact)

def View_booking(request):
    data=Booking.objects.all()
    return render(request,"View_Booking.html",{'data':data})



def View_payment(request):
    data=Payment.objects.all()
    return render(request,"View_payment.html",{'data':data})


def Delete_payment(request,dataid):
    data=Payment.objects.filter(id=dataid)
    data.delete()
    return redirect(View_payment)








