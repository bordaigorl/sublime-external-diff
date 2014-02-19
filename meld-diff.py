import sublime, sublime_plugin
import os


class MeldCmd(sublime_plugin.WindowCommand):

    def __init__(self, win):
        self.window = win
        self.MELD_BIN_PATH = win.active_view().settings().get("meld_bin_path", '/usr/bin/meld')

    def run_meld(self, files):
        lenFiles = len(files)
        if (lenFiles == 2):
            os.system('%s "%s" "%s" &' %(self.MELD_BIN_PATH, files[0], files[1]))
        if (lenFiles == 3):
            os.system('%s "%s" "%s" "%s" &' %(self.MELD_BIN_PATH, files[0], files[1], files[2]))
        return

    def is_enabled(self):
        return os.path.exists(self.MELD_BIN_PATH)


class MeldDiffCommand(MeldCmd):
    def run(self, files):
        self.run_meld(files)

    def is_visible(self, files):
        if (os.path.exists(self.MELD_BIN_PATH)):
            lenFiles = len(files)
            return (lenFiles >= 2 and lenFiles <= 3)
        return false


class MeldDiffQuickPanelCommand(MeldCmd):
    def run(self, index=None):
        self.open_files = self.__current_open_files()

        if len(self.open_files) > 0:
            self.window.show_quick_panel(self.open_files, self.__meld)
        else:
            sublime.status_message("No other open files")

    def __meld(self, index):
        if index >= 0:
            self.run_meld([self.window.active_view().file_name(), self.open_files[index]])

    def __current_open_files(self):
        files = [view.file_name() for view in self.window.views() if view.file_name() is not None ]

        # Ignores current file
        if int(sublime.version()) >= 3000:
            files.remove(self.window.active_view().file_name())
        else:
            files.remove(unicode(self.window.active_view().file_name()))

        return files
