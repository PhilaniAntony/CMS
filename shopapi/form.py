from django.forms import ModelForm
from accounts.models import  Customer,Tag,Product,Order

class CustomerForm(ModelForm):
    class Meta :
        model = Customer
        fields = '__all__'
        
class ProductForm(ModelForm):
    class Meta :
        model = Product
        fields = '__all__'
        
class TagForm(ModelForm):
    class Meta :
        model = Tag
        fields = '__all__'
        
class OrderForm(ModelForm):
    class Meta :
        model = Order
        fields = '__all__'