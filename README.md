Project Tyrfing
==

Project Tyrfing is an application that exhibits optimal sorting of
complex groups. By default the application simulates the sorting of
rods based on length and circumference, although these two attributes
can easily be abstracted to almost any set of objects.

In our simulation, there is assumed to be two processing units,
each which can handle two rods at any given time. Thus, ideally up to four rods
can be processed at once. In some cases, three rods will be processed
at once, such as when a matching pair and a lone rod are the only items
remaining. If no matches are left, rods can be sorted as single items,
which allows for the processing of one per processing unit, or two at
a time.

The program displays the time for all items to be sorted based on this
priority, stated formally as follows:

1.  Groups of four (two pairs)
2.  Single pairs (in addition to a lone rod if available)
3.  Lone rods (processed two at a time if possible)

Project Tyrfing uses a modified quicksort algorithm, `genMatches`, to
process a list of information, sorting by desired attribute (by default
defined as 'height', 'circumference', and 'length'. The algorithm runs at
an average efficiency of O(n logn) time.

At this point in time planned updates to Project Tyrfing include:
* Option for user input of data
* Option for user import of data with `json`
* Implementation of GUI via Kivy