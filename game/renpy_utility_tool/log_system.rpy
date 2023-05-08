init -998 python:
    import pythonpackages.renpy_utility.renpy_custom_log as myLog

    # 'define config.log' is in core.rpy
    error_notify = __("There is an {color=#f00}{b}ERROR{/b}{/color}. Please send the developer the logs found in: {color=#00ccff}[config.log]{/color}")
    warn_notify = _("There is an {color=#f5bc02}{b}WARN{/b}{/color}. Please send the developer the logs found in: {color=#00ccff}[config.log]{/color}")
    info_notify = False

    def log_error(msg: str, filename_line = None):
        myLog.log_error(msg, filename_line)
        if error_notify:
            notify_prevents_loops(msg = error_notify)
        return

    def log_warn(msg: str, filename_line = None):
        myLog.log_warn(msg, filename_line)
        if not IsNullOrWhiteSpace(warn_notify):
            notify_prevents_loops(msg = warn_notify)
        return

    def log_info(msg: str, filename_line = None):
        myLog.log_info(msg, filename_line)
        if not IsNullOrWhiteSpace(info_notify):
            notify_prevents_loops(msg = info_notify)
        return
