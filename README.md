# Variáveis, `print()`, f-strings e Estruturas Condicionais em Python

## 📚 Introdução

Este material apresenta conceitos fundamentais da linguagem **Python**, servindo como uma introdução à programação para quem está começando.

Os assuntos abordados são:

* Variáveis
* `print()`
* f-strings
* `if`
* `elif`
* `else`
* Operadores de comparação
* Operadores lógicos
* Exemplos práticos

---

## 🐍 1. Variáveis

Uma **variável** é um espaço utilizado pelo programa para armazenar um valor.

Em Python, não é necessário declarar antecipadamente o tipo da variável. O próprio Python identifica o tipo do valor atribuído.

### Exemplo

```python
nome = "Henrique"
idade = 25
altura = 1.75
estudando = True
```

Nesse exemplo:

```text
nome       → "Henrique"
idade      → 25
altura     → 1.75
estudando  → True
```

Cada variável armazena uma informação diferente.

### Principais tipos de dados

```python
nome = "Henrique"       # str → texto
idade = 25              # int → número inteiro
altura = 1.75           # float → número decimal
estudando = True        # bool → verdadeiro ou falso
```

Os quatro tipos mais comuns nesse início são:

| Tipo    | Significado | Exemplo          |
| ------- | ----------- | ---------------- |
| `str`   | Texto       | `"Python"`       |
| `int`   | Inteiro     | `25`             |
| `float` | Decimal     | `1.75`           |
| `bool`  | Booleano    | `True` / `False` |

---

## 🖨️ 2. `print()`

A função `print()` é utilizada para **exibir informações na tela**.

### Exemplo

```python
print("Olá, mundo!")
```

Resultado:

```text
Olá, mundo!
```

Também podemos exibir o conteúdo de uma variável:

```python
nome = "Henrique"

print(nome)
```

Resultado:

```text
Henrique
```

Podemos imprimir vários valores ao mesmo tempo:

```python
nome = "Henrique"
idade = 25

print(nome, idade)
```

Resultado:

```text
Henrique 25
```

---

## 🔤 3. f-strings

As **f-strings** permitem inserir variáveis diretamente dentro de uma string.

Para utilizar uma f-string, colocamos a letra `f` antes das aspas:

```python
nome = "Henrique"
idade = 25

print(f"Meu nome é {nome} e tenho {idade} anos.")
```

Resultado:

```text
Meu nome é Henrique e tenho 25 anos.
```

As variáveis são colocadas entre `{}`.

### Sem f-string

Uma forma menos prática seria:

```python
nome = "Henrique"
idade = 25

print("Meu nome é", nome, "e tenho", idade, "anos.")
```

### Com f-string

```python
print(f"Meu nome é {nome} e tenho {idade} anos.")
```

A f-string torna a construção de textos com variáveis muito mais simples e legível.

### Também podemos realizar operações

```python
a = 10
b = 5

print(f"A soma é {a + b}")
```

Resultado:

```text
A soma é 15
```

---

# 🔀 4. Estruturas condicionais

Estruturas condicionais permitem que o programa **tome decisões**.

Em vez de simplesmente executar todas as instruções, podemos dizer:

> "Se determinada condição for verdadeira, faça isso. Caso contrário, faça outra coisa."

Em Python, utilizamos principalmente:

```python
if
elif
else
```

---

## 🟢 5. `if`

`if` significa **"se"**.

Ele executa um bloco de código quando uma determinada condição é verdadeira.

### Exemplo

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
```

Como `18 >= 18` é verdadeiro, o programa executará:

```text
Você é maior de idade.
```

### Importante: indentação

Python utiliza **indentação** para determinar quais instruções pertencem ao `if`.

Correto:

```python
if idade >= 18:
    print("Maior de idade")
```

Incorreto:

```python
if idade >= 18:
print("Maior de idade")
```

A indentação normalmente é feita utilizando **4 espaços**.

---

# 🟡 6. `else`

`else` significa **"caso contrário"**.

Ele é executado quando a condição do `if` é falsa.

### Exemplo

```python
idade = 16

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

Como `16 >= 18` é falso, o resultado será:

```text
Menor de idade
```

Podemos visualizar a lógica assim:

```text
             idade >= 18?
                /    \
              SIM     NÃO
               |       |
               v       v
           Maior     Menor
```

---

# 🟠 7. `elif`

`elif` significa **"else if"**, ou seja, **"caso contrário, se..."**.

Ele permite verificar várias condições.

### Exemplo

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

Nesse caso, o Python verifica as condições **de cima para baixo**.

Como `nota` vale `7`:

```text
nota >= 9  → falso
nota >= 7  → verdadeiro
```

Portanto:

```text
Aprovado
```

Quando uma condição é encontrada como verdadeira, os próximos `elif` e o `else` não são executados.

---

# ⚖️ 8. Operadores de comparação

As estruturas condicionais normalmente utilizam operadores de comparação.

| Operador | Significado    |
| -------- | -------------- |
| `==`     | Igual          |
| `!=`     | Diferente      |
| `>`      | Maior que      |
| `<`      | Menor que      |
| `>=`     | Maior ou igual |
| `<=`     | Menor ou igual |

### Exemplos

```python
idade = 20

print(idade == 20)
```

Resultado:

```text
True
```

```python
print(idade > 18)
```

Resultado:

```text
True
```

```python
print(idade < 18)
```

