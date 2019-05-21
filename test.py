array = []
user_input = input("separate numbers with comma: ").strip()

array = [int(item) for item in user_input.split(',')]

print(array)