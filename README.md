cd ~
# Создаем виртуальное окружение
virtualenv env
# Активируем виртуальное окружение
source env/scripts/activate
# Клонируем проект
git clone https://github.com/AlexanderVorobei/sparrow-courses-list.git
# Ставим необходимые модули
pip install -r requirements.txt
# Инициируем базу данных
flask db init
# Создаем миграцию БД
flask db migrate -m "courses table"
# Запускаем сервер
flask run
