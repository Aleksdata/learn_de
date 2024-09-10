### Типы данных

Текст
char дополняет пробелами, varchar сохраняет как есть
экранирование в константе задается через $$

Например, для включения в константу символа новой строки нужно сделать так:
SELECT E'PGDAY\n17';

Вставка массива:
```sql
INSERT INTO pilots
VALUES ( 'Ivan', '{ 1, 3, 5, 6, 7 }'::integer[] ),
( 'Petr', '{ 1, 2, 5, 7 }'::integer[] ),
( 'Pavel', '{ 2, 5 }'::integer[] ),
( 'Boris', '{ 3, 5, 6 }'::integer[] );
```

Добавление элемента:
SET schedule = schedule || 7
SET schedule = array_append( schedule, 6 )
SET schedule = array_prepend( 1, schedule )

Remove:
SET schedule = array_remove( schedule, 5 )

SET schedule[ 1 ] = 2, schedule[ 2 ] = 3

Функция array_position возвращает индекс первого вхождения элемента с указанным значением в массив. 

Оператор @> означает проверку того факта, что в левом массиве содержатся все элементы правого массива. 

&&, который проверяет наличие общих элементов у массивов, т. е. пересекаются ли их множества значений.

unnest - перевод в столбец


json:
UPDATE pilot_hobbies
SET hobbies = hobbies || '{ "sports": [ "хоккей" ] }'
WHERE pilot_name = 'Boris';



Ограничения:
- check
- null
- unique
- primary key
- foreign key


- ON DELETE NO ACTION / RESTIRICT
Выдает ошибку если есть ссылающиеся записи на удаляемую, no action в рамках транзакции можно обработать позднее
- ON DELETE CASCADE
- ON DELETE SET NULL / SET DEFAULT (должно быть указано при создании таблицы)


Alter table:
Поскольку мы ввели в обращение числовые коды для классов обслуживания, то
необходимо модифицировать определение таблицы «Места», а именно: тип данных столбца «Класс обслуживания» (fare_conditions) изменить с varchar(10) на
integer. Для реализации такой задачи служит фраза USING команды ALTER TABLE.
Однако такой вариант команды не сработает:
```sql
ALTER TABLE seats
ALTER COLUMN fare_conditions SET DATA TYPE integer
USING ( CASE WHEN fare_conditions = 'Economy' THEN 1
WHEN fare_conditions = 'Business' THEN 2
ELSE
```


Представления
Materialized
- Можно создавать с командой with no data
- Для обновления используется команда Refresh materialized view
- Не сохраняет данные


Схема образует так называемое пространство
имен.