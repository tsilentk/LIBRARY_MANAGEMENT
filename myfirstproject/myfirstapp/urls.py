from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('usersignup/',views.usersignup),
    path('handlesignup/',views.handlesignup),
    path('userlogin/',views.userlogin),
    path('handlelogin/',views.handlelogin),
    path('userlogout/',views.userlogout),

    path('lib/',views.lib),

    path('addbook/',views.addbook),
    path('updatebook/',views.updatebook),
    path('seeallbooks/',views.seeallbooks),
    path('deletebook/',views.deletebook),


    path('addmember/',views.addmember),
    path('updatemember/',views.updatemember),
    path('seeallmembers/',views.seeallmembers),
    path('deletemember/',views.deletemember),

    path('addrecord/',views.addrecord),
    path('updaterecord/',views.updaterecord),
    path('seeallrecords/',views.seeallrecords),
    path('deleterecord/',views.deleterecord),
    path('seesearchrecords/',views.seesearchrecords),


    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    



   
]