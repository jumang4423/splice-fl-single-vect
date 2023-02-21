import sys
import os
import shutil
from tqdm import tqdm

if __name__ == '__main__':
    # get args
    original_folder = sys.argv[1]
    dest_folder = sys.argv[2]

    file_prefix = ".wav"

    # in the original folder, find the file_prefix file recursively
    files = []
    for root, dirs, filenames in os.walk(original_folder):
        for f in filenames:
            if f.endswith(file_prefix):
                files.append(os.path.join(root, f))



    # for each file, copy 2 destination folder but no subfolder
    for f in tqdm(files):
        shutil.copy(f, dest_folder)

    print("copied {} files".format(len(files)))
