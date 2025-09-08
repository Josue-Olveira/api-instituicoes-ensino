# API de Instituições de Ensino Superior - Brasil

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-red?style=for-the-badge&logo=sqlalchemy&logoColor=white)

### **Introdução**

Este relatório apresenta a arquitetura e implementação de uma API RESTful, desenvolvida para servir como a base estrutural de uma aplicação de software moderna. O projeto, parte da "Entrega 1", utiliza o ecossistema tecnológico de Python com FastAPI, SQLAlchemy e SQLite para transformar um conjunto de dados públicos em um serviço web interativo, seguro e bem documentado.

A fonte de dados selecionada foi o "Cadastro de Instituições de Ensino Superior (IES)" do portal `dados.gov.br`, um repositório rico de informações sobre o cenário educacional brasileiro. A API abstrai a complexidade desses dados, oferecendo endpoints intuitivos para consulta e manipulação, protegidos por um sistema de autenticação e autorização baseado em tokens JWT. O desenvolvimento foi guiado por princípios de código limpo, separação de responsabilidades e automação, resultando em uma aplicação estável e pronta para futuras expansões.

### **Aplicações e Casos de Uso**

Uma API como esta serve de alicerce para diversas aplicações práticas. Seu propósito principal é permitir que outros sistemas consumam e utilizem os dados de IES de forma programática, possibilitando a criação de:

* **Portais Web Educacionais:** Sites que permitem a estudantes pesquisar, filtrar e comparar instituições por estado (UF), município, nome ou sigla.
* **Aplicativos Móveis:** Ferramentas para que futuros universitários encontrem informações sobre faculdades e universidades diretamente de seus celulares.
* **Painéis de Análise de Dados (Dashboards):** Plataformas para pesquisadores ou gestores públicos visualizarem a distribuição e as características das instituições de ensino no país.
* **Integração com outros Sistemas:** A API pode ser usada para alimentar outros softwares que necessitem de uma fonte de dados validada e consistente sobre as IES do Brasil.

## ✨ Principais Funcionalidades

* **Autenticação JWT:** Sistema de login seguro que gera tokens de acesso para consumo da API.
* **Autorização baseada em Perfis (Roles):** Distinção entre usuários `admin` (com permissão de escrita) e `leitor` (permissão apenas para leitura).
* **Filtros Dinâmicos:** Filtragem da lista de instituições por `nome`, `sigla`, `municipio` e `uf` via query parameters.
* **Endpoints RESTful:** Rotas para criação e listagem de Instituições e suas Mantenedoras.
* **Banco de Dados com SQLAlchemy ORM:** Abstração da comunicação com o banco de dados SQLite.
* **Validação de Dados com Pydantic:** Modelos que garantem a integridade dos dados que entram e saem da API.
* **Documentação Automática:** Geração de documentação interativa com Swagger UI (`/docs`).
* **Script de Carga de Dados:** Utilitário para popular o banco de dados a partir do arquivo CSV original.

## 🛠️ Tecnologias Utilizadas

* **Backend:** FastAPI, Uvicorn
* **Banco de Dados:** SQLite
* **ORM:** SQLAlchemy
* **Validação de Dados:** Pydantic
* **Segurança:** Passlib, Python-Jose (JWT)
* **Processamento de Dados (Script):** Pandas
* **Testes:** Postman

## 📂 Estrutura do Projeto

/
├── api/
│   ├── core/         # Configurações centrais (DB, segurança)
│   ├── models/       # Modelos ORM do SQLAlchemy
│   ├── routers/      # Lógica dos endpoints da API
│   └── schemas/      # Modelos de validação do Pydantic
├── scripts/
│   └── load_data.py  # Script para popular o banco de dados
├── .gitignore
├── ies.db
├── ies_data.csv
├── main.py           # Ponto de entrada da aplicação FastAPI
├── README.md         # Este arquivo
└── requirements.txt


## 🚀 Como Executar o Projeto Localmente

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

Após iniciar o servidor, a documentação interativa gerada pelo Swagger UI estará disponível em:

➡️ **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

## 🧪 Como Testar

Para uma suíte de testes completa, utilize o **Postman**. Os arquivos de coleção e ambiente (`.json`) devem ser importados no aplicativo para executar o fluxo de testes que valida a criação de usuários, login, acesso a rotas públicas e o bloqueio de acesso a rotas protegidas.

## ✒️ Autor

Desenvolvido por **[Josué Oliveira de Castro]**.
