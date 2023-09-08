import csv
import openai

# Leitura dos IDs do arquivo 'ids.txt'
with open('ids.txt', 'r') as file:
    user_ids = [int(line.strip()) for line in file]

# Associe valores aos IDs (substitua pelos valores reais)
user_data = {
    100: 'Agnus',
    200: 'Dennys',
    300: 'Ruan'
}

# Crie uma lista de pares ID-valor a partir dos IDs lidos
user_data_list = [{'ID': id, 'Valor': user_data.get(id)} for id in user_ids]

# Nome do arquivo CSV onde os dados serão armazenados
csv_filename = 'dados.csv'

# Escreva os pares ID-valor no arquivo CSV
with open(csv_filename, 'w', newline='') as csv_file:
    fieldnames = ['ID', 'Valor']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    csv_writer.writeheader()
    csv_writer.writerows(user_data_list)

print(f'Dados foram gravados em {csv_filename}')

# Defina sua chave da API da OpenAI
openai_api_key = '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'
openai.api_key = openai_api_key

# Defina a lista de usuários com seus nomes
users = [
    {'name': 'Agnus'},
    {'name': 'Dennys'},
    {'name': 'Ruan'}
]

def generate_ai_news(user):
    user_name = user['name']
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Crie uma mensagem para {user_name} sobre os melhores jogadores da semana nas principais ligas de futebol de novo (máximo de 100 caracteres)",
        max_tokens=50  # Ajuste o número de tokens conforme necessário
    )
    return completion.choices[0].text.strip()

# Gere notícias para cada usuário
for user in users:
    news = generate_ai_news(user)
    print(news)
