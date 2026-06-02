Abaixo está um modelo de `README.md` pronto para usar no GitHub, baseado nos principais conceitos da apostila **Introdução à lógica de programação — Asimov Academy**. 

# Introdução à Lógica de Programação

Este repositório reúne os principais conceitos de **lógica de programação**, com exemplos práticos em **Python**.
O objetivo é apresentar uma base simples e didática para quem está começando a aprender programação.

---

## Sumário

* [O que é lógica de programação?](#o-que-é-lógica-de-programação)
* [O que é um algoritmo?](#o-que-é-um-algoritmo)
* [Estrutura básica de um algoritmo](#estrutura-básica-de-um-algoritmo)
* [Variáveis e constantes](#variáveis-e-constantes)
* [Tipos de dados](#tipos-de-dados)
* [Operadores](#operadores)
* [Estruturas condicionais](#estruturas-condicionais)
* [Estruturas de repetição](#estruturas-de-repetição)
* [Métodos e funções](#métodos-e-funções)
* [Exemplos práticos](#exemplos-práticos)
* [Boas práticas](#boas-práticas)
* [Conclusão](#conclusão)

---

## O que é lógica de programação?

A **lógica de programação** é a forma de organizar o raciocínio para resolver problemas por meio de instruções claras, ordenadas e compreensíveis para o computador.

Antes de aprender uma linguagem específica, como Python, JavaScript, Java ou C, é importante entender a lógica por trás dos programas.

A lógica de programação ajuda a:

* Organizar ideias em etapas;
* Resolver problemas de forma estruturada;
* Criar algoritmos;
* Entender melhor qualquer linguagem de programação;
* Desenvolver autonomia para construir soluções.

---

## O que é um algoritmo?

Um **algoritmo** é uma sequência finita e organizada de passos criada para resolver um problema ou executar uma tarefa.

Em outras palavras, é um conjunto de instruções que devem ser executadas em uma ordem lógica.

### Exemplo simples de algoritmo do dia a dia

Objetivo: comprar ovos se não houver ovos em casa.

```text
1. Abrir a geladeira
2. Verificar se há ovos
3. Se não houver ovos:
   3.1 Pegar a carteira
   3.2 Ir ao supermercado
   3.3 Comprar ovos
   3.4 Voltar para casa
4. Se houver ovos:
   4.1 Não comprar ovos
```

Esse exemplo mostra que um algoritmo precisa ser claro e completo. O computador executa exatamente aquilo que foi instruído, sem interpretar subjetividades.

---

## Estrutura básica de um algoritmo

A maioria dos algoritmos pode ser dividida em três partes principais:

### 1. Entrada

São os dados recebidos pelo programa.

Exemplo:

```python
nota1 = 8
nota2 = 7
nota3 = 9
nota4 = 6
```

### 2. Processamento

É a etapa em que os dados são manipulados.

Exemplo:

```python
media = (nota1 + nota2 + nota3 + nota4) / 4
```

### 3. Saída

É o resultado apresentado ao usuário.

Exemplo:

```python
print(media)
```

### Exemplo completo

```python
nota1 = 8
nota2 = 7
nota3 = 9
nota4 = 6

media = (nota1 + nota2 + nota3 + nota4) / 4

print("A média do aluno é:", media)
```

---

## Variáveis e constantes

### Variáveis

Variáveis são espaços na memória usados para armazenar informações que podem mudar durante a execução do programa.

Exemplo:

```python
idade = 25
nome = "Ana"
altura = 1.68
```

O valor de uma variável pode ser alterado:

```python
idade = 25
idade = 26

print(idade)
```

Saída:

```text
26
```

### Constantes

Constantes são valores que não deveriam ser alterados durante a execução do programa.

Em Python, por convenção, usamos letras maiúsculas para representar constantes:

```python
PI = 3.14159
TAXA_JUROS = 0.05
```

---

## Tipos de dados

Os tipos de dados indicam qual tipo de informação uma variável armazena.

### Inteiro

Representa números inteiros.

```python
idade = 30
quantidade = 10
```

### Decimal

Representa números com casas decimais.

```python
preco = 19.90
altura = 1.75
```

### Texto

Representa palavras, frases ou caracteres.

```python
nome = "Douglas"
cidade = "Belo Horizonte"
```

### Booleano

Representa valores lógicos: verdadeiro ou falso.

```python
maior_de_idade = True
tem_cadastro = False
```

---

## Operadores

Operadores são símbolos usados para realizar operações com valores e variáveis.

---

### Operadores aritméticos

| Operador | Descrição        | Exemplo  |
| -------- | ---------------- | -------- |
| `+`      | Soma             | `2 + 3`  |
| `-`      | Subtração        | `10 - 4` |
| `*`      | Multiplicação    | `5 * 2`  |
| `/`      | Divisão          | `10 / 2` |
| `**`     | Exponenciação    | `2 ** 3` |
| `%`      | Resto da divisão | `10 % 3` |

Exemplo:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a % b)
```

---

### Operadores relacionais

Operadores relacionais comparam valores e retornam `True` ou `False`.

| Operador | Descrição        | Exemplo  |
| -------- | ---------------- | -------- |
| `==`     | Igual a          | `5 == 5` |
| `!=`     | Diferente de     | `5 != 3` |
| `>`      | Maior que        | `10 > 5` |
| `<`      | Menor que        | `3 < 8`  |
| `>=`     | Maior ou igual a | `7 >= 7` |
| `<=`     | Menor ou igual a | `4 <= 9` |

Exemplo:

```python
idade = 18

print(idade >= 18)
print(idade < 18)
```

---

### Operadores lógicos

Operadores lógicos são usados para combinar condições.

| Operador | Descrição                                                    |
| -------- | ------------------------------------------------------------ |
| `and`    | Retorna verdadeiro se todas as condições forem verdadeiras   |
| `or`     | Retorna verdadeiro se pelo menos uma condição for verdadeira |
| `not`    | Inverte o valor lógico da condição                           |

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

## Estruturas condicionais

As estruturas condicionais permitem que o programa tome decisões.

A principal estrutura condicional é o `if`.

### Condicional simples

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade")
```

### Condicional com `else`

```python
idade = 16

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
```

### Condicional com `elif`

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

---

## Estruturas de repetição

As estruturas de repetição permitem executar um bloco de código várias vezes.

---

### Estrutura `while`

O `while` executa um bloco de código enquanto uma condição for verdadeira.

Exemplo:

```python
contador = 1

while contador <= 5:
    print("Contador:", contador)
    contador += 1
```

Saída:

```text
Contador: 1
Contador: 2
Contador: 3
Contador: 4
Contador: 5
```

### Cuidado com loop infinito

Um loop infinito acontece quando a condição nunca se torna falsa.

Exemplo incorreto:

```python
contador = 1

while contador <= 5:
    print(contador)
```

Nesse caso, o valor de `contador` nunca muda. Portanto, a condição `contador <= 5` será sempre verdadeira.

Exemplo correto:

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

---

### Estrutura `for`

O `for` é usado para percorrer sequências, como listas, textos ou intervalos numéricos.

Exemplo:

```python
for numero in range(1, 6):
    print(numero)
```

Saída:

```text
1
2
3
4
5
```

Exemplo com lista:

```python
nomes = ["Ana", "Bruno", "Carlos"]

for nome in nomes:
    print(nome)
```

---

## Métodos e funções

Funções são blocos de código criados para executar uma tarefa específica.

Elas ajudam a organizar o código e evitar repetição.

### Exemplo de função simples

```python
def saudacao():
    print("Olá, seja bem-vindo!")

saudacao()
```

### Função com parâmetro

```python
def saudacao(nome):
    print("Olá,", nome)

saudacao("Douglas")
```

### Função com retorno

```python
def calcular_media(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    return media

resultado = calcular_media(8, 7, 9, 6)

print("Média:", resultado)
```

---

## Exemplos práticos

### Exemplo 1: calcular média de notas

```python
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("Média:", media)

if media >= 7:
    print("Aluno aprovado")
elif media >= 5:
    print("Aluno em recuperação")
else:
    print("Aluno reprovado")
```

---

### Exemplo 2: verificar se precisa comprar batatas

Objetivo: uma receita precisa de 10 batatas. O programa verifica quantas existem em casa e calcula quantas precisam ser compradas.

```python
batatas_disponiveis = int(input("Quantas batatas existem em casa? "))

batatas_necessarias = 10

quantidade_comprar = batatas_necessarias - batatas_disponiveis

if quantidade_comprar > 0:
    print("Você precisa comprar", quantidade_comprar, "batatas.")
else:
    print("Você já tem batatas suficientes.")
```

---

### Exemplo 3: repetição até atingir uma condição

Objetivo: simular o ajuste de sal em uma receita.

```python
sal_suficiente = False

while not sal_suficiente:
    resposta = input("O sal está suficiente? Digite sim ou nao: ")

    if resposta == "sim":
        sal_suficiente = True
        print("Tempero finalizado.")
    else:
        print("Adicione mais sal e prove novamente.")
```

---

### Exemplo 4: sistema simples de login

```python
usuario_correto = "admin"
senha_correta = "1234"

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorretos.")
```

---

### Exemplo 5: contador regressivo

```python
contador = 10

while contador >= 1:
    print(contador)
    contador -= 1

print("Fim da contagem!")
```

---

## Boas práticas

Algumas boas práticas ajudam a escrever códigos mais claros e organizados:

* Use nomes de variáveis descritivos;
* Escreva o código em uma ordem lógica;
* Evite repetir código desnecessariamente;
* Comente partes importantes do código;
* Teste o programa com diferentes entradas;
* Divida problemas grandes em partes menores;
* Pratique com exemplos do cotidiano;
* Evite depender apenas de respostas prontas;
* Busque entender o erro antes de copiar uma solução.

---

## Como praticar lógica de programação

Algumas sugestões de exercícios:

1. Criar um algoritmo para calcular a idade de uma pessoa.
2. Criar um programa que verifica se um número é par ou ímpar.
3. Criar um programa que calcula o maior entre dois números.
4. Criar um sistema simples de aprovação de aluno.
5. Criar um programa que soma números de 1 a 100.
6. Criar um programa que simula um caixa eletrônico.
7. Criar um programa que calcula o IMC.
8. Criar um programa que verifica se uma senha está correta.
9. Criar um programa que lista os números pares de 1 a 50.
10. Criar uma função para calcular a média de uma lista de notas.

---

## Conclusão

A lógica de programação é a base para aprender qualquer linguagem de programação.
Mais importante do que decorar comandos é desenvolver a capacidade de pensar de forma estruturada, organizar ideias e transformar problemas em soluções computacionais.

Com o domínio de conceitos como algoritmos, variáveis, operadores, condicionais, repetições e funções, torna-se muito mais fácil avançar para linguagens, bibliotecas, frameworks e projetos mais complexos.

---

## Tecnologias utilizadas nos exemplos

* Python 3
* Lógica de programação
* Algoritmos
* Estruturas condicionais
* Estruturas de repetição
* Funções

---

## Autor

Material organizado para fins de estudo e prática em lógica de programação.