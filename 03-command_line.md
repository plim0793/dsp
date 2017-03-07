# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > pwd: print working directory
> > mkdir: make a directory
> > rmdir: remove a directory
> > touch: create an empty file in directory
> > rm: removes file
> > mv: renames file
> > ls -a: show all files including hidden files
> > cp: copy a file from one directory to another
> > cd: change directory
> > less: open file to see content in terminal

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
ls: lists the files/folders in the current working directory.
ls -a: displays all files.  
ls -l: list in long format.  
ls -lh: uses unit suffixes: Byte, Kilobyte, etc in order to reduce number of digits to three or less using base 2 for sizes.  
ls -lah: list in long format for all files and uses unit suffixes.  
ls -t: sort by time modified before sorting the operands by lexicongraphical order. 
ls - Glp: Enables colorized outpur for list in long format and writes a slash after each filename if that file is a directory.

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -a, ls -l, ls -lp, ls -t, and ls -S are my favorites because they are useful in sorting the list of files/folders in the directory.

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs is used to construct an argument list and execute utility.  
'''python
$ find . -name "*.txt" -print0 | xargs ls -l
'''

 

