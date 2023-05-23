from django.shortcuts import render
from django.views.generic.edit import FormView
import requests
import json
 

# Create your views here.

from .forms import HoroscopeForm


class HoroscopeCreateView(FormView):
    template_name = "cancer_horoscopes/get_prediction.html"
    form_class = HoroscopeForm

    # handle the POST request
    def post(self, request):
        # extract the sign amnd fext the horoscopes
        sign = request.POST. get('sign', '')
        req = requests.get( f"https://ohmanda.com/api/horoscope/{sign}" )
        context = req.json()
        print (context)
     #   context['form'] = self.form_class
        context['form'] = HoroscopeForm() 
        return render(request, "cancer_horoscopes/get_prediction.html", context)
        