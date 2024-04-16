import os
import sys
import shutil


target_dir = 'node_modules'


def remove_dir(directory):
    print(f"Processing: {directory}")
    for root, dirs, _ in os.walk(directory):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if dir == target_dir and os.path.exists(dir_path):
                print(f"Removing: {dir_path}")
                try:
                    shutil.rmtree(dir_path)
                except Exception as e:
                    print(f"Error occured when removing {dir_path}: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        directory = os.getcwd()
    else:
        directory = sys.argv[1]

    remove_dir(directory)
    print("Operation completed.")
