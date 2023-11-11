# **Aplicação Flask ETL com MongoDB**


O script Python corresponde a um ETL (Extract, Transform, Load) que extrai dados meteorológicos da API, transforma os dados e carrega-os em um banco de dados MongoDB.

A classe `WeatherETL` é responsável por todo o processo ETL. Ela tem os seguintes métodos:

- `__init__`: Este é o construtor da classe. Ele inicializa a conexão com o banco de dados MongoDB e define a coleção onde os dados serão armazenados.

- `get_openweather_data`: O método recebe o nome de uma cidade como parâmetro e faz uma requisição GET para a API do OpenWeatherMap para obter dados meteorológicos dessa cidade. Se a requisição for bem-sucedida (código de status HTTP 200), ele retorna os dados em formato JSON. Caso contrário, ele imprime uma mensagem de erro e retorna `None`.

- `etl_to_mongodb`: O método recebe os dados meteorológicos e o nome da cidade como parâmetros. Ele transforma os dados (determinando o "uso" com base na temperatura) e os carrega no MongoDB. O documento inserido no MongoDB contém a data e hora da ingestão, o nome da cidade, o tipo de dados ("Condições Meteorológicas"), os valores dos dados e o "uso" determinado.

- `determine_usage`: Este método recebe os dados meteorológicos como parâmetro e determina o "uso" com base na temperatura. Se a temperatura for maior que 25, ele retorna "Clima Quente". Caso contrário, ele retorna "Clima Moderado".

No final do script, a instância da classe `WeatherETL` é criada e o processo ETL é executado para uma lista de cidades brasileiras.

## Testes unitários

Corresponde conjunto de testes unitários para a classe `WeatherETL` que você forneceu anteriormente. Ele usa o módulo `unittest` do Python e a biblioteca `unittest.mock` para simular as dependências externas da classe. 

- `test_get_openweather_data_success`: Este teste verifica se o método `get_openweather_data` retorna os dados corretos quando a requisição GET para a API do OpenWeatherMap é bem-sucedida (código de status HTTP 200). Ele usa o método `patch` para simular a resposta da API.

- `test_get_openweather_data_failure`: Este teste verifica se o método `get_openweather_data` retorna `None` quando a requisição GET para a API do OpenWeatherMap falha (código de status HTTP 404). Novamente, ele usa o método `patch` para simular a resposta da API.

- `test_etl_to_mongodb`: Este teste verifica se o método `etl_to_mongodb` insere o documento correto no MongoDB. Ele usa o método `patch` para simular o cliente MongoDB e o método `determine_usage`. Ele também simula a data e hora atual para garantir que o documento inserido tenha a data e hora corretas.

No final do script, serão executos todos os testes unitários. Se algum teste falhar, ele imprimirá uma mensagem de erro no console. Se todos os testes passarem, ele não imprimirá nada.

