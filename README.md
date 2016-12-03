# neurohack-2016-starterkit

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/neurohack-2016-starterkit/Lobby)
<a href="https://everware.rep.school.yandex.net/hub/oauth_login?repourl=https://github.com/yandexdataschool/neurohack-2016-starterkit"><img src="https://img.shields.io/badge/run%20me-%40everware-blue.svg" /></a>

Информацию по контесту можно посмотреть [здесь](contest.md).

Текущие результаты: [ссылка](https://contest.yandex.ru/neuro/)

## Настройка окружения

Клонируйте репозиторий:
```
git clone https://github.com/yandexdataschool/neurohack-2016-starterkit && cd neurohack-2016-starterkit
```

Если вы используете Docker, то вам будет удобно использовать наш образ, в котором уже настроены окружения в соответствии с
рекомендациями ниже. Выполните
```
docker build -t neurohack_dec_2016 .
```

А затем `docker run -it -p 8888:8888 -v $(pwd):/notebooks neurohack_dec_2016`, для запуска Jupyter внутри контейнера, который станет доступен по [http://localhost:8888](http://localhost:8888).

### Python

Если вы уже имеете опыт установки пакетов, и у вас уже настроены удобные для вас окружения, то, возможно, вам достаточно
будет посмотреть в py(2|3)_environment.yml или requirements.txt и доставить нужные пакеты. Например, с помощью pip:
```
pip install -r requirements.txt
```

В любом случае мы рекомендуем установить менеджер пакетов [conda](http://conda.pydata.org/docs/), например:
```
curl https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh >conda_install.sh && \
chmod +x conda_install.sh && ./conda_install.sh -b -p /home/$USER/miniconda3 && rm conda_install.sh
```

После установки conda желательно закрыть/открыть терминал или вручную обновить `PATH`:
```
export PATH="/home/$USER/miniconda3/bin:$PATH"
```

В py(2|3)_environment.yml приведены те зависимости, которые установлены в Я.Контесте (кроме jupyter).
Установить окружение для python3 можно так:
```
conda env create --file py3_environment.yml
```

Для python2 используйте `py2_environment.yml`.

Далее, активируйте окружение `source activate py3_env`. Для неинтерактивных задач, где _не_ нужно взаимодействие с Я.Контестом, вы, возможно, захотите установить еще какие-то модули:
```
conda install -y [package]
```

Запустите Jupyter из активированного окружения: `jupyter-notebook`.

### R
Для работы с R вы также можете использовать conda, хотя пакеты для R обычно устанавливаются прямо из R.

Окружение можно установить следующим образом:
```
conda env create --file r_environment.yml && source activate r_env
```

Помимо этого устанавливаются пакеты из `install_modules.R`.
Например, выполните следующую команду, чтобы установить эти пакеты (которые также стоят в Я.Контесте):
```
Rscript install_modules.R
```

## Выгрузка данных

Данные для конкурса размещены на https://transfer.sh. Чтобы выгрузить их в свое окружение необходимо выполнить команду `./get_data.sh`, находясь в корневой директории локальной копии этого репозитория.
