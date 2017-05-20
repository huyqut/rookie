# Move around in `vi`

## Screen movement

- Scrolling by screen:
    - **`CTRL F`**: Forward 1 screen
    - **`CTRL B`**: Backward 1 screen
    - **`CTRL D`**: Forward 1/2 screen
    - **`CTRL U`**: Backward 1/2 screen

- Repositioning a screen:
    - **`z`** **`ENTER`**: Move current line to the top of the text editor.
    - **`z.`**: Move current line to be in the middle of the text editor.
    - **`z-`**: Move current line to the bottom of the text editor.

- Movement within a screen
    - Head line of the screen: Press **`H`**
    - Middle line of the screen: Press **`M`**
    - Last line of the screen: Press **`L`** 
    - Move to the n-th line from the head: Press `count` **`H`**
    - Move to the n-th line from the bottom: Press `count` **`L`**

- Movement by line:
    - **`+`** or **`ENTER`**: Move to the first non-space character of the next line.
    - **`-`**: Move to the first non-space character of the previous line.

- Movement on the same line:
    - **`^`**: Move to the first non-space character of the current line.
    - **`count |`**: Move to the count-th character.

## Movement within a text block

- End of a word:
    - **`e`**: End of a word (without special characters)
    - **`E`**: End of a word (with special characters)
    - **`(`**: Move to the beginning of the sentence.
    - **`)`**: Move to the end of the current sentece.
    - **`{`**: Move to the beginning of the paragraph.
    - **`}`**: Move to the end of the current paragraph.
    - **`[[`**: Move to the beginning of the current section.
    - **`]]`**: Move to the end of the current section.

## Movement by search

- To search for a pattern:
    ```
    /pattern
    ```
    - `pattern`: pattern to be searched.
    - After this, press **`ENTER`** then the cursor will come to the result.
    - To search backward, replace `/` with `?`.

- Repeat the last search:
    - **`n`**: Repeat the last search in the same direction.
    - **`N`**: Repeat the last search in the opposite direction.
    - **`/ ENTER`**: repeat search forward
    - **`? ENTER`**: repeat search backward

- Search can also be combined with `c` or `d` to change or replace or delete content.
    - If use with **`c`**, `vi` will delete all content from current cursor to the next/previous search result and jump to insert mode.
    - If use with **`d`**, `vi` will delete all content from current cursor to the next/previous search result and stay in the command mode.

- Find a character in the same line:
    - **`f key`**: Find the next character `key` in the same line.
    - **`F key`**: Find the previous character `key` in the same line.
    - **`t key`**: Find the next character `key` in the same line. (cursor move to 1 key before)
    - **`T key`**: Find the previous character `key` in the same line. (cursor move to 1 key before)
    - **`;`**: Repeat previous find in the same direction.
    - **`,`**: Repeat previous find in the opposite direction.

- Go to: press **`count G`** go to `count` line in the file.
    - **`` `` ``**: Return to previous position before calling `G`.
    - This can be combined with copy, change, edit syntax.
