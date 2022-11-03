from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q

from .models import *

def menu_render(request, template, context={}):
	fs = Family.objects.all()
	context['families'] = [f.name for f in fs]

	return render(request, template, context)

# Create your views here.
def index(request):
	return menu_render(request, 'snake/index.html')

def family(request, name):
	f = Family.objects.get(name=name)
	return menu_render(request, 'snake/family.html', {'family': f})

def genes(request):
	if request.method == 'GET':
		species = [(s.pk, s.scientific_name) for s in Species.objects.filter(sequenced=1)]
		return menu_render(request, 'snake/genes.html', {'species': species})

	elif request.method == 'POST':
		start = int(request.POST.get('start'))
		length = int(request.POST.get('length'))
		draw = int(request.POST.get('draw'))
		species = int(request.POST.get('species'))
		search = request.POST.get('search[value]')

		gs = Gene.objects.filter(species__pk=species)

		total_count = gs.count()

		if search:
			gs = gs.filter(Q(symbol__icontains=search) | Q(gene_id__icontains=search) |
							 Q(biotype__icontains=search))

			filter_count = gs.count()
		else:
			filter_count = total_count

		data = []
		for g in gs[start:start+length]:
			data.append((g.chrom, g.start, g.end, g.strand, g.cds_len,
						 g.exon_num, g.symbol, g.gene_id, g.biotype))

		return JsonResponse({
			'draw': draw,
			'recordsTotal': total_count,
			'recordsFiltered': filter_count,
			'data': data
		})

def genomes(request):
	if request.method == 'GET':
		gs = GenomeDownload.objects.all()
		return menu_render(request, 'snake/genomes.html', {'genomes': gs})

def epigenomes(request):
	if request.method == 'GET':
		es = EpigenomeDownload.objects.all()
		return menu_render(request, 'snake/epigenomes.html', {'epigenomes': es})

def transcriptomes(request):
	if request.method == 'GET':
		return menu_render(request, 'snake/transcriptomes.html')
	elif request.method == 'POST':
		return JsonResponse({})

