from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Stock_Name
from django.core import serializers
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Form_Query
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'StockMarket/signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'StockMarket/signup.html',
                              {'form': UserCreationForm(), 'error': 'Password did not match'})


def login(request):
    if request.method == 'GET':
        return render(request, 'StockMarket/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'StockMarket/login.html',
                          {'form': AuthenticationForm(), 'error': 'Password did not match'})
        else:
            login(request, user)
            return redirect('index')


@login_required
def index(request, stock_slug=None):
    if 's' in request.GET:
        s = request.GET['s']
        stock_name = Stock_Name.objects.filter(issuer_name__icontains=s)
    else:
        stock_name = Stock_Name.objects.all()
    # pagination
    paginator = Paginator(stock_name, 5)
    page_number = request.GET.get('page')
    stock_name = paginator.get_page(page_number)
    return render(request, 'StockMarket/index.html', {'stock_name': stock_name, 'form':query })

def stock_detail(request, id, slug):
    stock_name = get_object_or_404(Stock_Name,
                                   id=id,
                                   slug=slug,
                                   status=True)
    return render(request, 'StockMarket/detail.html', {'stock_name': stock_name})


def query(request):
    if request.method == "POST":
        name = request.POST['user_name']
        email = request.POST['email']
        query = request.POST['query']

        newenqury = Form_Query(user_name=name, email=email, enquery=query)
        newenqury.save()
    return render(request, 'StockMarket/query.html')

# Load More
def load_more(request):
    offset = int(request.POST['offset'])
    limit = 5
    stock_list = Stock_Name.objects.all()[offset:limit + offset]
    totalData = Stock_Name.objects.count()
    data = {}
    stock_list_json = serializers.serialize('json', stock_list)
    return JsonResponse(data={
        'stock_list': stock_list_json,
        'totalResult': totalData,
    })

@staff_member_required
def admin_query_detail(request, query_id):
    query = get_object_or_404(Form_Query, id=query_id)
    return render(request, 'admin/StockMarket/form_query/.html', {'query': query})
#alok