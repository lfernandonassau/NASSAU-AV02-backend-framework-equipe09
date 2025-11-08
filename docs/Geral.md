# Projeto GoConsig — Guia Rápido

Este documento descreve o fluxo mínimo para desenvolver e executar o backend (Django) e o frontend (React + Vite + Tailwind CSS) localmente, além de comandos úteis e práticas recomendadas.

## Pré-requisitos
- Python 3.10+ instalado
- Node.js (versão compatível com o projeto) e npm/yarn
- Git
- Recomendado: criar e ativar virtualenv (venv) na raiz do diretório

## Estrutura (resumida)
- backend-goconsig/       ← backend Django (pasta do projeto)
- frontend-goconsig/     ← frontend React + Vite (dist gerado em build)
- docs/                   ← documentação
- .env.example            ← template de variáveis de ambiente
- .gitignore              ← Arquivos sensíveis e de cache ignorados

## Backend (Django) — setup
1. Ativar venv e instalar dependências:
```powershell
1: cd NASSAU-AV02-backend-framework-equipe09

2: py -m venv venv

3: .\venv\Scripts\Activate.ps1

4: pip install -r requirements.txt
```

2. Gerar e aplicar migrations:
```powershell
py manage.py makemigrations

py manage.py migrate
```

3. Rodar servidor:
```powershell
py manage.py runserver
```

## Frontend (React + Vite + Tailwind CSS) — setup
1. Instalar dependências:
```powershell
1: cd frontend-goconsig

2: npm install
```

2. Desenvolvimento (Vite dev server com HMR):
```powershell
npm run dev

# abre normalmente em http://localhost:5173
```
- Recomenda-se rodar o dev server em paralelo ao Django e configurar proxy no vite.config.js para a API.

3. Gerar build de produção (gera `dist/`):
```powershell
npm run build
```

## Servir frontend a partir do Django (opção integrada)
- Fluxo recomendado em dev: gerar build (`npm run build`) e o Django serve o `dist/`.
- Verifique em `settings.py`:
  - `TEMPLATES['DIRS']` deve incluir `frontend-gocinsig/dist`
  - `STATICFILES_DIRS` deve incluir `frontend-gocinsig/dist`
- Depois de build:
```powershell
# na raiz do repo
py manage.py runserver
# acessar http://127.0.0.1:8000/ (irá servir index.html do dist)
```

Observação: se preferir desenvolvimento rápido, continue usando `npm run dev` e acesse o frontend na porta do Vite.

## Variáveis de ambiente
- Nunca comitar `.env` com segredos.
- Mantenha `.env.example` com placeholders:
```
SECRET_KEY=troque_por_uma_chave
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```
- Cada dev deve copiar `.env.example` → `.env` e preencher.

## Comandos Git úteis
- Atualizar sua feature com develop:
```bash
git fetch origin
git checkout feature/seu-nome
git merge origin/develop # ou git rebase origin/develop
git push origin feature/seu-nome
```

## Criar Pull Request (sugestão de fluxo)
1. Push da sua branch:
```bash
git push origin feature/seu-nome
```
2. Criar PR:
- Pela CLI (gh):
```bash
gh pr create --base develop --head feature/seu-nome --title "feat: descrição" --body "O que foi feito e como testar"
```

Inclua no PR:
- Descrição do que mudou
- Passos para testar localmente
- Indicação de migrations (se houver)

## Troubleshooting rápido
- CSS/JS não carregam: verifique URLs dos assets em `dist/index.html`; ajuste `vite.config.js` (base = '/static/') e rode `npm run build` de novo.
- SECRET_KEY não encontrada: copiar `.env.example` e preencher `.env` ou definir a variável de ambiente.
- Problema com imports depois de renomear apps: revisar `apps.py` (`name`/`label`) e `INSTALLED_APPS`.

## Boas práticas de documentação (o que incluir no `docs/` ou README principal)
- Como rodar localmente (conteúdo deste arquivo)
- Setup de banco e migrations
- Como rodar testes
- Como gerar build do frontend e fluxo de deploy
- Convenções de branch / PR template (colocar `.github/PULL_REQUEST_TEMPLATE.md`)

---