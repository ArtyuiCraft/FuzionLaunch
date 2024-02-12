# FuzionLaunch

FuzionLaunch is a launcher for apps entirely based around plugins. At its core, it's just a menu that loads menus/apps (it uses fzf for menus).

## Installation

1. Clone the repository.
2. If you are on Windows, run the .bat file. If you are on Linux or macOS, run the .sh file.

## Plugins

Plugins can be installed in the `plugins` folder.

### Plugin Creation

To create a plugin, follow these steps:

1. Import the plugin library:

```python
import plugins.pluglib as pluglib
```
2. Create the main function:
```python
def main():
    return pluglib.menu()
```
The main function must return a pluglib.menu. The parameters for pluglib.menu are as follows:
```python
pluglib.menu(
    name,  # Used for the name in the menu; must be a string
    func   # The code that needs to be run when selected; must be callable
)
```
