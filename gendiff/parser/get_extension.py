import os.path


def get_extension(filepath):
    if not os.path.isfile(filepath):
        return None
    _, ext = os.path.splitext(filepath)
    ext = ext.lower()
    return ext if len(ext) > 0 else None
