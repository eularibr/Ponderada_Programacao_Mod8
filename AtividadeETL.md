# Documentação - ETL em Flask com Teste de Integração para API OpenWeather

Essa atividade foi feita inicialmente acessando o seguinte site: https://openweathermap.org/current, e utilizando o seguinte link: https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}.
Ou seja, foi necessário pegar a minha API key no site, em que: 
- criei uma api key com o nome teste
- a api key gerada para mim foi: 7e15951f31a6f5146a44725003d8dd61, a qual usarei no meu código para a atividade.


**Passo 1**: Configuração do Ambiente

Antes de começar, é preciso obter o Python e o Flask instalados em seu ambiente. Pode-se instalar o Flask usando o seguinte comando:

- pip install Flask

**Passo 2**: Crie um arquivo chamado api.py para a aplicação Flask

**Passo 3**: Configuração do banco de dados

**Passo 4**: Teste de integração

- Crie um arquivo teste.py com o conteúdo fornecido.
- Execute os testes com o comando pytest teste.py.

**Passo 5**: Executar a aplicação e os testes

- Execute a aplicação com o comando python api.py.
- Execute os testes em outro terminal com o comando pytest teste.py.

- Estrutura de pasta no vscode:

- Arquivo api,py código:

- Tela de Front que retorna os dados:

Obs: os dados também podem ser vistos pelo terminal. Porém, na tela web, fica uma melhor visualização. 

- Esses dados foram puxados da API, e então armazenado em um banco de dados:
Logo, é possível visualizar na parte do banco de dados:
Sendo as colunas: 
- ID
- data_ingestao
- data_tipo
- valores
- uso
