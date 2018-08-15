# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Added
- Add `convert_div` filter from `thermohw` package to convert Bootstrap `alert-*` class divs to appropriate LaTeX environments

### Changed

### Fixed

### Removed

## [0.2.0] - 2018-AUG-03
### Added
- New keywords to the `setup()` function
- Configuration for flake8 in setup.cfg
- Start to add some typing
- Add docstrings to the `DLConvertHandler` class and `get` instance method

### Changed
- Rename `DLconvertFileHandler` to `DLConvertHandler`
- Raise an error if the `format` passed to the `get` handler is not `pdf`
- Directly use the `PDFExporter` rather than guessing the type

### Fixed
- Fix route URL for `dlconvert` handler
- Fix adding readme to the `long_description` in `setup.py`

## [0.1.3] - 2018-AUG-03
### Fixed
- Add all dependencies to `setup.py` and `meta.yaml`
- Fix `ANACONDA_TOKEN` secure variable on Travis CI

## [0.1.2] - 2018-AUG-03
### Added
- Add docstring to `__init__.py`
- Install `conda-verify` on Travis CI

### Fixed
- Secure variables for Travis CI need to be encrypted with the `--pro` flag
- Conda recipe Jinja variable expansion

## [0.1.1] - 2018-AUG-03
### Added
- Add setup.cfg file

### Fixed
- Fix adding channels to .travis.yml

## [0.1.0] - 2018-AUG-03
### Added
- Convert and download multiple selected Notebooks
- Automatically configure the extension to be used when installed

[Unreleased]: https://github.com/bryanwweber/convert_and_download/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/bryanwweber/convert_and_download/compare/v0.1.3...v0.2.0
[0.1.3]: https://github.com/bryanwweber/convert_and_download/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/bryanwweber/convert_and_download/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/bryanwweber/convert_and_download/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/bryanwweber/convert_and_download/compare/604b40c1df95b9097f7797efef2a463c597fda00...v0.1.0
