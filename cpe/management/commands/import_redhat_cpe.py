from django.core.management.base import BaseCommand, CommandError
from cpe.imports import *

class Command(BaseCommand):
    help = 'Import Red Hat CPE'
    def handle(self, *args, **options):
		try:
			import_redhat_cpe()
		except:
			raise CommandError('import_redhat_cpe failed')
		
		self.stdout.write('Successfully imported Red Hat CPE')