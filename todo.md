# TODO - Build and Publish Independent Raspbot/OLED Python Library

## 1. Define Scope and Strategy
- [ ] Decide the package name (PyPI + import name) and check availability.
- [ ] Define supported hardware/features for v1:
  - [ ] Motor control
  - [ ] Servo control
  - [ ] Ultrasonic distance
  - [ ] OLED text rendering
  - [ ] Line tracker
  - [ ] Button input
  - [ ] Buzzer control
  - [ ] RGB light bar control
  - [ ] IR sensor input
  - [ ] Camera capture (OpenCV-compatible)
- [ ] Decide minimum Python version (recommended: 3.10+).
- [ ] Define Raspberry Pi OS/hardware targets (Pi model, I2C bus assumptions).
- [ ] Decide whether OLED support is bundled or an optional extra.
- [ ] Decide whether camera/OpenCV support is bundled or provided as an optional extra.

## 2. Remove Dependency on Existing Raspbot Library
- [ ] Inventory every `Raspbot_Lib` call currently used in scripts.
- [ ] Create an API mapping document:
  - [ ] Existing function name
  - [ ] Current behavior
  - [ ] New function/class design in your library
- [ ] Re-implement low-level communication in your own module (I2C/register access).
- [ ] Validate register addresses and data formats from hardware docs.
- [ ] Add robust error handling for I/O failures (timeouts, missing bus/device).
- [ ] Keep compatibility wrappers only if needed for migration, then deprecate.

## 3. OLED Independence Plan
- [ ] Inventory required features from `yahboom_oled` (init, clear, write line, refresh).
- [ ] Design your own OLED interface (device + canvas/text abstraction).
- [ ] Choose implementation strategy:
  - [ ] Native driver implementation in your package, OR
  - [ ] Adapter around a maintained OLED backend as an optional dependency
- [ ] Implement text layout helpers (line wrapping, truncation, refresh strategy).
- [ ] Add graceful fallback if OLED not detected.

## 4. Package Architecture
- [ ] Create source layout (`src/`-based package).
- [ ] Suggested module structure:
  - [ ] `src/<package_name>/bus.py` (I2C/SPI helpers)
  - [ ] `src/<package_name>/robot.py` (high-level robot API)
  - [ ] `src/<package_name>/sensors/ultrasonic.py`
  - [ ] `src/<package_name>/sensors/line_tracker.py`
  - [ ] `src/<package_name>/sensors/ir.py`
  - [ ] `src/<package_name>/inputs/button.py`
  - [ ] `src/<package_name>/display/oled.py`
  - [ ] `src/<package_name>/actuators/buzzer.py`
  - [ ] `src/<package_name>/actuators/rgb_light_bar.py`
  - [ ] `src/<package_name>/camera/opencv_camera.py`
  - [ ] `src/<package_name>/exceptions.py`
  - [ ] `src/<package_name>/types.py`
- [ ] Keep side effects out of import time (no hardware auto-init on import).
- [ ] Use typed public interfaces.

## 5. Build and Metadata
- [ ] Add `pyproject.toml` (PEP 517/518 build system).
- [ ] Add metadata:
  - [ ] name, version, description, readme, license, classifiers
  - [ ] project URLs (repo, docs, issues)
  - [ ] authors/maintainers
- [ ] Define runtime dependencies and optional extras (e.g. `oled`, `dev`).
- [ ] Configure wheel + sdist builds.

## 6. Testing and Quality Gates
- [ ] Add unit tests for pure logic (data conversion, formatting, API behavior).
- [ ] Add unit tests for each peripheral API (line tracker, button, buzzer, RGB, IR, camera wrappers).
- [ ] Add hardware-in-the-loop smoke tests for real Raspberry Pi hardware.
- [ ] Add hardware smoke tests per module:
  - [ ] line tracker read stability
  - [ ] button debounce behavior
  - [ ] buzzer tone/on-off behavior
  - [ ] RGB light bar color/channel mapping
  - [ ] IR sensor trigger/read behavior
  - [ ] camera frame capture with OpenCV (`cv2.VideoCapture`)
- [ ] Add mocks/fakes for I2C bus to run CI without hardware.
- [ ] Add camera test doubles to run CI when no camera device is present.
- [ ] Add linting + formatting + type checks:
  - [ ] ruff (lint/format)
  - [ ] mypy or pyright
  - [ ] pytest with coverage
- [ ] Define minimum acceptable coverage for core modules.

## 7. Documentation and Examples
- [ ] Write README with:
  - [ ] install instructions
  - [ ] quickstart example
  - [ ] wiring/permissions notes (I2C enabled, user groups)
  - [ ] troubleshooting section
- [ ] Add API reference docs (docstrings first, docs site optional).
- [ ] Provide examples equivalent to your current scripts:
  - [ ] distance reading loop
  - [ ] OLED distance display
  - [ ] servo/motor basic usage
  - [ ] line tracker state display example
  - [ ] button-triggered action example
  - [ ] buzzer alert pattern example
  - [ ] RGB light bar animation example
  - [ ] IR sensor event example
  - [ ] OpenCV camera frame capture and preview example
- [ ] Add migration notes: from `Raspbot_Lib` and `yahboom_oled` to new API.

## 8. Release Process and PyPI Publication
- [ ] Create TestPyPI and PyPI accounts.
- [ ] Generate API tokens and store securely.
- [ ] Build artifacts locally (`python -m build`).
- [ ] Validate distributions (`twine check dist/*`).
- [ ] Publish first to TestPyPI and verify install/import on clean venv.
- [ ] Publish stable release to PyPI.
- [ ] Tag release in git and write release notes/changelog.

## 9. CI/CD and Maintenance
- [ ] Add CI pipeline for lint, type-check, tests, and package build.
- [ ] Add automated publish workflow for tagged releases (with manual approval).
- [ ] Add semantic versioning policy and changelog process.
- [ ] Add issue/PR templates.
- [ ] Define support matrix and deprecation policy.

## 10. Immediate Next Actions (Suggested Order)
- [ ] Extract current hardware operations from scripts into a draft module.
- [ ] Implement minimal independent class for ultrasonic sensor reads.
- [ ] Implement minimal independent OLED class with `init`, `clear`, `add_line`, `refresh`.
- [ ] Implement minimal independent classes for line tracker, button, buzzer, RGB light bar, and IR sensor.
- [ ] Implement OpenCV camera wrapper with safe open/release lifecycle.
- [ ] Replace usage in `03_test_oled.py` with your new package API.
- [ ] Add first tests and package metadata, then do a TestPyPI dry run.
