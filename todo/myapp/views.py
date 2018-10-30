from django.shortcuts import render,redirect;
from django.http import HttpResponse;
from myapp.forms import Tform;
from myapp.models import Tasks;
from django.views.decorators.http import require_POST
# Create your views here.
def index(request):
    form=Tform();
    qs=Tasks.objects.all();
    return render(request,"index.html",{"form":form,"qs":qs});
@require_POST
def add(request):
    form=Tform(request.POST);
    if form.is_valid():
        text=form.cleaned_data.get('text');
        new=Tasks(name=text);
        new.save();
        print(form.cleaned_data);
    return redirect("index");
def change(request,item_id):
    item=Tasks.objects.get(pk=item_id);
    item.finish=True;
    item.save();
    return redirect("index");
def delcom(request):
    Tasks.objects.filter(finish=True).delete();
    return redirect("index");
def delall(request):
    Tasks.objects.all().delete();
    return redirect("index");