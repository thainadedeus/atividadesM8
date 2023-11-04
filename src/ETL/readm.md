# **Aplicação Flask ETL com MongoDB**

## **Descrição**

Esta aplicação Flask ETL (Extract, Transform, Load) é projetada para extrair dados da API OpenWeather, transformá-los de acordo com as necessidades específicas do projeto e carregá-los no MongoDB. A aplicação fornece um endpoint para iniciar o processo ETL e armazena os dados no MongoDB para posterior análise.

## **Configuração**

### **Pré-requisitos**

- Python 3.x instalado
- MongoDB instalado e em execução
- Chave de API OpenWeather

### **Instalação de Dependências**

```
bashCopy code
python -m venv etl_env
source etl_env/bin/activate
pip install flask flask-pymongo requests

```

## **Uso**

### **Executando a Aplicação**

Para executar a aplicação Flask ETL, use o seguinte comando no diretório raiz do projeto:

```
bashCopy code
python app.py

```

A aplicação estará disponível em **`http://localhost:5000`**.

### **Endpoints da API**

- **/etl**
    - Método: GET
    - Descrição: Inicia o processo ETL, que envolve a extração de dados da API OpenWeather, a transformação desses dados e o carregamento no MongoDB.
    - Parâmetros: Nenhum.
    - Resposta: Retorna um JSON indicando o status do processo ETL.

## **Estrutura do Código**

A estrutura do código da aplicação Flask ETL é dividida em três partes principais:

1. **Configuração e Inicialização** (app.py)
    - Configuração do aplicativo Flask, incluindo a configuração do MongoDB.
    - Definição do modelo de dados (**`WeatherData`**).
    - Funções para a extração, transformação e carregamento de dados.
2. **Endpoint da API ETL** (app.py)
    - Definição do endpoint **`/etl`** que inicia o processo ETL.
    - Tratamento de requisições HTTP GET para iniciar a extração, transformação e carregamento de dados.
3. **Teste de Integração** (test_app.py)
    - Arquivo de teste que verifica se o processo ETL é bem-sucedido.
    - Usa a biblioteca **`unittest`** para testar o endpoint **`/etl`**.

##
