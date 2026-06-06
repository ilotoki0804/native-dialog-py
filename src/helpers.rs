use native_dialog::{FileDialogBuilder, MessageDialogBuilder, MessageLevel};
use pyo3::{
    exceptions::{PyRuntimeError, PyValueError},
    prelude::*,
};
use std::path::PathBuf;

pub type Filters = Vec<(String, Vec<String>)>;

#[inline]
pub fn message_dialog(title: String, text: String, level: &str) -> PyResult<MessageDialogBuilder> {
    let builder = MessageDialogBuilder {
        title,
        text,
        level: convert_literal_level(level)?,
        owner: Default::default(),
    };
    Ok(builder)
}

#[inline]
pub fn file_dialog(
    filename: Option<String>,
    location: Option<PathBuf>,
    title: String,
    filters: Option<Filters>,
) -> FileDialogBuilder {
    let builder = FileDialogBuilder {
        filename,
        location,
        title: Some(title),
        filters: Default::default(),
        owner: Default::default(),
    };
    if let Some(filters) = filters {
        builder.add_filters(filters)
    } else {
        builder
    }
}

#[inline]
pub fn convert_literal_level(level: &str) -> PyResult<MessageLevel> {
    match level {
        "info" => Ok(MessageLevel::Info),
        "warning" => Ok(MessageLevel::Warning),
        "error" => Ok(MessageLevel::Error),
        _ => Err(PyValueError::new_err(format!(
            "level argument only accepts 'info', 'warning', or 'error', but received {level}"
        ))),
    }
}

pub fn to_python_result<T>(native_dialog_result: native_dialog::Result<T>) -> PyResult<T> {
    use native_dialog::Error::*;

    let error = match native_dialog_result {
        Ok(result) => return Ok(result),
        Err(error) => error,
    };

    let exc = match error {
        Io(err) => PyRuntimeError::new_err(format!("system error of IO failure: {err}")),
        Utf8(_) => PyRuntimeError::new_err("invalid utf-8 sequence detected"),
        MissingDep => PyRuntimeError::new_err("cannot find implementation (kdialog/zenity/yad)"),
        Killed(signal) => {
            PyRuntimeError::new_err(format!("subprocess killed by signal: {signal:?}"))
        }
        Other(description) => PyRuntimeError::new_err(description),
    };

    Err(exc)
}
