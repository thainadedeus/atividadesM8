# Docker-compose com todos os parâmetros de um kafka

Kafka é o nome da plataforma de streaming de dados distribuídos, desenvolvida pela Apache Software Foundation. Ela permite que os dados sejam transmitidos em tempo real, em grande escala e com alta eficiência entre diferentes sistemas.

### **Entendimento:**

**Criação do Docker Compose com os Parâmetros Kafka e Seus Gerenciadores**:

- Criação do arquivo `docker-compose.yml` que define serviços para o Apache Kafka e seus gerenciadores ZooKeeper;

**Utilização dos Parâmetros Conforme a Documentação**:

- Os serviços Kafka e ZooKeeper são utilizados no arquivo `docker-compose.yml;`

**Implementação Funcional**:

- A implementação está correto, dada que a mensagem é direcionada ao ouvinte e interpretada com sucesso.

### Explicação do consumidor:

O código que você forneceu é um exemplo de um consumidor Kafka em Python usando a biblioteca `confluent-kafka`. Vou explicar o que cada parte do código faz:

**Importações**:

- `from confluent_kafka import Consumer, KafkaError`: Isso importa as classes necessárias da biblioteca `confluent-kafka` para criar um consumidor Kafka e lidar com erros relacionados ao Kafka.

**Configuração do Consumidor**:

- O código configura o consumidor Kafka com as seguintes opções:
    - `'bootstrap.servers'`: Especifica o servidor Kafka de inicialização;
    - `'group.id'`: Define o ID do grupo de consumidores a que este consumidor pertence ;
    - `'auto.offset.reset'`: Define o comportamento de reinicialização automática dos offsets.

**Assinatura de Tópicos**:

- `consumer.subscribe(['conversas'])`: Direciona o consumidor a se inscrever no tópico chamado 'conversas'.

**Loop de Consumo**:

- `while True`: Inicia um loop infinito para consumir mensagens repetitivamente.

**Recebimento de Mensagens**:

- `msg = consumer.poll(1.0)`: O consumidor aguarda por mensagens do tópico 'conversas' por até 1 segundo.

**Tratamento de Mensagens**:

- O código verifica se a mensagem é `None`. Se for `None`, significa que não houve mensagens disponíveis no tempo limite especificado.
- Se houver um erro relacionado ao Kafka (por exemplo, uma partição chegou ao fim), o código imprime uma mensagem de erro.
- Se uma mensagem válida for recebida, o código imprime a chave (se houver) e o valor da mensagem.

### Explicação do produtor:

**Importações**:

- `from confluent_kafka import Producer`: Isso importa a classe `Producer` da biblioteca `confluent-kafka`, que permite que você produza mensagens para um tópico Kafka.

**Configuração do Produtor**:

- `producer = Producer({'bootstrap.servers': 'localhost:9092'})`: Aqui, você configura o produtor Kafka com as seguintes opções:
    - `'bootstrap.servers'`: Especifica o servidor Kafka de inicialização para se conectar ao cluster Kafka.

**Produção de Mensagem**:

- `producer.produce('conversas', key='chave', value='faco o que eu posso com o que tenho no momento, quando tiver melhores condicoes, faco melhor')`: Este código envia uma mensagem para o tópico 'conversas' com a chave 'chave' e o valor especificado. Isso é feito com o método `produce()` do produtor.

**Flush (Esvaziamento) do Produtor**:

- `producer.flush()`: O método `flush()` é usado para garantir que todas as mensagens pendentes sejam enviadas para o cluster Kafka antes de encerrar o produtor.
