from django.core.management.base import BaseCommand, CommandError
from cve.imports import *

class Command(BaseCommand):
    help = 'Import NIST CVE'

    def handle(self, *args, **options):
		try:
			import_nist_cve()
		except:
			raise CommandError('import_nist_cve failed')
		
		self.stdout.write('Successfully imported NIST CVE')