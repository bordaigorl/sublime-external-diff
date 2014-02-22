# Meld Diff plugin for Sublime Text

A simple plugin to invoke *Meld* from Sublime Text.

To use this plugin, *Meld* has to be installed.
You can get it with

    sudo apt-get install meld

or another command according to your os.

This plugin is also compatible with *KDiff3*; to use it instead of *Meld* just put the path to *KDiff3* in the `meld_bin_path` setting.

## Usage

### From a view

To run *Meld* diffing a file against the current one you can press <kbd>ctrl+alt+d</kbd>: a quick panel will let you choose between the other opened files; selecting an entry will run *Meld* on the current and selected files. 

If the <kbd>ctrl+alt+d</kbd> key map is already in use by other installed plugins or custom keymaps, you can re-bind it to a custom key combination, calling the command `meld_diff_quick_panel`.

### In the Side Bar

When two or three files are selected in the side bar, you can find a `Diff files in Meld` entry in the context menu that will run *Meld* on the selected files.

## Settings

By default, *Meld*'s path is assumed to be `/usr/bin/meld` but this can be customised by changing the setting `meld_bin_path` in your User Settings.
