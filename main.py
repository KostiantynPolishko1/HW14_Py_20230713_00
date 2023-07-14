import os
from pathlib import Path
import shutil


def set_direct(dir: str) -> None:
    if os.path.exists(Path(Path.home(), dir)):
        os.chdir(Path(Path.home(), dir))
        print('\nset path', os.getcwd())
    else:
        print("\nERROR!\nTelegramDesktop is not available")


def create_folders(dict_f: dict) -> None:
    for i in range(len(dict_f)):
        if not os.path.isdir(dict_f[i][0]):
            os.mkdir(dict_f[i][0])

if __name__ == '__main__':
    target_dir = 'Downloads\Telegram Desktop'
    dict_folder = {0: ['Pictures', ['.bmp', '.png', '.jpg', '.jpeg', '.tif', '.tiff', 'gif']],
                   1: ['Video', ['.mp4', '.mov', '.avi', '.avchd', '.flv', '.f4v', '.swf', '.mkv', '.webm', '.html5']],
                   2: ['Music', ['.mp3', '.aac', '.alac', '.flac', '.wma', '.wav', '.aiff']],
                   3: ['Documents', ['.doc', '.docx', '.pdf', '.txt', '.rtf', '.pptx', '.csv', '.xls', '.xlsx', '.xlsm']],
                   4: ['Folders'],
                   5: ['Others']
                   }

    set_direct(target_dir)
    create_folders(dict_folder)
    # move_picture(dict_folder[0][1])

    print('END')
