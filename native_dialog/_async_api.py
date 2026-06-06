import os
import typing
from os import PathLike
from pathlib import Path

import _native_dialog

from native_dialog._base import Level, NativeDialogError

__all__ = [
    "async_support",
    "async_confirm",
    "async_alert",
    "async_open_multiple_files",
    "async_open_single_dir",
    "async_open_single_file",
    "async_save_single_file",
]

_native_dialog: typing.Any


def async_support() -> bool:
    return _native_dialog.async_support()


async def async_confirm(title: str, text: str, level: Level = "warning") -> bool:
    try:
        return await _native_dialog.async_confirm(title, text, level)
    except RuntimeError as exc:
        raise NativeDialogError(*exc.args)


async def async_alert(title: str, text: str, level: Level = "warning") -> None:
    try:
        return await _native_dialog.async_alert(title, text, level)
    except RuntimeError as exc:
        raise NativeDialogError(*exc.args)


async def async_open_multiple_files(
    filename: str | None = None,
    location: PathLike | None = None,
    title: str = "Open Files",
    filters: list[tuple[str, list[str]]] | None = None,
) -> list[Path]:
    try:
        return await _native_dialog.async_open_multiple_files(
            filename, None if location is None else os.fspath(location), title, filters
        )
    except RuntimeError as exc:
        raise NativeDialogError(*exc.args)


async def async_open_single_dir(
    filename: str | None = None, location: PathLike | None = None, title: str = "Open a Folder"
) -> Path:
    try:
        return await _native_dialog.async_open_single_dir(filename, location, title)
    except RuntimeError as exc:
        raise NativeDialogError(*exc.args)


async def async_open_single_file(
    filename: str | None = None,
    location: PathLike | None = None,
    title: str = "Open a File",
    filters: list[tuple[str, list[str]]] | None = None,
) -> Path:
    try:
        return await _native_dialog.async_open_single_file(
            filename, None if location is None else os.fspath(location), title, filters
        )
    except RuntimeError as exc:
        raise NativeDialogError(*exc.args)


async def async_save_single_file(
    filename: str | None = None,
    location: PathLike | None = None,
    title: str = "Save As",
    filters: list[tuple[str, list[str]]] | None = None,
) -> Path:
    try:
        return await _native_dialog.async_open_single_file(
            filename, None if location is None else os.fspath(location), title, filters
        )
    except RuntimeError as exc:
        raise NativeDialogError(*exc.args)
