# Solicita ao usuário que insira um nome para validação
nome = input("Digite o nome para validação: ")

# Inicializa a variável de controle
valido = True  # Indica se o nome é válido

# Verifica se o nome não está vazio
if len(nome) == 0:
    valido = False  # Se o nome estiver vazio, marca como inválido

# Percorre cada caractere do nome
for char in nome:
    # Verifica se o caractere está entre 'A' e 'Z', 'a' e 'z', ou é um espaço
    if not ('A' <= char <= 'Z' or 'a' <= char <= 'z' or char == ' '):
        valido = False  # Se encontrar um caractere inválido, marca como inválido

# Verifica se todas as condições foram atendidas
if valido:
    print(f"'{nome}' é um nome válido.")  # Nome é válido
else:
    print(f"'{nome}' é um nome inválido.")  # Nome é inválido
