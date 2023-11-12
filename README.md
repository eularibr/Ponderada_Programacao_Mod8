# Criação de um AWS Lambda com API Gateway em Python

**Introdução**:

Nessa documentação, explicarei como criar uma função AWS Lambda em Python e expô-la como uma API por meio do Amazon API Gateway. Utilizei o laboratório da AWS Academy como base para essa demonstração. Aqui terá informações sobre como configurar a função Lambda, criar um recurso e método no API Gateway e realizar um teste bem-sucedido usando o Postman.

## 1º Função criada - Retornando Nome + Mensagem

**Passo 1**: Acesse a AWS Management Console

Acesse a AWS Management Console em https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions/LarissaF
unction?tab=code


<div align="center">
<img src="https://github.com/eularibr/Ponderada_Programacao_Mod8/blob/main/imagens/Imagem1.png" width="900"/> <br>
</div>

**Passo 2**: Criação da Função Lambda

2.1. No console AWS Management, clique em "Serviços" no canto superior esquerdo e selecione "Lambda" na seção "Compute".

2.2. Clique em "Criar função" para iniciar o processo de criação da função Lambda.

2.3. Escolha "Função Lambda" para a execução de suas funções e clique em "Próximo" na parte inferior da página.

2.4. Na próxima página, configure as seguintes opções:

Nome da função: Dê um nome significativo para sua função Lambda.
Tempo de execução: Selecione a versão Python que deseja usar (por exemplo, Python 3.8).
Role: Selecione uma função existente ou crie uma nova função com as permissões adequadas para acessar seu banco de dados ou outros recursos.
2.5. Clique em "Criar função" para criar sua função Lambda.

2.6. O link para da minha função é: https://5ye3xx2m16.execute-api.us-east-1.amazonaws.com/default/LarissaFunction

2.7. O código que foi criado foi: 

<div align="center">
<img src="https://github.com/eularibr/Ponderada_Programacao_Mod8/blob/main/imagens/Imagem2.png" width="900"/> <br>
</div>

**Passo 3**: Configuração da API Gateway

3.1. No AWS Management Console, clique em "Serviços" e selecione "API Gateway" na seção "Networking & Content Delivery".

3.2. Clique em "Criar API" para começar a criar sua API.

3.3. Escolha "API HTTP" e clique em "Criar API HTTP".

3.4. Dê um nome à sua API e clique em "Criar API".

3.5. No painel esquerdo, clique em "Recursos" e, em seguida, clique com o botão direito do mouse em "/" para criar um novo recurso.

3.6. Dê um nome ao recurso (por exemplo, "meu-recurso") e clique em "Criar recurso".

3.7. Com o recurso selecionado, clique em "Criar método" e escolha o método HTTP que você deseja expor (por exemplo, POST).

3.8. Em "Configurar ação", selecione "Função Lambda" e escolha a função Lambda que você criou anteriormente.

3.9. Clique em "Salvar" e, em seguida, em "OK" para confirmar as permissões da função.

**Conclusão**:

URL da minha função: https://5ye3xx2m16.execute-api.us-east-1.amazonaws.com/default/LarissaFunction

Para testar essa API, utilizei a ferramenta Postman. Enviei uma solicitação POST para a URL gerada pela API Gateway e verifiquei se essa função Lambda respondia com sucesso. E ao final, a mensagem no código foi exibida com sucesso.
O teste que fiz foi o seguinte: 

- Primeiro colei a URL no postam
- Em seguida mudei da opção GET para POST
- Na aba ‘body’ escrevi o seguinte código: 

{
    "nome": "Larissa"
}

Em que a estrutura é:
 {
    "nome": "SeuNome"
}

Ou seja, qualquer nome que for digitado, será mostrado junto com a mensagem que programei.

Ficou assim no meu Postman:

- **Teste 1**: digitando um nome com POST

<div align="center">
<img src="https://github.com/eularibr/Ponderada_Programacao_Mod8/blob/main/imagens/Imagem3.png" width="900"/> <br>
</div>

Logo, dá para ver que o nome mostrado foi Larissa, junto com a frase. 
	
- **Teste 2**: digitando um nome com GET

	Um outro teste que foi feito, foi utilizado GET ao invés de POST e portanto a saída foi a seguinte “Apenas solicitações POST são permitidas”:

<div align="center">
<img src="https://github.com/eularibr/Ponderada_Programacao_Mod8/blob/main/imagens/Imagem4.png" width="900"/> <br>
</div>

- **Teste 3**: digitando um número com POST

<div align="center">
<img src="https://github.com/eularibr/Ponderada_Programacao_Mod8/blob/main/imagens/Imagem5.png" width="900"/> <br>
</div>

Pode-se notar que apareceu uma mensagem de que apenas strings são permitidas com o valor para o campo “nome”, pois no código foi definido que apenas strings seriam aceitas.

## 2º Função criada - Autenticação com token

Agora o outro teste que fiz com token de autenticação ficou assim: 

API endpoint: https://lp5lfrzjc0.execute-api.us-east-1.amazonaws.com/default/TesteFunction

O código da função criada foi:

<div align="center">
<img src="https://github.com/eularibr/Ponderada_Programacao_Mod8/blob/main/imagens/Imagem6.png" width="900"/> <br>
</div>

Testes no Postman:

- **Teste 1**: credenciais inválidas
<div align="center">
<img src="https://github.com/eularibr/Ponderada_Programacao_Mod8/blob/main/imagens/Imagem7.png" width="900"/> <br>
</div>

Retorna: Credenciais inválidas

- **Teste 2**: credenciais válidas:
<div align="center">
<img src="https://github.com/eularibr/Ponderada_Programacao_Mod8/blob/main/imagens/Imagem8.png" width="900"/> <br>
</div>

Retorna: Autenticação bem-sucedida.
