
Здравствуйте,

Размещаю ответы на Ваши задания:

1. В файле is_even.py представлена функция определения четности через перевод в двоичное исчисление.
При проверке timeit исходный код показал себя в 2 раза лучше.

2. В файлах circularbuffer1.py и circularbuffer2.py представлены реализации циклического буфера FIFO.
Оба реализованы с использованием словарей, т.к. они в отличии от списков выполняют запись, поиск, чтение и удаление по ключу за О(1).
Отличие в действии при переполнении. Первый перезаписывает новый элементы поверх старых. ВТорой пропускает элементы и дожидается освобождения буфера.
В целом очереди и стеки реализованы в модуле collections.

3. В файле mergesort.py приведена реализация алгоритма "Сортировка слиянием".
Алгоритм выбран из-за худшего и лучшего времени O(nlog(n)) и требуемой памяти O(n).
Лучший алгоритм (Timsort) реализован на C в методе sort языка Python.