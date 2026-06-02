# Textos em Python
print("Olá, Mundo!")  # String (str)
print('Python é legal!')  # String (str)    

# Strings podem ser definidas usando aspas simples ou duplas
print("Ele disse: 'Python é incrível!'")  # Usando aspas duplas
print('Ela respondeu: "Sim, é verdade!"')  # Usando aspas simples   

# Strings multilinha
texto_multilinha = """Este é um texto
multilinha em Python.
Ele pode conter várias linhas de texto."""
print(texto_multilinha)

# Concatenando strings
nome = "Alice"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome  # Concatenando com um espaço
print(nome_completo)

# Repetindo strings
repeticao = "Python " * 3  # Repete a string 3 vezes
print(repeticao)

# Acessando caracteres em uma string
frase = "Python é divertido!"
print(frase[0])  # Primeiro caractere
print(frase[7])  # Oitavo caractere
print(frase[-1])  # Último caractere
print(frase[-3])  # Terceiro caractere a partir do final

# Fatiamento de strings
print(frase[0:6])  # Fatiamento do início até o índice 5
print(frase[7:9])  # Fatiamento do índice 7 até o índice 8
print(frase[10:])  # Fatiamento do índice 10 até o final
print(frase[:6])  # Fatiamento do início até o índice 5
print(frase[::2])  # Fatiamento com passo 2 (pula um caractere) 

# Len() para obter o comprimento de uma string
print(len(frase))  # Imprime o número de caracteres na string   

# Help
help(str)  # Exibe a documentação da classe str (string)