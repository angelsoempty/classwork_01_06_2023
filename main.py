def filter_capitalized_strings(strings):
    capitalized_strings = [string for string in strings if string[0].isupper()]
    return capitalized_strings

input_strings = input("Введіть рядки: ").split()
filtered_strings = filter_capitalized_strings(input_strings)

print("Список рядків що починаються з великої літери: ")
for string in filtered_strings:
    print(string)
