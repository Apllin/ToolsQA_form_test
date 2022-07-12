import os.path


def get_abs_path(path):
    return str(
        os.path.abspath(f'../source/{path}')
    )

