from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .models import Client, Project
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import ClientForm,ProjectForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.
def home(request):
    # Implement your home view logic here
    return render(request, 'home.html')

""" @login_required """
def register_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list.html')
    else:
        form = ClientForm()
    return render(request, 'register_client.html', {'form': form})

""" @login_required """
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

@login_required
def client_detail(request):
    """  client = get_object_or_404(Client)
    return render(request, 'client_detail.html', {'client': client}) """
    clients = Client.objects.all()
    if clients.exists():
        return render(request, 'client_detail.html', {'clients': clients})
    else:
        return HttpResponse("No clients found.")

@login_required
def client_edit(request):
    """ client = get_object_or_404(Client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_detail.html')
    else:
        form = ClientForm(instance=client)
    return render(request, 'edit_client.html', {'form': form}) """
    clients = Client.objects.filter()
    if clients.exists():
        client = clients.first()  # Assuming there is only one client with this ID
        if request.method == 'POST':
            form = ClientForm(request.POST, instance=client)
            if form.is_valid():
                form.save()
                return redirect('client_detail/')  # Redirect to client detail page
        else:
            form = ClientForm(instance=client)
        return render(request, 'edit_client.html', {'form': form})
    else:
        return HttpResponse("Client does not exist.")

@login_required
def client_delete(request):
    """ client = get_object_or_404(Client)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list.html')
    return render(request, 'delete_client.html', {'client': client}) """
    if request.method == 'POST':
        client_name = request.POST.get('client_name')  # Assuming the client's name is submitted via a form
        clients = Client.objects.filter(name='client_name')
        if clients.exists():
            client = clients.first()
            client.delete()
            return redirect('client_list/')  # Assuming 'client_list' is the URL name for the client list page
        else:
            return HttpResponse("Client does not exist.")
    else:
        return HttpResponse("Invalid request method.")

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list.html')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})
 
@login_required
def assigned_projects(request):
    projects = request.user.projects.all()
    return render(request, 'assigned_projects.html', {'projects': projects}) 
 
@login_required
def project_list(request):
    projects = Project.objects.filter(users=request.user)
    return render(request, 'project_list.html', {'projects': projects})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('client_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')




""" user Login Realted 
def register_user(request):
    form= CreateUserForm() 
    if request.method == "POST":
        form= CreateUserForm(request.POST)
        if form.is_valid(): #checking if data is valid
            form.save() # saving into the db
            print("USer created successfully")
            messages.success(request,("user created Successfully"))
            return redirect("/")
        
        else:
            print("Error")
            messages.error
            (request,(Your password canÃ¢â‚¬â„¢t be too similar to your other personal information.
                                   Your password must contain at least 8 characters.
                                   Your password canÃ¢â‚¬â„¢t be a commonly used password.
                                   Your password canÃ¢â‚¬â„¢t be entirely numeric.))
    c={'form':form}
    return render(request,"register.html",c)        




def login_user(request):
    
    if request.method=="POST":
        username=request.POST['username']
        password= request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print("User Logged in Successfully")
            messages.success(request,("user login created Successfully"))
            return redirect("/")
        else:
            messages.error(request,("There was an error ,Try Again !!"))
            return redirect("login_user/")
    else:
        return render(request,"login.html")    


def logout_user(request):
    logout(request)
    messages.success(request,("Logged Out Successfully"))
    return redirect("/")
 """
