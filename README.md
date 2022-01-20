# API REST para o desafio da Framework
Atenção: Você precisa ter instalado Python 3 no seu computador.
 
Na pasta solution abra o CMD e execute o comando abaixo

```
pip instal -r requirement.txt
```
Caso esteja usando o Pycharm basta rodar o projeto, caso não esteja, ainda na pasta Solution execute o comando abaixo:
```
flask run
```
Neste ponto sua API deverá estar rodando no endereço http://127.0.0.1:5000/

# Endpoints
Os seguintes endpoints estão configurados:
## Tokens
- `/token` - GET - Obtém o token JWT
Não envia nada por não fazer nenhum tipo de cadastro, somente retorna o token <br>
**Retorno Token**
```
 "<token aqui>"
```
## Todos
É necessário enviar o token adquirido no endpoint acima no Authorization o token vai ficar igual ao exemplo abaixo: <br>
`Bearer <cole o token aqui>`<br>
- `/todos` - GET - Obtém lista de todos <br>
**Retorno todos**
- Em caso de sucesso
```
 {
  "id": <id do Registro>,
  "title": <nome do registro>
 }
```
- Em caso de erro
```
 {
  "error":{
    "Reason": "error description"
    }
 }
```
OBS: Também foi disponibilizado uma Colletion no postman para o mesmo e-mail que foi liberado o repositório do GitHub
