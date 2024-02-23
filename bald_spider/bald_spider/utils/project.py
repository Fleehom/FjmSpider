import os
import sys
from importlib import import_module


from bald_spider.settings.setting_manager import SettingsManager


def _get_closest(path='.'):
    path = os.path.abspath(path)
    return path


def _init_env():
    closest = _get_closest()
    if closest:
        project_dir = os.path.dirname(closest)
        sys.path.append(project_dir)


def get_settings(settings='settings'):
    _settings = SettingsManager({})
    _init_env()
    _settings.set_settinds(settings)
    return _settings


def merge_settings(spider, settings):
    if hasattr(spider, 'custom_settings'):
        custom_settings = getattr(spider, "custom_settings")
        settings.update_values(custom_settings)


def load_class(_path):
    if not isinstance(_path, str):
        if callable(_path):
            return _path
        else:
            raise TypeError(f"args expected string or object, got: {type(_path)}")

    module, name = _path.rsplit('.', 1)
    mod = import_module(module)
    try:
        cls = getattr(mod, name)
    except AttributeError:
        raise NameError(f"Mudule {module!r} doesn't define any object named {name!r}")
    return cls