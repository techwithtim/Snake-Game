# 'define config.log' is in core.rpy
define error_notify = _("Where was an ERROR. Please send the developer the logs found in: [config.log]")
define warn_notify = _("Where was an WARN. Please send the developer the logs found in: [config.log]")
define info_notify = False


init 1 python:
    def log_error(msg: str, filename_line: str = None):
        renpy.log("Error: " + msg)
        log_filename_line(filename_line)
        if error_notify:
            notify(error_notify)
        return

    def log_warn(msg: str, filename_line: str = None):
        renpy.log("Warn: " + msg)
        log_filename_line(filename_line)
        if warn_notify:
            notify(warn_notify)
        return

    def log_info(msg: str, filename_line: str = None):
        renpy.log("Info: " + msg)
        log_filename_line(filename_line)
        if info_notify:
            notify(info_notify)
        return

    def log_filename_line(filename_line: str = None):
        if filename_line:
            renpy.log("filename_line: " + filename_line)
