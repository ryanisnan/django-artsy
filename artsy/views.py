from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext

from models import Project, ProjectImage, Category

def project_index(request):
	""" Render the view that displays the entire list of projects. """
	
	projects = Project.objects.all()
	context = {
		'projects' : projects,
	}
	return render_to_response('project_index.html', context, RequestContext(request))
	
def project_detail(request, slug):
	""" Render the view that displays the details of a single project. """
	
	project = get_object_or_404(Project, slug=slug)
	project_images = ProjectImage.objects.filter(project=project)
	context = {
		'project' : project,
		'project_images' : project_images,
	}
	return render_to_response('project_detail.html', context, RequestContext(request))

def category_index(request, slug):
	""" Render the view that displays a category and its projects. """
	
	category = get_object_or_404(Category, slug=slug)
	projects = get_list_or_404(Project, category=category)
	context = {
		'category' : category,
		'projects' : projects,
	}
	return render_to_response('category_index.html', context, RequestContext(request))