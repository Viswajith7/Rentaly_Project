from django.urls import path
from Rentapp import views


urlpatterns=[

    path('Homepage/',views.Homepage,name="Homepage"),
    path('About_page/',views.About_page,name="About_page"),
    path('Product_page/<catg>/',views.Product_page,name="Product_page"),
    path('Single_product/<int:dataid>/',views.Single_product,name="Single_product"),
    path('Contact_page/',views.Contact_page,name="Contact_page"),
    path('Save_contact/',views.Save_contact,name="Save_contact"),
    path('Checkout/',views.Checkout,name="Checkout"),
    path('User_loginpage/',views.User_loginpage,name="User_loginpage"),
    path('Savereg/',views.Savereg,name="Savereg"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('Savebooking/',views.Savebooking,name="Savebooking"),
    path('Cart/',views.Cart,name="Cart"),
    path('Delete_cart/<int:dataid>/',views.Delete_cart,name="Delete_cart"),
    path('news/',views.news,name="news"),
    path('BLog_single/',views.BLog_single,name="BLog_single"),
    path('saveCheckout/',views.saveCheckout,name="saveCheckout"),

]