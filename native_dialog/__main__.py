import sys
from argparse import ArgumentParser, Namespace
from pathlib import Path

from native_dialog import alert, confirm
from native_dialog._api import (
    open_multiple_files,
    open_single_dir,
    open_single_file,
    save_single_file,
)

parser = ArgumentParser("native-dialog CLI", "open native dialogs in command-line")
subparsers = parser.add_subparsers()

confirm_subparser = subparsers.add_parser(
    "confirm",
    description="create confirm dialog. prints `true` if OK pressed, otherwise `false` printed",
)
confirm_subparser.set_defaults(subparser="confirm")
confirm_subparser.add_argument("title")
confirm_subparser.add_argument("text")
confirm_subparser.add_argument("--info", action="store_true", help="information level confirmation")
confirm_subparser.add_argument("--warning", action="store_true", help="warning level confirmation")
confirm_subparser.add_argument("--error", action="store_true", help="error level confirmation")

alert_subparser = subparsers.add_parser("alert", description="create alert dialog")
alert_subparser.set_defaults(subparser="alert")
alert_subparser.add_argument("title")
alert_subparser.add_argument("text")
alert_subparser.add_argument("--info", action="store_true", help="information level confirmation")
alert_subparser.add_argument("--warning", action="store_true", help="warning level confirmation")
alert_subparser.add_argument("--error", action="store_true", help="error level confirmation")

file_subparser = subparsers.add_parser("file", description="create file dialog")
file_subparser.set_defaults(subparser="file")
file_subparser.add_argument(
    "--filename",
    default=None,
    help="the default value of the filename text field in the dialog. For open dialogs of macOS and zenity, this is a no-op because there’s no such text field on the dialog.",
)
file_subparser.add_argument(
    "--location",
    default=None,
    help="the default directory that the dialog shows at open",
)
file_subparser.add_argument(
    "--location-cwd",
    action="store_true",
    help="set `--location` value as cwd. Ignored when the actual `--location` value presented.",
)
file_subparser.add_argument("--title", default=None, help="the window title for the dialog")
file_subparser.add_argument(
    "--add-filter",
    "-f",
    action="append",
    nargs=2,
    default=None,
    help="adds a file type filter. Two arguments provided, first arguemt will be a filter name and second argument will be filtered extensions. Extensions can be provided multiple times, comma seperated. For dialogs that open directories, this is also a no-op.",
)
file_subparser.add_argument(
    "--dir",
    "--directory",
    action="store_true",
    help="open a directory instead of a file. Ignored when the `--save` argument presents.",
)
file_subparser.add_argument(
    "--save",
    action="store_true",
    help="show save dialog instead of opening one",
)
file_subparser.add_argument(
    "--multiple",
    action="store_true",
    help="open multiple files. The output is newline seperated. Ignored when the `--save` or `--dir` argument presents.",
)


def main() -> None:
    args = parser.parse_args(sys.argv[1:] or ["--help"])

    match args:
        case Namespace(
            subparser="confirm" | "alert" as action,
            title=title,
            text=text,
            info=info,
            warning=warning,
            error=error,
        ):
            # warning is the default
            level = "error" if error else "warning" if warning else "info" if info else "warning"
            if action == "confirm":
                confirmed = confirm(title, text, level)
                if confirmed:
                    print("true")
                else:
                    print("false")
            else:
                alert(title, text, level)

        case Namespace(
            subparser="file",
            filename=filename,
            location=location,
            location_cwd=is_cwd_location,
            title=title,
            add_filter=filters,
            dir=is_directory,
            multiple=is_multiple,
            save=is_save,
        ):
            location = Path.cwd() if location is None and is_cwd_location else location
            filters = None if filters is None else [(name, extensions.split(",")) for name, extensions in filters]
            if is_save:
                file = save_single_file(filename, location, title, filters)
                print(file)
            elif is_directory:
                file = open_single_dir(filename, location, title)
                print(file)
            elif is_multiple:
                files = open_multiple_files(filename, location, title, filters)
                print("\n".join(str(file) for file in files))
            else:
                file = open_single_file(filename, location, title)
                print(file)


if __name__ == "__main__":
    main()
