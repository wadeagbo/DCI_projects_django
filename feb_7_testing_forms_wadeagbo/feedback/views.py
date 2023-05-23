from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Feedback
from .forms import AddFeedbackForm 

# Create your views here.

def list_api(request):
    feedback = [{'email': f.email, 'message': f.message} for f in Feedback.objects.all()]
    return JsonResponse({"feedback": feedback})

def list_view(request):
    feedback = Feedback.objects.all()
    return render(request, 'feedback/index.html', {'feedback': feedback})    


def new_feedback(request):
    if request.method == 'POST':
        # create an instance of the form
        form = AddFeedbackForm(request.POST)
        # check that the form is valid and save
        if form.is_valid():
            form.save()
            return redirect("feedback:list")
    else:
        form = AddFeedbackForm()
    return render(request, "feedback/new_feedback.html", {"form": form})