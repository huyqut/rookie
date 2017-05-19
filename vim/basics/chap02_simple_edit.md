# Simple Editing with `vi`

## Move the cursor

- Insert mode:
    - Press **`i`** to start the insert mode at the current cursor.
    - Press **`I`** to start insert mode at the beginning of a line.

- Single character movement:
    - **`UP`**: Move up 1 line
    - **`DOWN`**: Move down 1 line
    - **`LEFT`**: Move left 1 character (If this is the beginning of the line, `vi` does NOT move to previous line)
    - **`RIGHT`**: Move right 1 character (If this is the end of the line, `vi` does NOT move to the next line)
    - Other keys equivalent to the above keys:
        - **`h`** `=` **`LEFT`**
        - **`j`** `=` **`DOWN`**
        - **`k`** `=` **`UP`**
        - **`l`** `=` **`RIGHT`**

- Countable character movement:
    ```
    count key
    ```
    - `count`: Number of characters/lines to move
    - `key`: Either `h`, `j`, `k`, `l` keys in the single movement.

- Set newline automatically:
    - During insert mode, newline is introduced only when user press **`ENTER`** key.
    - We can set wrap-around (wrap right margin) so that when a number of characters remaining is reached, `vi` auto inserts a new line:
        ```
        :set wm=count
        ```
        - `count`: # of remaining characters from the right to insert newline.

- Beginning and End of line:
    - **`0`**: Beginning of the line
    - **`$`**: End of the line

- Enable line number: (number option)
    ```
    :set nu
    ```

- Move by a word (a block of characters)
    - Forward:
        - A block may not contain special characters (`,`,`.`, etc.): press **`w`**
        - A block may contain special characters: press **`W`**
    - Backward:
        - A block may not contain special characters (`,`, `.`, etc.): press **`b`**
        - A block may contain special characters: press **`B`**

- Move by multiple words:
    ```
    count key
    ```
    - `count` can be any number
    - `key` can be either **`w`**, **`W`**, **`b`**, **`B`**.

## Simple Edits

- Append: 
    - Press **`a`** then `vi` will switch to insert mode but the cursor is moved to the next character.
    - Press **`A`** then `vi` will go to the end and switch to insert mode.

- Change content: press **`c`** to make the movement of cursor deletes content on its path (change means delete content and user can start write new content)
    - **`ch`**: Replace the left character
    - **`cl`** or **`s`**: Replace the current character
    - **`cj`**: Replace current AND next line.
    - **`ck`**: Replace current AND above line.
    - **`cw`**: Replace from current cursor to the end of the word (no special characters)
    - **`cW`**: Replace from current cursor to the end of the word (with special characters)
    - **`cb`**: Replace from current cursor to the beginning of the word (with no special characters)
    - **`cB`**: Replace from current cursor to the beginning of the word (with special characters)
    - **`cc`** or **`S`**: Replace a line
    - **`c$`** or **`C`**: Replace from current cursor to the end of a line
    - **`c0`**: Replace from current cursor to the beginning of a line
    - Except for `$` and `0`, `count` variable can be inserted between `c` and the other key to specify how many units to be replaced:
        - **`c5h`**: Replace 5 left characters
        - **`c7l`** or **`7s`**: Replace 7 characters from current cursor
        - **`c8j`**: Replace 9 lines (including current line)
        - **`c3k`**: Replace 4 lines (including current line)
        - **`c5w`**: Replace the next 5 words (no special characters)
        - **`c5W`**: Replace the next 5 words (with special characters)
        - **`c4b`**: Replace the previous 4 words (no sepcial characters)
        - **`c4B`**: Replace the previous 4 words (with special characters)
        - **`c3c`** or **`3S`**: Replace 3 lines (including current lines)

- Replace a character: **`r`** `key`
    - Press `r` and then press the new character to replace the old.
    - Everything is still in command mode.

- Replace content: **`R`** `content`
    - This will replace from current cursor to the end of the line.
    - Press **`ESC`** to finish replacement.

- Change case: press **`~`** to change from lower-case to upper-case (and vice versa)

- Delete content: Use the same rule for changing content but 2 exceptions.
    - Any place with **`c`** is replaced with **`d`**.
    - Any place with **`C`** is replaced with **`D`**.
    - Any place with **`s`** is replaced with **`x`**.
    - Any place with **`S`** is replaced with **`X`**.

- Copy (Yank): The same rule applied as change content except
    - Replace **`c`** for **`y`**.
    - Replace **`C`** for **`Y`**.
    - Above commands are to copy content.

- Paste (Put): press **`p`** key to paste a content to the location of a file.

- Repeat the last edit: press **`.`**

- Undo edit:
    - Undo the last edit: press **`u`**
    - Undo the last operation on the same line: press **`U`**

- Blank line:
    - Press **`o`**: open a blank line BELOW the cursor.
    - Press **`o`**: open a blank line ABOVE the cursor.

- Join 2 lines: Press **`J`** and then the be below line will be appended to the current line. (To repeat, use **`.`**)
