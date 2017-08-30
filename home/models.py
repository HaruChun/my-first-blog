from django.db import models
#from jsonfield import JSONField

class Book(models.Model):
	isbn = models.BigIntegerField(primary_key=True)
	title = models.CharField(max_length=128)

	def __str__(self):
		return self.title
# Create your models here.
