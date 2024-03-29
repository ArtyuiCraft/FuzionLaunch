import fzfmenus
import os
import importlib.util

main_menu = []

def get_plugin_folder():
    main_py_directory = os.path.dirname(os.path.abspath(__file__))
    plugin_folder = os.path.join(main_py_directory, 'plugins')

    return plugin_folder

def discover_plugins(plugin_folder):
    plugins = []
    plugin_folder = get_plugin_folder()
    for file_name in os.listdir(plugin_folder):
        if file_name.endswith('.py'):
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

selected = fzfmenus.menu(main_menu_names)
for plugin in main_menu:
    if plugin.name == selected:
        plugin.selected()
        break
