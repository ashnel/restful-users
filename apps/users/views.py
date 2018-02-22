# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from time import strftime, localtime
from django.core.urlresolvers import reverse
from .models import *

def index(request):
    users = User.objects.all()
    # user_id = users.id
    # user_full_name = user.first_name + " " + user.last_name
    # user_email_address = user.email_address
    # user_created_at = strftime('%B %d, %Y', user.created_at.timetuple())
    return render(request, 'users/index.html', {'all_users': users})

def new(request):
    return render(request, 'users/new.html')

def create(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email_address'])
    user = User.objects.latest('id')
    user_id = user.id
    return redirect('/users/' + str(user_id) + '/show')

def edit(request, user_number):
    print user_number
    edited_user = User.objects.get(id=user_number)
    user_first_name = edited_user.first_name
    user_last_name = edited_user.last_name
    user_email_address = edited_user.email_address
    return render(request, 'users/edit.html', {'id': user_number, 'first_name': user_first_name, 'last_name': user_last_name, 'email_address': user_email_address})

def destroy(request, user_number):
    deleted_user = User.objects.get(id=user_number)
    deleted_user.delete()
    return redirect('/users')

def show(request, user_number):
    user = User.objects.get(id=user_number)
    user_id = user.id
    user_full_name = user.first_name + " " + user.last_name
    user_email_address = user.email_address
    user_created_at = strftime('%B %d, %Y', user.created_at.timetuple())
    return render(request, 'users/show.html', {'id': user_number, 'full_name': user_full_name, 'email_address': user_email_address, 'created_at': user_created_at})

def update(request, user_number):
    updated_user = User.objects.get(id=user_number)
    updated_user.first_name = request.POST['first_name']
    updated_user.last_name = request.POST['last_name']
    updated_user.email_address = request.POST['email_address']
    updated_user.save()
    return redirect('/users/{}/show'.format(user_number))