from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.utils.safestring import mark_safe
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

# send_mail('Subject here', 'Here is the message.', 'from@example.com',
#     ['to@example.com'], fail_silently=False)


# Create your views here.
def home(request):
	title = 'Welcome'
	context = {
		"title": title,
	}

	return render(request, "home.html", context)

#str(user_id)[:11].replace('-','').lower()
# import uuid

def contact(request):
	title = 'Contact Us'
	context = {
		"title": title,
	}
	return render(request, "contact_us.html", context)

def about(request):
	title = 'About Us'
	context = {
		"title": title,
	}

	return render(request, "about.html", context)

def faq(request):
	title = 'FAQ'
	context = {
		"title": title,
	}

	return render(request, "faq.html", context)

def team_profile(request):
	title = 'About Us'
	context = {
		"title": title,
	}

	return render(request, "team_profile.html", context)



@login_required
def staff_home(request):
	context = {

	}
	return render(request, "staff_home.html", context)


def timeline(request):
	title = 'Timeline'
	context = {
		"title": title,
	}

	return render(request, "timeline.html", context)

def new_invoice(request):
	title = 'New invoice'
	context = {
		"title": title,
	}

	return render(request, "invoice-1.html", context)

def paid_invoice(request):
	title = 'Paid Invoice'
	context = {
		"title": title,
	}

	return render(request, "invoice-1.html", context)

def unpaid_invoice(request):
	title = 'Unpaid Invoice'
	context = {
		"title": title,
	}

	return render(request, "invoice-1.html", context)

def checkout_shipping(request):
	title = 'Shipping'
	context = {
		"title": title,
	}

	return render(request, "shop-checkout-shipping.html", context)

def checkout_payment(request):
	title = 'Payment'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
	}

	return render(request, "shop-checkout-payment.html", context)

def checkout_review(request):
	title = 'Review'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form,
	}

	return render(request, "shop-checkout-order.html", context)

def pricing(request):
	title = 'Review'
	context = {
		"title": title,
	}

	return render(request, "pricing-3.html", context)

def services(request):
	title = 'Review'
	context = {
		"title": title,
	}

	return render(request, "services-1.html", context)
def terms(request):
	title = 'Terms'
	context = {
		"title": title,
	}

	return render(request, "terms.html", context)

def blog(request):
	title = 'Review'
	context = {
		"title": title,
	}

	return render(request, "blog-fluid-1.html", context)

def projects(request):
	title = 'Review'
	context = {
		"title": title,
	}

	return render(request, "portfolio-two-col-boxed.html", context)

