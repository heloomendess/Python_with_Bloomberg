nome_email = [{'nome': 'Ana', 'email': 'ana@gmail.com', 'mulher': True},
              {'nome': 'Amanda', 'email': 'amanda@gmail.com', 'mulher': True},
              {'nome': 'Maria', 'email': 'maria@gmail.com', 'mulher': True},
              {'nome': 'Heloisa', 'email': 'helo@gmail.com', 'mulher': True},
              {'nome': 'Pedro', 'email': 'pedro@gmail.com', 'mulher': False},
              {'nome': 'João', 'email': 'joao@gmail.com', 'mulher': False},
              {'nome': 'André', 'email': 'andre@gmail.com', 'mulher': False},
              {'nome': 'Mathias', 'email': 'mathias@gmail.com', 'mulher': False}
]


def enviar_mensagem(nome_email):
    nome = nome_email["nome"]
    email = nome_email["email"]
    mulher = nome_email["mulher"]
    
    if mulher == True:
        mensagem = f"Olá querida {nome}, seu email ({email}) foi enviado com sucesso!"
    else:
        mensagem = f"Olá {nome}, seu email ({email}) foi enviado com sucesso!"
    
    print(mensagem)

for nome_email in nome_email:
    enviar_mensagem(nome_email)

