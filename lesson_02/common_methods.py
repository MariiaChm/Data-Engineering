import os


def create_or_clear_directory(directory) -> None:
    os.makedirs(directory, exist_ok=True)

    for file_name in os.listdir(directory):
        os.remove(os.path.join(directory, file_name))
