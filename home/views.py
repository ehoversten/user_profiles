from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.models import Post

from home.forms import HomeForm
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/dashboard.html'


    def get(self, request):
        # initalize form instance
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)

        context = {
            'form' : form,
            'posts': posts,
            'users': users
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            text = form.cleaned_data['post']
            print(text)
            form = HomeForm()

        context = {
            'form' : form,
            'text' : text,
        }
        return redirect('home:dashboard')
