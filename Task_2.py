from collections import deque

def is_palindrome(s):
    # Видаляємо пробіли, переводимо рядок у нижній регістр і залишаємо тільки алфавітні символи
    clean_string = ''.join(char.lower() for char in s if char.isalnum())

    # Створюємо двосторонню чергу
    char_deque = deque(clean_string)

    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False  # Не є паліндромом

    return True  # Є паліндромом

# Приклади використання

print(is_palindrome("madam"))  # True
print(is_palindrome("level"))  # True
print(is_palindrome("noon"))   # True
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("Hello"))  # False