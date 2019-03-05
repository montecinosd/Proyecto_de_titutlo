from django.shortcuts import render
from Registro_fullpega.models import *
from Registro_fullpega.forms import *
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/auth/login')
def index(request):
		data={}
		template_name = "index_super_user.html"
		return render(request, template_name,data)
