Title: Taking Notes With Markdown and Pandoc
Date: 2016-9-21
Category: Other
tags: 30 Day Challenge
Author: Frank Hrach

### Installing
A friend of mine suggested that I try and type my notes in markdown format instead of typing them all into plain text. I decided to take his advice after he listed off some of the advantages of doing so. Firstly, the notes are very portable and can be complied into a number of different formats as needed, notably into PDF, HTML, and even into presentations with a little know-how. Secondly, it allows for notes to be read and searched much more easily because PDFs are much comfortable and readable than raw text files on mobile devices. Finally, the notes look immaculate with very little effort, at least, compared to the amount of formatting required for an equivalent Word or OneNote document. By focusing on the content and not the format of my notes, it lets me concentrate on the actual content, and ultimately, take better notes.


Getting Pandoc setup is easy and is available on just about every OS. Either download it from your OS's software repos, or, get a pre-built version from their [download page](https://github.com/jgm/pandoc/releases/tag/1.17.2). After it's installed, it's useful to have a LaTeX compiler installed, and it is required for exporting a PDF. Take a look at Pandoc's [installation guide](http://pandoc.org/installing.html) to find out which LaTeX implementations it works with. Once you've installed these, you're good to go!


### Metadata
Pandoc supplies a format to define the title, author, and date modified for the document. Which can be used as follows:

```
% Title Goes here
% Authors Go Here; Separated by Semicolons
% Date; Separated by Semicolons
```

If the title is long enough that you want to control how many lines it takes up manually, simply do the following:

```
% Title Line One
  Title Line Two
% Authors Go Here; Separated by Semicolons
% Date; Separated by Semicolons
```

### Note Taking
This is entirely up to you! However, I recommend using headers as the primary form of organization because Pandoc forms a full interactive tree in the PDF allowing you to easily find and jump between sections. Headers in markdown are easy a level 1 header is just `#I Am a Level One Header` and a level 2 is simply `##I Am a Level Two Header` and so on and so forth. For readability purposes, I generally use mostly Level One and Level Three headers.

There are two kinds of lists, just like HTML, ordered lists and unordered lists. Their names are self explanatory, so, to make an unordered list, simply place an `*` before each line, and place each member of the list on a different line. For an ordered list, simply replace the asterisk with `1.`, `2.`, etc. For either type, to add a sublist simply indent the asterisk or number. It is important to note that markdown requires there to be two newlines between a paragraph and the start of a list, otherwise, it doesn't become a list. So to have a list after a paragraph of normal text, it must be formated similar to the following:

```
I am a paragraph with some text

1. I am an ordered List
2. I am an ordered List
	1. I am an ordered sub-list
3. I am an ordered List
	* I am an unordered sub-list

* I am an unordered list
* I am an unordered list
	1. I am an ordered sub-list
* I am an unordered list
	* I am an unordered sub-list
```

### Compiling To a PDF

Once you're ready to convert, simply run the following command to exporta as a PDF:

```
pandoc some_file.md -s -o some_file.pdf
```

And that's it! After the command completes there will be a pdf with your notes converted into a beautiful document.
