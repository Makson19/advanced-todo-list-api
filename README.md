# ToDo List API

Este projeto consiste em uma API RESTful desenvolvida em Python para gerenciar uma lista de tarefas (to-do list). A API permite aos usuários criar, editar, listar e excluir tarefas, além de incluir funcionalidades de autenticação e controle de acesso por meio de um sistema de gerenciamento de usuários.

## Funcionalidades principais

1. **Cadastro de Usuário:** Permite a criação de novos usuários com validação de dados e armazenamento seguro de senhas.

2. **Login de Usuário:** Realiza a autenticação de usuários existentes utilizando tokens JWT (JSON Web Token), garantindo acesso seguro à API.

3. **Gerenciamento de Tarefas**:
   * **Criar Tarefa:** O usuário pode criar novas tarefas com informações como título, descrição e status (pendente ou concluída).
   * **Listar Tarefas:** Exibe todas as tarefas de um usuário autenticado.
   * **Atualizar Tarefa:** Permite a atualização de tarefas já existentes, incluindo status e informações adicionais.
   * **Excluir Tarefa:** O usuário pode remover tarefas da lista.

4. **Validação de Autorização:** O sistema garante que apenas o usuário autenticado possa acessar, modificar ou excluir suas próprias tarefas.

## Instalação

Clone o projeto e acesse a pasta onde ele está:
~~~git
git clone https://github.com/Makson19/advanced-todo-list-api.git

cd advanced-todo-list-api
~~~

Após clonar o repositório e acessar a pasta do projeto, abra o terminal e crie um ambiente virtual:
~~~python
python3 -m venv venv
~~~

Concluindo a criação, ative o ambiente:
~~~python
source venv/bin/activate
~~~

Para desativar o ambiente digite no terminal:
~~~python
deactivate
~~~

Com o ambiente criado e ativado, para instalar as libs do projeto digite no terminal:
~~~python
pip install -r requirements.txt
~~~

Com todas as libs já instaladas, para executar o projeto digite:
~~~python
python manage.py runserver
~~~

## Tecnologias Utilizadas

* [Django](https://www.djangoproject.com/)
* [Django Filter](https://django-filter.readthedocs.io/en/stable/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

## Endpoints

Com o projeto em execução, acesse o link para a documentação dos endpoints: [API Doc](http://127.0.0.1:8000/swagger/)
