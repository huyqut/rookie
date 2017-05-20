# Beyond Basics

## Options when starting `vi`

- Open file and move cursor to a specific place:
    ```
    vi +n file
    vi + file
    vi +/pattern file
    ```
    - `file` is the file-path of the target.
    - `+n` indicates that the file starts at n-th line.
    - `+` indicates the last line.
    - `+/pattern` indicates starting the file at the 1st occurence of the `pattern`. 

- Read-only Mode:
    ```
    vi -R file
    view file
    ```
    - Both serve as the command to view file in read-only mode.
    - To overwrite read-only mode, use **`:w!`** or **`:wq`**.
