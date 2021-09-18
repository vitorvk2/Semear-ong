# Projeto para ong Semear

Este projeto pauta a criação de uma estrutura online para a ONG Semear de Marília-SP que necessita de uma organização dos seus alunos e orientadores de maneira prática e rápida. Para isso o projeto será feito com Django para parte Web e API e Flutter para mobile, no banco de dados utilizaremos o MySQL


## Dependências

Para usar rodar o projeto é necessário ter o Python no mínimo na versão 3.6 e MySQL 5.7 já no mobile Flutter 2.0.3


## Install

> MySQL:

```sql
CREATE DATABASE semear;
```

> Ambiente

Linux (debian based):
```bash
apt install python3-pip
```

Windows e Macos já vem o pip instaldo


```bash
pip install virtualenv

git clone ...

cd .../site

virtualenv -p python3 env

. ./env/bin/active

pip install -r requirements.txt
````

Crie um arquivo ```.env``` com base no ```.env.example```, troque as informações da chave e rode 

```bash
python manage.py migrate

python manage.py runserver
```

O site vai iniciar na porta 8000 do localhost

> Mobile

```bash
cd .../app/semear

flutter pub get

flutter run 
```