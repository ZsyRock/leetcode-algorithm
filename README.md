# leetcode-algorithm
algorithms I used when doing leetcode questions
1.Reverse:
A.Use reverse function directly:
original_list = [1, 2, 3, 4, 5]
original_list.reverse()
print(original_list)
Or
A1. 
original_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(original_list))
print(reversed_list)
B.Algorithm method:
original_list = [1, 2, 3, 4, 5]
reversed_list = []
for item in original_list:
    reversed_list.insert(0, item) ##Grammer: list.insert(index, element)
print(reversed_list)
C.Algorithm method2:
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)  # 输出 [5, 4, 3, 2, 1]
