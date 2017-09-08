import sublime, sublime_plugin
import os

class ExternalDiffBaseCmdEventListener(sublime_plugin.EventListener):
    def on_deactivated(self, view):
        if view.file_name():
            view.window().run_command("external_diff", { "deactivated_file_name": view.file_name() })

# The base class for the ExternalDiff
class ExternalDiffBaseCmd(sublime_plugin.WindowCommand):

    def get_external_diff_bin(self):
        view = self.window.active_view()
        default_bin = '/usr/bin/meld'
        if view:
            return view.settings().get("external_diff_bin", default_bin)
        return default_bin

    def run_external_diff(self, files):
        external_diff_bin = self.get_external_diff_bin()
        if os.path.exists(external_diff_bin):
            lenFiles = len(files)
            if (lenFiles == 2):
                os.system('"%s" "%s" "%s" &' %(external_diff_bin, files[0], files[1]))
            if (lenFiles == 3):
                os.system('"%s" "%s" "%s" "%s" &' %(external_diff_bin, files[0], files[1], files[2]))
            return
        else:
            sublime.error_message("Cannot find the externa diff program: " + external_diff_bin)
            return

    #def is_enabled(self):
    #    return os.path.exists(self.get_external_diff_bin())

# For the comamnd : external_diff, extends from ExternalDiffBaseCmd
class ExternalDiffCommand(ExternalDiffBaseCmd):
    def __init__(self, window):
        super(ExternalDiffCommand, self).__init__(window)
        self.recent_deactived_file = ""

    def run(self, deactivated_file_name=None):
        if deactivated_file_name:
            self.recent_deactived_file = get_correct_file_name(deactivated_file_name)
        else:
            if self.recent_deactived_file:
                self.run_external_diff([get_correct_file_name(self.window.active_view().file_name()),
                    self.recent_deactived_file])
            else:
                sublime.status_message("No recent file")

# For the comamnd : external_diff_quick_panel, extends from ExternalDiffBaseCmd
class ExternalDiffQuickPanelCommand(ExternalDiffBaseCmd):
    def run(self):
        self.open_files = self.__current_open_files()

        if len(self.open_files) > 0:
            self.window.show_quick_panel(self.open_files, self.__on_select_file)
        else:
            sublime.status_message("No other open files")

    def __on_select_file(self, index):
        if index >= 0:
            self.run_external_diff([get_correct_file_name(self.window.active_view().file_name()), self.open_files[index]])

    def __current_open_files(self):
        files = [view.file_name() for view in self.window.views() if view.file_name() is not None ]

        files.remove(get_correct_file_name(self.window.active_view().file_name()))
        return files

# For the command : external_diff_side_bar, extends from ExternalDiffBaseCmd (call in side bar)
class ExternalDiffSideBarCommand(ExternalDiffBaseCmd):
    def run(self, files):
        self.run_external_diff(files)

    def is_visible(self, files):
        if (self.is_enabled()):
            lenFiles = len(files)
            return (lenFiles >= 2 and lenFiles <= 3)
        return false

def get_correct_file_name(filename):
    if filename:
        if int(sublime.version()) >= 3000:
            return filename
        else:
            return unicode(filename)
    return None
