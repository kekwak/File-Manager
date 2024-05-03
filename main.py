from misc.utils import FileManager, process_command
from misc.config import path, banner


def file_manager_cli(fm):
    command = input('Введите команду: ').strip().split()
    out = process_command(fm, command)
    return out
        
if __name__ == '__main__':
    print(banner)
    fm = FileManager(path)
    running = True
    while running:
        running, _ = file_manager_cli(fm)