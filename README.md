# polyomino_test

### Ручной запуск:
В файле `data.txt` указываем данные из 3 строк:
1. Размер стола
2. Массив прямоугольных полиомино
3. Массив П-полиомино
```пример
(4, 6)
[((2, 2), 2)]
[((3, 4), 1), ((2, 3), 1)]
```
Запускаем
```
python3 main.py < data.txt
```

### Запуск тестов
Должно хватить запуска скрипта `run.sh`
Возможно ему потребуются права на исполнение.
Скрипт создаст виртуальную среду, установит туда `pytest` и заупустит тесты
```
chmod +x run.sh
./run.sh
```
