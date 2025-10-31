# Requisitos do Projeto !!!IMPORTANTE!!!

Este projeto utiliza a linguagem **Python**. Para garantir o funcionamento correto e evitar conflitos de dependências, é necessário utilizar um ambiente virtual (**venv**).

## Para que serve a venv?

A **venv** cria um ambiente isolado para instalar pacotes e dependências apenas para este projeto, sem interferir em outros projetos ou na instalação global do Python. Isso facilita o gerenciamento das bibliotecas e evita incompatibilidades.

## Como criar e ativar a venv

1. Abra o terminal na pasta do projeto.
2. Crie o ambiente virtual com o comando:
   ```
   python -m venv venv
   ```
3. Ative o ambiente virtual:
   - No Windows:
     ```
     .\venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```
     source venv/bin/activate
     ```

## Instalação das dependências

Com a venv ativada, instale as dependências usando:
```
pip install -r requirements.txt
```

## Observações

- **Mantenha sempre as versões dos pacotes o mais atualizadas possível**, conforme especificado no arquivo `requirements.txt` (usando `>=`).
- Execute todos os comandos dentro da venv para garantir o correto funcionamento do projeto.
- A linguagem utilizada é **Python**.
