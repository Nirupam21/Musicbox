from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from .models import Upload
from django.core.files.storage import FileSystemStorage
from django.views.generic import View
from music.forms import UserForm
from django.contrib.auth import authenticate

def home(request):
    return render(request,'home.html')
# Create your views here.
def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return render(request,'upload.html/',{'user':user})
    else:
        return render(request,'login.html',{'errMsg':'Invalid username or password'})

def uploadpage(request):
    return render(request,'upload.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html',{})


def upload(request):
    try:
            if request.method == 'POST' and request.FILES['file'] and request.FILES['thumb']:
                try:
                    myfile = request.FILES['file']
                    t = request.FILES['thumb']
                    fs = FileSystemStorage()
                    file = fs.save(myfile.name, myfile)
                    thumb = fs.save(t.name, t)
                    uname = request.POST.get('uname', '')
                    filename = request.POST.get('file_name', '')
                    obj = Upload()
                    obj.file_uploader = uname
                    obj.name = filename
                    obj.file = file
                    obj.thumbnail = thumb
                    obj.save()

                    return render(request, "upload.html", {'msg': 'File uploaded successfully :)'})
                except:
                    return render(request, "upload.html", {'msg': 'Something went wrong, retry !'})


            else:
                return render(request, "upload.html", {})
    except:
        return HttpResponseRedirect('/home/')


def myUploads(request):
        a = auth.get_user(request)
        items = Upload.objects.filter(file_uploader=a)
        return render(request,"myuploads.html",{'items':items})

def uploadplay(request,pk):
    a=Upload.objects.filter(pk=pk)
    b=auth.get_user(request)
    items = Upload.objects.filter(file_uploader=b)
    return render(request,'myuploads.html',{'a':a},{'items':items})

def play(request,pk):
    a=Upload.objects.filter(pk=pk)
    return render(request, 'audioplay.html',{'a': a})

def welcome(request):
    items = Upload.objects.all()
    return render(request, "welcome.html", {'items': items})

def login(request):
    return render(request,"login.html")

def search(request):
    if request.method == 'POST':
        try:
            i = request.POST.get("search", '')
            record = Upload.objects.filter(name=i)
            return render(request,'search.html',{'record':record})
        except:
            return render(request,'search.html',{'errMsg': 'Song Not Found!!!'})

class UserFormView(View):
    a=UserForm
    template='signup.html'

    def get(self,request):
        form = self.a(None)
        return render(request,self.template,{'form':form})

    def post(self,request):
        form = self.a(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user=authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return render(request, 'upload.html/', {'user': user})

        return render(request, 'signup.html/', {'form': form})


