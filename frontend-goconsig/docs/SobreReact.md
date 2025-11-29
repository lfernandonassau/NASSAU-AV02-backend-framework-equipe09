# React

O React é uma biblioteca JavaScript para construir interfaces de usuário. Ele permite a criação de componentes reutilizáveis que podem gerenciar seu próprio estado, tornando mais fácil a construção de aplicações interativas e dinâmicas.

## Vantagens do React

1. **Componentização**: O React permite que você divida sua interface em componentes independentes, facilitando a reutilização e a manutenção do código.
2. **Virtual DOM**: O React utiliza um Virtual DOM para otimizar a atualização da interface, melhorando o desempenho das aplicações.
3. **Unidirecionalidade**: O fluxo de dados no React é unidirecional, o que torna mais fácil entender como os dados fluem pela aplicação e facilita a depuração.

A estrutura de pastas do React geralmente inclui uma pasta `src` onde ficam os arquivos de código-fonte, incluindo componentes, estilos e testes.

# Junção Django + React

As paginas HTML FINAL ficarão no diretorio `front-end-goconsig/dist`, que é gerado a partir do build do React. Para atualizar o conteúdo dessas páginas, é necessário fazer o build do projeto React novamente. Apenas o gestor do projeto pode fazer isso !!!! caso seja um developer você deve utilizar o comando abaixo para gerar uma visualização local do front-end:

```bash
npm run dev
```
