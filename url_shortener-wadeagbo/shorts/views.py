from django.shortcuts import render, redirect
from .forms import ShortURLForm
from .models import ShortURL
import datetime
import pytz

def index(request):
    if request.method == 'POST':
        form = ShortURLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_list')
    else:
        form = ShortURLForm()
    return render(request, 'shorts/index.html', {'form': form})

def url_redirect(request, shortened):
    url = ShortURL.objects.get(shortened=shortened)
    tz = pytz.timezone('Europe/Berlin')
    now = datetime.datetime.now(tz)
    if url.expiration_date >=now:
        return redirect(url.long_url)
    else:
        return render(request, 'shorts/expired.html')

def url_list(request):
    urls = ShortURL.objects.all()
    return render(request, 'shorts/url_list.html', {'urls': urls})
