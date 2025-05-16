import os

def create_directories():

    main_dir = "MyFiles"

    os.mkdir(main_dir)

    subdirs = ["Docs", "Images", "Videos"]

    for subdir in subdirs:

        subdir_path = os.path.join(main_dir, subdir)

        os.mkdir(subdir_path)

if __name__ == "__main__":

    create_directories()