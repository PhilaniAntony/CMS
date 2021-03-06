from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='accounts'
urlpatterns = [
    #Admin page  ex: /home/
    path('', views.home_view, name= 'home'),
    #user ex: user/
    path('user/', views.user_view, name= 'user'),
    path('account/', views.account_settings, name="account"),
    #register ex: register/
    path('register/', views.register_view, name= 'register'),
    #register ex: /login/
    path('login/', views.login_view, name= 'login'),
    #logout  ex: /logout/
    path('logout/', views.login_view, name= 'logout'),
    #products  ex : /products/
    path('products/', views.products_view, name='products'),
    #customer id  ex: /customer/id
    path('customer/<str:pk>', views.customer_view, name='customer'),
    #createorder id  ex: /createorder/id
    path('createorder/<str:pk>/', views.create_Order, name= "createorder"),
     #update id  ex: /updateorder/id
    path('updateorder/<str:pk>/', views.update_Order, name= "updateorder" ),
      #delete id  ex: /updateorder/id
    path('deleteorder/<str:pk>/', views.delete_Order, name= "deleteorder" ),
    #Password Reset Views
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name= "accounts/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name= "accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name= "accounts/password_reset_form.html"), name='password_reset_confirm' ),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name= "accounts/password_reset_done.html"), name='password_reset_complete'),

]
