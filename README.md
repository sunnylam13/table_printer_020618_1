# Table Printer Using Lists

A function named printTable() takes a list of lists of strings and displays it in a well-organized table with each column right-justified. 

Assume that all the inner lists will contain the same number of strings.

The code will first have to find the longest string in each of the inner lists so that the whole column can be wide enough to fit all the strings. 

You can store the maximum width of each column as a list of integers. 

The printTable() function can begin with colWidths = [0] * len(tableData), which will create a list containing the same number of 0 values as the number of inner lists in tableData. 

That way, colWidths[0] can store the width of the longest string in tableData[0], colWidths[1] can store the width of the longest string in tableData[1], and so on. 

You can then find the largest value in the colWidths list to find out what integer width to pass to the rjust() string method.

## References

ABS: 234

## Resources

https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data

https://stackoverflow.com/questions/12032214/print-new-output-on-same-line

