# Aplicação de Criptografia AES com Flask

Esta é uma aplicação web simples para criptografar e descriptografar textos usando o algoritmo AES. A aplicação é construída com Flask, uma microframework para Python, e usa a biblioteca `pycryptodome` para operações criptográficas.

## Funcionalidades

- Criptografar texto usando AES
- Descriptografar texto criptografado usando AES

## Requisitos

- Python 3.x
- Flask
- pycryptodome
- waitress

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seuusuario/suarepositorio.git
    cd suarepositorio
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install flask pycryptodome waitress
    ```

## Uso

1. Execute a aplicação:

    ```bash
    python app.py
    ```

2. Abra o navegador e acesse:

    ```
    http://127.0.0.1:5000
    ```

3. Na página inicial, você pode escolher entre criptografar ou descriptografar um texto. Insira o texto e a senha, e clique em "Processar". O resultado será exibido em uma nova página.

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Flask
- `templates/`: Diretório contendo os templates HTML
  - `index.html`: Template da página inicial
  - `result.html`: Template da página de resultados