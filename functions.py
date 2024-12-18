#functions - модуль для импорта функций

#TODO - добавить импорты внешних зависимостей
#import "название зависимостей"

import os
import shutil


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





def func2():
    pass

