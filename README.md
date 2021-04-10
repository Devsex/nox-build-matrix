# nox-build-matrix
GitHub action to generate a build matrix for a project's Noxfile.

## Inputs

### `noxfile`

Path to your noxfile. Defaults to `noxfile.py`.

### `keywords`

Keyword filters to apply to the list of sessions. Equivalent to Nox's `-k` option.

## Outputs

### `matrix`

A JSON representation of your build matrix. Pass this through `fromJson` and then to the matrix option for another workflow job to use the generated matrix.

## Usage

For example usage information, refer to [example.yml](https://github.com/nint8835/nox-build-matrix/blob/main/example.yml)
