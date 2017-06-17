<?hh

include 'utils.php';

//  String initialization
$str = "Hello World";
pra($str);

//  Get a character from ASCII value
pra(chr(48));

//  Get ASCII value from a character
pra(ord('a'));

//  Lower-case a string
pra(strtolower("This is it"));

//  Upper-case a string
pra(strtoupper("This is it"));

//  Length of a string
pra(strlen($str));

//  Traverse each character of the string
$length = strlen($str);
for ($i = 0; $i < $length; ++$i) { // cannot use `foreach` with string
    echo $str[$i];
}

//  Count number of chars and map it to an array (based on every char in 256 ASCII)
pra(count_chars($str)); // default is mode 0
pra(count_chars($str, 1)); // Same as 0 but only list chars that have counts > 0
pra(count_chars($str, 2)); // Same as 0 but only list chars that have counts = 0

//  Reverse a string
pra(strrev($str));

//  String comparison
//  < 0: lexicographically less than in order
//  = 0: 2 strings are the same
//  > 0: lexicographically greater than in order
pra(strcmp("Yes", "No"));

//  Trim white space at the beginning of the string
pra(ltrim("   Yes"));

//  Trim white space at the end of the string
pra(rtrim("Yes    "));

//  Apply both `ltrim` and `rtrim`
pra(trim("   Yess   "));

//  Substring
pra(substr($str, 0, 3));
pra(substr($str, 1, 1));
pra(substr($str, -3, 2)); // negative means the offset from the end: -3 = length - 3

//  Substring counts
pra(substr_count($str, "l", 1, 5));

//  Split a string into an array
pra(str_split($str)); // default step is 1
pra(str_split($str, 3));
