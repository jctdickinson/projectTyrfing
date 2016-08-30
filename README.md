Project Tyrfing
==

Project Tyrfing is an application that exhibits optimal sorting of complex groups. By default the application simulates the sorting of rods based on length and circumference, although these two attributes can easily be abstracted to almost any set of objects.

Currently, the program will display the time it takes to join rods of similar length and circumference. In our simulation, up to four rods can be processed at once when in ideal circumstances. When rods cannot be paired, they are processed one at a time.

For comparison, the program will display the time it takes to process a set of rods by with optimal sorting based on the following priority:

1.  Groups of four (two pairs)
2.  Single pairs
3.  Lone rods

Project Tyrfing uses a modified quicksort algorithm to process a list of information, sorting by desired attribute (by default defined as 'height', 'circumference', and 'length'.