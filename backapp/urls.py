from django.urls import path
from backapp import views

urlpatterns= [
    path('adminpage/', views.adminpage, name="adminpage"),
    path('addcategory/', views.addcategory, name="addcategory"),
    path('savecategory/',views.savecategory,name="savecategory"),
    path('displaycategory/',views.displaycategory,name="displaycategory"),
    path('editcategory/<int:dataid>/',views.editcategory,name="editcategory"),
    path('updatecategory/<int:dataid>/',views.updatecategory,name="updatecategory"),
    path('deletecategory/<int:dataid>/',views.deletecategory,name="deletecategory"),
    path('Add_product/',views.Add_product,name="Add_product"),
    path('Save_product/',views.Save_product,name="Save_product"),
    path('Display_product/',views.Display_product,name="Display_product"),
    path('Edit_product/<int:dataid>/',views.Edit_product,name="Edit_product"),
    path('Update_product/<int:dataid>/',views.Update_product,name="Update_product"),
    path('Delete_product/<int:dataid>/',views.Delete_product,name="Delete_product"),
    path('Admin_login_page/',views.Admin_login_page,name="Admin_login_page"),
    path('Admin_login/',views.Admin_login,name="Admin_login"),
    path('Admin_logout/',views.Admin_logout,name="Admin_logout"),
    path('View_contact/',views.View_contact,name="View_contact"),
    path('Delete_contact/<int:dataid>/',views.Delete_contact,name="Delete_contact"),
    path('View_user/',views.View_user,name="View_user"),
    path('Delete_user/<int:dataid>/',views.Delete_user,name="Delete_user"),
    path('View_booking/',views.View_booking,name="View_booking"),

    path('View_payment/',views.View_payment,name="View_payment"),
    path('Delete_payment/<int:dataid>/',views.Delete_payment,name="Delete_payment"),



]