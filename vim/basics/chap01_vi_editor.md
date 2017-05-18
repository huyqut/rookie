# `vi` editor

## Open a file

```sh
vi file-name
```

- `file-name` can either be relative or absolute path in terminal.
- `vi` does not edit your file instantly. It copies the file to a buffer and edit that buffer. After you've done your job, you can now go save it directly to the original one.

## Modes of `vi`

There are 2 modes in `vi`:
- **Command** mode: This is where you write your command to edit your file. By default, if you open `vi`, you jump into the this mode. If you are on the other mode, use **`ESC`** key to go back to command mode.
- **Insert** mode: This is where you actually edit your file and write something. To jump into this mode, press `i` key.

## Save & Quit a file

All of the following lines are executed inside command mode (type the command and hit **`ENTER`** key):
- `:w`: Save a file without quitting
- `:q`: Quit a file if you have not made any edits
- `:wq`: Save and Quit a file

An equivalent of `:wq` is to type `ZZ` (without hitting **`ENTER`** key).

## Cascade edits

- `:e!`: Clear all edits you have made and show the original content.
- `:q!`: Quit without saving anything

## Write a file (different from current location)

- `:w file-name`: Write a file the path of `file-name`.
- `:w! file-name`: Over-write a file if it existed.
