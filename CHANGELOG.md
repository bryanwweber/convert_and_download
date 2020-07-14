# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

<!-- markdownlint-disable MD022 MD024 MD032 -->

## [Unreleased]
### Added

### Changed
- Bump dependency versions
- Switch to GitHub Actions for building
- Switch branch to main

### Fixed

### Removed

## [0.2.4] - 2019-JAN-19
### Changed
- "Convert and download selected" button text is now sentence case rather than title case
- Conversion loop is simplified to be a single loop
- Fix or ignore Markdown lint errors in CHANGELOG.md

### Fixed
- Convert and download button is shown when files are selected with "Select all" checkbox

## [0.2.3] - 2018-OCT-01
### Changed
- Only run LaTeX once when converting

## [0.2.2] - 2018-AUG-30
### Changed
- Bump minimum version of `thermohw` to 0.4.0

### Fixed
- Add `convert_raw_html` filter to `PDFExporter` to match newer versions of `thermohw`

## [0.2.1] - 2018-AUG-14
### Added
- Add `convert_div` filter from `thermohw` package to convert Bootstrap `alert-*` class divs to appropriate LaTeX environments

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

[Unreleased]: https://github.com/bryanwweber/convert_and_download/compare/v0.2.4...HEAD
[0.2.4]: https://github.com/bryanwweber/convert_and_download/compare/v0.2.3...v0.2.4
[0.2.3]: https://github.com/bryanwweber/convert_and_download/compare/v0.2.2...v0.2.3
[0.2.2]: https://github.com/bryanwweber/convert_and_download/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/bryanwweber/convert_and_download/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/bryanwweber/convert_and_download/compare/v0.1.3...v0.2.0
[0.1.3]: https://github.com/bryanwweber/convert_and_download/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/bryanwweber/convert_and_download/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/bryanwweber/convert_and_download/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/bryanwweber/convert_and_download/compare/604b40c1df95b9097f7797efef2a463c597fda00...v0.1.0
