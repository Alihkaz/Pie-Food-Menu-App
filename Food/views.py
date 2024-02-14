


#imports
from django.shortcuts import render , redirect
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView



#--------------------home page----------------------
def index(request):

    item_list=Item.objects.all()
   
    context={
      'item_list':item_list
    }

    return render(request,'Food/index.html',context)


#--------------------Recreating the home page as a class based list view ----------------------

class IndexClassView(ListView): #this view is same as the index view ,
                                #which will display items from the db as a list in the home page but its a class based list view

    model=Item;
    template_name='Food/index.html'
    context_object_name='item_list'





#--------------------details page depending on each item id----------------------
def detail(request,item_id):
   
    item=Item.objects.get(pk=item_id)
   
    context={
      'item':item
    }
  
    return render(request,'Food/detail.html',context)






#--------------------Recreating the detail view as a class based detail view ----------------------

class FoodClassView(DetailView): #this view is same as the detail view ,
                                #which will display  the details of an items
                               # from the db detail page according to the requested item pk but its a class based detail view

    model=Item;
    template_name='Food/detail.html'
   




#--------------------adding item page where the form is rendered , and data is saved----------------------
def add_item(request):
    form=ItemForm(request.POST or None)

    if form.is_valid():
        form.save() #saving the data that we get from the form inputs in the database
        return redirect("Food:index")
    
    #if request is get:

    return render(request,'Food/item_form.html',{'form':form}) #passing the form to the html page so the user can fill 






#--------------------Recreating the add_item view as a class based create view ----------------------

class CreateItem(CreateView):
    model = Item;
    fields=['item_name','item_desc','item_price','item_img']
    template_name='food/item_form.html'
 
    def form_valid(self,form):
        form.instance.user_name = self.request.user
 
        return super().form_valid(form)


#--------------------editing item feature according to a certain item id ----------------------
def edit_item(request,id):
    
    #the item the user wants to edit
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST or None , instance=item)#we get the item according to a certain item id and show its data to edit
 
    #when the user clicks on save :
    if form.is_valid():
        form.save()
        return redirect("Food:index")
    
    #if request is get:
    return render(request,'Food/item_form.html',{'form':form , 'item':item})





#--------------------deleting item feature according to a certain item id ----------------------
def delete_item(request,id):
    
    #the item the user wants to delete
    item=Item.objects.get(id=id)
    
 
    #when the user clicks on confirm delete in the confirmation page :
    if request.method=='POST':
        item.delete()
        return redirect("Food:index")
    
    #if request is to delete the nitem we will redirect the user to the confirmation page:
    return render(request,'Food/delete_item.html',{'item':item})

