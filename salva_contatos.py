from google.oauth2 import service_account
import googleapiclient.discovery

# Função para salvar o contato na agenda do Google
def salvar_contato_google(nome, sobrenome, telefone):
    credenciais = service_account.Credentials.from_service_account_file(
        'C:\Users\marce\PycharmProjects\SistemaAtividros\venv\credentials.json',
        scopes=['https://www.googleapis.com/auth/contacts']
    )

    service = googleapiclient.discovery.build('people', 'v1', credentials=credenciais)

    contato = {
        'names': [
            {
                'givenName': nome,
                'familyName': sobrenome
            }
        ],
        'phoneNumbers': [
            {
                'value': telefone
            }
        ]
    }

    service.people().createContact(body=contato).execute()
    print("Contato salvo na agenda do Google com sucesso.")

# Exemplo de uso:
if __name__ == "__main__":
    nome_cliente = "teste"
    sobrenome_cliente = "Silva"
    telefone_cliente = "+551234567890"  # Substitua pelo número de telefone do cliente

    salvar_contato_google(nome_cliente, sobrenome_cliente, telefone_cliente)
