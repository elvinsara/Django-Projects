from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Item
from django.template import loader
from .forms import ItemForm

# Create your views here.

def helloworld(request):
    
    return HttpResponse("hello world")

def getAllItems(request):
    item_list = Item.objects.all()
    #template = loader.get_template('food\index.html')
    return render(request,'food/index.html',{'item_list':item_list})

def details(request,pk):
    item = Item.objects.get(pk=pk)
    return render(request,'food/details.html',{'item':item})
    #return HttpResponse(f'Details page {pk}')

def addItem(request):
    item_form = ItemForm(request.POST or None)
    if item_form.is_valid():
        item_form.save()
        return redirect('food:allfood')
    return render(request,'food/create.html',{'item_form':item_form})

def updateItem(request,pk):
    item = Item.objects.get(pk=pk)
    item_form = ItemForm(request.POST or None, instance=item)
    if item_form.is_valid():
        item_form.save()
        return redirect('food:allfood')
    return render(request,'food/create.html',{'item_form':item_form})

def deleteItem(request,pk):
    item = Item.objects.get(pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('food:allfood')
    return render(request,'food/delete.html',{'item':item})

    

