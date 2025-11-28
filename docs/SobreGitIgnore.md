# !!! ATENÇÃO !!!

## O que é o `.gitignore`? 🤔
`.gitignore` é um arquivo de texto que informa ao Git quais arquivos e pastas ele deve ignorar. Itens listados nele não serão rastreados nem adicionados ao repositório quando você executar `git add .`.

## Por que usar? ✅
- Mantém o repositório limpo de arquivos gerados automaticamente (builds, caches, artefatos).
- Evita commit de arquivos locais de configuração (IDE, sistema operacional).
- Reduz o tamanho do repositório removendo binários e dependências que não precisam ser versionadas.
- Facilita o trabalho em equipe evitando conflitos de arquivos específicos da máquina.

## Exemplos comuns de entradas
```
# Python
__pycache__/
*.pyc

# Ambiente
.env
venv/

# Editor / OS
.vscode/
.DS_Store

# Build / dist
build/
dist/
*.egg-info/
```

## Segurança 🔒
- Nunca comite credenciais (senhas, tokens, chaves privadas). Mesmo que depois remova, o histórico do Git mantém as informações.
- Se credenciais vazarem, rotacione ou revogue imediatamente as chaves/credentials.
- Coloque arquivos sensíveis (ex.: `.env`) no `.gitignore`. Use variáveis de ambiente seguras e armazenamentos de segredos (GitHub Secrets, Vaults).

Ferramentas de apoio:
- `git-secrets` ou hooks de pré-commit para bloquear commits contendo padrões sensíveis.
- GitHub/GitLab Secrets para CI/CD.

## O que fazer se um arquivo sensível já foi commitado ⚠️
1. Remover do índice (mas manter local):
```
git rm --cached caminho/do/arquivo
git commit -m "Remover arquivo sensível do repositório"
```
2. Remover do histórico (opções):
- BFG Repo-Cleaner (mais simples):
    - https://rtyley.github.io/bfg-repo-cleaner/
- `git filter-branch` (mais complexo)
3. Rotacionar credenciais comprometidas imediatamente.

## Boas práticas finais ✨
- Versione apenas o que é necessário para reproduzir o ambiente (requirements/lockfiles, config de build).
- Forneça exemplos de arquivos sensíveis versionáveis como `example.env` com valores falsos para documentação.
- Use `git check-ignore -v <arquivo>` para diagnosticar porque um arquivo está sendo ignorado.

Seguindo essas orientações você mantém histórico limpo, equipe mais produtiva e reduz riscos de vazamento de segredos.

---


Observação: não ignore arquivos que são necessários para reproduzir o ambiente, como `requirements.txt`, `pyproject.toml` ou arquivos de lock (ex.: `poetry.lock`, `Pipfile.lock`). Esses devem ser versionados.