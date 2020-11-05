from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Business,Profile,Neighbourhood
from django.contrib.auth.models import User
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from .forms import EditProfileForm,NewBusinessForm
# Create your views here

def index(request):
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    try:
        profile = Profile.objects.filter(user = current_user).first()
    except:
        return redirect('edit-profile')
    business = Business.objects.filter(user = current_user).all()
    total_business = business.count()
    title = "Profile"
    return render(request,'profile.html',{"profile":profile,"title":title,"business":business,"current_user":current_user,"total_business":total_business,})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')

    else:
        form = EditProfileForm()
    title = "Edit-profile"
    return render(request, 'edit_profile.html', {"form": form,"title":title})

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            profile = Profile.objects.filter(user = current_user).first()
            business.neighbourhood= profile.neighbourhood
            business.save()
        return redirect('profile')

    else:
        form = NewBusinessForm()
        title = 'New business'
    return render(request, 'new_business.html', {"form": form,"title":title})

@login_required(login_url='/accounts/login/')
def view_business(request,business_id):
    business = Business.objects.filter(id=business_id).first()
    title = f"Business-{business.name}"
    return render(request,'business.html',{"business":business,"title":title})

def search_results(request):
    title='Search'
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_businesss = Business.objects.filter(name__icontains=search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"title":title,"businesss": searched_businesss})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message,"title":title})