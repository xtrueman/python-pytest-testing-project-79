### Hexlet tests and linter status:
[![Actions Status](https://github.com/xtrueman/python-pytest-testing-project-79/workflows/hexlet-check/badge.svg)](https://github.com/xtrueman/python-pytest-testing-project-79/actions)

PageLoader – утилита командной строки, которая скачивает страницы из интернета и сохраняет их на компьютере. Вместе со страницей она скачивает все ресурсы (картинки, стили и js) давая возможность открывать страницу без интернета.  
  
Пример использования:

    page-loader -o /var/tmp https://ru.hexlet.io/courses

    INFO:root:requested url: https://ru.hexlet.io/courses
    INFO:root:output path: /var/tmp
    INFO:root:write html file: /var/tmp/ru-hexlet-io-courses.html
    INFO:root:create directory for assets: /var/tmp/ru-hexlet-io-courses_files
    Downloading: |████████████████████████████████| 100.0% (eta: 0)
    Page was downloaded as '/var/tmp/ru-hexlet-io-courses.html'  

Утилита скачивает ресурсы и показывает прогресс в терминале.  
