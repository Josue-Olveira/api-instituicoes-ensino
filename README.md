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

/
├── api/
│   ├── core/         # Configurações centrais (DB, segurança)
│   ├── models/       # Modelos ORM do SQLAlchemy
│   ├── routers/      # Lógica dos endpoints da API
│   └── schemas/      # Modelos de validação do Pydantic
├── scripts/
│   └── load_data.py  # Script para popular o banco de dados
├── .gitignore        # Arquivos e pastas a serem ignorados pelo Git
├── ies.db            # Arquivo do banco de dados SQLite
├── ies_data.csv      # Arquivo de dados brutos
├── main.py           # Ponto de entrada da aplicação FastAPI
├── README.md         # Este arquivo
└── requirements.txt  # Lista de dependências do projeto


## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para configurar e executar a aplicação no seu ambiente local.

### **Pré-requisitos**
* [Python 3.11+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads/)

### **Instalação**

1.  **Clone o repositório:**
    ```bash
    git clone [https://docs.github.com/pt/repositories/creating-and-managing-repositories/quickstart-for-repositories](https://docs.github.com/pt/repositories/creating-and-managing-repositories/quickstart-for-repositories)
    cd [NOME-DA-PASTA-DO-REPOSITÓRIO]
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Linux / macOS
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Popule o Banco de Dados:**
    * Baixe o arquivo `CSV` do [portal de dados abertos](https://dados.gov.br/dados/conjuntos-dados/cadastro-de-instituicoes-de-educacao-superior) e salve-o na raiz do projeto com o nome `ies_data.csv`.
    * Execute o script de carga:
    ```bash
    python scripts/load_data.py
    ```

5.  **Inicie o Servidor da API:**
    ```bash
    uvicorn main:app --reload
    ```
    O servidor estará disponível em `http://127.0.0.1:8000`.

## 📚 Documentação da API

Após iniciar o servidor, a documentação interativa gerada pelo Swagger UI estará disponível no seguinte endereço:

➡️ **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

Lá, você pode visualizar todos os endpoints, seus schemas e testá-los diretamente pelo navegador.

### **Endpoints Principais**

| Método HTTP | Endpoint                        | Descrição                                         | Protegido? | Permissão Necessária |
|-------------|---------------------------------|---------------------------------------------------|------------|----------------------|
| `POST`      | `/users/`                       | Cria um novo usuário (`admin` ou `leitor`).       | Não        | N/A                  |
| `POST`      | `/token`                        | Autentica um usuário e retorna um token JWT.      | Não        | N/A                  |
| `GET`       | `/api/instituicoes/`            | Lista todas as instituições de ensino.            | Não        | N/A                  |
| `POST`      | `/api/instituicoes/`            | Cria uma nova instituição de ensino.              | **Sim** | `admin`              |
| `GET`       | `/api/mantenedoras/`            | Lista todas as mantenedoras.                      | Não        | N/A                  |
| `POST`      | `/api/mantenedoras/`            | Cria uma nova mantenedora.                        | **Sim** | `admin`              |

## 🧪 Como Testar

Para uma suíte de testes completa, utilize o **Postman**. Os arquivos de coleção e ambiente podem ser solicitados ao autor ou criados seguindo a documentação.

## ✒️ Autor

Desenvolvido por **[Josue Oliveira de Castro]**.

