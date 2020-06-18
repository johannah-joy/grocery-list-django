from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# from django.template import loader
from django.utils import timezone
from .models import GroceryItem

# Create your views here.
def index(request):
  # template = loader.get_template('grocery_list/index.html')
  # form = GroceryItemForm()
  incompleted_items = GroceryItem.objects.filter(completed=False).order_by('created_date')
  completed_items = GroceryItem.objects.filter(completed=True).order_by('completed_date')
  context = {
    'incompleted_items': incompleted_items,
    'completed_items': completed_items
  }
  # return HttpResponse(template.render(context, request))
  return render(request, 'grocery_list/index.html', context)


def add(request):
  if request.POST['text_description']:
    GroceryItem.objects.create(created_date=timezone.now(), text_description=request.POST['text_description'])
  # template = loader.get_template('item.html')
  # context = {
  #   'item': grocery
  # }
  # return HttpResponse(template.render(context, request))
  return HttpResponseRedirect(reverse('grocery_list_app:index'))

def complete(request, pk):
  item = get_object_or_404(GroceryItem, pk=pk)
  if item.completed:
    item.completed = False
    item.completed_date = None
  else:
    item.completed = True
    item.completed_date = timezone.now()
  item.save()
  return HttpResponseRedirect(reverse('grocery_list_app:index'))

def delete(request, pk):
  item = get_object_or_404(GroceryItem, pk=pk)
  item.delete()
  return HttpResponseRedirect(reverse('grocery_list_app:index'))