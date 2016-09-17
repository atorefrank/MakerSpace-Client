from django.db import models
from .signal import notify
# Create your models here.



def  new_notification(*args, **kwargs):
	notify.connect(new_notification)