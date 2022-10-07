import os
from translation import Translation
from gi.repository import Caja, GObject, Gtk, Gdk
from gi import require_version

require_version('Gtk', '3.0')
require_version('Caja', '2.0')


class CajaCopyPath(Caja.MenuProvider, GObject.GObject):

    def __init__(self):
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

    def get_file_items(self, window, files):
        return self._create_menu_items(files, "File")

    def get_background_items(self, window, file):
        return self._create_menu_items([file], "Background")

    def _create_menu_items(self, files, group):
        plural = len(files) > 1
        item_path = Caja.MenuItem(
            name="CajaCopyPath::CopyPath" + group,
            label=Translation.t("copy_paths") if plural else Translation.t("copy_path"),
        )
        item_name = Caja.MenuItem(
            name="CajaCopyPath::CopyName" + group,
            label=Translation.t("copy_names") if plural else Translation.t("copy_name"),
        )

        item_path.connect("activate", self._copy_paths, files)
        item_name.connect("activate", self._copy_names, files)
        return [item_path, item_name]

    def _copy_paths(self, menu, files):
        paths = list(map(lambda f: f.get_location().get_path(), files))
        if len(paths) > 0:
            self.clipboard.set_text(", ".join(paths), -1)

    def _copy_names(self, menu, files):
        paths = list(map(lambda x: os.path.basename(x.get_location().get_path()), files))
        if len(paths) > 0:
            self.clipboard.set_text(", ".join(paths), -1)
