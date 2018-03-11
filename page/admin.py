from django.contrib import admin
from .models import Project, Project_Photo, Vizualizace
# Register your models here.


class ProjectPhotoInLine(admin.TabularInline):
    model = Project_Photo
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info',    {'fields' : ['name','type']}),
        ('Description', {'fields' : ['text']}),
        ('Intro photo', {'fields' : ['screen']}),
        ('Date information', {'fields' : ['published_date']}),
    ]
    inlines = [ProjectPhotoInLine]
    list_display = ('name' , 'published_date')
    list_filter = ['published_date']
    search_fields = ['name']


class VizualizaceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info',    {'fields' : ['name']}),
        ('Photo', {'fields' : ['screen']}),
        ('Date information', {'fields' : ['published_date']}),
    ]
    list_display = ('name' , 'published_date')
    list_filter = ['published_date']
    search_fields = ['name']

#admin.site.register(Introduction, IntroductionAdmin)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Vizualizace, VizualizaceAdmin)
