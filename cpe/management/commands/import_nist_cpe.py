from django.core.management.base import BaseCommand, CommandError
from cpe.imports import *

class Command(BaseCommand):
    help = 'Import NIST CPE'
    def handle(self, *args, **options):
		try:
			import_nist_cpe()
		except:
			raise CommandError('import_nist_cpe failed')
		
		self.stdout.write('Successfully imported NIST CPE')