from django.core.management.base import BaseCommand, CommandError
from iavm.libs.IAVM import *

class Command(BaseCommand):
    help = 'Create IAVM-to-CPE Document'

    def handle(self, *args, **options):
		try:
			iavm_to_cpe_doc()
		except:
			raise CommandError('iavm_to_cpe_doc failed')
		
		self.stdout.write('Successfully created IAVM-to-CPE Document')