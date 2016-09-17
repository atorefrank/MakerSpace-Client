from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib import auth
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'newsletter.views.about', name='about'),
    url(r'^team_profile/$', 'newsletter.views.team_profile', name='team_profile'),
    url(r'^timeline/$', 'newsletter.views.timeline', name='timeline'),
    url(r'^services/$', 'newsletter.views.services', name='services'),
    url(r'^pricing/$', 'newsletter.views.pricing', name='pricing'),
    url(r'^staff/$', 'newsletter.views.staff_home', name='staff'),
    url(r'^faq/$', 'newsletter.views.faq', name='faq'),
    url(r'^terms/$', 'newsletter.views.terms', name='terms'),
    url(r'^blog/$', 'newsletter.views.blog', name='blog'),
    url(r'^projects/$', 'newsletter.views.projects', name='projects'),
    url(r'^new_invoice/$', 'newsletter.views.new_invoice', name='new_invoice'),
    url(r'^paid_invoice/$', 'newsletter.views.paid_invoice', name='paid_invoice'),
    url(r'^unpaid_invoice/$', 'newsletter.views.unpaid_invoice', name='unpaid_invoice'),
    url(r'^checkout_shipping/$', 'newsletter.views.checkout_shipping', name='checkout_shipping'),
    url(r'^checkout_payment/$', 'newsletter.views.checkout_payment', name='checkout_payment'),
    url(r'^checkout_review/$', 'newsletter.views.checkout_review', name='checkout_review'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
	urlpatterns == static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns == static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('accounts.views',
    url(r'^register/$', 'register', name='register'),
    url(r'^sign_in/$', 'sign_in', name='sign_in'),
    url(r'^sign_out/$', 'sign_out', name='sign_out'),
    url(r'^user_account/$', 'user_account', name='user_account'),
)


urlpatterns += patterns('billing.views',
    url(r'^upgrade/$', 'upgrade', name='upgrade'),
    url(r'^billing/$', 'billing_history', name='billing_history'),
    url(r'^billing/cancel/$', 'cancel_subscription', name='cancel_subscription'),
)


