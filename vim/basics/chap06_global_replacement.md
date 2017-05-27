# Global Replacement

## Basics

- `:s/old/new/`: Substitute `new` to the first occurence of `old` at the current line.
- `:s/old/new/g`: Substitute `new` to every occurence of `old` at the current line.
- `:5,10s/old/new/g`: Substitute `new` to every occurence of `old` from line 5 to line 10.
- `:11,$s/old/new/g`: Substitute `new` to every occurence of `old` from line 11 to the end of file.
- `:%s/old/new/g`: Substitute `new` to every occurence of `old` in the file.

## Confirmation on replacement

- Use `gc` instead of `g`. It will prompt to each word of matches and prompt confirmation.

## Context sensitive replacement

```
:g/pattern/s/old/new/g
```
- This will search for all lines that contain `pattern` and then do the job of replacing `new` to `old` occurences.

## Pattern matching rules

- The pattern is formalized to regular expression, not just words or characters.
- Rules:
    - Metacharacters used in search pattern:
        - `.`: matches a single character except for the new line character. Example: `...` means matching exactly 3 single characters.
        - `*`: matches zero or more characters that precedes it immediately. Example: `xyz*` means matching any string `xy`, `xyz`, `xyzz`, ...
        - `^`:
            - If `^` is at the beginning of the expression, it requires the matches to be at the beginning of the line.
            - Otherwise, `^` stands the meaning for itself.
            - Example:
                - `^Patch`: match any `Patch` word with condition that `Patch` must start at the beginning of a line.
                - `xyz^abc`: match any `xyz^abc`.
        - `$`:
            - If `$` is at the end of the expression, it requires the matches to be at the end of the line.
            - Otherwise, `$` stands the meaning for itself.
            - Example:
                - `Patch$`: match any `Patch` word with condition that `Patch` must be at the end of a line.
                - `xyz$abc`: match any `xyz$abc`.
        - `\`: escape character. Any character that is preceded by this one is treated as the character itself, not by any other meaning. Example: `\\` matches any `\` character, `\^xyz` matches any `^xyz` word (`^` is escaped).
        - `[]`: matches any single character inside the square brackets.
            - `p[aez]t`: matches either `pat`, `pet`, `pzt`.
            - Hyphens `-` can be used to to represent a range of consecutive characters (based on ASCII)
                - `[a-z]`: all alphabetic lower-case characters.
                - `[A-Z]`: all alphabetic upper-case characters.
                - `[0-9]`: all numeric characters.
                - `[xyz0-9]`: multiple characters can be mixed with hyphens to match. This matches either `0` to `9` or `x`, or `y`, or `z`.
        - `\(` and `\)`: Match and save (to be reused) the pattern enclosed between 2 special characters into a buffer list. The buffer list is counted from 1 up to 9. The pattern can be replayed by using `\n` where `n` is the buffer count of the pattern saved. `\n` can be used for both pattern string and replacement string.
            - `:%s/\(abcd) or \(cdef\)/\2 or \1/`: This will replace any pattern `abcd or cdef` with `cdef or abcd`.
            - `:%s/\(todo)\1\1/ToWhat/`: This will replace any pattern `todotodotodo` with `ToWhat`.
        - `\<`: prefix matching
            - `:%s/\<hel/yup/`: This will replace any word that begins with `hel` to be `yup`. For example, `hello` will be replaced by `yup`.
        - `\>`: postfix matching
            - `:%s/ion\>/yup/`: This will replace any word that ends with `ion` to be `yup`. For example, `function` will be replaced by `yup`.
        - `~`: Last search pattern
            - Search for `The` just before. Then to search for `Theme`, use `/~me`.
    - Posic bracket expressions:
        - `[:alpha:]`: all alphabetic characters
        - `[:upper:]`: all upper alphabetic characters
        - `[:lower:]`: all lower alphabetic characters
        - `[:digit:]`: all numeric characters
        - `[:alnum:]`: include `[:alpha:]` and `[:digit:]`.
        - `[:xdigit:]`: include all characters from hexadecimal (`[a-fA-F0-9])`)
        - `[:blank:]`: space and tab characters
        - `[:cntrl:]`: Control characters
        - `[:punct:]`: Punctuation characters
        - `[:graph:]`: Printable and non-space characters
        - `[:print:]`: Printable characters (including space and tab)
    - Metacharacters used in replacement string:
        - `\n`: reuse a saved pattern in buffer. `n` is a number from `1` to `9`.
        - `\`: treat the following character as its original meaning.
        - `&`: entire text that is matched from the pattern.
            - `%s/Hello/& There!/`: This will replace `Hello` with `Hello There!`.
            - `1,10s/.*/(&)/`: This will enclose every line from 1 to 10 with parenthesis `()`.
        - `~`: Last substitute pattern.
            - First, use command `%s/his/their/` will replace `his` with `their`. Then use command `%s/her/~/` will replace `her` with `their`.
        - `\u` - upper case the character after. `\i` - lower case the character after.
            - `%s/\(abcd\) and \(Efgh\)/\l\2 and \u\1/`: This will replace `abcd and Efgh` with `efgh and Abcd`. 
            - Search `%s/his/their/` will replace `his` with `their`. Then use command `%s/her/\u~/` will replace `her` with `Their`.
        - `\U` - upper case every character behind until `\e` or `\E` is reached. `\E` - lower case every character behind until `\U` or `\u` is reached.
            - `%s/Python/\UPython/`: This will replace any `Python` with `PYTHON`.

- Tricks:
    - `%s/  */ /`: Replace 1 or more spaces with a single space.
    - `g/^$/d`: Delete all blank lines.
    - `g/^[ ^I]*$/d`: Delete all lines that is blank or only contains spaces or tabs.
    - `%s/^  *\(.*\)/\1/`: Remove any leading spaces.
    - `%s/\(.*\)  *$/\1/`: Remove any trailing spaces.
    - `%s/.*/^I&/`: Add tab to any lines.
    - `g/.*/mo0`: Reverse order of lines.
    - `g!/Paid in full/s/$/ Overdue/` or `v/...`: Append `Overdue` to any line that does not contain `Paid in full`.

