# bwconvert

---

* [Russian Text](#Russian)
* [English Text](#English)

---

## <a name="Russian">Russian README.</a>

Конвертер из Bitwarden json в csv для KeePassXC.

![Python-3](./image/python-3-icon.svg "Python 3") &nbsp;![Linux](./image/linux.svg "Linux") &nbsp;![Win-7](./image/win-7-icon.svg "Win-7") &nbsp;![Win-10](./image/win-10-icon.svg "Win-10")

## <a name="Oglavlenie">Оглавление</a>

1. [Установка.](#Setup)
2. [Обзор утилиты](#ShowUtilites)
3. [Об авторе.](#About)

---

## <a name="Setup">1. Установка.</a>

Для установки программы воспользуйтесь следующей командой при помощи **Makefile**:

```bash
cd ~
git clone https://github.com/maximalisimus/bwconvert.git
cd bwconvert
sudo make DESTDIR=/ install
```

Для контроля установки в **Makefile** предусмотрены некоторые переменные, которыми вы могли бы воспользоваться.

* **DESTDIR** - местоположение в системе, директория. По умолчанию задаётся корень системы.
* **POSTDIR** - установочная директория перед папкой с программой, т.е. родительская директория программы. По умолчанию равна **&laquo;usr/share&raquo;**. <u>Обязательно должна присутствовать. Не допускается устанавливать пустой.</u>
* **INSTALLDIR** - удалённый корень будущей системы. Используется для создания правильной символической ссылки в **&laquo;/usr/bin/&raquo;**.
* **TARGET** - название директории с самой программой.

Остальные переменные не рекомендуется менять каким-либо образом.

Если вам нужно изменить установочную директорию в системе - воспользуйтесь переменными *DESTDIR*, *POSTDIR* и *TARGET*. 

Например, я хочу установить программу в **&laquo;/opt/bwconvert/&raquo;**.

```bash
sudo make DESTDIR=/ POSTDIR=opt install
```

Для удаления программы в **Makefile** имеются соответствующие команды:

* uninstall - удалить пграмму.
* clear - очистить всё.

Если же вы хотите использовать способ установки с помощью **setup.py**, воспользуйтесь следующим методом.

С помощью следующей команды проверьте, что у вас установлена ​​актуальная версия setuptools.

```bash
Debian: $ sudo apt install python-virtualenv python3-virtualenv python3-venv virtualenv python3-virtualenvwrapper python-distlib python-filelock python-platformdirs python-stevedore
Archlinux: $ sudo pacman -S python-distlib python-filelock python-platformdirs python-stevedore python-virtualenv python-virtualenvwrapper
Python PIP: $ python -m pip install --upgrade pip setuptools virtualenv virtualenvwrapper --upgrade
```
Также клонируем репозиторий и переходим в него.


```bash
cd ~
git clone https://github.com/maximalisimus/bwconvert.git
cd bwconvert
```

Устанавливаем.

```bash
# Так
$ python setup.py install

# Или так
$ pip install .
```

Для сборки утилиты в 2 вида пакета - архив (скорее всего **.tar.gz**) со всеми необходимыми файлами и **.whl** файл для **PIP**-а, воспользутесь следующей командой.

```bash
# Сначала перейдите в каталог с репозиторием, если не перешли.
$ cd bwconvert

# Можно собирать.
$ python setup.py sdist bdist_wheel
```

В папке dist должны повится 2 соответствующих архива.

---

[К оглавлению](#Oglavlenie)

---

## <a name="ShowUtilites">2. Обзор утилиты.</a>

Помощь программы выглядит следующим образом (Параметры и ключи. Русифицикация.):

```bash
$ python bwconvert/bwconvert.py -h
usage: bwconvert.py [-h] [-v] [-info] [-j JSON] [-o OUTPUT]

Конвертер из Bitwarden json в csv для KeePassXC.

позиционные аргументы:
  JSON                  Входной json-файл экспортированной Bitwarden
                        база данных.

необязательные аргументы:
  -h, --help            показать справку и выйти
  -V, --version         Версия.
  -info, --info         Информация об авторе.
  -o OUTPUT, --output OUTPUT
                        Выходной csv-файл базы данных для KeepasXC.
```

При этом, если не вводить никаких ключей, пользователь автоматически перенаправляется на страницу помощи.

Ключ **&laquo;-o&raquo;** нужен если вы хотите изменить выходное имя файла и его местоположение в системе.

Без указания входного файла базы, которую необходимо конвертировать - работать не будет.

Посмотрим на пример использования. Допустим, мне не нравится такое длинное имя базы экспорта и я хочу его изменить.

Обратите внимание, что расширение файла указывать не обязательно - оно автоматически будет применено правильное.


```bash
$ python bwconvert/bwconvert.py ./bitwarden_export_20231011172535.json -o ./bitwarden_export
```

На выходе должен появится файл **&laquo;bitwarden_export.csv&raquo;**.

---

## <a name="about">3. Обо Мне</a>

<details>
	<summary>Подробнее ...</summary>
	
Автор данной разработки **Shadow**: [maximalisimus](https://github.com/maximalisimus).

Имя автора: **maximalisimus**: [maximalis171091@yandex.ru](mailto:maximalis171091@yandex.ru).

Дата создания: **02.10.2023**

</details>

---

[К оглавлению](#Oglavlenie)

---

## <a name="English">English README.</a>

Converter from Bitwarden json to csv for KeePassXC.

![Python-3](./image/python-3-icon.svg "Python 3") &nbsp;![Linux](./image/linux.svg "Linux") &nbsp;![Win-7](./image/win-7-icon.svg "Win-7") &nbsp;![Win-10](./image/win-10-icon.svg "Win-10")

## <a name="EngOglavlenie">Table of contents</a>

1. [Installation.](#SetupEng)
2. [Utility Overview.](#ShowUtilitesEng)
3. [About the author.](#AboutEng)

---

## <a name="SetupEng">1. Installation</a>

To install the program, use the following command using **Makefile**:

```bash
cd ~
git clone https://github.com/maximalisimus/bwconvert.git
cd bwconvert
sudo make DESTDIR=/ install
```

To control the installation, there are some variables in the **Makefile** that you could use.

* **DESTDIR** - location in the system, directory. By default, the root of the system is set.
* **POSTDIR** - the installation directory in front of the program folder, i.e. the parent directory of the program. By default, it is equal to **&laquo;usr/share&raquo;**. <u>Must be present. It is not allowed to set an empty one.</u>
* **INSTALLDIR** - the remote root of the future system. Used to create the correct symbolic link in **/usr/bin/**.
* **TARGET** - the name of the directory with the program itself.

It is not recommended to change the other variables in any way.

If you need to change the installation directory in the system, use the variables *DESTDIR*, *POSTDIR* and *TARGET*. 

For example, I want to install a program in **/opt/bwconvert/**.

```bash
sudo make DESTDIR=/ POSTDIR=opt install
```

To delete a program in the **Makefile** there are appropriate commands:

* uninstall - delete the program.
* clear - clear everything.

If you want to use the installation method using **setup.py**, use the following method.

Use the following command to check that you have the current version of setuptools installed.

```bash
Debian: $ sudo apt install python-virtualenv python3-virtualenv python3-venv virtualenv python3-virtualenvwrapper python-distlib python-filelock python-platformdirs python-stevedore
Archlinux: $ sudo pacman -S python-distlib python-filelock python-platformdirs python-stevedore python-virtualenv python-virtualenvwrapper
Python PIP: $ python -m pip install --upgrade pip setuptools virtualenv virtualenvwrapper --upgrade
```

We also clone the repository and go to it.


```bash
cd ~
git clone https://github.com/maximalisimus/bwconvert.git
cd bwconvert
```

Installing.

```bash
# Так
$ python setup.py install

# Или так
$ pip install .
```

To build the utility into 2 types of package - archive (most likely **.tar.gz**) with all the necessary files and **.whl** file for **PIP**, use the following command.

```bash
# First, go to the repository directory, if you haven't moved.
$ cd bwconvert

# You can collect.
$ python setup.py sdist bdist_wheel
```

2 corresponding archives should appear in the dist folder.

---

[To the table of contents](#EngOglavlenie)

---

## <a name="ShowUtilitesEng">2. Utility Overview.</a>

The program's help looks like this (Parameters and keys.):

```bash
$ python bwconvert/bwconvert.py -h
usage: bwconvert.py [-h] [-v] [-info] [-o OUTPUT] JSON

Converter from Bitwarden json to csv for KeePassXC.

positional arguments:
  JSON                  The input json file of the exported Bitwarden
                        database.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         Version.
  -info, --info         Information about the author.
  -o OUTPUT, --output OUTPUT
                        The output csv file of the database for KeepasXC.
```

At the same time, if you do not enter any keys, the user is automatically redirected to the help page.

The key **&laquo;-o&raquo;** is needed if you want to change the output file name and its location in the system.

Without specifying the input file of the database to be converted, it will not work.

Let's look at an example of usage. Let's say I don't like such a long name of the export database and I want to change it.

Please note that it is not necessary to specify the file extension - it will automatically be applied correctly.


```bash
$ python bwconvert/bwconvert.py ./bitwarden_export_20231011172535.json -o ./bitwarden_export
```

A file should appear at the output **&laquo;bitwarden_export.csv&raquo;**.

---

[To the table of contents](#EngOglavlenie)

---

## <a name="AboutEng">3. About the author.</a>


<details>
	<summary>More detailed ...</summary>

The author of this development **Shadow**: [maximalisimus](https://github.com/maximalisimus).

Author's name: **maximalisimus**: [maximalis171091@yandex.ru](mailto:maximalis171091@yandex.ru).

Date of creation: **02.10.2023**

</details>

---

[To the table of contents](#EngOglavlenie)

---
