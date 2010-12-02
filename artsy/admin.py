from django.contrib import admin
from designersportfolio.models import Project, ProjectImage, Category

class ProjectImageAdmin(admin.TabularInline):
	model = ProjectImage
	
class CategoryAdmin(admin.ModelAdmin):
	model = Category
	
class ProjectAdmin(admin.ModelAdmin):
	inlines = [
		ProjectImageAdmin,
	]
	
	list_display = ('title', 'simple_description')
	prepopulated_fields = { 'slug' : ('title',) }
	list_filter = ('category',)

admin.site.register(Category, CategoryAdmin)	
admin.site.register(Project, ProjectAdmin)