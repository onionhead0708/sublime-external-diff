External Diff plugin for Sublime Text
=====================================

Invoke external diff program from Sublime Text to compare:

1. The current file and recent opened file
2. The current file and one of the open files that selected from a quick panel

## Install

1. Download all files and put them under `<sublime-text>/Packages/externalDiff`
2. Define following User Setting:
```
"external_diff_bin": "<path_to_the_compare_program>"
```

## Usage

### Press the keys:

<kbd>ctrl+k</kbd> <kbd>ctrl+0</kbd>: Compare the recent and current opened file
<kbd>ctrl+k</kbd> <kbd>ctrl+9</kbd>: Open a quick panel to list the opened files; selecting an entry will run external diff program on the current and selected files.

### Command Palette

Press <kbd>ctrl+shift+p</kbd> to bring up the Command Palette panel, there are following 2 items:

 +  ExternalDiff: `external_diff` - Compare recent opened file
 + ExternalDiff: `external_diff_quick_panel` - Open a quick panel to list the opened files for comparison


## Key Mapping
Re-bind the key mapping in the `Preference -> Key Bindings`
```
[
   { "keys": ["ctrl+k", "ctrl+0"], "command": "external_diff"},
   { "keys": ["ctrl+k", "ctrl+9"], "command": "external_diff_quick_panel"}
]
```

## Settings
Customize the path of the external diff program by change the setting `external_diff_bin` in the User Settings.

# Notes
Coding forked from:
* https://github.com/bordaigorl/sublime-external-diff
* https://github.com/jugyo/SublimeRecentActiveFiles
