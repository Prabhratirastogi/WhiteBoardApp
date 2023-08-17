# from django.urls import path
# from account import views 

# urlpatterns = [
#     path('signup/',views.signup,name = 'signup'),
#     path('login/',views.handlelogin,name = 'handlelogin'),
#     path('logout/',views.handlelogout,name = 'handlelogout'),
#     path('activate/<uidb64>/<token>', views.ActivateAccountView.as_view(),
#     name = 'activate'),
# ]


from django.urls import path
from account import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('auth/signup/',views.signup,name='signup'),
    path('auth/login/',views.handlelogin,name='handlelogin'),
    path('auth/logout/',views.handlelogout,name='handlelogout'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
    path('request-reset-email/',views.RequestResetEmailView.as_view(),name='request-reset-email'),
    path('set-new-password/<uidb64>/<token>',views.SetNewPasswordView.as_view(),name='set-new-password'),
]