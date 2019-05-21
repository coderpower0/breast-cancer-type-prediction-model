from function import some_fun

array = []
user_input = input("separate numbers with comma: ").strip()

array = [int(item) for item in user_input.split(',')]

print(array, some_fun())