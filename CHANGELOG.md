# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [9.0.0] - 2025-01-10

### Breaking Changes
- **Migrated from OpenAI Gym to Gymnasium**: The project now uses `gymnasium` instead of the deprecated `gym` library
  - Import changed from `import gym` to `import gymnasium as gym`
  - All gym dependencies replaced with gymnasium equivalents
- **Updated API signatures**:
  - `reset()` now returns `(observation, info)` tuple instead of just `observation`
  - `step()` now returns `(observation, reward, terminated, truncated, info)` instead of `(observation, reward, done, info)`
  - Metadata key changed from `render.modes` to `render_modes`
  - Metadata key changed from `video.frames_per_second` to `render_fps`
- **Python version requirements**: Dropped support for Python 3.5-3.8, now requires Python 3.9+
- **Removed deprecated `return_info` parameter** from `reset()` method

### Added
- **Python 3.13 support**: Full compatibility with Python 3.13
- **SubprocVecEnv support**: Added `__getstate__` and `__setstate__` methods for proper multiprocessing support
  - Environments can now be pickled and used with `gymnasium.vector.SubprocVecEnv`
  - Proper handling of C++ objects during serialization
  - Automatic reinitialization of emulator state in child processes
- Support for Python 3.10, 3.11, and 3.12

### Changed
- **Updated dependencies to latest versions**:
  - `gym>=0.17.2` → `gymnasium>=1.0.0`
  - `numpy>=1.18.5` → `numpy>=2.2.1`
  - `pyglet<=1.5.21,>=1.4.0` → `pyglet>=2.1.0`
  - `tqdm>=4.48.2` → `tqdm>=4.67.1`
  - `twine>=1.11.0` → `twine>=6.0.1`
- Package description updated from "OpenAI Gym interface" to "Gymnasium interface"
- Documentation strings updated to reflect Gymnasium API
- **JoypadSpace wrapper** migrated to Gymnasium API:
  - Updated imports from `gym` to `gymnasium`
  - Updated `reset()` method to accept `**kwargs` and return `(observation, info)` tuple
  - Updated docstrings to reflect new terminated/truncated flags

### Migration Guide

#### Updating Your Code

**Old code (v8.x with gym):**
```python
import gym
from nes_py import NESEnv

env = NESEnv('path/to/rom.nes')
observation = env.reset()
observation, reward, done, info = env.step(action)
```

**New code (v9.x with gymnasium):**
```python
import gymnasium as gym
from nes_py import NESEnv

env = NESEnv('path/to/rom.nes')
observation, info = env.reset()
observation, reward, terminated, truncated, info = env.step(action)
done = terminated or truncated
```

#### Using with SubprocVecEnv

```python
from gymnasium.vector import SubprocVecEnv
from nes_py import NESEnv

# Create multiple parallel environments
def make_env(rom_path):
    def _init():
        return NESEnv(rom_path)
    return _init

envs = SubprocVecEnv([make_env('path/to/rom.nes') for _ in range(4)])
observations, infos = envs.reset()
observations, rewards, terminateds, truncateds, infos = envs.step(actions)
```

### Removed
- Support for Python 3.5, 3.6, 3.7, and 3.8
- Compatibility with OpenAI Gym (use gymnasium instead)

### Fixed
- **NumPy 2.x compatibility issues** in `_rom.py`:
  - Fixed overflow errors by converting numpy scalar types to Python integers
  - Affects `prg_rom_size`, `chr_rom_size`, and `prg_ram_size` properties

### Technical Notes
- All code has been tested with Python 3.13 and the latest versions of dependencies
- C++ emulator core remains unchanged and fully compatible
- The migration maintains backward compatibility where possible, but the API changes are necessary for gymnasium compatibility
- All wrappers (including JoypadSpace) are fully compatible with the new API

## [8.2.1] and earlier

See previous releases for older changes.
