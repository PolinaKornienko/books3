#main - стартовый мподуль проекта
# Коммит от Вероники

#импорт измодуля
from functions import group_photos_by_index, distribute_photos

#функция запуска импортированных функций
def main():
    base_folder = "/Users/polinakornienko/envs/books3/data"
    distribute_photos(base_folder)

if __name__ == '__main__':
    main()


   