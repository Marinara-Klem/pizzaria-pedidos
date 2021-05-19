# pizzaria-pedidos

Um sistema para delivery de pizzas, com cadastro simples de sabores, e pedidos, contendo status do pedido do cliente


## como criar uma virtualenv

```shell
virtualenv venv
```

## como ativar virtualenv

```shell
source venv/bin/activate
```

## como rodar as migrações
```shell
python pizzaria/manage.py makemigrations && python pizzaria/manage.py migrate
```

## como criar um administrador
```shell
python pizzaria/manage.py createsuperuser
```

## como rodar o sistema
```shell
python pizzaria/manage.py runserver
```

## e acesse localhost:8000/admin no navegador