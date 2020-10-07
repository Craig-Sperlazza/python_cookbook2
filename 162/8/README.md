# project-8a

Write a generator function named count_seq that doesn't take any parameters and generates a sequence that starts like this: 2, 12, 1112, 3112, 132112, 1113122112, 311311222112, 13211321322112, ...

To get a number in the sequence, enumerate how many there are of each digit (in a row) in the previous number.  For example, the first number is "one 2", which gives us the second number "12".  That number is "one 1" followed by "one 2", which gives us the third number "1112".  That number is "three 1" followed by "one 2", or 3112.  Etc.

Your generator function won't just go up to some limit - it will keep going indefinitely. It may need to treat the first one or two values as special cases, which is fine.

Your file must be named: **count_seq.py**
