from django.db import models

class Category_metal(models.Model):
	title = models.CharField(max_length=200)
	def __str__(self):
		return self.title
class Metal(models.Model):
	title = models.CharField(max_length = 140, blank = True)
	description = models.TextField()
	category = models.ForeignKey(Category_metal,on_delete=models.CASCADE)
	image = models.FileField(blank=True)
	image2 = models.FileField(blank=True)
	image3 = models.FileField(blank=True)	
	image4 = models.FileField(blank=True)
	image5 = models.FileField(blank=True)

	def __str__(self):
		return self.title