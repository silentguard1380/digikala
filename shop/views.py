from django.shortcuts import render,redirect
from .models import Product
# Create your views here.


from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def helloworld(request):

    products=Product.objects.all()

    context={'products':products}

    return render(request,'index.html',context=context)

def about(request):

    return render(request,'about.html',context={})



def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)

            messages.success(request,'you are login now')

            return redirect('home')




    else:
        return render(request,'login.html')


def logout_user(request):
    logout(request)
    messages.success(request ,'با موفقیت خارج شدی')
    return redirect('home')

