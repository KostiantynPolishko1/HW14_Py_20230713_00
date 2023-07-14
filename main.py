import os
from pathlib import Path
import shutil
import json

def toJSON_File(_dict: dict, f_name: str) ->None:
    with open(f_name, "w") as myFile:
        json.dump(_dict, myFile)

def JSON_File_toDict(f_name: str) ->dict:
    _dict = {}
    with open(f_name, "r") as myFile:
        _dict = json.load(myFile)
    return _dict

def set_direct(dir: str) -> None:
    if os.path.exists(Path(Path.home(), dir)):
        os.chdir(Path(Path.home(), dir))
        print('\nset path', os.getcwd())
    else:
        print("\nERROR!\nTelegramDesktop is not available")


def create_folders(dict_f: dict) -> None:
    for i in range(1, len(dict_f)):
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
    for i in dict_f:
        arr_f.append(dict_f[i][0])

    for f_name in os.listdir():
        if not f_name in arr_f:
            shutil.move(f_name, Path(os.getcwd(), dict_f[6][0]))  # move inside folder 'Folders'

if __name__ == '__main__':

    dict_folder = {0: ['Downloads\Telegram Desktop', 'data.txt'],
                   1: ['Pictures', ['.bmp', '.png', '.jpg', '.jpeg', '.tif', '.tiff', 'gif']],
                   2: ['Video', ['.mp4', '.mov', '.avi', '.avchd', '.flv', '.f4v', '.swf', '.mkv', '.webm', '.html5']],
                   3: ['Music', ['.mp3', '.aac', '.alac', '.flac', '.wma', '.wav', '.aiff']],
                   4: ['Documents', ['.doc', '.docx', '.pdf', '.txt', '.rtf', '.pptx', '.csv', '.xls', '.xlsx', '.xlsm']],
                   5: ['Others'],
                   6: ['Folders']
                   }

    # toJSON_File(dict_folder, dict_folder[0][1])
    # dict_folder = JSON_File_toDict(data_file)
    # print(list(dict_folder.keys()))


    set_direct(dict_folder[0][0])
    create_folders(dict_folder)

    move_picture(dict_folder[1])
    move_video(dict_folder[2])
    move_music(dict_folder[3])
    move_doc(dict_folder[4])
    move_file(dict_folder[5])
    move_folder(dict_folder)

    print('DONE')
else:
    print('ERROR!')

#===================data back_up======================#