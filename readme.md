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
