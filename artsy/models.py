from django.db import models

import os.path

"""
Determine the upload path for this particular project.
An example upload path would be 'apps/artsy/my-project/image1.jpg'
The path, when used is added to the project's MEDIA_ROOT setting.
"""
def get_project_image_upload_path(instance, filename):
	try:
		path = os.path.join('apps/artsy', instance.slug, filename)
	except TypeError:
		try:
			path = os.path.join('apps/artsy', instance.project.slug, filename)
		except TypeError:
			pass
	return path
		
"""
A Category for projects to be filed under. Example categories might be
Typography, Web, Print, Concept Art, etc.
"""
class Category(models.Model):
	title = models.CharField(max_length=32)
	slug = models.CharField(max_length=32, help_text='A slug is how this category is represented when in the URL.')
	priority = models.SmallIntegerField(default=0, help_text='Priority defines the order in which categories are retrieved, in descending order.')

	class Meta:
		ordering = ('-priority',)
		verbose_name_plural = 'Categories'
		
	def __unicode__(self):
		return self.title
	
"""
A Project is the core object of artsy. A project represents a discrete
unit of work. A project can belong to a category, and have a collection of
images, as well as the standard attributes listed below.
"""
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

"""
An image associated to a project. A ProjectImage can have a thumbnail image
as well as an actual image. ProjectImages can be ordered too on a per-project
basis.
"""		
class ProjectImage(models.Model):
	project = models.ForeignKey('Project')
	thumbnail = models.ImageField(upload_to=get_project_image_upload_path, null=True, blank=True)
	image = models.ImageField(upload_to=get_project_image_upload_path)
	order = models.SmallIntegerField(default=0, help_text='The ordering in which this image should show up when displayed by other images for this project, in ascending order.')
	description = models.CharField(max_length=255, null=True, blank=True, help_text='A simple textual description of this image.')
	
	class Meta:
		ordering = ('order',)