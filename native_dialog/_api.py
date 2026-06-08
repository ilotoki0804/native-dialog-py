import os
from os import PathLike
from pathlib import Path

import native_dialog.native_dialog as raw
from native_dialog._base import Level, NativeDialogError

__all__ = [
    "confirm",
    "alert",
    "open_multiple_files",
    "open_single_dir",
    "open_single_file",
    "save_single_file",
]


def confirm(title: str, text: str, level: Level | None = "warning") -> bool:
    try:
        return raw.confirm(title, text, "warning" if level is None else level)
    except RuntimeError as exc:
        raise NativeDialogError(*exc.args)


def alert(title: str, text: str, level: Level = "warning") -> None:
    try:
        return raw.alert(title, text, "warning" if level is None else level)
    except RuntimeError as exc:
        raise NativeDialogError(*exc.args)


def file_dialog(
    filename: str | None = None,
    location: PathLike | None = None,
    title: str | None = None,
    filters: list[tuple[str, list[str]]] | None = None,
    *,
    directory: bool = False,
    save: bool = False,
    multiple: bool = False,
) -> Path | list[Path]:
    if save:
        return save_single_file(filename, location, title, filters)
    if directory:
        return open_single_dir(filename, location, title)
    if multiple:
        return open_multiple_files(filename, location, title, filters)
    else:
        return open_single_file(filename, location, title, filters)


def open_multiple_files(
    filename: str | None = None,
    location: PathLike | None = None,
    title: str | None = "Open Files",
    filters: list[tuple[str, list[str]]] | None = None,
) -> list[Path]:
    try:
        return raw.open_multiple_files(
            filename,
            None if location is None else os.fspath(location),
            "Open Files" if title is None else title,
            filters,
        )
    except RuntimeError as exc:
        raise NativeDialogError(*exc.args)


def open_single_dir(
    filename: str | None = None,
    location: PathLike | None = None,
    title: str | None = "Open a Folder",
) -> Path:
    try:
        return raw.open_single_dir(filename, location, "Open a Folder" if title is None else title)
    except RuntimeError as exc:
        raise NativeDialogError(*exc.args)


def open_single_file(
    filename: str | None = None,
    location: PathLike | None = None,
    title: str | None = "Open a File",
    filters: list[tuple[str, list[str]]] | None = None,
) -> Path:
    try:
        return raw.open_single_file(
            filename,
            None if location is None else os.fspath(location),
            "Open a File" if title is None else title,
            filters,
        )
    except RuntimeError as exc:
        raise NativeDialogError(*exc.args)


def save_single_file(
    filename: str | None = None,
    location: PathLike | None = None,
    title: str | None = "Save As",
    filters: list[tuple[str, list[str]]] | None = None,
) -> Path:
    try:
        return raw.open_single_file(
            filename, None if location is None else os.fspath(location), "Save As" if title is None else title, filters
        )
    except RuntimeError as exc:
        raise NativeDialogError(*exc.args)
