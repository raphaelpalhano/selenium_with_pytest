# Selenium com Python


# Execução


### Config
**cli**: `python venv pyenv`
**cli**: `./pyenv/Scripts/Activate.ps1`
**cli**: `pipenv install`

### Execute
**cli**: `pipenv run python -m pytest`


# Configurando browser

* Acesse o arquivo ./config.json e modfiquei a opção browser

~~~json
{
    "browser": "Headless Chrome",
    "implicit_wait": 10
}

~~~


# Execução Paralela

* Baixe o pacote: `pipenv install pytest-xdist`
* Execute o comando: `pipenv run python -m pytest -n 2` 
**OBS** -n é o indicar de quantidade e o número 2 é quantas thread vão executar simultaneamente