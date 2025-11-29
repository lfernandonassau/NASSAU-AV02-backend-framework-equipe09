from django.contrib import admin
from .models import HistoricoSimulacao


@admin.register(HistoricoSimulacao)
class HistoricoSimulacaoAdmin(admin.ModelAdmin):
	list_display = (
		'id', 'cliente', 'simulacao', 'data_registro'
	)
	list_filter = ('data_registro',)
	search_fields = ('cliente__nome', 'simulacao__id')
