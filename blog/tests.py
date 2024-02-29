from django.test import TestCase

lst=[1,2,3,4,5,6,7,8,9]
num=4
def paginator(lst_numbers, n):
    lst2 = []
    for i in range(lst_numbers,n):
        lst2.append(lst2[i:i+n])
print(paginator(lst,num))
#[[1,2,3,4],[5,6,7,8],[9]]

