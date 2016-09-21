Title: Some Useful Vim Commands
Date: 2016-9-20
Category: Tech
tags: 30 Day Challenge, Vim
Author: Frank Hrach

Despite many other options being available, I still use Vim daily for various tasks from taking notes to writing this post. However, I'll admit that Vim has a lot of strange and somewhat arbitrary key combinations which are quite useful. I'm going to list a few which I use daily which might not be common knowledge or I frequently forget.

| Mode | Keystrokes | Effect |
|:-----|:-----------|:-------|
| Normal | ```$``` | Moves the cursor to the end of the current line |
| Normal | ```0``` | Moves the cursor to the first non-whitespace character of the current line |
| Normal | ```shift+j``` | Joins the current line with the line below it |
| Normal | ```~``` | Toggles between capital and lowercase letters under the cursor |
| Normal | ```]s```| Moves to the next misspelled word |
| Normal | ```[s```| Moves to the previous misspelled word |
| Insert | ```ctrl+x s``` | Brings up a list of suggestions if a misspelled word is after the cursor. The list can be navagiated with ```ctrl+n``` and ```ctrl+p``` |
| Normal | ```ctrl+a``` | If the cursor is over a number, increments it by 1 |
| Normal | ```ctrl+x``` | If the cursor is over a number, decrements it by 1 |
| Normal | ```z=```	| If ```set spell``` and the cursor is over a misspelled word, will bring up a list of correcton candidates |
| Normal | ```shift+h``` | Moves the cursor to the top of the screen |
| Visual Block | ```shift+I``` | Enters insert mode and inserts whatever is typed in each highlighted square |
