import os
import pickle
from pathlib import Path
import shutil

def file_readb(file_name: str) ->dict:
    data_str: str
    data_dict: dict

    try:
        with open((file_name + '.txt'), 'rb') as file:
            data_str = pickle.load(file)
    except FileNotFoundError:
        print("ERROR! FILE ABSENT")
    except Exception as FileNotWorkError:
        print("ERROR! ABOARD FILE READ")

    data_dict = eval(data_str)
    return data_dict

def bypassFile(path, lev: int = 1) -> None:
    print('\t'*lev, ':', os.listdir(path))

    for i in os.listdir(path):
        if os.path.isdir(Path(path, i)):
            print('\t'*(lev+1), '->', i)
            bypassFile(Path(path, i), lev+4)

def file_writeb(file_name: str, data_dict: dict) ->None:
    with open((file_name + '.txt'), 'wb') as file:
        try:
            pickle.dump(str(data_dict), file)
        except Exception as FileNotWorkError:
            print("ERROR! ABOARD FILE RECORD")

def set_direct(dir: str) -> None:
    if os.path.exists(Path(Path.home(), dir)):
        os.chdir(Path(Path.home(), dir))
        print('\nsource\t', os.getcwd())
    else:
        print("\nERROR!\nTelegramDesktop is not available")

def create_folders(dict_f: dict) -> None:
    for i in range(1, len(dict_f)):
        if not os.path.isdir(dict_f[i][0]):
            os.mkdir(dict_f[i][0])

def check_FileRename(target_dir: str, file_name: str):
    ind = 0
    while True:
        if os.path.exists(Path(os.getcwd(), target_dir, file_name).stem + ('{}({})'.format(global_s, ind)) +
                          Path(os.getcwd(), target_dir, file_name).suffix):
            ind += 1
        else:
            return Path(file_name).rename(Path(file_name).stem + ('{}({})'.format(global_s, ind)) +
                                          Path(file_name).suffix)

def move_picture(arr_f: list) -> None:
    for f_name in os.listdir():
        if Path(f_name).suffix.lower() in arr_f[1] and os.stat(f_name).st_ino != 0:

            if os.path.exists(Path(os.getcwd(), arr_f[0], f_name)):
                f_name = check_FileRename(arr_f[0], f_name)

            shutil.move(f_name, Path(os.getcwd(), arr_f[0]))  # move inside folder 'Pictures'

def move_video(arr_f: list) -> None:
    for f_name in os.listdir():
        if Path(f_name).suffix.lower() in arr_f[1] and os.stat(f_name).st_ino != 0:

            if os.path.exists(Path(os.getcwd(), arr_f[0], f_name)):
                f_name = check_FileRename(arr_f[0], f_name)

            shutil.move(f_name, Path(os.getcwd(), arr_f[0]))  # move inside folder 'Video'

def move_music(arr_f: list) -> None:
    for f_name in os.listdir():
        if Path(f_name).suffix.lower() in arr_f[1] and os.stat(f_name).st_ino != 0:

            if os.path.exists(Path(os.getcwd(), arr_f[0], f_name)):
                f_name = check_FileRename(arr_f[0], f_name)

            shutil.move(f_name, Path(os.getcwd(), arr_f[0]))  # move inside folder 'Music'

def move_doc(arr_f: list) -> None:
    for f_name in os.listdir():
        if Path(f_name).suffix.lower() in arr_f[1] and os.stat(f_name).st_ino != 0:

            if os.path.exists(Path(os.getcwd(), arr_f[0], f_name)):
                f_name = check_FileRename(arr_f[0], f_name)

            shutil.move(f_name, Path(os.getcwd(), arr_f[0]))  # move inside folder 'Documents'

def move_file(arr_f: list) -> None:
    for f_name in os.listdir():
        if not Path(f_name).suffix == '' and os.stat(f_name).st_ino != 0:

            if os.path.exists(Path(os.getcwd(), arr_f[0], f_name)):
                f_name = check_FileRename(arr_f[0], f_name)

            shutil.move(f_name, Path(os.getcwd(), arr_f[0]))  # move inside folder 'Others'

def move_folder(dict_f: dict) -> None:
    arr_f = []
    for i in range(1, len(dict_f)):
        arr_f.append(dict_f[i][0])

    for f_name in os.listdir():
        if not f_name in arr_f and os.stat(f_name).st_ino != 0:
            shutil.move(f_name, Path(os.getcwd(), dict_f[6][0]))  # move inside folder 'Folders'

#==========================================main==========================================#

if __name__ == '__main__':

    global_s = '_copy'
    f_name = 'data'

    data = file_readb(f_name)

    print('\n\tPy application. Move files')
    set_direct(data[0][0])

    print('Before:')
    bypassFile(os.getcwd())

    create_folders(data)

    move_picture(data[1])
    move_video(data[2])
    move_music(data[3])
    move_doc(data[4])
    move_file(data[5])
    move_folder(data)

    print('DONE.\nAfter:')
    bypassFile(os.getcwd())
else:
    print('ERROR!')

#=============================back_up====================================#
# data = {0: ['Downloads\Telegram Desktop', 'data.txt'],
#         1: ['Pictures', ['.bmp', '.png', '.jpg', '.jpeg', '.tif', '.tiff', 'gif']],
#         2: ['Video', ['.mp4', '.mov', '.avi', '.avchd', '.flv', '.f4v', '.swf', '.mkv', '.webm', '.html5']],
#         3: ['Music', ['.mp3', '.aac', '.alac', '.flac', '.wma', '.wav', '.aiff']],
#         4: ['Documents', ['.doc', '.docx', '.pdf', '.txt', '.rtf', '.pptx', '.csv', '.xls', '.xlsx', '.xlsm']],
#         5: ['Others'],
#         6: ['Folders']
#         }
# file_writeb(f_name, data)