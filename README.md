


# Sistema de Cadastro e Busca de produtos - API

O sistema deve permitir cadastro de produtos de tecnologia como:

- Periféricos
- Eletrônicos
- Eletrodomésticos

O sistema deve permitir cadastro de novos usuários.
O sistema deve permitir cadastro de novos pedidos.

## Requisitos

- Realizar o Git clone
- Python (versão mais recente)
- Instalar as Libs
- manter o arquivo models.py no mesmo diretório

# Preparação e uso
## 1 - Link para o Git clone:

https://github.com/gabrooo/CPII_Coding.git

## 2 - Instalar as libs python (dependências)

- pip install flask
- pip install flask_restful
- pip install flask_sqlalchemy
- pip install requests

## 3 - Execução

- **1** - execute "python .\MAIN.py" no powershell para subir o webserver 
- **2** - O GET ou visualização podem ser feitos via powershell ou navegador
-- **2.1** - **Via powershell:** Execute "python .\GET.py" e então será possível selecionar o endpoint e o id do item que deseja visualizar.
-- **2.2** - **Via navegador:** Acesse o webserver via navegador digitando "127.0.0.1:5000/{nome_do_endpoint}/{nº_do_id_do_item}" sendo possível visualizar 3 tabelas que devem ser inseridos entre as chaves: usuario, products e pedidos
- **3** - Para catalogar novos **usuários** execute "python .\POST_USER.py", e então serão inputados os dados que estão no arquivo users.txt, se deseja inserir diferentes dados, altere no arquivo seguindo padrão de valores separados por ";" nas colunas na seguinte ordem: nome, email e idade.
- **4** - Para catalogar novos **produtos** execute "python .\POST_PRODUTOS.py", e então serão inputados os dados que estão no arquivo products.txt, se deseja inserir diferentes dados, altere no arquivo seguindo padrão de valores separados por ";" nas colunas na seguinte ordem:  nome, preço e quantidade.
- **5** - Para catalogar novos **pedidos** execute "python .\POST_ORDER.py", e então serão inputados os dados que estão no arquivo orders.txt, se deseja inserir diferentes dados, altere no arquivo seguindo padrão de valores separados por ";" nas colunas na seguinte ordem: nome, status do pedido e id do produto.

