from django.core.management.base import BaseCommand
from apps.home.models import Bloco

class Command(BaseCommand):
    help = 'Cria automaticamente os blocos definidos em BLOCO_CHOICES'

    def handle(self, *args, **kwargs):
        criados = 0
        for valor, _ in Bloco.BLOCO_CHOICES:
            obj, created = Bloco.objects.get_or_create(nome=valor)
            if created:
                criados += 1
                self.stdout.write(self.style.SUCCESS(f'Bloco criado: {valor}'))
            else:
                self.stdout.write(self.style.WARNING(f'Bloco já existe: {valor}'))

        self.stdout.write(self.style.SUCCESS(f'{criados} blocos criados com sucesso.'))
