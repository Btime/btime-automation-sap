## Do inicio!

Siga o passo á passo para rodar a aplicação! 

### Pré-Requisitos

É necessário ter instalado corretamente em seu computador:

- Python 3.8+

### Instalação

Siga o passo a passo para instalar a aplicação:

1. Clone o repositório abrindo o Git Bash:
```bash
git clone https://github.com/Btime/btime-automation-sap.git
```

2. Crie um Ambiente Virtual (venv) e ative:
```bash
Windows: python -m venv venv
         venv/scripts/activate

Linux/Mac: python3 -m venv venv
           source venv/bin/activate
```

3. Instale as dependências necessárias após ativar a venv:
```bash
pip install -r requirements.txt
```
### Dependências

Lista de dependências do projeto:
```bash
﻿selenium==3.0.0
urllib3==2.2.1
```

4. Crie um .env com as seguintes variaveis de configuração:
```
STEPS = /path/local/steps.yaml
WINIUM_DRIVER = /path/local/winium.desktop.exe
```

## Logs 
Os logs de execução são armazenados no arquivo `log.log` na raiz do projeto.

## Uso
Após configurado, inicie a automação.

