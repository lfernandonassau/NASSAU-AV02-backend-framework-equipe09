# Requisitos do Projeto

Este projeto usa Python. Para evitar conflitos de dependências, use um ambiente virtual (`venv`). Abaixo estão instruções passo a passo pensadas para o professor executar o projeto em Windows (PowerShell) — também há notas para Linux/macOS quando aplicável.

---

## 1) Pré-requisitos

- Python 3.11+ recomendado (ver `requirements.txt` para versões exatas).
- Ferramenta `py` (launcher do Python) no Windows facilita os comandos.
- Acesso ao terminal (PowerShell no Windows).

---

## 2) Criar e ativar a `venv` (Windows - PowerShell)

1. Abra PowerShell na raiz do projeto (pasta que contém `manage.py`).

2. Crie o ambiente virtual:

```powershell
py -m venv venv
```

3. Ative a `venv` (PowerShell):

```powershell
.\\venv\\Scripts\\Activate
```

Obs.: se o PowerShell bloquear a execução de scripts, execute apenas para a sessão atual:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
.\\venv\\Scripts\\Activate
```

Linux / macOS (para referência):

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3) Instalar dependências

Com a `venv` ativada, instale os pacotes do `requirements.txt`:

```powershell
py -m pip install -r requirements.txt
```

Notas:

- Se houver falha na instalação de algum pacote binário, instale compiladores ou versões wheel compatíveis.
- O arquivo `requirements.txt` já inclui `argon2-cffi` (necessário se `Argon2PasswordHasher` estiver habilitado) e `drf-spectacular` (para docs OpenAPI).

---

## 4) Preparar o banco e aplicar migrações

```powershell
py .\\manage.py migrate
```

Se quiser popular dados de exemplo (se houver fixtures), use `loaddata` conforme o repositório fornecer.

---

## 5) Criar superuser (admin)

```powershell
py .\\manage.py createsuperuser
```

Siga as instruções interativas para fornecer `username`, `email` (opcional) e `password`.

---

## 6) Executar o servidor de desenvolvimento

```powershell
py .\\manage.py runserver
```

Em seguida, abra no navegador:

- `http://localhost:8000/` → front (React) integrado
- `http://localhost:8000/admin/` → painel Django (use o superuser criado)

Se você adicionou `drf-spectacular` e instalou dependências, também poderá abrir:

- `http://localhost:8000/api/schema/swagger-ui/` → Swagger UI (interativa)
- `http://localhost:8000/api/schema/redoc/` → Redoc

---

## 7) Rodar testes (opcional)

O projeto inclui `pytest` no `requirements.txt`. Para executar os testes:

```powershell
py -m pytest
```

---

## 8) Problemas comuns & soluções rápidas

- Erro de activation no PowerShell: execute `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force` antes de ativar a `venv`.
- `ValueError: Couldn't load 'Argon2PasswordHasher'` — instale `argon2-cffi`:

```powershell
py -m pip install argon2-cffi
```

- Linter/IDE acusa imports faltando (`drf_spectacular.views`) — instale dependências com `pip install -r requirements.txt` e reinicie a IDE.
- Problemas com HTTPS/HSTS no dev server: o servidor de desenvolvimento do Django só serve HTTP. Se o navegador insistir em HTTPS por HSTS, limpe o HSTS no navegador ou use um profile diferente.
- Admin bloqueado pelo `django-axes`: use o comando para desbloquear um usuário específico se necessário:

```powershell
py .\\manage.py axes_reset_username <username>
```

---

## 9) Boas práticas

- Execute todos os passos na ordem: criar venv → ativar → instalar dependências → migrar → criar superuser → rodar servidor.
- Use `DEBUG=False` e configure `ALLOWED_HOSTS` para deploy/avaliação em ambiente público.
- Não mantenha credenciais ou tokens em arquivos de documentação.
