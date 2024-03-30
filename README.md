# FuzionLaunch

FuzionLaunch is a launcher for apps entirely based around plugins. At its core, it's just a menu that loads menus/apps (it uses fzf for menus).

## Installation

1. Clone the repository.
2. If you are on Windows, run the Fuzion.bat file. If you are on Linux or macOS, run the Fuzion file.

## Plugins

Plugins can be installed in the `plugins` folder that is located at `~/.config/fuzion/plugins/`.

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
### uploading a plugin to FuzionPlug
to upload a plugin to [FuzionPlug](https://github.com/artyuiCraft/fuzionplug) you just need to add your plugin in a pull request and i will add it if it follows the plugin guidelines

#### plugin guidelines
1. no nsfw content.
2. should be a plugin for FuzionLaunch and not a plugin for another program.
3. no plugin that hacks the system or hacks it.
4. it can be anything from a game to just launching a app but nothing that does something against the rules.
