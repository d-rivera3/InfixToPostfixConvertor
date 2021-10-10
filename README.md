# InfixToPostfixConvertor

Write a program that converts expressions in “normal” infix notation into postfix (i.e., RPN, notation). Support the 
following operators (based on the C language standard table of operators):

- Level 1 

| Operator | Description |
| :---: | --- |
| `()` | function expression    |
| `[]` | array expression       |

- Level 2

| Operator | Description |
| :---: | --- |
| - | unary minus (minus sign)  |
| + | unary plus (plus sign)    |
| ~ | bitwise inverse           |
| ! | logical inverse           |

- Level 4

| Operator | Description |
| :---: | --- |
| * | multiplication  |
| / | division        |
| % | modulus         |

- Level 5

| Operator | Description |
| :---: | --- |
| - | subtraction | 
| + | addition    |

- Level 6

| Operator | Description |
| :---: | --- |
| <<                | shift left    |
| &#62;&#62;        | shift right   |
| <<<               | rotate left   |
| &#62;&#62;&#62;   | rotate right  |

- Level 7

| Operator | Description |
| :---: | --- |
| <         | less than                 |
| &#62;     | greater than              |
| <=        | less than or equal to     |
| &#62;=    | greater than or equal to  |

- Level 8

| Operator | Description |
| :---: | --- |
| == | equal to       | 
| != | not equal to   |

- Level 9

| Operator | Description |
| :---: | --- |
| & | bitwise AND |

- Level 10

| Operator | Description |
| :---: | --- |
| ^ | bitwise XOR |

- Level 11

| Operator | Description |
| :---: | --- |
| &#124; | bitwise OR  |


- Level 12

| Operator | Description |
| :---: | --- |
| && | logical AND    |

- Level 13

| Operator | Description |
| :---: | --- |
| ^^ | logical XOR    |

- Level 14

| Operator | Description |
| :---: | --- |
| &#124;&#124; | logical OR |

Note that the equality relational operator, ‘==’, replaces the original ‘=’. This is to eventually
permit assignment operators to serve as expression operators as well.


The input to the program will come from the file **_infix.txt_** with one expression per line. 
The output should be contained in two files:
1. The first is ***postfix.txt*** with one RPN expression per line 
2. The other is ***results.txt*** which contains the result of evaluating the RPN expression. 

A given line number in each of the three files should all refer to the same expression. If the program
cannot handle a particular line, it needs to output something for that line. Either
output whatever results, or output “ERROR” to the RPN file and “NaN” to the results
file.

For simplicity, the expression operands will be either function calls or non-negative 16-bit
singed integers (i.e., values between 0 and +32767, inclusive). The answers should be 16-bit
signed integers (i.e., values between -32768 and +32767, inclusive). The evaluations should
reflect the use of 16-bit arithmetic, meaning that overflow in either direction should result in
“wrapping around”; thus 32767 + 1 should result in -32768.

The only functions that you need to support in your evaluations are:
- sq(x)
  >sq(x) function returns the square of x
- abs(x)
  >abs(x) function returns the absolute value of x
- min(x,y)
  >min(x,y) function returns the minimum value of x and y
- max(x,y)
  >the max(x,y) function returns the larger of the two values.

As usual, the relational and logical operators return 0 for false and -1 for true.

The format of postfix.txt file should be comma delimited with no spaces.

For, for example, the input
>2 * sq(123 – 234) << 36 % 17

should yield
>2,123,234, –,sq,*,36,17,%,<<

Note that the result of this is -32504. Be sure you understand why this is the case.