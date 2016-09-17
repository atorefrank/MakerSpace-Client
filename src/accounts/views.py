from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.utils.safestring import mark_safe
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render


from accounts.forms import RegisterForm, LoginForm
from accounts.models import MyUser

# Create your views here.

def sign_out(request):
	logout(request)

	return HttpResponseRedirect('/')

def sign_in(request):
	title = 'Sign In'
	form = LoginForm(request.POST or None)
	next_url = request.GET.get('next')
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			if next_url is not None:
				return HttpResponseRedirect(next_url)
			return HttpResponseRedirect("/")

	context = {
		"title": title,
		"form": form,
	}

	return render(request, "sign_in.html", context)

def register(request):
	title = 'Login Register'
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password2']
		#MyUser.objecys.create_user(username=username, email=email, password=password)
		new_user = MyUser()
		new_user.username = username
		new_user.email = email
		new_user.set_password(password)
		new_user.save
		return redirect('sign_in')
		#return HttpResponseRedirect(reverse('login'))

	context = {
		"title": title,
		"form": form,
		"action_value": "",
		"submit_btn_value": "Register",
	}

	return render(request, "sign_up.html", context)

@login_required
def user_account(request):
	#if request.user.is_authenticated
		title = 'My Account'
		context = {
			"title": title,
		}

		return render(request, "user-account.html", context)
	#else:
		#return HttpResponseRedirect('/login/')