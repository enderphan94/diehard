# diehard
RNG tests - compiled C project

# Compile

$ `make`

it returns an error of "return". So just follow the message to adjust the `return;` to `return 0` and `complile` it again.

Tested: MacOS

# Execution

1. Compiling the RNG code to get the output file which should be presented as an ASCII format in this case.
2. Run command 
`dieharder -a -g 202 -f output.txt` //switch to `-g 201` if the file saved in binary format
```
-a runs all the tests with standard/default options to create a user-controllable report
-f filename - generators 201 or 202 permit either raw binary or formatted  ASCII  numbers  to  be read in from a file for testing
-g generator number - selects a specific generator for testing
```

# Windows

Download the `diehard.zip` file

# Note:

There is a `dieharder` tool, install it by `brew install dieharder`

# Refs:

https://web.archive.org/web/20160125103112/http://stat.fsu.edu/pub/diehard/
