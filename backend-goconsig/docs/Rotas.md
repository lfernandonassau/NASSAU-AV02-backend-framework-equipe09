# Rotas da aplicação (API & front)

## Visão geral

- **Arquivo fonte:** `goconsig/urls.py`
- **Router DRF registrado (prefixo `/api/`):** `clientes`, `parceiros`, `bancos`, `simulacoes`
- **Views adicionais (rotas explícitas):** `HistoricoSimulacaoListAPIView` — rotas fora do prefixo `/api/` (ver seção específica)

---

## Convenções (padrão do `DefaultRouter`)

As rotas registradas pelo `DefaultRouter` do Django REST Framework seguem o padrão RESTful:

- `GET /api/<recurso>/` -> list
- `POST /api/<recurso>/` -> create
- `GET /api/<recurso>/{id}/` -> retrieve
- `PUT /api/<recurso>/{id}/` -> update (substitui todo o recurso)
- `PATCH /api/<recurso>/{id}/` -> partial_update (se suportado)
- `DELETE /api/<recurso>/{id}/` -> destroy

---

## Rotas registradas pelo router (`/api/`)

| Método(s)               | Caminho                 | Descrição                                     | Notas / Autenticação              |
| ----------------------- | ----------------------- | --------------------------------------------- | --------------------------------- |
| GET, POST               | `/api/clientes/`        | Lista clientes / cria novo cliente            | ViewSet: `ClienteViewSet`         |
| GET, PUT, PATCH, DELETE | `/api/clientes/{id}/`   | Recupera / atualiza / deleta cliente por ID   | `pk` é o identificador do cliente |
| GET, POST               | `/api/parceiros/`       | Lista parceiros / cria novo parceiro          | ViewSet: `ParceiroViewSet`        |
| GET, PUT, PATCH, DELETE | `/api/parceiros/{id}/`  | Recupera / atualiza / deleta parceiro por ID  |                                   |
| GET, POST               | `/api/bancos/`          | Lista bancos / cria novo banco                | ViewSet: `BancoViewSet`           |
| GET, PUT, PATCH, DELETE | `/api/bancos/{id}/`     | Recupera / atualiza / deleta banco por ID     |                                   |
| GET, POST               | `/api/simulacoes/`      | Lista simulações / cria nova simulação        | ViewSet: `SimulacaoViewSet`       |
| GET, PUT, PATCH, DELETE | `/api/simulacoes/{id}/` | Recupera / atualiza / deleta simulação por ID |                                   |

> Observação: os verbos `PATCH` e `PUT` dependem das ações implementadas no respectivo `ViewSet`.

---

## Rotas específicas (definidas explicitamente em `urls.py`)

> Importante: as duas rotas abaixo foram definidas fora do prefixo `/api/` no `goconsig/urls.py`.

| Método(s) |                               Caminho | Descrição                                                              | Nome da rota              |
| --------- | ------------------------------------: | ---------------------------------------------------------------------- | ------------------------- |
| GET       | `/simulacoes/<int:sim_id>/historico/` | Lista o histórico de simulações associado à simulação `sim_id`         | `historico-por-simulacao` |
| GET       |                         `/historico/` | Lista todo o histórico de simulações; suporta filtros via query params | `historico-list`          |

> Observação: se você preferir que estas rotas fiquem sob `/api/`, mova os `path()` correspondentes para `path('api/', include(...))` ou altere os caminhos no `urls.py`.

---

## Rotas de autenticação (JWT)

O projeto expõe endpoints para obtenção e refresh de tokens JWT (registrados sob `/api/`):

- `POST /api/token/` — gera par (access, refresh). Corpo de exemplo: `{"username": "user", "password": "pass"}`
- `POST /api/token/refresh/` — atualiza token `access` usando `refresh` token

Requisições autenticadas devem enviar o header `Authorization: Bearer <access_token>` (DRF + SimpleJWT padrão).

---

## Rotas do Django/Front e utilitárias

| Método | Caminho   | Descrição                                            | Observações                                                |
| ------ | --------- | ---------------------------------------------------- | ---------------------------------------------------------- |
| GET    | `/admin/` | Painel administrativo do Django                      | `admin.site.urls`                                          |
| GET    | `/`       | Serves `index.html` via `TemplateView` — front React | Template: `index.html` (rota raiz está mapeada para React) |

## Rotas comentadas / não ativas (presentes no arquivo como comentário)

- `''` (home) -> `core_views.home` (comentado)
- `login/` -> `usuarios_views.login` (comentado)
- `cadastro/` -> `usuarios_views.cadastro` (comentado)

Essas rotas estão comentadas no `goconsig/urls.py` e não estão ativas no momento.

---

## Autenticação e permissões (observações)

As permissões e requisitos de autenticação não são definidos no `urls.py`. Elas dependem das configurações dos `ViewSet` e das `APIView` (por exemplo: `permission_classes`, `authentication_classes`).

Por exemplo, o projeto usa JWT (`rest_framework_simplejwt`) e, tipicamente, no `settings.py` há configurações de `REST_FRAMEWORK` como `DEFAULT_AUTHENTICATION_CLASSES` e `DEFAULT_PERMISSION_CLASSES`.

Verifique `app_*/*.py` (especialmente `views.py`) e `goconsig/settings.py` para confirmar políticas (ex.: `IsAuthenticated`, `IsAdminUser`, `SessionAuthentication`).

---

## Exemplos rápidos (curl)

Obter token (exemplo):

```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"seu_usuario","password":"sua_senha"}'
```

Usar token para acessar rota protegida (ex.: listar bancos):

```bash
curl -X GET http://localhost:8000/api/bancos/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

Recuperar histórico por simulação (sim_id = 5):

```bash
curl -X GET http://localhost:8000/simulacoes/5/historico/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

Exemplo PowerShell (Invoke-RestMethod) para obter token:

```powershell
$body = @{ username = 'seu_usuario'; password = 'sua_senha' } | ConvertTo-Json
$token = Invoke-RestMethod -Method Post -Uri 'http://localhost:8000/api/token/' -Body $body -ContentType 'application/json'
# usar $token.access para chamadas autenticadas
Invoke-RestMethod -Method Get -Uri 'http://localhost:8000/api/bancos/' -Headers @{ Authorization = "Bearer $($token.access)" }
```

---

## Observações finais

- As rotas REST principais estão sob o prefixo `/api/` (registradas pelo `DefaultRouter`).
- As rotas de histórico estão atualmente fora de `/api/` (ver seção "Rotas específicas"); ao consumir do front, confirme o caminho exato usado.
- Inclua sempre o header `Authorization: Bearer <token>` nas requisições a endpoints protegidos.
- Não deixe credenciais em arquivos de documentação; para compartilhar com outras pessoas, gere usuários temporários ou instrua a criar contas locais.

## Documentação automática (OpenAPI / Swagger)

Se `drf-spectacular` estiver instalado, a API expõe endpoints de documentação automática:

- `GET /api/schema/` — JSON OpenAPI (raw)
- `GET /api/schema/swagger-ui/` — UI Swagger interativa
- `GET /api/schema/redoc/` — UI Redoc para leitura da especificação

Instale as dependências e acesse `/api/schema/swagger-ui/` no navegador para explorar os endpoints e testar chamadas.

Para mais detalhes de cada endpoint (campos, validações, exemplos de request/response), consulte as `views` e `serializers` dos apps: `app_usuarios`, `app_parceiros`, `app_bancos`, `app_emprestimos`, `app_historico`.
