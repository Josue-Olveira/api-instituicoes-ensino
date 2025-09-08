# API de Instituições de Ensino Superior - Brasil

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-red?style=for-the-badge&logo=sqlalchemy&logoColor=white)

Este projeto consiste em uma API RESTful desenvolvida como parte da **Entrega 1 – ESTRUTURA INICIAL DA API COM SQLITE**. A aplicação utiliza dados públicos do portal [dados.gov.br](http://dados.gov.br) sobre o Cadastro de Instituições de Ensino Superior (IES) para fornecer endpoints seguros e bem documentados para consulta e manipulação de dados.

O objetivo principal foi construir uma base estrutural robusta, com foco em boas práticas de desenvolvimento, organização de código, autenticação segura via JWT e documentação automática.

## ✨ Principais Funcionalidades

* **Autenticação JWT:** Sistema de login seguro que gera tokens de acesso para consumo da API.
* **Autorização baseada em Perfis (Roles):** Distinção entre usuários `admin` (com permissão de escrita) e `leitor` (permissão apenas para leitura).
* **Endpoints RESTful:** Rotas para criação e listagem de Instituições e suas Mantenedoras.
* **Banco de Dados com SQLAlchemy ORM:** Abstração da comunicação com o banco de dados SQLite para uma manipulação de dados mais simples e segura.
* **Validação de Dados com Pydantic:** Modelos de validação que garantem a integridade dos dados que entram e saem da API.
* **Documentação Automática:** Geração automática de documentação interativa com Swagger UI (`/docs`) e ReDoc (`/redoc`).
* **Script de Carga de Dados:** Um script utilitário para popular o banco de dados a partir do arquivo CSV original.

## 🛠️ Tecnologias Utilizadas

* **Backend:** FastAPI, Uvicorn
* **Banco de Dados:** SQLite
* **ORM:** SQLAlchemy
* **Validação de Dados:** Pydantic
* **Segurança:** Passlib (para hashing de senhas), Python-Jose (para JWT)
* **Processamento de Dados (Script):** Pandas
* **Testes:** Postman

## 📂 Estrutura do Projeto

O projeto segue uma estrutura organizada por camadas para facilitar a manutenção e escalabilidade:
