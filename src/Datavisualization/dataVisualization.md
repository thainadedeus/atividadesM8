# Data visualization

## Configuração do Redshift com o Metabase

A configuração do Amazon Redshift com o Metabase inicia-se com a adição de uma conexão de banco de dados. Isso é realizado ao clicar no ícone de engrenagem no canto superior direito e navegar até Configurações do administrador > Bancos de dados > Adicionar um banco de dados.

Após a adição de um banco de dados, as configurações podem ser editadas a qualquer momento. As configurações incluem o nome de exibição para o banco de dados na interface do Metabase, o endereço IP do banco de dados ou seu nome de domínio, a porta do banco de dados, o nome do banco de dados ao qual se deseja conectar, e os esquemas que se deseja sincronizar e verificar.

É necessário fornecer o nome de usuário do banco de dados para a conta que será usada para se conectar ao banco de dados e a senha para o nome de usuário. Além disso, opções podem ser anexadas à string de conexão que o Metabase usa para se conectar ao banco de dados.

Após a conclusão dessas etapas, a exploração, visualização e publicação de dados do Amazon Redshift no Metabase podem ser iniciadas.

## Desenvolvimento da view e análise dos dados

A view desenvolvida é uma representação virtual dos dados contidos nas tabelas**`despesa_individual`** e **`rendimento_trabalho.`** 

Justifica-se a sua criação a fim de observar a relação entre as rendas adquiridas pelas mais diversas formas de trabalho e as despesas de cada indivíduo representado na pesquisa da POF. 

O gráfico de barras mostra três categorias diferentes: “Monetária, à vista, para a Unidade de Consumo”, “Cartão de crédito, à vista, para a Unidade de Consumo Forma de Aquisição” e “Doação”.

1. A primeira barra representa a categoria “Monetária, à vista, para a Unidade de Consumo” e atinge até 5.000.000 no eixo y.
2. A segunda barra representa a categoria “Cartão de crédito, à vista, para a Unidade de Consumo Forma de Aquisição” e se estende até aproximadamente 3.500.000 no eixo y.
3. A terceira barra representa a categoria “Doação” e é significativamente menor que as outras duas barras, atingindo cerca de 1.500.000 no eixo y.
![Gráfico](https://github.com/thainadedeus/atividadesM8/blob/main/imagens/grafico.png)
