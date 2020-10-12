# CHANGELOG

> https://keepachangelog.com

All notable changes to this project will be documented in this file.

## [0.0.3] 2020-10-12

### Added
- Better logs and traces when reporting handled errors

## [0.0.2] 2020-10-10

### Fixed
- Seems that version `0.15.x` of Gradle Profiler is not outputing statistical measures like `mean` and `stddev` in the CSV file anymore, thus analysis was failling since benchmark parsing could not succeed. We fix that, getting these two measures by ourselves.

## [0.0.1] 2020-09-24

### Added
- Initial release.
- Straight-forward comparison between two Gradle benchmarks with paired t-test
- Proper results reporting
- Proper errors reporting
