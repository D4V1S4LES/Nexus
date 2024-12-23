
# Projeto: Aplicativo Web em Flask

Este projeto é uma aplicação web desenvolvida utilizando o framework Flask. Abaixo você encontrará uma explicação detalhada do funcionamento geral do aplicativo, as principais funcionalidades, a estrutura do código e a lista de dependências necessárias para rodá-lo.

---

## Funcionalidades Principais

- **Estrutura baseada no Flask**: O arquivo principal `app.py` gerencia as rotas e a lógica do servidor.
- **Interface HTML**: Arquivos na pasta `templates` fornecem as páginas web renderizadas dinamicamente.
- **Recursos estáticos**: A pasta `static` contém os arquivos CSS, JavaScript e imagens.

---

## Estrutura do Projeto e Explicação do Código

### Arquivo Principal: `app.py`

O `app.py` é o coração da aplicação e contém a seguinte estrutura:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

- **Importações**: O módulo `Flask` é importado para criar o servidor, e `render_template` é usado para renderizar os arquivos HTML.
- **Definição do aplicativo**: `app = Flask(__name__)` inicializa a aplicação Flask.
- **Rotas**: 
  - A rota `/` define a página inicial do aplicativo, renderizando o arquivo `index.html`.
- **Execução**: `app.run(debug=True)` inicia o servidor em modo de depuração.

### Pastas Importantes

- **`templates/`**:
  - Contém arquivos HTML que são renderizados dinamicamente pelas rotas do Flask. Exemplo:

```html
<!-- Exemplo de index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página Inicial</title>
</head>
<body>
    <h1>Bem-vindo ao Aplicativo Flask</h1>
</body>
</html>
```

- **`static/`**:
  - Contém arquivos estáticos como CSS e JavaScript. Exemplos de uso incluem estilização ou scripts para interatividade da página.

---

## Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone <URL-do-seu-repositorio>
   cd <nome-da-pasta-clonada>
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado)**:
   ```bash
   python -m venv venv
   source venv/bin/activate # ou "venv\Scripts\activate" no Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o aplicativo**:
   ```bash
   python app.py
   ```

5. **Acesse no navegador**:
   O aplicativo estará disponível em `http://127.0.0.1:5000`.

---

## Dependências

Abaixo está a lista detalhada de dependências encontradas no arquivo `requirements.txt`:

- **Flask**: Framework web para Python. 
  - Instalação: `pip install Flask`
  - Documentação: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

Outras dependências podem ser adicionadas ao projeto conforme necessário e listadas no `requirements.txt`.

---

## Personalização

- **Templates**: Modifique os arquivos HTML na pasta `templates/` para alterar a interface.
- **Estilo**: Atualize os arquivos CSS na pasta `static/` para personalizar o design.
- **Rotas**: Adicione ou modifique as rotas no arquivo `app.py` para incluir novas funcionalidades.

---
