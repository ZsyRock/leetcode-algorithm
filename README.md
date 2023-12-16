# leetcode-algorithm
algorithms I used when doing leetcode questions
1.Reverse:
A.Use reverse function directly:
Or
reversed_list = list(reversed(original_list))
B.Algorithm method:
for item in original_list:
    reversed_list.insert(0, item) ##Grammer: list.insert(index, element)
C.Algorithm method2:
reversed_list = my_list[::-1]
