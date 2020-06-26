from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import marks
from django.db.models import Q
from accounts.forms import stform


# Create your views here.


def teach(request):
    return render(request,'teach.html')

def teach1(request):
    if request.method == "POST":
        if request.POST.get('id') and request.POST.get('name') and request.POST.get('sub1') and request.POST.get('sub2')  and request.POST.get('sub3') and request.POST.get('sub4') and request.POST.get('sub5') and request.POST.get('Dob'):
            Marks = marks()
            
            Marks.id = request.POST.get('id')
            Marks.name = request.POST.get('name')
            Marks.sub1 = request.POST.get('sub1')
            Marks.sub2 = request.POST.get('sub2')
            Marks.sub3 = request.POST.get('sub3')
            Marks.sub4 = request.POST.get('sub4')
            Marks.sub5 = request.POST.get('sub5')
            Marks.Dob = request.POST.get('Dob')
            
            Marks.save();
            messages.info(request,"data saved successfully")
            
        return render(request,'teach1.html')
        
    return render(request,'teach1.html')
    

def stud(request):
    return render(request,'stud.html')

def stud1(request):
    if request.method == 'GET': 
        id = request.GET.get('id')
        name = request.GET.get('name')
        
        
        Gets = marks.objects.filter(Q(id__iexact=id) | Q(name__iexact=name)).order_by()
        
        # messages.info(request, "reults for :")
            
    else:
        messages.info(request, "please check your roll number")
        return render(request,'stud1.html')
            
    return render(request, 'stud1.html', {'Gets':Gets})

    # return render(request,'stud1.html')
# student block

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('stud1')
        else:
            messages.info(request, "invalild username or password")
            return redirect('login')
    else:
        return render(request, 'login.html')
        

def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect ('register')
                print("user name taken")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect('register')
            else:    
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print("user created")
                          
        else:
            print("password not matching...")
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('login')

    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

# teacher block

# def logout1(request):
    # auth.logout(request)
    # return redirect('/')

def log(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('teach1')
        else:
            messages.info(request, "invalild username or password")
            return redirect('log')
    else:
        return render(request, 'log.html')

def reg(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect ('reg') 
                print("user name taken")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect('reg')
            else:    
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print("user created")
                 
        else:
            print("password not matching...")
            messages.info(request, "password not matching")
            return redirect('reg')
        return redirect('log')

    else:
        return render(request,'reg.html')


def submit(request):
    if request.method == "POST":
        if request.POST.get('id') and request.POST.get('name') and request.POST.get('sub1') and request.POST.get('sub2')  and request.POST.get('sub3') and request.POST.get('sub4') and request.POST.get('sub5') and request.POST.get('Dob'):
            Marks = marks()
            
            Marks.id = request.POST.get('id')
            Marks.name = request.POST.get('name')
            Marks.sub1 = request.POST.get('sub1')
            Marks.sub2 = request.POST.get('sub2')
            Marks.sub3 = request.POST.get('sub3')
            Marks.sub4 = request.POST.get('sub4')
            Marks.sub5 = request.POST.get('sub5')
            Marks.Dob = request.POST.get('Dob')
            
            Marks.save();
            messages.info(request,"data saved successfully")
            
        return render(request,'teach1.html')
        
    return render(request,'teach1.html')




# def search(request):
    # if request.method == 'GET': 
        # q = request.GET.get('q')
        # Gets = marks.objects.filter(id=q)
        # messages.info(request, "reults for :")    
    # else:
        # messages.info(request, "please check your roll number")
        # return render(request,'stud1.html') 
    # return render(request, 'stud1.html', {'Gets':Gets,})

def details(request):
    data = marks.objects.all()
    return render(request,'details.html',{'data':data})

def delete(request,id):
    marks.objects.get(id=id).delete()
    messages.info(request,'deleted successfully!')
    return redirect('details')

def edit(request,id):
    data = marks.objects.get(id=id)

    return render(request,'edit.html',{'data':data})

def update(request,id):
    update = marks.objects.get(id=id)
    form = stform(request.POST,instance=update)
    if form.is_valid():
        form.save()
        messages.success(request,'updated successfully!')
        return render(request,'edit.html',{'marks':update})


