import os
import shutil


class FileManager:
    def __init__(self, base_dir):
        self.base_dir = os.path.abspath(base_dir)
        self.current_dir = self.base_dir

    def list_dir(self):
        try:
            return os.listdir(self.current_dir)
        except Exception as e:
            return f'Ошибка при попытке просмотра директории: {e}'

    def change_dir(self, path):
        try:
            new_dir = os.path.abspath(os.path.join(self.current_dir, path))
            if not os.path.exists(new_dir):
                return "Указанная директория не существует."
            if new_dir.startswith(self.base_dir):
                self.current_dir = new_dir
                return f"Перешел в директорию {self.current_dir}"
            else:
                return "Выход за пределы рабочей директории запрещен."
        except Exception as e:
            return f"Ошибка смены директории: {e}"

    def make_dir(self, name):
        try:
            os.mkdir(os.path.join(self.current_dir, name))
            return f'Директория {name} создана'
        except Exception as e:
            return f'Ошибка создания директории: {e}'

    def remove_dir(self, name):
        try:
            shutil.rmtree(os.path.join(self.current_dir, name))
            return f'Директория {name} удалена'
        except Exception as e:
            return f'Ошибка удаления директории: {e}'

    def create_file(self, name):
        try:
            open(os.path.join(self.current_dir, name), 'w').close()
            return f'Файл {name} создан'
        except Exception as e:
            return f'Ошибка создания файла: {e}'

    def read_file(self, name):
        try:
            with open(os.path.join(self.current_dir, name), 'r') as file:
                return file.read()
        except Exception as e:
            return f'Ошибка чтения файла: {e}'

    def write_file(self, name, content):
        try:
            with open(os.path.join(self.current_dir, name), 'w') as file:
                file.write(content)
            return f'Содержимое записано в файл {name}'
        except Exception as e:
            return f'Ошибка записи в файл: {e}'

    def delete_file(self, name):
        try:
            os.remove(os.path.join(self.current_dir, name))
            return f'Файл {name} удален'
        except Exception as e:
            return f'Ошибка удаления файла: {e}'

    def copy_file(self, src, dst):
        try:
            shutil.copy(os.path.join(self.current_dir, src), os.path.join(self.current_dir, dst))
            return f'Файл {src} скопирован в {dst}'
        except Exception as e:
            return f'Ошибка копирования файла: {e}'

    def move_file(self, src, dst):
        try:
            shutil.move(os.path.join(self.current_dir, src), os.path.join(self.current_dir, dst))
            return f'Файл {src} перемещен в {dst}'
        except Exception as e:
            return f'Ошибка перемещения файла: {e}'

    def rename_file(self, src, dst):
        try:
            os.rename(os.path.join(self.current_dir, src), os.path.join(self.current_dir, dst))
            return f'Файл {src} переименован в {dst}'
        except Exception as e:
            return f'Ошибка переименования файла: {e}'

def process_command(fm, command):
    if not command:
        return True, False
    
    cmd = command[0]
    args = command[1:]

    running = True
    if cmd == 'exit':
        running = False
    elif cmd == 'ls':
        print(fm.list_dir())
    elif cmd == 'cd':
        if args:
            print(fm.change_dir(args[0]))
        else:
            print('Директория не указана')
    elif cmd == 'mkdir':
        if args:
            print(fm.make_dir(args[0]))
        else:
            print('Имя директории не указано')
    elif cmd == 'rmdir':
        if args:
            print(fm.remove_dir(args[0]))
        else:
            print('Имя директории не указано')
    elif cmd == 'create':
        if args:
            print(fm.create_file(args[0]))
        else:
            print('Имя файла не указано')
    elif cmd == 'read':
        if args:
            print(fm.read_file(args[0]))
        else:
            print('Имя файла не указано')
    elif cmd == 'write':
        if len(args) > 1:
            print(fm.write_file(args[0], ' '.join(args[1:])))
        else:
            print('Недостаточно параметров для команды записи')
    elif cmd == 'delete':
        if args:
            print(fm.delete_file(args[0]))
        else:
            print('Имя файла не указано')
    elif cmd == 'copy':
        if len(args) == 2:
            print(fm.copy_file(args[0], args[1]))
        else:
            print('Недостаточно параметров для команды копирования')
    elif cmd == 'move':
        if len(args) == 2:
            print(fm.move_file(args[0], args[1]))
        else:
            print('Недостаточно параметров для команды перемещения')
    elif cmd == 'rename':
        if len(args) == 2:
            print(fm.rename_file(args[0], args[1]))
        else:
            print('Недостаточно параметров для команды переименования')
    else:
        print('Неизвестная команда')
    
    return running, True