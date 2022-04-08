from django.shortcuts import render
from . import template
from .forms import blogForm
from .models import blogentry


def home(request):
    if request.method=="POST":
        form =blogForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_blog= blogentry.objects.all()
            return render(request, 'index.html', {'blog_news':all_blog})
    else:
        all_blog = blogentry.objects.all()
        return render(request, 'index.html', {'blog_news': all_blog})

