import os
import shutil

def group_photos_by_index(folder_path):
    """
    Группирует фотографии из подпапок по индексу.
    Возвращает словарь, где ключи — индексы групп, а значения — списки путей к файлам.
    """
    grouped_photos = {}

    # Получаем список подпапок
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    subfolders.sort()  # Сортируем папки

    for subfolder in subfolders:
        subfolder_path = os.path.join(folder_path, subfolder)

        # Получаем изображения в подпапке
        images = sorted(
            [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]
        )

        for index, image in enumerate(images):
            if index not in grouped_photos:
                grouped_photos[index] = []
            grouped_photos[index].append(os.path.join(subfolder_path, image))

    return grouped_photos

def distribute_photos(base_folder):
    """
    Создаёт новые папки в каждой из основных папок (например, А, Б, В) и распределяет туда фотографии.
    """
    # Получаем список всех основных папок
    main_folders = [f for f in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, f))]
    main_folders.sort()  # Сортируем основные папки

    for main_folder in main_folders:
        main_folder_path = os.path.join(base_folder, main_folder)

        # Группируем фотографии по индексу
        photo_groups = group_photos_by_index(main_folder_path)

        # Создаём новые папки и распределяем фотографии
        for group_index, photos in photo_groups.items():
            # Создаём новую папку для группы
            group_folder = os.path.join(main_folder_path, f"new_{group_index + 1}")
            os.makedirs(group_folder, exist_ok=True)  # Создаём папку, если её ещё нет

            for photo_index, photo_path in enumerate(photos):
                # Генерируем новое имя файла
                new_name = f"{photo_index + 1}_{os.path.basename(photo_path)}"
                new_path = os.path.join(group_folder, new_name)
                shutil.copy(photo_path, new_path)  # Копируем файл

