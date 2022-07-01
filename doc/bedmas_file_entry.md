# entering calculations: 

`end` ends the file for reading (bedmas_file_reader)  
`#` is a comment

first array contains the numbers to be operated on in order

second array contains the operators being used between each value

including `=` is optional 

example:
```
[1, 2]
[*, =]
```
would represent the equation `1 * 2 = 2`

## brackets

### brackets are added to the operator that should be prioritised.

example:
``` 
[1, 2, 5]
[*, (+), =]
```
would represent the equation `1 * (2 + 5) = 7`

### You  can also have more than one operator within a set of brackets

example:
``` 
[1, 2, 5, 7]
[/, (+, /), =]
```
would represent the equation `1 * (2 + 5 / 7) = 2.714`

### Nesting brackets also works

example:
``` 
[1, 2, 5, 7]
[/, ((+), /), =]
```
would represent the equation `1 * ((2 + 5) / 7) = 1`
