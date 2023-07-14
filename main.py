import os
from pathlib import Path
import shutil
def set_direct(dir: str) ->None:
    if os.path.exists(Path(Path.home(), dir)):
        os.chdir(Path(Path.home(), dir))
        print('\nset path', os.getcwd())
    else:
        print("\nERROR!\nTelegramDesktop is not available")

def create_folders(arr: list) ->None:
    for folder in arr:
        if not os.path.isdir(folder):
            os.mkdir(folder)

if __name__ == '__main__':
    target_dir = 'Downloads\Telegram Desktop'
    arr_folder = ['Pictures', 'Video', 'Music', 'Documents', 'Others']

    set_direct(target_dir)
    create_folders(arr_folder)

    print('END')

