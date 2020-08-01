from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

#from .forms import TopicForm, EntryForm
from .models import Topic, Entry


def index(request):
    return render(request, 'blog/index.html')
