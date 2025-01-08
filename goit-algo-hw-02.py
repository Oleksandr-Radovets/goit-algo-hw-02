
# Завдання 1.

import queue
import random
import time

# ствоорюєм чергу
request_queue = queue.Queue()

# рахунок для індифікаторів
request_id_counter = 1

#Створюєм нову заявку
def generate_request():
    global request_id_counter
    new_request = {"id": request_id_counter, "description": f"Request #{request_id_counter}"}
    request_queue.put(new_request)
    print(f"Generated: {new_request}")
    request_id_counter += 1

# Обробляєм заявку
def process_request():
    if not request_queue.empty():
        current_request = request_queue.get()
        print(f"Processing: {current_request}")
        time.sleep(1)  # Імітація часу обробки заявки
    else:
        print("Queue is empty, no requests to process.")

def main():
    try:
        while True:
            user_action = input("Enter 'g' to generate a request, 'p' to process a request, or 'q' to quit: ").lower()
            if user_action == "g":
                generate_request()
            elif user_action == "p":
                process_request()
            elif user_action == "q":
                print("Exiting the program.")
                break
            else:
                print("Invalid input. Please enter 'g', 'p', or 'q'.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")

if __name__ == "__main__":
    main()



# Завдання 2.

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