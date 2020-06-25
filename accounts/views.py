from django.shortcuts import render
from .forms import PostsForm



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Posts

# Create your views here.
def indexView(request):
    return render(request,'index.html')
@login_required    
def dashboardView(request):
    return render(request,'dashboard.html')
def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()

    return render(request,'registration/register.html',{'form':form})
def loginView(request):
    return render(request,'registration/login.html')
def post_create(request):
    form = PostsForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PostsForm()
    context = {
        'form':form
    }
    return render(request,'form.html',context)
