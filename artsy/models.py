from django.db import models

import os.path
	
def get_project_image_upload_path(instance, filename):
	try:
		path = os.path.join('apps/designersportfolio', instance.slug, filename)
	except TypeError:
		try:
			path = os.path.join('apps/designersportfolio', instance.project.slug, filename)
		except TypeError:
			pass
	return path
		

class Category(models.Model):
	title = models.CharField(max_length=32)
	slug = models.CharField(max_length=32, help_text='A slug is how this category is represented when in the URL.')
	priority = models.SmallIntegerField(default=0, help_text='Priority defines the order in which categories are retrieved, in descending order.')

	class Meta:
		ordering = ('-priority',)
		verbose_name_plural = 'Categories'
		
	def __unicode__(self):
		return self.title
	
class Project(models.Model):
	title = models.CharField(max_length=140)
	slug = models.SlugField(max_length=140, help_text='A slug is how this project is represented when in the URL.')
	category = models.ForeignKey('Category', null=True, blank=True)
	simple_description = models.CharField(null=True, blank=True, max_length=140, help_text='A simple line of text to describe the project in as few words as possible.')
	description = models.TextField(null=True, blank=True, help_text='A textual description of the project.')
	priority = models.SmallIntegerField(default=0, help_text='Priority defines the order in which projects are retrieved, in descending order.')
	date_created = models.DateField(auto_now_add=True)
	preview_image = models.ImageField(null=True, blank=True, upload_to=get_project_image_upload_path, help_text='A simple image that is typically used as a preview to this project.')
	
	class Meta:
		get_latest_by = 'date_created'
		ordering = ('-priority','-date_created')
	
	def __unicode__(self):
		return self.title
	
	@models.permalink
	def get_absolute_url(self):
		from designersportfolio.views import project_detail
		return (project_detail, [self.slug])
		
class ProjectImage(models.Model):
	project = models.ForeignKey('Project')
	image = models.ImageField(upload_to=get_project_image_upload_path)
	order = models.SmallIntegerField(default=0, help_text='The ordering in which this image should show up when displayed by other images for this project, in ascending order.')
	description = models.CharField(max_length=255, null=True, blank=True, help_text='A simple textual description of this image.')
	
	class Meta:
		ordering = ('order',)