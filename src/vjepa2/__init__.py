# Alias package for vjepa2 without moving existing source tree.
# This maps vjepa2.* to the top-level packages inside src/.
import sys as _sys
import types as _types
import importlib.util as _util

def _alias_pkg(_alias: str, _target: str):
    spec = _util.find_spec(_target)
    if spec is None or getattr(spec, "submodule_search_locations", None) is None:
        return
    mod = _types.ModuleType(_alias)
    mod.__path__ = list(spec.submodule_search_locations)
    mod.__package__ = _alias
    _sys.modules[_alias] = mod

for _name in ("models", "datasets", "masks", "utils", "hub"):
    _alias_pkg(__name__ + "." + _name, _name)
