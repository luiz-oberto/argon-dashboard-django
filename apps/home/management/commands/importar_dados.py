import re
from django.core.management.base import BaseCommand
from apps.home.models import ItemPatrimonio

class Command(BaseCommand):
    help = 'Importar dados de um arquivo .txt para o banco de dados'

    def handle(self, *args, **kwargs):
        file_path = 'C:\\Users\\o Dev\\Desktop\\argon-dashboard-django\\texto_atualizado.txt' # mudar

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.readlines()

            pattern = r'^[0-9]{7}'  # Padrão para o código de 7 dígitos

            for line in content:
                match = re.match(pattern, line)
                if match:
                    # Se encontrar um código no início da linha
                    codigo = match.group(0)
                    # Extrai a descrição e o local do resto da linha
                    restante = line[len(codigo):].strip().split(' - ')
                    descricao = restante[0] if len(restante) > 0 else 'Descrição não informada'
                    local = restante[1] if len(restante) > 1 else 'Local não informado'

                    # Cria o objeto e salva no banco de dados
                    ItemPatrimonio.objects.create(
                        codigo=codigo,
                        descricao=descricao,
                        local=local
                    )

            self.stdout.write(self.style.SUCCESS('Dados importados com sucesso!'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro ao importar dados: {e}'))
