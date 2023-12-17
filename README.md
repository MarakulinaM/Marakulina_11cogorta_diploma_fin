# Marakulina_11cogorta_diploma_fin

Автоматизирован следующий сценарий в приложении Яндекс Самокат:
Клиент создает заказ.
Проверяется, что по треку заказа можно получить данные о заказе.

Для коррекной работы кода и запуска автотеста необходимо:
- во вкладке Python Packages в поисковой строке набрать Pytest и нажать Install.
- в этой же вкладке (Python Packages) в поисковой строке набрать requests. В списке выбрать пакет requests, нажать Install.

В проекте используются следующие переменные/ручки/функции:

- URL_SERVICE - ссылка на сервер приложения Яндекс.Самокат;

- CREATE_ORDER - ручка для создания заказа;

- CHECK_ORDER_TRACK - ручка проверки поиска заказа по трек-номеру;

- def create_track() - функция создания заказа;

- def get_track() - функция получения трек-номера заказа; ВАЖНО!!! Трек-номер выдается в виде числа, его нужно преобразовать в строку!

- def check_order() - функция поиска заказа по трек-номеру заказа.

В файле configuration.py:
- в переменной URL_SERVICE должна быть указана актуальная ссылка на сервер приложения Яндекс.Самокат.
- в переменных CREATE_ORDER (создание заказа) и CHECK_ORDER_TRACK (получение информации о заказе по его номеру) необходимо перепроверить запрос к api.

В файле data.py указаны необходимые для создания заказа данные. 

В файл sender_stand_request.py включены функции:
- по созданию заказа - def create_track();
- по получению трек-номера заказа - def get_track();
- по поиску заказа по трек-номеру - def check_order();

В файле check_order_track_test.py прописан автотес для проверки поиска заказа по трек-номеру - def test_check_order_track().
Для запуска автотеста необходимо:
В поле выбора конфигурации выбрать пункт Edit Configurations.
В открывшемся окне нажать значок «+» (Add New Configuration).
В списке конфигураций выбрать Python tests → pytest.
В открывшемся окне в строке Target выберать пункт Custom.
Нажать кнопку Apply, а затем OK.
Потом запустить конфигурацию pytest с помощью зелёной стрелки.


Решение задач по SQL запросам размещено в файле SQL_requests
