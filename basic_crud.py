#basic crud in django
from django.shortcuts import render, redirect, get_object_or_404
from .models import MyModel

def create_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        new_item = MyModel.objects.create(name=name, description=description)
        return redirect('item_list')
    return render(request, 'appname/item_form.html')


def list_items(request):
    items = MyModel.objects.all()
    return render(request, 'appname/item_list.html', {'items':items})

def edit_item(request, item_id):
    item = get_object_or_404(MyModel, id=item_id)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.description = request.POST.get('description')
        item.save()
        return redirect('item_list')
    return render(request, 'appname/item_form.html', {'item' : item})

def delete_item(request, item_id):
    item = get_object_or_404(MyModel, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'appname/item_confirm_delete.html', {'item' : item})