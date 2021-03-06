# Задача 7. Канторово множество
# Определим числовые множества   следующим образом:
# пусть   Разделим сегмент   на три части точками   и удалим из него интервал  .
# Получим  множество   состояшащее из  двух сегментов    Для того, чтобы построить
# множество   каждый из этих  числовых сегментов снова разделим на три части.
# Точками   - первый сегмент, и точками   – второй сегмент, и снова удалим
# средние интервалы  , и так далее. Таким образом, если числовое множество
# уже построено, для построения множества  поделим каждый из сегментов
# на 3 равных части и удалим средние части.
# Написать программу, которая определяет принадлежность точки числовой оси с
# координатой   множеству    – положительные целые числа.


def in_cantor_set(a: int, b: int):
    R = []
    D = []

    p = 3
    k = 0
    c = p * a

    R.append(int(c / b))
    D.append(c % b)

    while True:
        k += 1
        c = p * D[k - 1]
        R.append(int(c / b))
        D.append(c % b)
        j = 0
        while D[j] != D[k]:
            j += 1
        if j < k:
            break
    print()
    for j in range(k):
        print(D[j], " ", R[j], "--")
    R.append(1)
    j = 0
    while R[j] != 1:
        j += 1
    return j == k + 1


if __name__ == "__main__":
    print("A= ", end="")
    a = int(input())
    print("B= ", end="")
    b = int(input())

    if in_cantor_set(a, b):
        print("YES")
    else:
        print("NO")
