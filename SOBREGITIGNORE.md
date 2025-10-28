# !!! ATENÇÃO !!!

Adicione ao `.gitignore` sempre que possível todos os arquivos, pastas ou extensões listadas abaixo — por segurança e para evitar poluição do repositório com artefatos gerados localmente.

---

## Byte-compiled / optimized
- __pycache__/
- *.py[cod]
- *$py.class

## C extensions
- *.so

## Distribution / packaging
- .Python
- build/
- dist/
- downloads/
- eggs/
- .eggs/
- lib/
- lib64/
- parts/
- sdist/
- var/
- *.egg-info/
- *.egg
- .installed.cfg

## PyInstaller
- *.manifest
- *.spec

## Installer logs
- pip-log.txt
- pip-delete-this-directory.txt

## Unit test / coverage
- htmlcov/
- .tox/
- .nox/
- .pytest_cache/
- .coverage
- .coverage.*
- .cache
- nosetests.xml
- coverage.xml

## Translations
- *.mo
- *.pot

## Jupyter
- .ipynb_checkpoints

## Environments / virtualenvs
- venv/
- .venv/
- env/
- ENV/
- env.bak/
- venv.bak/
- .python-version

## dotenv / config locais
- .env
- .env.*
- config.local.py
- local_settings.py
- secrets.json

## Type checker caches
- .mypy_cache/
- .pyre/

## IDEs and editors
- .vscode/
- .idea/
- *.sublime-workspace
- *.sublime-project

## Sistema / OS
- .DS_Store
- Thumbs.db

## Logs e bancos locais
- *.log
- *.sqlite3
- *.db

## Build artifacts
- wheelhouse/

## Compiled / temporários
- *.pyc
- *.pyo
- *.pyd

---

Observação: não ignore arquivos que são necessários para reproduzir o ambiente, como `requirements.txt`, `pyproject.toml` ou arquivos de lock (ex.: `poetry.lock`, `Pipfile.lock`). Esses devem ser versionados.