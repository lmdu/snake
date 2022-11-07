from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
	list_display = ('name', 'created')

@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
	list_display = ('family', 'scientific_name', 'ncbi_taxonomy',
		'sequenced', 'annotated', 'expressed'
	)

@admin.register(Gene)
class GeneAdmin(admin.ModelAdmin):
	list_display = ('species', 'chrom', 'start', 'end', 'strand',
		'symbol', 'gene_id', 'biotype'
	)

@admin.register(GeneExpression)
class GeneExpressionAdmin(admin.ModelAdmin):
	pass

@admin.register(GenomeDownload)
class GenomeDownloadAdmin(admin.ModelAdmin):
	list_display = ('species', 'assembly_level', 'scaffold_n50',
		'contig_n50', 'genome_version'
	)

#@admin.register(EpigenomeDownload)
#class EpigenomeDownloadAdmin(admin.ModelAdmin):
#	pass

@admin.register(GenomeBrowser)
class GenomeBrowserAdmin(admin.ModelAdmin):
	list_display = ('species', 'url')

@admin.register(TranscriptomeDownload)
class TranscriptomeDownloadAdmin(admin.ModelAdmin):
	list_display = ('species', 'name', 'link')
