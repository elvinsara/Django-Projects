from django.forms import ModelForm
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        #fields = ['item_name','item_desc','item_price','item_image']