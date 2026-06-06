import typing

__all__ = "Level", "NativeDialogError"

Level = typing.Literal["info", "warning", "error"]


class NativeDialogError(Exception):
    """Native dialog exceptions"""
