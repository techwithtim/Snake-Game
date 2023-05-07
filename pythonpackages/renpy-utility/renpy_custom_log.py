import renpy.exports as renpy

__all__ = [
    "log_error",
    "log_warn",
    "log_info",
    "log_filename_line",
]


def log_error(msg: str, filename_line=None):
    renpy_log_and_print("Error: " + msg)
    log_filename_line(filename_line)
    renpy_log("")
    return


def log_warn(msg: str, filename_line=None):
    renpy_log_and_print("Warn: " + msg)
    log_filename_line(filename_line)
    renpy_log("")
    return


def log_info(msg: str, filename_line=None):
    renpy_log_and_print("Info: " + msg)
    log_filename_line(filename_line)
    renpy_log("")
    return


def log_filename_line(filename_line=None):
    if filename_line:
        renpy_log_and_print("filename_line: " + str(filename_line))
    return


def renpy_log_and_print(msg: str):
    renpy_log(msg)
    print(msg)
    return


def renpy_log(msg: str):
    renpy.log(msg)
    return
