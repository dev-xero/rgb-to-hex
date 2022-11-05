# RGB to HEX code
Python script to convert an RGB text sequence into HEX Code

So this simple python script converts a comma separated input rgb string into hex code  
The format for the input looks something like this: `255, 255, 255`  
Assuming that is the input, the output would be this: `0xffffff`  

## Formatting
There's also an additional formatting option that changes the default format a little  
There are two options available currently:
- `native (DEFAULT)` and
- `color`  


#### `color mode`
Input: (255, 255, 255), 'color'  
Output: #FFFFFFF

#### `native mode`
Input: (255, 255, 255), 'native' (can be omitted)  
Output: 0xffffff

Any other mode will default to **native mode**  
<br />

Made with ☕ and Python
