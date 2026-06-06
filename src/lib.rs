use pyo3::prelude::*;

mod helpers;

/// native interface to native_dialog
#[pymodule]
mod _native_dialog {
    use crate::helpers::*;
    use pyo3::prelude::*;
    use std::path::PathBuf;

    #[pyfunction]
    fn confirm(title: String, text: String, level: &str) -> PyResult<bool> {
        let dialog = message_dialog(title, text, level)?.confirm();
        to_python_result(dialog.show())
    }

    #[pyfunction]
    fn alert(title: String, text: String, level: &str) -> PyResult<()> {
        let dialog = message_dialog(title, text, level)?.alert();
        to_python_result(dialog.show())
    }

    #[pyfunction]
    fn open_multiple_files(
        filename: Option<String>,
        location: Option<PathBuf>,
        title: String,
        filters: Option<Filters>,
    ) -> PyResult<Vec<PathBuf>> {
        let dialog = file_dialog(filename, location, title, filters).open_multiple_file();
        to_python_result(dialog.show())
    }

    #[pyfunction]
    fn open_single_dir(
        filename: Option<String>,
        location: Option<PathBuf>,
        title: String,
    ) -> PyResult<Option<PathBuf>> {
        let dialog = file_dialog(filename, location, title, None).open_single_dir();
        to_python_result(dialog.show())
    }

    #[pyfunction]
    fn open_single_file(
        filename: Option<String>,
        location: Option<PathBuf>,
        title: String,
        filters: Option<Filters>,
    ) -> PyResult<Option<PathBuf>> {
        let dialog = file_dialog(filename, location, title, filters).open_single_file();
        to_python_result(dialog.show())
    }

    #[pyfunction]
    fn save_single_file(
        filename: Option<String>,
        location: Option<PathBuf>,
        title: String,
        filters: Option<Filters>,
    ) -> PyResult<Option<PathBuf>> {
        let dialog = file_dialog(filename, location, title, filters).save_single_file();
        to_python_result(dialog.show())
    }
}