Resultado:

```text
False
```

### ⚠️ Atenção ao `=` e `==`

Essa é uma diferença fundamental:

```python
idade = 20
```

`=` significa **atribuição**.

Estamos colocando o valor `20` dentro da variável `idade`.

Já:

```python
idade == 20
```

significa **comparação**.

Estamos perguntando:

> "A variável `idade` é igual a 20?"

---

# 🧠 9. Operadores lógicos

Também podemos combinar várias condições.

Os principais operadores são:

* `and` → E
* `or` → OU
* `not` → NÃO

### `and`

Todas as condições precisam ser verdadeiras.

```python
idade = 25
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir.")
```

Nesse caso, as duas condições precisam ser verdadeiras.

### `or`

Pelo menos uma condição precisa ser verdadeira.

```python
tem_dinheiro = False
tem_cartao = True

if tem_dinheiro or tem_cartao:
    print("Pode realizar a compra.")
```

### `not`

Inverte o resultado lógico.

```python
ligado = False

if not ligado:
    print("O equipamento está desligado.")
```

---

# 💡 10. Exemplo prático

Podemos combinar variáveis, `print()`, f-string e estruturas condicionais em um único programa.

```python
nome = "Henrique"
idade = 25
nota = 8.5

print(f"Aluno: {nome}")
print(f"Idade: {idade}")
print(f"Nota: {nota}")

if nota >= 9:
    situacao = "Excelente"
elif nota >= 7:
    situacao = "Aprovado"
elif nota >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Situação: {situacao}")
```

Resultado:

```text
Aluno: Henrique
Idade: 25
Nota: 8.5
Situação: Aprovado
```

---

# 🔎 11. Como o programa pensa

O código acima pode ser interpretado da seguinte maneira:

```text
1. Criar a variável nome
        ↓
2. Criar a variável idade
        ↓
3. Criar a variável nota
        ↓
4. Mostrar as informações
        ↓
5. A nota é >= 9?
        ↓
      NÃO
        ↓
6. A nota é >= 7?
        ↓
      SIM
        ↓
7. situação = "Aprovado"
        ↓
8. Mostrar a situação
```

Essa lógica de **armazenar informações → verificar condições → tomar decisões → apresentar resultados** está presente em praticamente todo tipo de programa.

---

# 🧪 12. Exemplo: sistema de aprovação

```python
nome = "João"
nota1 = 7
nota2 = 8

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"{nome} foi aprovado!")
    print(f"Média: {media}")
else:
    print(f"{nome} foi reprovado.")
    print(f"Média: {media}")
```

Resultado:

```text
João foi aprovado!
Média: 7.5
```

Observe que a variável `media` também pode ser utilizada dentro da condição.

---

# 🛠️ 13. Exemplo: classificação de idade

```python
idade = 25

if idade < 12:
    categoria = "Criança"
elif idade < 18:
    categoria = "Adolescente"
elif idade < 60:
    categoria = "Adulto"
else:
    categoria = "Idoso"

print(f"Categoria: {categoria}")
```

Resultado:

```text
Categoria: Adulto
```

O programa verifica cada condição até encontrar a primeira que seja verdadeira.

---

# 📌 Resumo dos conceitos

### Variáveis

Armazenam informações:

```python
nome = "Henrique"
idade = 25
```

### `print()`

Exibe informações:

```python
print("Olá!")
```

### f-string

Permite inserir variáveis dentro de textos:

```python
print(f"Olá, {nome}!")
```

### `if`

Executa código quando uma condição é verdadeira:

```python
if idade >= 18:
    print("Maior de idade")
```

### `elif`

Permite testar outra condição:

```python
elif idade >= 12:
    print("Adolescente")
```

### `else`

Executa quando nenhuma condição anterior foi satisfeita:

```python
else:
    print("Criança")
```

---

# 🚀 Exercícios para praticar

### Exercício 1 — Apresentação

Crie variáveis para armazenar:

* Nome
* Idade
* Cidade

Depois utilize `print()` e f-string para mostrar uma apresentação.

### Exercício 2 — Maior de idade

Crie uma variável `idade` e faça um programa que informe se a pessoa é maior ou menor de idade.

### Exercício 3 — Notas

Crie duas notas, calcule a média e informe:

```text
Média >= 7 → Aprovado
Média >= 5 → Recuperação
Média < 5 → Reprovado
```

### Exercício 4 — Número

Crie uma variável `numero` e determine se ela é:

```text
Positiva
Negativa
Zero
```

### Exercício 5 — Sistema de acesso

Crie as variáveis:

```python
usuario = "admin"
senha = "1234"
```

Utilize `if`, `elif` e `else` para verificar se o usuário e a senha estão corretos.

---

## 📖 Conceito fundamental

Uma das ideias mais importantes para quem está começando a programar é entender que um programa é, essencialmente, uma sequência de **dados + processamento + decisões**.

Em Python:

```text
VARIÁVEIS
    ↓
armazenam dados
    ↓
PROCESSAMENTO
    ↓
realiza operações
    ↓
CONDIÇÕES
    ↓
tomam decisões
    ↓
PRINT / SAÍDA
    ↓
mostra o resultado
```

Dominar esses conceitos fornece uma base sólida para avançar posteriormente para **loops (`for` e `while`), funções, listas, dicionários, módulos, tratamento de erros e programação orientada a objetos**.
