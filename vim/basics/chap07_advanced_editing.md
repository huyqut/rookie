# Advanced Editing in `vi`

## `set` command

The `set` command can be used to toggle option on or off.
```
:set option 
:set nooption
```
To set an option on, simply invoke `set` with the option name. To set an option off, precede `no` to the option name in `set` command.

An option can also be assigned a value:
```
:set option=123456
```

- See all options available in `vi`: (including options that are set off, which precede `no` at the beginning)
    ```
    :set all
    ```
- To see the current value of an option:
    ```
    :set option?
    ```

## `.exrc` file

The `.exrc` file manages options for `vi` (which uses `ex` editor underneath). The following is an example in the `.exrc` file:
```
set nowrapscan wrapmargin=7
```

## Some Options

| Option | Default | Description |
| --- | --- | --- |
| `autoindent` or `ai` | `noai` | Indent a line with the same level of indentation to the previous line. Indentation is in space. This should be used with `sw` option. |
| `shiftwidth` or `sw` | `8` | Define an indentation width in space. |
| `autoprint` or `ap` | `ap` | Print changes after editing command. |
| `directory` or `dir` | `/tmp` | Name the directory where `ex` or `vi` store buffer files. |
| `errorbells` or `eb` | `eb` | Bell sounds when error |
| `flash` or `fp` | `nofp` | Flash the screen instead of bell |
| `ignorecase` or `ic` | `noic` | Ignore case-sensitive during search |
| `list`  | `nolist` | Print a tab as `^I` and ends lines with `$`. |
| `magic` | `magic` | Wildcard characters `.`, `*`, `[`, `]` have special meaning in pattern search. |
| `novice` | `nonovice` | Require to use long commands in `ex` such as `copy` instead of `cp` |
| `number` or `nu` | `nonu` | Display line numbers on the left |
| `readonly` or `ro` | `noro` | Every write attempt to the file is failed. To overwrite, must use `!`. |
| `report` | `5` | Report edits just been made on status line if there are at least a number of lines are affected. Default is 5. |
| `shell` or `sh` | `/bin/sh` | Path name for shell used in `:!` and `:sh`. |
| `showmatch` or `sm` | `nosm` | Show match of opening parenthesis or curly braces (`{`, `(`) when typing closing parenthesis or curly braces (`}`, `)`). Bell rings if there is no match. |
| `tabstop` or `ts` | `8` | Define number of spaces to be used with a tab is typed in `INSERT MODE`. |
| `wrapmargin` or `wm` | `0` | Define right margin. If the margin is reached, it automatically inserts carriage return to a new line. |  
| `wrapsearch` or `ws` | `ws` | Search for wrap-around. |

## Executing terminal or shell commands in `vi`

### One-line command

```
:!command
```
- `command`: command used in shell and terminal.

### Multiple commands

```
:sh
```
- This will jump out of `vi` temporarily to the shell to execute whatever commands out there.
- When done, go back to `vi` by using `CTRL-D`.

## Filtering a text through `sh` commands

We can send a block of text through a command in shell.

### Filtering a text with `ex`

- To sort from line 13 to line 31:
    ```
    :13,31!sort
    ```
    - This will pass all lines from 13 to 31 (inclusively) through the sort command. Then the `sort` command will return the output to replace the lines 13 to 31 again.

### Filtering a text with `vi`

[ To be continued ]

## Saving commands

### Word Abbreviation

```
:ab abbr phrase
```

- `ab`: set abbreviation command in `ex` editor.
- `abbr`: abbreviation to be used.
- `phrase`: full phrase to replace the abbreviation.
- Use the abbreviation inside phrase can cause tail recursion. The behavior is not consistent so it is advised to avoid touching edges like this case.

```
:unab abbr
```
- `unab`: remove abbreviation setting.
- `abbr`: abbreviation to be removed.

### `map` Command

- List all mappings:
    ```
    :map
    ```
- Map a character `x` to a command `sequence`:
    ```
    :map x sequence
    ```
- Unmap character `x`:
    ```
    :map x
    ```
- List of unused characters that can be used in mapping:
    - Letters: **`g`** **`K`** **`V`** **`v`**
    - Control Keys: **`^A`** **`^K`** **`^O`** **`^W`** **`^X`**
   - Symbols: **`_`** **`*`** **`\`** **`=`**