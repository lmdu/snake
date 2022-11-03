from django.db import models

# Create your models here.
class Family(models.Model):
	name = models.CharField(max_length=30, help_text="Family name")
	tree = models.ImageField(upload_to='snake/treeimg', blank=True, help_text="Tree image file")
	description = models.TextField(help_text="Family detailed description", blank=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Species(models.Model):
	SEQUENCED = (
		(0, 'non-sequenced'),
		(1, 'sequenced')
	)
	ANNOTATED = (
		(0, 'non-annotated'),
		(1, 'annotated')
	)
	EXPRESSED = (
		(0, 'non-estimated'),
		(1, 'estimated')
	)
	family = models.CharField(max_length=20, help_text="Family name")
	scientific_name = models.CharField(max_length=50, help_text="Species scientific name")
	common_name = models.CharField(max_length=50, help_text="Species common name", blank=True)
	ncbi_taxonomy = models.CharField(max_length=20, help_text="NCBI taxonomy ID", blank=True)
	short_taxonomy = models.CharField(max_length=255, help_text="Short taxonomy description", blank=True)
	description = models.TextField(help_text="Species description", blank=True)
	sequenced = models.SmallIntegerField(choices=SEQUENCED, default=0, help_text="Genome was sequenced")
	annotated = models.SmallIntegerField(choices=ANNOTATED, default=0, help_text="Genome was annotated")
	expressed = models.SmallIntegerField(choices=EXPRESSED, default=0, help_text="Gene expression was estimated")

	def __str__(self):
		return self.scientific_name

class Gene(models.Model):
	chrom = models.CharField(max_length=100, help_text="Chromosome name")
	start = models.IntegerField(help_text="Gene start position")
	end = models.IntegerField(help_text="Gene end position")
	strand = models.CharField(max_length=2, help_text="Gene strand")
	cds_len = models.IntegerField(help_text="CDS length")
	exon_num = models.IntegerField(help_text="exon number")
	symbol = models.CharField(max_length=30, help_text="Gene symbol")
	gene_id = models.CharField(max_length=30, help_text="Gene ID number")
	gene_name = models.CharField(max_length=255, help_text="Gene long name", blank=True)
	biotype = models.CharField(max_length=100, help_text="Gene biotype", blank=True)
	ncbi_id = models.CharField(max_length=30, help_text="NCBI gene ID", blank=True)
	species = models.ForeignKey(Species, on_delete=models.CASCADE)

	def __str__(self):
		return self.symbol

class GeneExpression(models.Model):
	tissue = models.CharField(max_length=100, help_text="tissue or sample")
	category = models.CharField(max_length=50, help_text="tissue type or category")
	express = models.FloatField(help_text="gene expression value")
	gene = models.ForeignKey(Gene, on_delete=models.CASCADE)
	species = models.ForeignKey(Species, on_delete=models.CASCADE)

class EpigenomeDownload(models.Model):
	reads = models.CharField(max_length=255)
	link = models.CharField(max_length=255)
	species = models.ForeignKey(Species, on_delete=models.CASCADE)

class GenomeDownload(models.Model):
	LEVELS = [
		(0, 'unknown'),
		(1, 'chromosome'),
		(2, 'scaffold'),
		(3, 'contig')
	]

	assembly_level = models.SmallIntegerField(choices=LEVELS, default=0, help_text="Assembly level")
	scaffold_n50 = models.IntegerField(help_text="Scaffold N50 length")
	contig_n50 = models.IntegerField(help_text="Contig N50 length")
	genome_version = models.CharField(max_length=20, blank=True)
	genome_link = models.CharField(max_length=255, help_text="Genome download link")
	annot_link = models.CharField(max_length=255, help_text="Genome annotation download link")
	species = models.ForeignKey(Species, on_delete=models.CASCADE)
