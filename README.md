# native-dialog-py

Python port for [native-dialog][native-dialog] crate.

[native-dialog]: https://docs.rs/native-dialog/latest/native_dialog/index.html

## Installation

Use uv to add native_dialog on package:

```bash
uv add native-dialog
```

Use uvx to use command-line scripts:

```bash
uvx native-dialog alert "hello!" --info
```

## Examples

On python script:

```python
import native_dialog

# alert
native_dialog.alert("you are under attack!", "perpare evacuation", "error")

# confirm
native_dialog.confirm("you are under attack!", "would you prepare evacuation?", "error")

# warning, info level dialog (default is "warning")
native_dialog.alert("homework reminder", "complete your homework!", "info")

# select files with filter
native_dialog.open_single_file("Select an Image File", filter=[("images", ["png", "jpg", "jpeg"])])

# select multiple files
native_dialog.open_multiple_files("Select Assets", filter=[("images", ["png", "jpg", "jpeg"]), ("programming", ["toml", "py", "rs"])])

# save file
native-dialog.save_single_file("Save File")

# file_dialog function
native_dialog.file_dialog("Open Multiple Files", multiple=True)
```

Here are command line examples:

```bash
# alert
native-dialog alert 'you are under attack!' "prepare evacuation" --error

# confirm
native-dialog confirm 'you are under attack!' "would you prepare evacuation?" --error

# warning, info level dialog
native-dialog alert "homework reminder" "complete your homework!" --info
native-dialog confirm "nuclear reacter overheated" "nuclear reacter is overheated. Would you try cooling them?" --warning
# warning is the default. You can omit it completely.
native-dialog confirm "nuclear reacter overheated" "nuclear reacter is overheated. Would you try cooling them?"

# select file
native-dialog file

# select with filter
native-dialog file --title "Select an Image File" --add-filter images png,jpg,jpeg

# select multiple files
native-dialog file --title "Select Assets" --add-filter images png,jpg,jpeg --add-filter programming toml,py,rs --multiple

# save file
native-dialog file --title "Save File" --save
```

## Async support

Async support does exists, but it is disabled by default. You need to enable `async` feature on the Rust side and access async API through `native_dialog._async_api`.

It might be enabled by default when the async support for pyo3 is stablized. Currently it's buggy to use.

## Changelog

Treat native-dialog as unstable. Pin your dependency as `~=0.X.0` when using this.

### v0.3.0

* Add level and NativeDialog to the top level
* Add support for experimental async (can be enabled through `async` feature flag on Config.toml, not enabled on default python build)
* Add command-line program
* Add file_dialog function
* allow None for title
* Strangthen pyproject.toml and add LICENSE

### 0.2.0

initial release
