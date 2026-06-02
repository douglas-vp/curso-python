# Aprendendo Python: Conceitos Básicos

Este repositório reúne os principais conceitos básicos da linguagem **Python**, com explicações simples e exemplos práticos para iniciantes.

O objetivo é servir como material de estudo, consulta rápida e prática para quem está começando na programação com Python.

---

## Sumário

- [O que é Python?](#o-que-é-python)
- [Como estudar Python](#como-estudar-python)
- [Ambiente de desenvolvimento](#ambiente-de-desenvolvimento)
- [Scripts, console e debugger](#scripts-console-e-debugger)
- [Tipos numéricos: int e float](#tipos-numéricos-int-e-float)
- [Textos: strings](#textos-strings)
- [Variáveis](#variáveis)
- [Entrada de dados com input](#entrada-de-dados-com-input)
- [Formatação de texto com f-strings](#formatação-de-texto-com-f-strings)
- [Controle de fluxo](#controle-de-fluxo)
- [Listas e tuplas](#listas-e-tuplas)
- [Sequências e slicing](#sequências-e-slicing)
- [Laços de repetição](#laços-de-repetição)
- [Dicionários](#dicionários)
- [Métodos](#métodos)
- [Compreensão de listas](#compreensão-de-listas)
- [Funções](#funções)
- [Módulos e biblioteca padrão](#módulos-e-biblioteca-padrão)
- [Conclusão](#conclusão)
- [Tecnologias utilizadas nos exemplos](#tecnologias-utilizadas-nos-exemplos)
- [Autor](#autor)

---

## O que é Python?

Python é uma linguagem de programação de alto nível, conhecida por sua sintaxe simples, clara e fácil de ler.

Ela é muito utilizada em diversas áreas, como:

- Análise de dados;
- Ciência de dados;
- Inteligência artificial;
- Automação de tarefas;
- Desenvolvimento web;
- Criação de scripts;
- Ensino de programação.

Por ser uma linguagem simples e poderosa, Python é uma excelente escolha para quem está começando a programar.

---

## Como estudar Python

A melhor forma de aprender Python é praticando.

Algumas recomendações importantes:

- Digite os exemplos manualmente;
- Execute os códigos;
- Altere os exemplos e observe os resultados;
- Leia mensagens de erro com atenção;
- Resolva exercícios;
- Crie pequenos projetos;
- Pesquise dúvidas na documentação, fóruns e comunidades.

Programar não é apenas decorar comandos. Programar é aprender a resolver problemas usando lógica e código.

---

## Ambiente de desenvolvimento

Para escrever e executar códigos em Python, é necessário utilizar um ambiente de desenvolvimento.

Algumas opções são:

- Mu Editor;
- VS Code;
- PyCharm;
- Jupyter Notebook;
- Google Colab;
- Terminal ou console interativo.

Para iniciantes, uma ferramenta mais simples pode facilitar o aprendizado, pois permite focar nos conceitos da linguagem antes de lidar com configurações mais avançadas.

---

## Scripts, console e debugger

Em Python, é possível executar código de diferentes formas.

### Scripts

Um script é um arquivo com extensão `.py` que contém comandos Python.

Exemplo:

```python
print("Olá, mundo!")
print("Estou aprendendo Python!")
```

Scripts são úteis porque ficam salvos no computador e podem ser executados novamente.

### Console

O console permite testar comandos de forma interativa.

Exemplo:

```python
2 + 3
```

Resultado:

```text
5
```

O console é útil para testar ideias rapidamente, mas o código digitado nele geralmente não fica salvo.

### Debugger

O debugger permite executar o código linha por linha.

Ele ajuda a:

- Encontrar erros;
- Entender a ordem de execução;
- Acompanhar valores de variáveis;
- Corrigir problemas no programa.

---

## Tipos numéricos: int e float

Python possui dois tipos numéricos principais: `int` e `float`.

### int

O tipo `int` representa números inteiros.

```python
idade = 30
quantidade = 10
temperatura = -2
```

### float

O tipo `float` representa números com casas decimais.

```python
altura = 1.75
preco = 19.90
peso = 72.5
```

### Verificando o tipo de dado

A função `type()` permite verificar o tipo de um valor.

```python
print(type(10))
print(type(10.5))
```

Saída:

```text
<class 'int'>
<class 'float'>
```

### Operações matemáticas

```python
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(2 ** 3)
```

Saída:

```text
15
5
50
2.0
8
```

---

## Textos: strings

Textos em Python são representados pelo tipo `str`, conhecido como string.

Strings podem ser criadas com aspas simples ou duplas.

```python
nome = "Douglas"
curso = 'Python'
```

### Concatenando strings

```python
nome = "Douglas"
mensagem = "Olá, " + nome

print(mensagem)
```

Saída:

```text
Olá, Douglas
```

### Repetindo strings

```python
print("Python " * 3)
```

Saída:

```text
Python Python Python
```

### Tamanho de uma string

A função `len()` retorna a quantidade de caracteres de uma string.

```python
nome = "Python"

print(len(nome))
```

Saída:

```text
6
```

---

## Variáveis

Variáveis são nomes usados para armazenar valores.

```python
nome = "Ana"
idade = 25
altura = 1.68
```

As variáveis tornam o código mais claro e organizado.

Exemplo:

```python
pi = 3.14
raio = 5
area = pi * raio ** 2

print(area)
```

### Regras para nomes de variáveis

Boas práticas para nomear variáveis:

- Usar nomes claros;
- Não começar com número;
- Não usar espaços;
- Não usar palavras reservadas do Python;
- Preferir letras minúsculas e `_`.

Exemplos corretos:

```python
nome_usuario = "Ana"
idade = 25
valor_total = 150.75
```

Exemplos incorretos:

```python
2idade = 25
nome usuario = "Ana"
if = 10
```

---

## Entrada de dados com input

A função `input()` permite receber dados digitados pelo usuário.

```python
nome = input("Digite seu nome: ")

print("Olá,", nome)
```

Por padrão, todo valor recebido com `input()` é tratado como texto.

Exemplo com conversão para número:

```python
idade = int(input("Digite sua idade: "))

print("Daqui 5 anos você terá", idade + 5)
```

---

## Formatação de texto com f-strings

As f-strings permitem inserir variáveis dentro de textos de forma simples.

```python
nome = "Douglas"
idade = 30

print(f"Olá, {nome}. Você tem {idade} anos.")
```

Saída:

```text
Olá, Douglas. Você tem 30 anos.
```

Também é possível usar expressões dentro das chaves.

```python
idade = 30

print(f"Daqui 5 anos você terá {idade + 5} anos.")
```

Saída:

```text
Daqui 5 anos você terá 35 anos.
```

---

## Controle de fluxo

Controle de fluxo permite que o programa tome decisões com base em condições.

### if

```python
idade = 18

if idade >= 18:
    print("Maior de idade")
```

### if e else

```python
idade = 16

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

### if, elif e else

```python
nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

### Operadores de comparação

| Operador | Descrição |
|---|---|
| `==` | Igual |
| `!=` | Diferente |
| `>` | Maior que |
| `<` | Menor que |
| `>=` | Maior ou igual |
| `<=` | Menor ou igual |

### Operadores booleanos

| Operador | Descrição |
|---|---|
| `and` | Todas as condições precisam ser verdadeiras |
| `or` | Pelo menos uma condição precisa ser verdadeira |
| `not` | Inverte o valor lógico |

Exemplo:

```python
idade = 20
tem_cnh = True

if idade >= 18 and tem_cnh:
    print("Pode dirigir")
else:
    print("Não pode dirigir")
```

---

## Listas e tuplas

### Listas

Listas armazenam vários valores em uma única variável.

```python
frutas = ["maçã", "banana", "laranja"]

print(frutas)
```

Acessando elementos:

```python
print(frutas[0])
print(frutas[1])
```

Alterando valores:

```python
frutas[1] = "uva"

print(frutas)
```

Adicionando itens:

```python
frutas.append("abacaxi")

print(frutas)
```

### Tuplas

Tuplas também armazenam vários valores, mas são imutáveis.

```python
coordenadas = (10, 20)

print(coordenadas)
```

Tuplas são úteis quando os dados não devem ser alterados.

---

## Sequências e slicing

Strings, listas e tuplas são exemplos de sequências.

O slicing permite acessar partes de uma sequência.

```python
texto = "Python"

print(texto[0])
print(texto[1])
print(texto[0:3])
```

Saída:

```text
P
y
Pyt
```

Exemplo com lista:

```python
numeros = [10, 20, 30, 40, 50]

print(numeros[1:4])
```

Saída:

```text
[20, 30, 40]
```

Também é possível usar um valor de pulo.

```python
numeros = [1, 2, 3, 4, 5, 6]

print(numeros[0:6:2])
```

Saída:

```text
[1, 3, 5]
```

---

## Laços de repetição

Laços de repetição permitem executar um bloco de código várias vezes.

### for

O `for` é usado para percorrer sequências.

```python
nomes = ["Ana", "Bruno", "Carlos"]

for nome in nomes:
    print(nome)
```

Saída:

```text
Ana
Bruno
Carlos
```

### range

A função `range()` gera uma sequência de números.

```python
for numero in range(5):
    print(numero)
```

Saída:

```text
0
1
2
3
4
```

Exemplo com início, fim e passo:

```python
for numero in range(1, 10, 2):
    print(numero)
```

Saída:

```text
1
3
5
7
9
```

### while

O `while` repete um bloco enquanto uma condição for verdadeira.

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

Saída:

```text
1
2
3
4
5
```

### break

O `break` interrompe o loop.

```python
for numero in range(10):
    if numero == 5:
        break
    print(numero)
```

### continue

O `continue` pula para a próxima repetição.

```python
for numero in range(6):
    if numero == 3:
        continue
    print(numero)
```

---

## Dicionários

Dicionários armazenam dados no formato chave e valor.

```python
pessoa = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "Belo Horizonte"
}
```

Acessando valores:

```python
print(pessoa["nome"])
print(pessoa["idade"])
```

Alterando valores:

```python
pessoa["idade"] = 26
```

Adicionando nova chave:

```python
pessoa["profissao"] = "Desenvolvedora"
```

Verificando se uma chave existe:

```python
print("nome" in pessoa)
```

Saída:

```text
True
```

---

## Métodos

Métodos são funções associadas a objetos.

### Métodos de string

```python
texto = "Python"

print(texto.upper())
print(texto.lower())
```

Saída:

```text
PYTHON
python
```

Outros exemplos:

```python
frase = "Estou aprendendo Python"

print(frase.startswith("Estou"))
print(frase.endswith("Python"))
print(frase.count("o"))
print(frase.replace("Python", "programação"))
```

### Métodos de lista

```python
numeros = [3, 1, 2]

numeros.append(4)
print(numeros)

numeros.sort()
print(numeros)

numeros.reverse()
print(numeros)

numeros.pop()
print(numeros)
```

### Métodos de dicionário

```python
pessoa = {
    "nome": "Ana",
    "idade": 25
}

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get("nome"))
```

---

## Compreensão de listas

Compreensão de listas é uma forma curta de criar listas.

Exemplo tradicional:

```python
quadrados = []

for numero in range(1, 6):
    quadrados.append(numero ** 2)

print(quadrados)
```

Com list comprehension:

```python
quadrados = [numero ** 2 for numero in range(1, 6)]

print(quadrados)
```

Saída:

```text
[1, 4, 9, 16, 25]
```

Exemplo com condição:

```python
pares = [numero for numero in range(1, 11) if numero % 2 == 0]

print(pares)
```

Saída:

```text
[2, 4, 6, 8, 10]
```

---

## Funções

Funções agrupam instruções para executar uma tarefa específica.

Elas ajudam a:

- Organizar o código;
- Evitar repetição;
- Facilitar manutenção;
- Melhorar a legibilidade.

### Criando uma função

```python
def saudacao():
    print("Olá, seja bem-vindo!")
```

Chamando a função:

```python
saudacao()
```

### Função com parâmetro

```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Ana")
```

### Função com retorno

```python
def somar(a, b):
    return a + b

resultado = somar(10, 5)

print(resultado)
```

Saída:

```text
15
```

### Parâmetros com valor padrão

```python
def apresentar(nome, idade=18):
    print(f"{nome} tem {idade} anos.")

apresentar("Ana")
apresentar("Bruno", 25)
```

### Função sem retorno

```python
def mostrar_mensagem():
    print("Essa função apenas exibe uma mensagem.")

resultado = mostrar_mensagem()

print(resultado)
```

Saída:

```text
Essa função apenas exibe uma mensagem.
None
```

Quando uma função não possui `return`, ela retorna `None`.

---

## Módulos e biblioteca padrão

Módulos são arquivos ou bibliotecas que adicionam funcionalidades ao Python.

Para usar um módulo, utilizamos `import`.

```python
import math

print(math.sqrt(25))
```

Saída:

```text
5.0
```

### Importando com alias

```python
import math as m

print(m.pi)
```

### Importando partes específicas

```python
from math import sqrt

print(sqrt(36))
```

### Exemplos de módulos da biblioteca padrão

#### math

```python
import math

print(math.pi)
print(math.sqrt(16))
```

#### random

```python
import random

numero = random.randint(1, 10)

print(numero)
```

#### datetime

```python
from datetime import datetime

agora = datetime.now()

print(agora)
```

---

## Conclusão

Python é uma linguagem de programação acessível, versátil e muito utilizada em diferentes áreas da tecnologia. Seu aprendizado é uma excelente porta de entrada para quem deseja desenvolver raciocínio lógico, criar automações, trabalhar com dados, construir aplicações e avançar para temas mais complexos.

Ao estudar conceitos como variáveis, tipos de dados, strings, listas, tuplas, dicionários, estruturas condicionais, laços de repetição, funções, métodos e módulos, o estudante constrói uma base sólida para resolver problemas de forma organizada e eficiente.

Mais importante do que decorar comandos é praticar constantemente, testar hipóteses, compreender os erros e transformar cada conceito aprendido em pequenos programas funcionais.

---

## Tecnologias utilizadas nos exemplos

- Python 3
- IDE Mu
- VS Code ou outra IDE de preferência
- Console Python
- Scripts com extensão `.py`
- Biblioteca padrão do Python
- Módulos como `math`, `random` e `datetime`

---

## Autor

Material organizado para fins de estudo e prática dos conceitos básicos de Python.