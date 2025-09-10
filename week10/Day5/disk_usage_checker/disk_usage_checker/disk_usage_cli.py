import shutil
import argparse

args=None
def check_disk_usage(path):
    try:
        total, used, free = shutil.disk_usage(path)
        print(f"\nDisk usage for path: {path}")
        print(f"Total: {total / (1024 ** 3):.2f} GB")
        print(f"Used:  {used / (1024 ** 3):.2f} GB")
        print(f"Free:  {free / (1024 ** 3):.2f} GB")
        print(f"Usage: {used / total * 100:.2f}%\n")
    except Exception as e:
        print(f"unexpected error: {e}")

def initialize_parse():
    global args
    default_path = "/"
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--path",
        type=str,
        default=default_path,
        help=f"Filesystem path to check disk usage."
    )
    args = parser.parse_args()
    

if __name__ == "__main__":
    initialize_parse()
    check_disk_usage(args.path)
