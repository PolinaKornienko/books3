#functions - модуль для импорта функций

#TODO - добавить импорты внешних зависимостей
#import "название зависимостей"

import os
import shutil

def distribute_photos(base_folder):
    """
    Создаёт новые папки в каждой из основных папок (А, Б, В, Г) и распределяет туда фотографии.
    """
    # Получаем список всех основных папок (А, Б, В, Г)
    main_folders = [f for f in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, f))]
    main_folders.sort()

    for main_folder in main_folders:
        main_folder_path = os.path.join(base_folder, main_folder)

        # Группируем фотографии по их индексу
        photo_groups = group_photos_by_index(main_folder_path)

        # Создаём новые папки и распределяем фотографии
        for group_index, photos in photo_groups.items():
            group_folder = os.path.join(main_folder_path, f"new_{group_index + 1}")
            if not os.path.exists(group_folder):
                os.makedirs(group_folder)

            for photo_index, photo_path in enumerate(photos):
                # Генерируем новое имя файла
                new_name = f"{photo_index + 1}_{os.path.basename(photo_path)}"
                new_path = os.path.join(group_folder, new_name)
                shutil.copy(photo_path, new_path)
                
def group_photos_by_index(base_folder):
    """
    Группирует фотографии из подпапок каждой основной папки (А, Б, В, Г) по индексу.
    Возвращает словарь, где ключи — индексы групп, а значения — списки путей к файлам.
    """
    grouped_photos = {}

    # Получаем список подпапок (1, 2, 3)
    subfolders = [f for f in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, f))]
    subfolders.sort()

    for subfolder in subfolders:
        subfolder_path = os.path.join(base_folder, subfolder)
        images = sorted(
            [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]
        )

        for index, image in enumerate(images):
            if index not in grouped_photos:
                grouped_photos[index] = []
            grouped_photos[index].append(os.path.join(subfolder_path, image))

    return grouped_photos