# Alias package for vjepa2 without moving existing source tree.
# This maps vjepa2.* to the top-level packages inside src/.
import sys as _sys
import types as _types
import importlib.util as _util
import os as _os

_DEF_NAMES = ("models", "datasets", "masks", "utils", "hub")

# Base directory that contains the top-level source tree siblings of this package
_base_dir = _os.path.abspath(_os.path.join(_os.path.dirname(__file__), _os.pardir))


def _alias_pkg(_alias: str, _target: str):
    # Try spec-based discovery first (works when top-level package is importable)
    spec = _util.find_spec(_target)
    paths = None
    if spec is not None and getattr(spec, "submodule_search_locations", None):
        paths = list(spec.submodule_search_locations)
    else:
        # Fallback: point to physical directory next to this package
        candidate = _os.path.join(_base_dir, _target)
        if _os.path.isdir(candidate):
            paths = [candidate]
    if not paths:
        return
    mod = _types.ModuleType(_alias)
    mod.__path__ = paths
    mod.__package__ = _alias
    _sys.modules[_alias] = mod

for _name in _DEF_NAMES:
    _alias_pkg(__name__ + "." + _name, _name)
