# Проект по тестированию API сайта "https://thinking-tester-contact-list.herokuapp.com/"
> <a target="_blank" href="https://thinking-tester-contact-list.herokuapp.com/">Ссылка на cайт</a>

## Список проверок
### <a href='https://github.com/evgeniili0322/contact-list-api-tests/blob/master/tests/test_users.py'>/users</a>
 - Проверка регистрации пользователя;
 - Проверка схемы ответа авторизаци;
 - Проверка тела ответа авторизации

### <a href='https://github.com/evgeniili0322/contact-list-api-tests/blob/master/tests/test_contacts.py'>/contacts</a>
 - Проверка схемы ответа создания контакта;
 - Проверка тела ответа создания контакта;
 - Проверка схемы ответа получения списка контактов;
 - Проверка тела ответа удаления контакта.

## Технoлoгии и инструмeнты
<p align="center">
<a href="https://www.python.org/"><img src="design/icons/python.svg" width="50" height="50"  alt="Python" title="Python"/></a>
<a href="https://docs.pytest.org/"><img src="design/icons/pytest.svg" width="50" height="50"  alt="PyTest" title="PyTest"/></a>
<a href="https://www.jenkins.io/"><img src="design/icons/jenkins.svg" width="50" height="50"  alt="Jenkins" title="Jenkins"/></a>
<a href="https://qameta.io/allure-report/"><img src="design/icons/allure.png" width="50" height="50"  alt="allure-report" title="allure-report"/></a>
<a href="https://qameta.io/allure-report/"><img src="design/icons/allure_testops.png" width="50" height="50"  alt="allure-report" title="allure-report"/></a>
<a href="https://www.atlassian.com/software/jira"><img src="design/icons/jira.png" width="50" height="50"  alt="allure-report" title="allure-report"/></a>
<a href="https://github.com/"><img src="design/icons/github.png" width="50" height="50"  alt="Github" title="Github"/></a>
<a href="https://web.telegram.org/"><img src="design/icons/telegram.png" width="50" height="50"  alt="Telegram" title="Telegram"></a>
</p>

# Запуск автотестов в Jenkins
#### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/007-eugene0322-unit24-api/">проект</a>
#### 2. Выбрать пункт "**Build Now**"
![This is an image](design/images/jenkins-job.png)
#### 3. Результат запуска сборки можно посмотреть в отчёте Allure
![This is an image](design/images/jenkins-allure.png)

## Запуск автотестов локально
### Создание виртуального окружения и установка зависимостей:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Запуск:

```bash
pytest tests
```
### Получение отчёта:
```bash
allure serve
```

## Allure Отчет
##### После прохождения тестов, результаты можно посмотреть в генерируемом Allure отчете.
![This is an image](design/images/jenkins-allure.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](design/images/allure-graphs.png)

##### Во вкладке Suites находятся собранные тест кейсы, у которых описаны шаги и добавлено тело ответа и curl запрос.
![This is an image](design/images/allure-suits.png)

# Интеграция с Allure TestOps и Jira
#### Результаты прохождения тестов, а также сами тест-кейсы будут отправлены в Allure TestOps
![This is an image](design/images/allure-testops.png)
#### Также на основе результатов прохождения тестов будет сгенерирован дашборд
![This is an image](design/images/allure-dashboard.png)
#### Все тест кейсы также могут быть прикреплены к задаче в Jira Software
![This is an image](design/images/jira.png)

# Настроено автоматическое оповещение о результатах сборки Jenkins в Telegram
![This is an image](design/images/telegram-bot-report.png)
