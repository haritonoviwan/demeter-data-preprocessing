import os

# Папка, в которой находятся файлы .DAT
folder_path = r' '

# Имена файлов с расширением .DAT
dat_files = [f for f in os.listdir(folder_path) if f.endswith('.DAT')]

# Имя выходного файла
output_file = os.path.join(folder_path, 'combined_output.DAT')  # Сохраняем в ту же папку

# Открываем выходной файл для записи в бинарном режиме
with open(output_file, 'wb') as outfile:
    for dat_file in dat_files:
        file_path = os.path.join(folder_path, dat_file)
        # Открываем каждый .DAT файл в бинарном режиме
        with open(file_path, 'rb') as infile:
            # Читаем и записываем содержимое файла побайтово
            outfile.write(infile.read())
            print(f'{dat_file} успешно объединён.')

print(f'Все файлы объединены в {output_file}.')