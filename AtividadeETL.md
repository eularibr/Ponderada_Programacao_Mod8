# Documentação - ETL em Flask com Teste de Integração para API OpenWeather

**Introdução**

Este documento fornece um guia para criar uma ETL (Extração, Transformação e Carga) em Flask, juntamente com testes de integração, para obter dados climáticos da API OpenWeather e armazená-los em um banco de dados SQLite. 
O objetivo é extrair informações climáticas de várias cidades, transformá-las em um formato adequado e carregá-las em uma tabela no banco de dados.


Essa atividade foi feita inicialmente acessando o seguinte site: https://openweathermap.org/current, e utilizando o seguinte link: https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}.
Ou seja, foi necessário pegar a minha API key no site, em que: 
- criei uma api key com o nome teste
- a api key gerada para mim foi: 7e15951f31a6f5146a44725003d8dd61, a qual usarei no meu código para a atividade.


**Passo 1**: Configuração do Ambiente

Antes de começar, é preciso obter o Python e o Flask instalados em seu ambiente. Pode-se instalar o Flask usando o seguinte comando:

- pip install Flask

**Passo 2**: Crie um arquivo chamado api.py para a aplicação Flask. O projeto consiste em um arquivo principal chamado `api.py`. Este arquivo contém a configuração da aplicação Flask, a definição do modelo de dados, funções para obter dados climáticos da API OpenWeather e uma rota para realizar a ETL.


**Passo 3**: Configuração do Banco de Dados. Um banco de dados SQLite é utilizado para armazenar os dados climáticos. O arquivo `database.db` é criado automaticamente quando a aplicação é executada pela primeira vez. 

**Passo 4**: Teste de integração

- Crie um arquivo teste.py com o conteúdo fornecido.
- Execute os testes com o comando pytest teste.py.

**Passo 5**: Executar a aplicação e os testes

- Execute a aplicação com o comando **python api.py**.
- Execute os testes em outro terminal com o comando **pytest teste.py**.

- Estrutura de pasta no vscode:

<div align="center">
<img src="https://github.com/eularibr/Ponderada_Programacao_Mod8/blob/main/imagens/ETL-imagem1.png" width="500"/> <br>
</div> <br>

É importante ressaltar que quando for rodar um novo terminal no arquivo api.py, é necessário fazer as seguintes instalações para que não dê erro: 

- **pip install Flask**
- **pip install flask_sqlalchemy**
- **pip install datetime**
- **pip instal pytz**

O mesmo vale para o arquivo teste.py: 

- **pip install pytest**
- **pip install responses**
- **pip install api**
- **pip install app**
- **pip install db**
- **pip install WeatherData**
Para rodar os testes, é necessário digitar o seguinte comando no terminal: python -m pytest teste.py.


**Arquivo api.py código**:

<div align="center">
<img src="https://github.com/eularibr/Ponderada_Programacao_Mod8/blob/main/imagens/ETL-imagem2.png" width="900"/> <br>
</div> 

<div align="center">
<img src="https://github.com/eularibr/Ponderada_Programacao_Mod8/blob/main/imagens/ETL-imagem3.png" width="900"/> <br>
</div>

<div align="center">
<img src="https://github.com/eularibr/Ponderada_Programacao_Mod8/blob/main/imagens/ETL-imagem4.png" width="900"/> <br>
</div> <br>

No código acima, há:

- Importação de bibliotecas necessárias
- Configuração do nível de log para DEBUG
- Inicialização da aplicação Flask
- Configuração da URI do banco de dados SQLite
- Configuração do fuso horário para o horário de Brasília
- Função para obter a data e hora atual no fuso horário do Brasil
- Definição do modelo de dados para representar informações climáticas no banco
- Função para realizar a ETL (Extração, Transformação e Carga) dos dados climáticos
- Chave de API da OpenWeather, a qual peguei no site
- Lista de cidades que quero obter dados climáticos
- Loop sobre as cidades para obter os dados climáticos
- Construção da URL para fazer a requisição à API OpenWeather
- Realização da requisição à API
- Obtenção dos dados climáticos em formato JSON
- Retorno da lista de dados climáticos
- Rota para exibir todos os dados climáticos na página web
- Renderização do template HTML para exibir os dados na página
- Execução da aplicação Flask quando o script é executado diretamente
- Criação de todas as tabelas necessárias no banco de dados
- Entre outros. <br>

**Arquivo teste.py código**:

<div align="center">
<img src="https://github.com/eularibr/Ponderada_Programacao_Mod8/blob/main/imagens/ETL-imagem5.png" width="900"/> <br>
</div> <br>

No código acima, há:

- Importação das bibliotecas necessárias para teste
- Biblioteca para simular respostas de requisições HTTP
- Fixture para configurar o ambiente de teste e criar um cliente de teste
- Configuração para modo de teste
- Criação de um cliente de teste
- Criação de todas as tabelas no banco de dados para o teste
- Retorna o cliente de teste
- Teste da rota associada à Extração, Transformação e Carga (ETL) dos dados climáticos
- Simulação de uma resposta da API OpenWeather para a rota de teste
- Asserções para verificar se a resposta da rota está correta
- Teste da rota que exibe todos os dados climáticos na página web
- Entre outros.

**Tela de Front que retorna os dados**:

<div align="center">
<img src="https://github.com/eularibr/Ponderada_Programacao_Mod8/blob/main/imagens/ETL-imagem6.png" width="900"/> <br>
</div> <br>

Obs: os dados também podem ser vistos pelo terminal. Porém, na tela web, fica uma melhor visualização. 


<div align="center">
<img src="https://github.com/eularibr/Ponderada_Programacao_Mod8/blob/main/imagens/ETL-imagem7.png" width="900"/> <br>
</div> <br>

Esses dados foram puxados da API, e então armazenado em um banco de dados:

<div align="center">
<img src="https://github.com/eularibr/Ponderada_Programacao_Mod8/blob/main/imagens/ETL-imagem8.png" width="900"/> <br>
</div> <br>

Logo, é possível visualizar na parte do banco de dados:

<div align="center">
<img src="https://github.com/eularibr/Ponderada_Programacao_Mod8/blob/main/imagens/ETL-imagem9.png" width="900"/> <br>
</div> <br>

Sendo as colunas: 
- ID
- data_ingestao
- data_tipo
- valores
- uso

**Conclusão**

Este guia mostra um processo passo a passo para criar uma ETL em Flask e realizar testes de integração. Nessa documentação, entende-se como obter dados climáticos da API OpenWeather, armazená-los em um banco de dados e garantir a integridade do sistema por meio de testes automatizados.
