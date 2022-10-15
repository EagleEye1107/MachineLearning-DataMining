'''
    IMPORTANT note : this version of supervised discretization is not optimized
    because it's for educational purposes to be able to understand each step of the method when implemented manually on benchmarks
'''

def SupervisedDiscr(list, n):
    # Step-0 : Sort our list
    list.sort()

    # Step-1 : Pre-division into as many intervals as there is a class change. Separator -> /######/
    i = 0
    while list[i] != list[-1]:
        if list[i][1] != list[i+1][1] :
            list.insert(i+1, '/######/')
            i += 2
        else :
            i += 1
    
    # Step-2 : If we have same value X in different intervals, we remove the separators between these intervals
    # to have the values of X in the same interval
    i = 1
    while i != len(list) - 2 :
        if list[i] == '/######/':
            if list[i-1][0] == list[i+1][0]:
                list.pop(i)
        i += 1
    
    # Step-3 : Grouping of intervals such that there are at least n values of the same class in each interval
    i = 0
    cpt_y = 0
    cpt_n = 0
    while i != len(list) - 1 :
        while list[i] != '/######/' :
            if list[i][1] == 'Y' :
                cpt_y += 1
            elif list[i][1] == 'N' :
                cpt_n += 1
            i += 1
        if cpt_y < n and cpt_n < n :
            list.pop(i)
        else :
            cpt_y = 0
            cpt_n = 0
            i += 1
    
    # Step-4 : Grouping of adjacent intervals gaving the same majority class
    i = 0
    cpt_y = 0
    cpt_n = 0
    posToDelete = 0
    majClass0 = ''
    while i <= len(list) - 1 :
        while list[i] != '/######/' :
            if list[i][1] == 'Y' :
                cpt_y += 1
            elif list[i][1] == 'N' :
                cpt_n += 1
            i += 1
            if i == len(list) : 
                break
        if cpt_y > cpt_n:
            if majClass0 == '' :
                posToDelete = i
                majClass0 = 'Y'
            elif majClass0 == 'Y':
                list.pop(posToDelete)
                i -= 1
                posToDelete = i
            elif majClass0 == 'N':
                majClass0 = 'Y'
        else:
            if majClass0 == '' :
                posToDelete = i
                majClass0 = 'N'
            elif majClass0 == 'N':
                list.pop(posToDelete)
                i -= 1
                posToDelete = i
            elif majClass0 == 'Y':
                majClass0 = 'N'
        cpt_y = 0
        cpt_n = 0
        i += 1
    
    # Step-5 : final intervals
    i = 0
    k = 0
    a = 0
    classes = {}
    while i <= len(list) - 2 :
        if list[i] == '/######/':
            a = ( list[i-1][0] + list[i+1][0] ) / 2
            classes[f'classe-{k}'] = f'<= {a}'
            k += 1
        i += 1
    classes[f'classe-{k}'] = f'> {a}'
    
    # return list
    return classes


list1 = [[75, 'Y'], [64, 'Y'], [83, 'Y'], [65, 'N'], [68, 'Y'], [72, 'Y'], [69, 'Y'], [70, 'Y'], [85, 'N'], [71, 'N'], [72, 'N'], [75, 'Y'], [80, 'N'], [81, 'Y']]

print(SupervisedDiscr(list1, 3))