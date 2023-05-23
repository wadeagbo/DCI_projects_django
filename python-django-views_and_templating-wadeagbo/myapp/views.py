from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

# Create your views here.

def about_view(request):
	#return HttpResponse("Hello, World!")
	#return JsonResponse({"my favorite book":"Biology"})
	return render(request, "myapp/about.html", {}) # {} can be removed for now . {} holds variable of html
 
def base_view(request):
	return render (request, "myapp/about.html", {})



class HomePageView(TemplateView):
	template_name = "myapp/home.html"

class AboutPageView(TemplateView):
	template_name = "myapp/about.html"
