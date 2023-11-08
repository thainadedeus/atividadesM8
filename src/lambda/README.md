# Lambda e API gateway

### **1. AWS Lambda:**

O AWS Lambda é um serviço de computação serverless oferecido pela Amazon Web Services (AWS). Ele permite que você execute código sem a necessidade de provisionar ou gerenciar servidores. 

- **Serverless**: Não necessita de gerenciamento da infraestrutura, como servidores. O AWS Lambda dimensiona automaticamente para atender à demanda.
- **Event-Driven**: O AWS Lambda é acionado por eventos, como alterações em dados no Amazon S3, chamadas de API Gateway, eventos de banco de dados, etc.

### **2. Amazon API Gateway:**

A Amazon API Gateway é um serviço da AWS que facilita a criação, publicação, manutenção, monitoramento e segurança de APIs (interfaces de programação de aplicativos).

- **Criação de APIs RESTful**: A API Gateway permite que você crie APIs RESTful que fornecem acesso a recursos e funcionalidades de aplicativos.
- **Gerenciamento de Tráfego**: Você pode definir como o tráfego da API é roteado para diferentes recursos e serviços da AWS.
- **Autenticação e Autorização**: A API Gateway oferece suporte à autenticação e autorização, permitindo que você controle quem pode acessar sua API.
- **Monitoramento:** Monitorar o tráfego da API, gerar logs e criar métricas para entender o uso da API.
- **Integração com Serviços AWS**: A API Gateway pode ser facilmente integrada com serviços da AWS, como AWS Lambda, Amazon DynamoDB, Amazon S3, etc.

![Visão geral](https://github.com/thainadedeus/atividadesM8/blob/main/imagens/visao_geral.png)


### 3**. Função lambda:**

Esse código é uma função AWS Lambda escrita em Python que serve como uma API simples com autenticação Bearer Token. 

1. Importação do módulo `json` para lidar com JSON.
2. Definição da variável `API_TOKEN` com um valor de exemplo "123" que será usado como token de autenticação.

A função `lambda_handler` é a principal função Lambda que processará as solicitações. 

- Verifica se o método HTTP é POST através do campo `'httpMethod'` no evento.
- Obtém o cabeçalho 'Authorization' da solicitação para verificar se ele contém um token de autenticação no formato "Bearer {API_TOKEN}".
- Se o cabeçalho de autorização estiver ausente ou não corresponder ao token esperado, a função retorna uma resposta de erro 401 (Não autorizado) com a mensagem "Falha na autenticação ou método não permitido".
- Se o cabeçalho de autorização estiver presente e corresponder ao token esperado, a função tenta analisar o corpo da solicitação como JSON. Se a análise for bem-sucedida, ele retorna uma resposta de sucesso 200 com a mensagem "Autenticado com sucesso e processado com êxito". Se houver um erro na decodificação do JSON, ele retornará uma resposta de erro 400 com uma mensagem de erro específica.
- Se a solicitação não for um método POST ou se não houver corpo na solicitação, a função retornará uma resposta de erro 400 com a mensagem "Solicitação inválida".

A fim de testar essa função, foi utilizado o Postman.

![Postman](https://github.com/thainadedeus/atividadesM8/blob/main/imagens/postman.png)

