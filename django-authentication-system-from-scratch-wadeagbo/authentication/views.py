from django.shortcuts import render,  HttpResponseRedirect
from authentication.forms import LoginForm
from django.views.generic import FormView, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

 



# class LoginView(FormView):
#     template_name = 'authentication/login.html'
#     form_class = LoginForm
#     #success_url = '/home/'
#     success_url = reverse_lazy("home")

#     def form_valid(self, form):
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user = authenticate(self.request, username=username, password=password)
#         if user is not None:
#             login(self.request, user)
#             return redirect(self.success_url)
#         return render(self.request, self.template_name, {'form': form})

# class LogoutView(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect('login')

#class HomeView(LoginRequiredMixin, TemplateView):
#    template_name = 'authentication/home.html'


class LogoutView(View):
    def dispatch(self, request):
        self.request.session.flush()
        return HttpResponseRedirect(reverse('home'))

class LoginView(FormView):
    template_name = 'authentication/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('success')
 
     
    def form_valid(self, form):
        username = form.data.get('username', None)
        password = form.data.get('password', None)

        # hard coded
        if (username == 'admin' and password == 'admin') or (username == 'lucas' and password == 'lucas'):
            # generate session id
            self.request.session.flush()
            self.request.session["user_id"] = username
            # redirect to a success URL
            return HttpResponseRedirect(self.success_url)

        else:
            # reload the form
            return super().form_valid(self.request)
