# 🛍️ Flask E-commerce API

Uma API para gerenciamento de usuários, produtos e carrinhos de compra, desenvolvida em Flask com SQLAlchemy, CORS e autenticação via Flask-Login. Este projeto faz parte do estudo de introdução ao desenvolvimento web com Python e Flask, utilizando funcionalidades modernas para criar uma aplicação de e-commerce funcional.

## 📋 Sumário
- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Configuração do Projeto](#configuração-do-projeto)
- [Estrutura do Banco de Dados](#estrutura-do-banco-de-dados)
- [Endpoints](#endpoints)
  - [Autenticação](#autenticação)
  - [Gerenciamento de Produtos](#gerenciamento-de-produtos)
  - [Carrinho de Compras](#carrinho-de-compras)
- [Execução do Projeto](#execução-do-projeto)
- [Contribuições](#contribuições)
- [Licença](#licença)

---

## 📖 Sobre o Projeto

Esta API permite o cadastro, autenticação e gerenciamento de usuários, produtos e carrinhos de compra. Com um fluxo de autenticação seguro, ela permite adicionar produtos ao banco de dados, gerenciar itens no carrinho e finalizar a compra. 

### Principais Funcionalidades
- Cadastro e login de usuários.
- CRUD de produtos.
- Adição e remoção de itens no carrinho de compra.
- Checkout e limpeza do carrinho após a compra.

## 💻 Tecnologias Utilizadas
- **Flask**: Framework de desenvolvimento web em Python.
- **Flask-SQLAlchemy**: ORM para integração com bancos de dados.
- **Flask-Login**: Gerenciamento de sessões e autenticação.
- **Flask-CORS**: Controle de recursos de origem cruzada.
- **SQLite**: Banco de dados simples e embutido.

## 🚀 Configuração do Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Ou "venv\Scripts\activate" no Windows
   pip install -r requirements.txt
   ```

3. Inicie o banco de dados:
   ```python
   from app import db
   db.create_all()
   ```

## 🗄️ Estrutura do Banco de Dados

A estrutura do banco de dados foi criada usando o SQLAlchemy com três tabelas principais:

- **User**: Tabela para os dados do usuário (ID, nome de usuário e senha).
- **Product**: Tabela para o cadastro de produtos (ID, nome, preço e descrição).
- **CartItem**: Tabela intermediária que relaciona usuários com produtos em seus carrinhos.

## 📫 Endpoints

### 🔐 Autenticação
- `POST /login`: Autenticação de usuário.
- `POST /logout`: Logout do usuário.

### 🛒 Gerenciamento de Produtos
- `POST /api/products/add`: Adiciona um novo produto.
- `DELETE /api/products/delete/<int:product_id>`: Remove um produto pelo ID.
- `GET /api/products/<int:product_id>`: Consulta um produto específico pelo ID.
- `PUT /api/products/update/<int:product_id>`: Atualiza as informações de um produto.
- `GET /api/products`: Lista todos os produtos cadastrados.

### 🛍️ Carrinho de Compras
- `POST /api/cart/add/<int:product_id>`: Adiciona um produto ao carrinho do usuário.
- `DELETE /api/cart/remove/<int:product_id>`: Remove um produto do carrinho do usuário.
- `GET /api/cart`: Visualiza os itens no carrinho do usuário.
- `POST /api/cart/checkout`: Finaliza a compra e limpa o carrinho.

## 🏃 Execução do Projeto

Após configurar o projeto e o banco de dados, execute o servidor:
```bash
python app.py
```
A aplicação estará disponível em `http://localhost:5001`.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_ para melhorias.

## 📝 Licença

Este projeto é distribuído sob a licença MIT.
