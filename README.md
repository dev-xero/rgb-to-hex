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

## MIT License
Copyright (c) 2022 CodeNinja-tech

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

<br />
<br />

Made with ☕ and Python
