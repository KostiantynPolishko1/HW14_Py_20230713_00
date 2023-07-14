import os
from pathlib import Path
import shutil
def set_direct(folder: str) ->None:

    if os.path.exists(Path(Path.home(), folder)):
        os.chdir(Path(Path.home(), folder))
        print('\nset path', os.getcwd())
    else:
        print("\nERROR!\nTelegramDesktop is not available")

if __name__ == '__main__':
    app_folder = 'Downloads\Telegram Desktop'
    set_direct(app_folder)

