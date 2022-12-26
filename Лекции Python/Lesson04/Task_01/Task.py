# Задача 1
# Идея: совместная разработка
# 
# Система собирает информацию с датчиков, в ней есть 
# модуль логирования, который заносит в журнал все 
# обращения к датчикам. 
# В системе есть модуль, выполняющий обращения для 
# получения данных с датчиков и модуль генерации html-представления.
# Запуск системы осуществляется из головного модуля.

# Модуль 1: сбор информации с датчиков    - data_provider
#                                           - get_temperature, get_pressure, get_wind_speed
# Модуль 2: логирование                   - logger
#                                           - temperature_logger, pressure_logger, wind_speed_logger
# Модуль 3: UI                            - user_interface
#                                           - temperature_view, pressure_view, wind_speed_view
# Модуль 4: HTML-генератор                - html_creater
#                                           - create
# Модуль 5: главный модуль                - main
#                                           - кнопка запуска

