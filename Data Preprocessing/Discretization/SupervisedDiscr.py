
def SupervisedDiscr(list, n):
    list.sort()

    # Step-1 : pre-division into as many intervals as there is a class change. 
    i = 0
    while list[i] != list[-1]:
        if list[i][1] != list[i+1][1] :
            list.insert(i+1, '/')
            i += 2
        else :
            i += 1
    
    # Step-2 : 
    i = 0
    cpt_y = 0
    cpt_n = 0
    to_delete = []
    
    while i != len(list) - 1 :
        while list[i] != '/' :
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


    return list


list1 = [[75, 'Y'], [64, 'Y'], [83, 'Y'], [65, 'N'], [68, 'Y'], [72, 'Y'], [69, 'Y'], [70, 'Y'], [85, 'N'], [71, 'N'], [72, 'N'], [75, 'Y'], [80, 'N'], [81, 'Y']]

print(SupervisedDiscr(list1, 3))