from django.db import models
                                                                                       

class Category_geo(models.Model):
	title = models.CharField(max_length = 120)
	def __str__(self):
		return self.title
class Category_new(models.Model):
	title = models.CharField(max_length = 120 , blank = True, null = True)
	def __str__(self):
		return self.title


class Geology(models.Model):
	title = models.CharField(max_length = 160)
	description = models.TextField()
	advanced_description = models.TextField(blank = True, null = True)
	category = models.ForeignKey(Category_geo,on_delete=models.CASCADE)
	category_search = models.ForeignKey(Category_new,on_delete=models.CASCADE, blank = True, null = True)
	image = models.FileField(blank=True, null = True)

	date= models.DateTimeField('published_date')

	def __str__(self):
		return self.title

# Create your models here.
