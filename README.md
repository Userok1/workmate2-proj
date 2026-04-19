# workmate2-proj

## CLI приложение для обработки данных из Youtube

Для использования приложения склонируйте репозиторий:
```terminal
git clone https://github.com/Userok1/workmate2-proj.git
```
Перейдите в папку проекта и создайте виртуальное окружение и активируйте его:
Для Linux/MacOS:
```terminal
python3 -m venv .venv
source .venv/bin/activate
```
Для Windows:
```terminal
python -m venv .venv
.venv/Scripts/activate
```

Установите зависимости с помощью pip, предварительно активировав виртуальное окружение:
```terminal
pip install -r requirements.txt
```
Пример запуска приложения:
<img width="2242" height="1140" alt="scrn" src="https://github.com/user-attachments/assets/cdb50967-0b78-448e-88b1-820791c1634a" />

Запуск тестов проекта:
```terminal
pytest
```
Покрытие тестами:
<img width="3070" height="906" alt="tests" src="https://github.com/user-attachments/assets/ba8c61b2-6ed5-495e-9339-c9afe9a76f24" />

Для запуска линтера и форматера используйте следующие команды соответственно:
```terminal
make check-fix
make format
```
