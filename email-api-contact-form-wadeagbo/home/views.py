from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def home(request):
    location = request.GET.get('location', '')
    sort = request.GET.get('sort', '')
    # breakpoint()
    print(request.FILES)

    return HttpResponse(f'Hello ' + location + sort, status=418)