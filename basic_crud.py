from django.shortcuts import render, redirect
from .models import MyModel

def create_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        new_item = MyModel.objects.create(name=name, description=description)
        return redirect('item_list')
    return render(request, 'appname/item_form.html')