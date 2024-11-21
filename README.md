# isrpo4 unittest

Gusev Anton Olegovich M3103 465692

Таблица результатов тестировки:
| Название теста                     | Входные данные                     | Результат работы программы | Статус теста  |
|------------------------------------|------------------------------------|----------------------------|----------------|
| test_circle_area                   | 0                                  | -1                         | Пройден        |
| test_circle_area                   | -100                               | -1                         | Пройден        |
| test_circle_area                   | 4                                  | 50.2654824574              | Пройден        |
| test_circle_area                   | 1                                  | 3.141592653589793          | Пройден        |
| test_circle_perimeter              | 0                                  | -1                         | Пройден        |
| test_circle_perimeter              | -100                               | -1                         | Пройден        |
| test_circle_perimeter              | 3                                  | 18.8495559215              | Пройден        |
| test_circle_perimeter              | 0.5                                | 3.141592653589793          | Пройден        |
| test_rectangle_area                | 0, 100                             | -1                         | Пройден        |
| test_rectangle_area                | -100, 7                           | -1                         | Пройден        |
| test_rectangle_area                | 4, 9                               | 36                         | Пройден        |
| test_rectangle_area                | 1, 1000                            | 1000                       | Пройден        |
| test_rectangle_perimeter           | 0, 100                             | -1                         | Пройден        |
| test_rectangle_perimeter           | -100, 7                           | -1                         | Пройден        |
| test_rectangle_perimeter           | 4, 9                               | 26                         | Пройден        |
| test_rectangle_perimeter           | 0.5, 3                             | 7                          | Пройден        |
| test_square_area                   | 0                                  | -1                         | Пройден        |
| test_square_area                   | -100                               | -1                         | Пройден        |
| test_square_area                   | 4                                  | 16                         | Пройден        |
| test_square_area                   | 7                                  | 49                         | Пройден        |
| test_square_perimeter              | 0                                  | -1                         | Пройден        |
| test_square_perimeter              | -100                               | -1                         | Пройден        |
| test_square_perimeter              | 5                                  | 20                         | Пройден        |
| test_square_perimeter              | 7                                  | 28                         | Пройден        |
| test_triangle_area                 | 7, 0                               | -1                         | Пройден        |
| test_triangle_area                 | 9, -100                            | -1                         | Пройден        |
| test_triangle_area                 | 4, 7                               | 14                         | Пройден        |
| test_triangle_area                 | 3, 9                               | 13.5                       | Пройден        |
| test_triangle_perimeter            | 7, 5, 0                            | -1                         | Пройден        |
| test_triangle_perimeter            | 9, 13, -100                        | -1                         | Пройден        |
| test_triangle_perimeter            | 4, 7, 5                            | 16                         | Пройден        |
| test_triangle_perimeter            | 3, 5, 3                            | 11                         | Пройден        |
| test_triangle_is_valid             | 2, 5, 3                            | False                      | Пройден        |
| test_triangle_is_valid             | 3, 5, 3                            | True                       | Пройден        |
| test_triangle_is_valid             | 10, 15, 23                         | True                       | Пройден        |
| test_triangle_is_valid             | 25, 11, 13                         | False                      | Пройден        |
# История коммитов

### Коммит 49849fa405a3b0a575986c03694e9a64d5d3cd71
- **Автор:** Anton <465692@niuitmo.ru>
- **Дата:** 21 ноября 2024, 01:16:28 (UTC+3)
- **Сообщение:** Добавлены тесты и внесены изменения в библиотеку геометрии.

### Коммит 06b509657dc7b97c99847d4e703c4de897e5aecb
- **Автор:** Anton <465692@niuitmo.ru>
- **Дата:** 21 ноября 2024, 00:48:21 (UTC+3)
- **Сообщение:** Добавлен файл `geometric_lib.py`.

### Коммит 7f1e88b53edfdbe661cf08896fafc57d360f683e
- **Автор:** Anton Gusev <115722265+Zuneve@users.noreply.github.com>
- **Дата:** 20 ноября 2024, 23:57:45 (UTC+3)
- **Сообщение:** Начальный коммит.

