from django.core.management.base import BaseCommand, CommandError
from iavm.imports import *

class Command(BaseCommand):
    help = 'Import DISA IAVM-to-CVE'

    def handle(self, *args, **options):
		try:
			import_disa_iavm_cve()
		except:
			raise CommandError('import_disa_iavm_cve failed')
		
		self.stdout.write('Successfully imported DISA IAVM-to-CVE')