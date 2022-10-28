init -998 python:
    # 'define config.log' is in core.rpy
    error_notify = __("Where was an ERROR. Please send the developer the logs found in: [config.log]")
    warn_notify = _("Where was an WARN. Please send the developer the logs found in: [config.log]")
    info_notify = False

    def log_error(msg: str, filename_line = None):
        renpy.log("Error: " + msg)
        log_filename_line(filename_line)
        if error_notify:
            notifyEx(msg = error_notify)
        return

    def log_warn(msg: str, filename_line = None):
        renpy.log("Warn: " + msg)
        log_filename_line(filename_line)
        if not IsNullOrWhiteSpace(warn_notify):
            notifyEx(msg = warn_notify)
        return

    def log_info(msg: str, filename_line = None):
        renpy.log("Info: " + msg)
        log_filename_line(filename_line)
        if not IsNullOrWhiteSpace(info_notify):
            notifyEx(msg = info_notify)
        return

    def log_filename_line(filename_line = None):
        if filename_line:
            renpy.log("filename_line: [filename_line]")
        return
