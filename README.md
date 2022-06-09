## Repositório para estudos de Orientação a Objetos em Python
(em andamento)
<hr>
<br>

Material base:

Playlist Orientação a Objetos do canal <strong>Programador Lhama</strong> (link abaixo)

https://www.youtube.com/watch?v=WP5p4QEqLLQ&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=1

<br>

Para clonar este repositório:
```
git clone https://github.com/keilapassos/orientacao-a-objetos-python
```

Após clonar e entrar no diretório do projeto, crie um ambiente virtual e entre nele

```
python -m venv venv --upgrade-deps
```

```
source venv/bin/activate
```


Já dentro do seu ambiente virtual, instale as dependências do projeto:

```
pip install -r requirements.txt
```

<br>

Para alguns arquivos, você pode usar o shell do python para praticar. Para isso, no seu terminal digite <strong>python</strong> e faça suas operações.
Exemplo de código utilizando o shell do python - usando arquivo pessoa.py:

```
>>> from pessoa import Pessoa
>>> keila = Pessoa('Keila', 27, 123456789)
>>> keila.beber('coca-cola')
Bebendo coca-cola
>>> keila.beber('vinho')
Apresente o cpf
123456789
>>> exit()
```


<br>

Os arquivos <i>pessoa.py</i> e <i>calculadora.py</i> tratam sobre Encapsulamento Privado, possui exemplos de atributos e de métodos privados.

vídeo base:

`
https://www.youtube.com/watch?v=RJWucpLGBng&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=3
`

<br>

O arquivo <i>sistema_cadastral.py</i> mostra como pode ser usado o princípio de responsabilidade única do SOLID.
<br>
Neste exemplo refatoramos uma classe que possui muitos funcionamentos 'encapsulados' num só método.
Com a refatoração, apesar de uma quantidade maior de código, temos uma estrutura mais legível do código, e sua manutenção se torna mais fácil também, pois caso precise de alguma alteração dentro da classe, é só ir direto ao método e modificá-lo.


Com este exemplo de classe além do princípio citado acima, aprendi também sobre o <i> isinstance(item, tipo) </i> que retorna True se o item especificado é do mesmo tipo especificado, caso contrário ele retorna False.
O isinstance não se limita a apenas um tipo, ele pode ser usado para verificar se um item está dentro de alguns tipos, por exemplo:

<br>


```
x = isinstance("Hello", (float, int, str, list, dict, tuple))
```


vídeo base:

`
https://www.youtube.com/watch?v=CM-JPix8hcI&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=5
`

<br><br>

Neste projeto utilizei o pre-commit para padronizar todos os arquivos antes de fazer o commit.
Caso queira utilizá-lo em outros projetos, abaixo um passo-a-passo de como utilizei ele:

1. instalar o pre-commit
```
pip install pre-commit
```
<br>


2. atualizar o requirements.txt com a nova instalação
```
pip freeze > requirements.txt
```

<br>

3. inicializei o repositório git local
```
git init
```

<br>

4. instalar scripts git hooks para que o pre-commit rode automaticamente em cada commit
```
pre-commit install
```

<br>

5. criar arquivo .pre-commit-config.yaml e adicionar os hooks desejados

<br>

6. adicionar e commitar arquivos modificados

<br>

7. corrigir formatações, se necessário, e depois disso adicionar e commitar novamente.

<br>

8. subir o cógigo ao repositório github

<br>


Para rodar o pre-commit em todos os arquivos adicionados:
```
pre-commit run --all-files
```

<br>

...continua
