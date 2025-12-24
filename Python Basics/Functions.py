def calc_expenses(expense):
    total=0
    for item in expense:
        total=total+item
    return total;

luv_exp_list=[2200,2340,2560,5590]
dhruv_exp_list=[123, 3456, 678, 128]

luv_exp=calc_expenses(luv_exp_list)
dhruv_exp=calc_expenses(dhruv_exp_list)

print(luv_exp)
print(dhruv_exp)

def sum(a,b):
    return a+b

n=sum(5, 6)
print(n)    