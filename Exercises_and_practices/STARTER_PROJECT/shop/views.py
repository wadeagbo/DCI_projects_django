from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.
def index (request):
    return HttpResponse("Hello DCI class")
    #return JsonResponse({"message": "Hello DCI Class"})
   # return render(request, "shop/index.html", {}) 

# def shop_list(request):
#     return JsonResponse({ "book" : "Biology" })


def shop_list(request):
     return render(request,  "shop/shop_list.html", {"list" : [1,2, 3, 4]}) # we pass key in template file and loop over


def shop_item(request, item_id):
    return HttpResponse(f" Shop item number {item_id}")

def shop_search(reqest, term):
      return HttpResponse(f" Shop search for {term}")

def shop_slug(reqest, keyword):
      return HttpResponse(" Shop slug search for" + keyword)

def shop_uuid (request, key_uuid):
    return HttpResponse ("This is UUID format" + key_uuid)


# def shop_artile_list(request, year):
#     return HttpResponse ("Artile belongs to year" + year)

def shop_article_list(request, year):
     return HttpResponse (f"Artile belongs to year  {year}" )

months = ['', 'January', 'February' , 'March'] #  More month

def shop_article_list_version_2(request, **kwaargs):
    # logic will handle number correctly
    print(kwaargs)
    if kwaargs and kwaargs['is_int']:
        print("month is a number")
        month = kwaargs.get('month')
        month = months[month]
    elif kwaargs and kwaargs['is_int']==False:
        print("month is a string") 
        month = kwaargs.get('month')
    return HttpResponse (f" Hello world --{month}" )


def shop_validate_phone(request, phone_no):
    return HttpResponse (f" This {phone_no} is validated")

