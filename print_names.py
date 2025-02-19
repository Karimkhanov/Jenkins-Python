# print("Testing Jenkins! Hello from your student Tursynkhan XD")

import sys

def main():
    # Проверяем, переданы ли аргументы (имена)
    if len(sys.argv) < 2:
        print("No names are specified. Please pass at least one name as an argument.")
        sys.exit(1)
    
    # Обрабатываем каждое переданное имя
    for name in sys.argv[1:]:
        print(f"Hello, {name}!")

if __name__ == '__main__':
    main()
