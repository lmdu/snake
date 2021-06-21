from django.urls import path
from . import views

app_name = 'snake'

urlpatterns = [
	path('', views.index, name='index'),
	path('family/<name>', views.family, name='family'),
	path('genes', views.genes, name='genes'),
	path('genomes', views.genomes, name='genomes'),
	path('epigenomes', views.epigenomes, name='epigenomes'),
	path('transcriptomes', views.transcriptomes, name='transcriptomes'),
]