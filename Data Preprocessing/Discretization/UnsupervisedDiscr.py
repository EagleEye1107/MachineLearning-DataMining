

def EqualIntervalsDiscr(list, k):
    list.sort()
    a = (list[-1] - list[0]) / k

    classes = {}
    b = list[0]
    for i in range(k):
        if i == k-1 :
            classes[f'classe-{i}'] = f'[{b}, {b + a}]'
        else:
            classes[f'classe-{i}'] = f'[{b}, {b + a}['
        b = b + a
    return classes


def EqualFreqDiscr(list, k):
    list.sort()
    m = round(len(list) / k)

    classes = {}
    b = 0
    for i in range(k):
        if i == k-1 :
            classes[f'classe-{i}'] = f'[{list[b]}, {list[-1]}]'
        else:
            classes[f'classe-{i}'] = f'[{list[b]}, {list[b + m]}['
        b = b + m
    return classes


list1 = [75, 64, 83, 65, 68, 72, 69, 70, 85, 71, 72, 75, 80, 81]


print(EqualIntervalsDiscr(list1, 3))
print(EqualFreqDiscr(list1, 3))