import renpy.exports as renpy

__all__ = [
    "log_error",
    "log_warn",
    "log_info",
    "log_filename_line",
]


def log_error(msg: str, filename_line=None):
    renpy.log("Error: " + msg)
    log_filename_line(filename_line)
    renpy.log("")
    return


def log_warn(msg: str, filename_line=None):
    renpy.log("Warn: " + msg)
    log_filename_line(filename_line)
    renpy.log("")
    return


def log_info(msg: str, filename_line=None):
    renpy.log("Info: " + msg)
    log_filename_line(filename_line)
    renpy.log("")
    return


def log_filename_line(filename_line=None):
    if filename_line:
        renpy.log("filename_line: " + str(filename_line))
    return
