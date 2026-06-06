import typing

Level = typing.Literal["info", "warning", "error"]


class NativeDialogError(Exception):
    """Native dialog exceptions"""
