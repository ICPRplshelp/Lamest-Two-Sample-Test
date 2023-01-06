# Lamest Two Sample Test

For those who want to test statistical significance of two collections
of samples having their means different, but did not take a formal
stats course.

Paste all numbers in `1control.txt` for group 1 and `2treatment.txt` for group 2.
Numbers should be seperated by newlines. Don't worry about leading or trailing whitespace because they are removed when
the file is opened. Best to paste from a CSV file, and
from a row directly.

To be clear: null hypothesis is that the means of the two samples are the same; the alternative hypothesis is that they
aren't.
The alternative hypothesis is true when the p-value is lower than 0.05, at least by convention.
