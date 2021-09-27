import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Items
from django.contrib import messages
from django.views.generic import (
    CreateView,
    UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


@login_required
def item_list_view(request):
    context = {}
    if request.method == 'POST':
        context['items'] = Items.objects.filter(user=request.user, date=request.POST.get('date')).all()
        context['date'] = request.POST.get('date')
    else:
        context['items'] = Items.objects.filter(user=request.user).all()
        context['date'] = ""

    return render(request, 'bag/item_list.html', context)

def item_create_view(request):
    if request.method == 'POST':
        Items(user=request.user, date=request.POST.get('date'), title=request.POST.get(
            'iname'), quantity=request.POST.get('iquant'), status=request.POST.get('status')).save()
        return redirect('item-list')

    else:
        return render(request, 'bag/item_create.html')


def item_update_view(request, item_id):
    item_update = Items.objects.filter(uuid=item_id).first()
    if item_update == None:
        return redirect('item-list')
    if request.method == 'POST':
        item_update.title = request.POST.get('iname')
        item_update.date = request.POST.get('date')
        item_update.status = request.POST.get('status')
        item_update.quantity = request.POST.get('iquant')
        item_update.save()
        return redirect('item-list')

    else:
        return render(request, 'bag/item_update.html', {'item':item_update, 'date':str(item_update.date)})


@login_required
def delete_view(request, item_id):
    item_delete = Items.objects.filter(uuid=item_id).first()
    if item_delete == None:
        return HttpResponse('Some Problem Occurred')
    if item_delete.user != request.user:
        return HttpResponse('Not permitted')
    messages.success(request, 'Post deleted successfully')
    item_delete.delete()
    return redirect('item-list')
