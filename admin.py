from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
	pass

@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
	pass

@admin.register(Gene)
class GeneAdmin(admin.ModelAdmin):
	pass

@admin.register(GeneExpression)
class GeneExpressionAdmin(admin.ModelAdmin):
	pass

@admin.register(GenomeDownload)
class GenomeDownloadAdmin(admin.ModelAdmin):
	pass

@admin.register(EpigenomeDownload)
class EpigenomeDownloadAdmin(admin.ModelAdmin):
	pass
