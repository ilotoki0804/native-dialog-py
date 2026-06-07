import os
import typing
from os import PathLike
from pathlib import Path

import _native_dialog

from native_dialog._base import Level, NativeDialogError

__all__ = [
    "confirm",
    "alert",
    "open_multiple_files",
    "open_single_dir",
    "open_single_file",
    "save_single_file",
]

_native_dialog: typing.Any


def confirm(title: str, text: str, level: Level | None = "warning") -> bool:
    try:
        return _native_dialog.confirm(title, text, "warning" if level is None else level)
    except RuntimeError as exc:
        raise NativeDialogError(*exc.args)


def alert(title: str, text: str, level: Level = "warning") -> None:
    try:
        return _native_dialog.alert(title, text, "warning" if level is None else level)
    except RuntimeError as exc:
        raise NativeDialogError(*exc.args)


def open_multiple_files(
    filename: str | None = None,
    location: PathLike | None = None,
    title: str | None = "Open Files",
    filters: list[tuple[str, list[str]]] | None = None,
) -> list[Path]:
    try:
        return _native_dialog.open_multiple_files(
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
        return _native_dialog.open_single_dir(filename, location, "Open a Folder" if title is None else title)
    except RuntimeError as exc:
        raise NativeDialogError(*exc.args)


def open_single_file(
    filename: str | None = None,
    location: PathLike | None = None,
    title: str | None = "Open a File",
    filters: list[tuple[str, list[str]]] | None = None,
) -> Path:
    try:
        return _native_dialog.open_single_file(
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
        return _native_dialog.open_single_file(
            filename, None if location is None else os.fspath(location), "Save As" if title is None else title, filters
        )
    except RuntimeError as exc:
        raise NativeDialogError(*exc.args)
