#main - стартовый мподуль проекта
# Коммит от Вероники

#импорт измодуля
from functions import group_photos_by_index, distribute_photos

#функция запуска импортированных функций
def main():
    base_folder = "/Users/polinakornienko/Downloads/drive-download-20241217T211138Z-001"
    group_photos_by_index(base_folder)

if __name__ == '__main__':
   main()