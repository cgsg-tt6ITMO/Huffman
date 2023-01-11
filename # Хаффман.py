# FILENAME:     "Хаффман.py"
# PROGRAMMER:   Troitskaya Tamara, isu: 368924, ITMO University
# LAST UPDATE:  31.12.2022
# PURPOSE:      Laba # 1. Huffman's algorithm realisation.

# вспомогательные функции

# функция поиска элемента в двумерном массиве
def ind(element, arr):
  for i in range(len(arr)):
    for j in range(len(arr[len(arr)-1])):
      if element == arr[i][j]:
        return i
  return (-1)


# функция разворота строки
def inversed(s):
    res=""
    for i in range(len(s)-1,-1,-1):
        res = res + s[i]
    return res


# перевод из двоичного кода в символ (bin -> str)
def bin_to_char(s):
  a = int(s, 2)
  return chr(a)


# считывание входных данных из файла
f = open("Z:/Huffman/input.txt")
inp = ""
for i in f:
  inp += i
f.close()

# выписываем все символы алфавита
abc = []
for i in inp:
  if i not in abc:
    abc.append(i)

# выписываем частоты для каждого символа
ver = []
for i in abc:
  ver.append(inp.count(i))

# создаём удобный для сортиовки массив
m = []
for i in range(len(abc)):
  m.append([ver[i], abc[i]])
m.sort()
print(m)

# создаём первичный массив инвёрснутых кодов
codes = [[m[_][1]]for _ in range(len(m))]

"""
смысл алгоритма: берём 2 первых элемента. для них присваиваем 0, 1 и потом изменяем массив m и сортируем его снова
"""
while len(m) > 1:
  # самый редкий элемент имеет самый длинный код
  l = [_ for _ in m[0][1]]
  for i in l:
    ind1 = ind(i, codes)
    codes[ind1].append("0")
  # второй по редкости элемент
  l = [_ for _ in m[1][1]]
  for i in l:
    ind2 = ind(i, codes)
    codes[ind2].append("1")
  # сокращаем длину массива m
  newel = m[0][1]+m[1][1]
  newver = m[0][0]+m[1][0]
  m[1][0] = newver
  m[1][1] = newel
  m.pop(0)
  m.sort()

# финальный массив кодов - словарь ключей
table = []
for i in codes:
  s = ""
  for j in range(1, len(i)):
    s = s + i[j]
  table.append([i[0], inversed(s)])
print(table)

# каждый символ заменяем на его код
bin_res = ""
for i in inp:
  bin_res += table[ind(i, codes)][1]

# разбиваем строку из {0,1} на блоки по 8 цифр и присваиваем символ. типо сжатие
zashifrovannoe = ""
for i in range(0, len(bin_res), 8):
  b = bin_to_char(bin_res[i:i+8])
  zashifrovannoe += b
print(zashifrovannoe)

# записываем результат в файл
fname = "Z:/Huffman/output.txt"
with open(fname, "w", encoding="utf-8") as f:
  # размер словаря
  f.write("dictionary size: " + str(len(table)))
  f.write('\n')
  # сам словарь
  for i in table:
    f.write(str(i))
  f.write('\n')
  # зашифрованный текст
  for i in zashifrovannoe:
    f.write(i)
  f.close()

# END OF "Хаффман.py" FILE
