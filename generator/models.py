from django.db import models

# Create your models here.
class PasswordSafe(models.Model):
	platform = models.CharField(max_length = 20, null = False, blank = True)
	Password = models.CharField(max_length = 20, null = False, blank = False)

	def __str__(self):
		return self.platform
