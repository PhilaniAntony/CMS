from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
'''
comment
over
lionh
lin
'''
app_name='shopapi'
urlpatterns = [
    #Products 
    path('', views.home_view, name= 'api_overview'),
    path('create_product/', views.createProduct_view, name='create_products'),
    path('products/', views.products_view, name='products'),
    path('product/<str:pk>/', views.product_view, name='product'),
    path('update_product/<str:pk>/', views.updateProduct_view, name='update_products'),
    path('delete_product/<str:pk>/', views.deleteProduct_view, name='delete_products')
    
 
   
    #path('reset_password/', auth_views.PasswordResetView.as_view(template_name= "accounts/password_reset.html"), name="reset_password"),
    #path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name= "accounts/password_reset_sent.html"), name="password_reset_done"),
    #path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name= "accounts/password_reset_form.html"), name='password_reset_confirm' ),
    #path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name= "accounts/password_reset_done.html"), name='password_reset_complete'),

]