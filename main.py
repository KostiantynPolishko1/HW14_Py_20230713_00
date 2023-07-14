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

def move_picture(arr_f: list) -> None:
    for f_name in os.listdir():
        if Path(f_name).suffix.lower() in arr_f[1]:
            shutil.move(f_name, Path(os.getcwd(), arr_f[0]))  # move inside folder 'Pictures'

def move_video(arr_f: list) -> None:
    for f_name in os.listdir():
        if Path(f_name).suffix.lower() in arr_f[1]:
            shutil.move(f_name, Path(os.getcwd(), arr_f[0]))  # move inside folder 'Video'

def move_music(arr_f: list) -> None:
    for f_name in os.listdir():
        if Path(f_name).suffix.lower() in arr_f[1]:
            shutil.move(f_name, Path(os.getcwd(), arr_f[0]))  # move inside folder 'Music'

def move_doc(arr_f: list) -> None:
    for f_name in os.listdir():
        if Path(f_name).suffix.lower() in arr_f[1]:
            shutil.move(f_name, Path(os.getcwd(), arr_f[0]))  # move inside folder 'Documents'

def move_file(arr_f: list) -> None:
    for f_name in os.listdir():
        if not Path(f_name).suffix == '':
            shutil.move(f_name, Path(os.getcwd(), arr_f[0]))  # move inside folder 'Others'

def move_folder(dict_f: dict) -> None:
    arr_f = []
    for i in dict_folder:
        arr_f.append(dict_folder[i][0])

    for f_name in os.listdir():
        if not f_name in arr_f:
            shutil.move(f_name, Path(os.getcwd(), dict_f[5][0]))  # move inside folder 'Folders'

if __name__ == '__main__':
    target_dir = 'Downloads\Telegram Desktop'
    dict_folder = {0: ['Pictures', ['.bmp', '.png', '.jpg', '.jpeg', '.tif', '.tiff', 'gif']],
                   1: ['Video', ['.mp4', '.mov', '.avi', '.avchd', '.flv', '.f4v', '.swf', '.mkv', '.webm', '.html5']],
                   2: ['Music', ['.mp3', '.aac', '.alac', '.flac', '.wma', '.wav', '.aiff']],
                   3: ['Documents', ['.doc', '.docx', '.pdf', '.txt', '.rtf', '.pptx', '.csv', '.xls', '.xlsx', '.xlsm']],
                   4: ['Others'],
                   5: ['Folders']
                   }

    set_direct(target_dir)
    create_folders(dict_folder)

    move_picture(dict_folder[0])
    move_video(dict_folder[1])
    move_music(dict_folder[2])
    move_doc(dict_folder[3])
    move_file(dict_folder[4])
    move_folder(dict_folder)

    print('DONE')
else:
    print('ERROR!')
