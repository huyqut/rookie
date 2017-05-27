# `ex` Editor

`ex` is the underlying mechanism of `vi`.

- Print a line: `p` can be ommitted
    ```
    np
    ```
    - `n`: line number
- Print by range:
    ```
    from,to
    ```
    - `from`: begin of range
    - `to`: end of range
- A line number should be prepended to the word itself. Otherwise, it only affects the current line.

- Substitue a word:
    ```
    ns/origin/update/
    ```
    - `n`: line number to be affected (if there is no `n`, then it will affect the current line).
    - `origin`: pattern to be replaced.
    - `update`: pattern to replace.

## Editing with `ex`

- Basic keywords:
    - `d`: delete
    - `m`: move
    - `co` or `t`: copy
    - Examples:
        - `3,7d`: Delete line 3 to 7 (inclusively)
        - `15,19m23`: Move all lines from 15 to 19 (inclusively) to after line 23.
        - `23,31co15`: Copy all lines from 23 to 31 (inclusively) to after line 15.
    - To show line numbers:
        ```
        :set number
        :set nu
        ```
    - Disable show line numbers:
        ```
        :set nonumber
        :set nonu
        ```
    - Temporarily show line numbers:
        ```
        fromt,to#
        ```
    - Total number of lines: `:=`
    - Current line number: `:.=`
    - Line number of the 1st match of `pattern`: `:/pattern/=`

- Line Addressing Symbols:
    - `.`: current line
    - `$`: last line of file
    - `%`: every line
    - `+n`: n-th line below counting from the current line.
    - `-n`: n-th line above counting from the current line. 
    - Examples:
        - `:.,$d`: Delete from current line (inclusive) to the end of file.
        - `:23,.m$`: Move every line from line 23 to current line (inclusive) to the end of file.
        - `%d`: Delete every line in the file.
        - `%t$`: Copy every line in the file and paste it to the end of the file.
- Search patterns:
    - `:/pattern/d`: delete the next line containing `pattern`.
    - `:/pattern/+d`: delete the line after the next line containing `pattern`.
    - `:/from/,/to/d`: delete all lines from the line containing pattern `from` to the line containing pattern `to`.
    - `:.,/pattern/d`: delete all lines from current line to the next line containing `pattern`.

- Global search patterns: `:g` and its opposite `:g!`
    - `:g/pattern`: Find the last occurence of the `pattern`.
    - `:g/pattern/p`: Display all lines temporarily containing the `pattern`.
    - `:g!/pattern/nu`: Find all lines that do not contain pattern and also the line number.
    - `:[from],[to]g/pattern/p`: Display all lines from line `[from]` to line `[to]`.

- Multiple commands: `ex` editor also uses `|` to separate multiple commands in one line.

- Saving and Exiting:
    - `:w`: Write buffer to the file.
    - `:q`: Quit a file (no edit is made)
    - `:wq`: Write and quit
    - `:x`: Write (if modefied) and quit
    - `:w!`: Overwrite
    - `:q!`: Quit without saving
    - `:w [filename]`: Write a to new `filename`
    - Saving a part of the file:
        - `:230,$w [filename]`: write from line 230 to the end of file to the new `filename`.
        - `:.,600w [filename]`: write from current line to line 600 to the new `filename`.
    - Append a file: use `>>` after `w` to append.
        - `:230,$w>> [filename]`: write from line 230 to the end of file at the end of `filename`.
        - `:.,600w>> [filename]`: write from current line to line 600 to the end of file `filename`.
- Copy content from another file to current cursor:
    ```
    :read [filename]
    :r [filename]
    ```
    - Can be combined with other range before it.

## Open multiple files

```
vi [filename1] [filename2]
```

- Open another file inside `vi`:
    ```
    :e [filename]
    ```
    - Switch a file: **`CTRL ^`**
