## Lullaby - Serviço responsável pelos produtos favoritos de nossos clientes

## Técnologias utilizadas

### Backend
* [Python](https://www.python.org/)
* [Redis](https://redis.io/)
* [PostgreSQL](https://www.postgresql.org/)


## Execução do projeto

1. Como pré-requisito, possuir [docker](https://www.docker.com/).
2. Dentro da pasta do projeto, executar o comando: `docker-compose up`.

> Este comando irá levantar todos os containers necessários para inicializar nosso projeto.

### API's disponíveis
**Lista de todos os colaboradores**
```
GET: <SERVER>/api/customer
```

**Adicionar um novo colaborador**
```
POST: <SERVER>/api/customer
BODY: 
{
    "name": <Nome do cliente>,
    "email": <Enail do cliente>
}
```

**Buscar, deletar e atualizar um colaborador**
```
GET/DELETE/PUT/PATCH: <SERVER>/api/customer/<ID CONSUMIDOR>
```

**Buscar todos os favoritos de um colaborador**
```
GET: <SERVER>/api/customer/<ID CONSUMIDOR>/favorite
```

**Adicionar produto favorito**
```
POST: <SERVER>/api/customer/<ID CONSUMIDOR>/favorite
BODY: 
{
    "product_id": <ID DO PRODUTO>
}
```

**Ver detalhes de um produto favorito / Deletar o favorito**
```
GET/DELETE: <SERVER>/api/customer/<ID CONSUMIDOR>/favorite/<ID PRODUTO>
```


### Autorização:
Foi criada uma autorização simples, utilizando api key utilizada em todas as requests realizadas para a aplicação.
A API KEY default configurada no docker-compose é `123456`, onde espera-se este dado no header da requisição.
