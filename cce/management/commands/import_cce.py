from django.core.management.base import BaseCommand, CommandError
from cce.imports import *

class Command(BaseCommand):
    help = 'Import NIST CCE'
    def handle(self, *args, **options):
		try:
			import_nist_cce()
		except:
			raise CommandError('import_nist_cce failed')
		
		self.stdout.write('Successfully imported NIST CCE')