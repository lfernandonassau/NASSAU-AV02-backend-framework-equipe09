## Django

Para inicializar um projeto Django, siga os passos abaixo:

1. **Instale o Django**: Certifique-se de que você tem o Django instalado. Você pode instalá-lo usando o pip:

   ```
   pip install django 
   ```
   ou
   ```
   pip install -r requirements.txt
   ```

3. **Navegue até o Diretório do Projeto**: Entre no diretório do seu projeto:

   ```
   cd back-end-goconsig
   ```

4. **Chave de API**: Para algumas funcionalidades, você pode precisar de uma chave de API. Verifique a documentação do Django ou do serviço que está utilizando para obter instruções sobre como gerar e usar uma chave de API.

* crie um arquivo `.env` na raiz do projeto e adicione a chave de API nele, por exemplo:
   ```
   API_KEY=sua_chave_aqui
   ```

5. **Inicie o Servidor de Desenvolvimento**: Você pode iniciar o servidor de desenvolvimento do Django com o seguinte comando:

   ```
   python manage.py runserver
   ```

6. **Acesse o Projeto no Navegador**: Abra o seu navegador e acesse `http://127.0.0.1:8000/` para ver a página inicial do seu projeto Django.
