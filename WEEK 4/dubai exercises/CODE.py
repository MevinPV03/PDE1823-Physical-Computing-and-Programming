#Q1 – String Slicing (‘put’)

word = "computing"
print(word[3:6])

#Q2 – Find nth Largest Element

def find_n_max(lst, n):
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[n - 1]

mylist = [30, 21, 16, 66, 78, 109, 1, 4, 52]

nth_max = find_n_max(mylist, 3)
print("3rd largest element:", nth_max)

#Q3 – Tuple Unpacking

tup = (1, 3, 5, 7)

a, b, c, d = tup

print(a, b, c, d)

#Q4 – Square Values in Tuple

tup = (1, 3, 5, 7)

new_tup = tuple(x**2 for x in tup)

print(new_tup)

#Q5 – Multiply Tuple Elements by Index

L = [(2, 4, 6), (1, 3, 5), (10, 20, 30)]

result = [tuple(x * i for x in t) for i, t in enumerate(L)]

print(result)

#Q6 – Multiply Two Lists (Nested Loops)

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

for x in list1:
    for y in list2:
        print(f"{x} * {y} = {x * y}")

#Q7 – Check Balanced Brackets

def check_balance(brackets):
    count = 0

    for bracket in brackets:
        if bracket == "[":
            count += 1
        elif bracket == "]":
            count -= 1

        if count < 0:
            return False

    return count == 0

print(check_balance("[[[]]]"))   # True
print(check_balance("[[][]]"))   # True
print(check_balance("[[]"))      # False
print(check_balance("][]["))     # False
print(check_balance(""))         # True