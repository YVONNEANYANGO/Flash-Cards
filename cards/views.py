from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Flashes,Profile
from .forms import ProfileForm
from django.shortcuts import get_object_or_404
# Create your views here.

@login_required(login_url='accounts/login/')
def welcome(request):
    flashes = Flashes.objects.all()
    print(flashes)
    
    return render(request, 'welcome.html', {"flashes":flashes})

@login_required(login_url='accounts/login/')
def profile(request):
    # ivone = request.user.id
    profile = Profile.objects.all()
    # user = request.user

    return render(request, 'profile.html', {'profile':profile})


@login_required(login_url='/accounts/login/')
def flashes(request):
    flashes = Flashes.ojects.get_all()
    return render(request, "welcome.html", {"flashes":flashes})


def search_results(request):

    if 'flashes' in request.GET and request.GET["flashes"]:
        search_term = request.GET.get("flashes")
        searched_flashes = Project.search_by_subject(search_term)

        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"flashes": searched_flashes})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def newprofile(request):
#  ivone = request.user.id
 profile = Profile.objects.all()
 if request.method == 'POST':
   instance = get_object_or_404(Profile)
   form = ProfileForm(request.POST, request.FILES,instance=instance)
   if form.is_valid():
     form.save()

   return redirect('welcome')

 else:
   form = ProfileForm()

 return render(request, 'newprofile.html',{'form':form,'profile':profile})



