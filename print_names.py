print("Testing Jenkins! Hello from your student Tursynkhan XD")

import sys

def main():
    # Проверяем, переданы ли аргументы (имена)
    if len(sys.argv) < 2:
        print("Не указаны имена. Пожалуйста, передайте хотя бы одно имя как аргумент.")
        sys.exit(1)
    
    # Обрабатываем каждое переданное имя
    for name in sys.argv[1:]:
        print(f"Привет, {name}!")

if __name__ == '__main__':
    main()
