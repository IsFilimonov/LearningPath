6. Операционные системы lite
============================

+---------------------+----------------------------------+
| Ограничение времени | 1 секунда                        |
+---------------------+----------------------------------+
| Ограничение памяти  | 64Mb                             |
+---------------------+----------------------------------+
| Ввод                | стандартный ввод или input.txt   |
+---------------------+----------------------------------+
| Вывод               | стандартный вывод или output.txt |
+---------------------+----------------------------------+

Васин жесткий диск состоит из M секторов. Вася последовательно устанавливал на него различные операционные системы следующим методом: он создавал новый раздел диска из последовательных секторов, начиная с сектора номер :math:`a_i` и до сектора :math:`bi` включительно, и устанавливал на него очередную систему. При этом, если очередной раздел хотя бы по одному сектору пересекается с каким-то ранее созданным разделом, то ранее созданный раздел «затирается», и операционная система, которая на него была установлена, больше не может быть загружена.

Напишите программу, которая по информации о том, какие разделы на диске создавал Вася, определит, сколько в итоге работоспособных операционных систем установлено и работает в настоящий момент на Васином компьютере.

Формат ввода
------------

Сначала вводятся натуральное число M — количество секторов на жестком диске (:math:`≤ M ≤ 109``) и целое число N — количество разделов, которое последовательно создавал Вася (:math:`≤ N ≤ 1000``).

Далее идут N пар чисел :math:`a_i` и :math:`b_i`, задающих номера начального и конечного секторов раздела (:math:`1 ≤ ai ≤ bi ≤ M`).

Формат вывода
-------------- 

Выведите одно число — количество работающих операционных систем на Васином компьютере.

Пример 1
--------

**Ввод**:

.. include:: in_1.txt
   :literal:

**Вывод**:

.. include:: out_1.txt
   :literal:

Пример 2
--------

**Ввод**:

.. include:: in_2.txt
   :literal:

**Вывод**:

.. include:: out_2.txt
   :literal:
