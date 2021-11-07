from django.db import models

# Create your models here.
class Vbet(models.Model):

	full_name = models.CharField(max_length=20)
	email = models.EmailField( null=True, blank=True)
	company = models.CharField(max_length=15, null=True, blank=True)
	position = models.CharField(max_length=50, null=True, blank=True)
	logo = models.ImageField(upload_to='media/', null=True, blank=True)
	phone = models.CharField(max_length=16, null=True, blank=True)






	"""docstring for Vbet"""
	# def __init__(self, arg):
	# 	super(Vbet, self).__init__()
	# 	self.arg = arg
	# 	