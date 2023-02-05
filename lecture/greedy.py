def fun1 (string:str) :
    li = list(map(int, string))
    result = 1
    for i in li:
        if i <= 1 :
            result += i
        else:
            result *= i
    return result
# print(fun1("02984"))

def fun2 (num:int, str_li:str):
    li = list(map(int, str_li.split()))
    li = sorted(li)
    result = 0
    while len(li) != 0:
        pop_num = li[-1]
        print(pop_num)
        if len(li) < pop_num:
            break
        else:
            line = len(li) - pop_num
            del li[line:]
            print(li)
            result += 1
    return result
print(fun2(5, "2 3 1 2 2"))
#
# list1 = [2, 3, 1, 2, 2]
# num = 1
# del list1[-1 : -2]
# print(list1)

def fun2_example (num:int, str_li:string):
    li = list(map(int, str_li.split()))
    li.sort()

    result = 0
    count = 0
    for i in li:
        count += 1
        if count >= i:
            result += 1
            count = 0
    return result