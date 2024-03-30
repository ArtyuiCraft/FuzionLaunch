import fzfmenus
import os
import importlib.util

main_menu = []

def get_plugin_folder():
    path = os.path.expanduser('~/.config/fuzion/plugins')
    os.makedirs(path, exist_ok=True)
    return path

def discover_plugins(plugin_folder):
    plugins = []
    plugin_folder = get_plugin_folder()
    for file_name in os.listdir(plugin_folder):
        if file_name.endswith('.py') and not file_name.startswith("_"):
            if file_name == "pluglib.py": continue
            plugin_name = os.path.splitext(file_name)[0]
            plugins.append(plugin_name)
    return plugins

def load(plugin_name):
    plugin_folder = get_plugin_folder()
    plugin_path = os.path.join(plugin_folder, plugin_name + ".py")
    if not os.path.exists(plugin_path):
        raise ImportError(f"Plugin '{plugin_name}' not found at '{plugin_path}'")
    spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
    if spec is None:
        raise ImportError(f"Failed to load plugin '{plugin_name}'")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

for plugin in discover_plugins(get_plugin_folder()):
    main_menu.append(load(plugin).main())

main_menu_names = [i.name for i in main_menu]
main_menu_names.append("exit")
while True:
    selected = fzfmenus.menu(main_menu_names)
    if selected == "exit":
        break
    for plugin in main_menu:
        if plugin.name == selected:
            plugin.selected()
            input("press enter to return to Fuzion...")
            break
