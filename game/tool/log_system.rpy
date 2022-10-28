init -998 python:
    # 'define config.log' is in core.rpy
    error_notify = __("Where was an {color=#f00}{b}ERROR{/b}{/color}. Please send the developer the logs found in: {color=#00ccff}[config.log]{/color}")
    warn_notify = _("Where was an {color=#f5bc02}{b}WARN{/b}{/color}. Please send the developer the logs found in: {color=#00ccff}[config.log]{/color}")
    info_notify = False

    def log_error(msg: str, filename_line = None):
        renpy.log("Error: " + msg)
        log_filename_line(filename_line)
        if error_notify:
            notifyExFirst(msg = error_notify)
        renpy.log("")
        return

    def log_warn(msg: str, filename_line = None):
        renpy.log("Warn: " + msg)
        log_filename_line(filename_line)
        if not IsNullOrWhiteSpace(warn_notify):
            notifyExFirst(msg = warn_notify)
        renpy.log("")
        return

    def log_info(msg: str, filename_line = None):
        renpy.log("Info: " + msg)
        log_filename_line(filename_line)
        if not IsNullOrWhiteSpace(info_notify):
            notifyExFirst(msg = info_notify)
        renpy.log("")
        return

    def log_filename_line(filename_line = None):
        if filename_line:
            renpy.log("filename_line: " + str(filename_line))
        return
