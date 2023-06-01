def filter_python_strings(strings):
    python_strings = [string for string in strings if "Python" in string]
    return python_strings
input_strings = input('Введіть рядки: ').split()
filtered_strings = filter_python_strings(input_strings)

print('Список рядків що містять слово Python: ')
for string in filtered_strings:
    print(string)
