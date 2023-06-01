def palindrome(slovo):
    slovo = slovo.replace(' ', '').lower()
    reversed_slovo = slovo[::-1]
    if slovo == reversed_slovo:
        print('Слово є паліндромом')
    else:
        print('Слово не є паліндромом')

slovo = input('Введіть слово: ')
palindrome(slovo)