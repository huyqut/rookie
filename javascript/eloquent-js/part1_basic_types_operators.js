/**
 * BASIC DATA TYPES IN JAVASCRIPT
 */

// Print a message
console.log("Hello World");

// BOOLEANS
console.log(true);
console.log(false);
let bool = true;
console.log(bool);
let other = false;
let or = bool || other;
console.log(or);
let and = bool && other;
console.log(and);
let not = !other;
console.log(not);

// NUMBERS (64 bits)
console.log(10);
console.log(20 * 3 - 7 / 2);
let integer = 123;
console.log(integer);
let float = 321.798;
let num_add = integer + float;
console.log(num_add);
let num_sub = integer - float;
console.log(num_sub);
let num_mul = integer * float;
console.log(num_mul);
let num_div = integer / float;
console.log(num_div);
let num_rem = integer % float;
console.log(num_rem);
let big_num = 2.648e13;
console.log(big_num);
let hexa = 0x123;
console.log(hexa);
console.log(NaN); // Not a number
console.log(Infinity); // Infinity

// STRINGS
let str_double = "Go to hell!";
let str_single = 'Go to well!';
console.log(str_double);
console.log(str_single);
let concat = str_double.concat(str_single);
console.log(concat);
let multi_concat = "Yes" + concat + "No" + str_double + str_single + "Maybe?";
console.log(multi_concat);
let str_length = multi_concat.length;
console.log(str_length);
let trim = "  fdsa   ".trim();
console.log(trim.length);
let upper = concat.toUpperCase();
console.log(upper);
let lower = concat.toLowerCase();
console.log(lower);
let char6 = lower.charAt(6);
console.log(char6);
let asciiChar6 = lower.charCodeAt(6);
console.log(asciiChar6);

// TYPE
console.log(typeof bool);
console.log(typeof float);
console.log(typeof char6);

console.log(parseInt("123"));
console.log(parseInt("123.321"));
console.log(parseInt("123.987"));
console.log(parseInt("   321 "));
console.log(parseInt("123xyz"));
console.log(parseInt("xyz123"));
console.log(parseInt("0x123", 16)); // Hexadecimal
console.log(parseInt("0123", 8));

console.log(parseFloat("321"));
console.log(parseFloat("321.123"));
console.log(parseFloat("321.987"));
console.log(parseFloat("   777.666 "));
console.log(parseFloat("333.333.333"));
console.log(parseFloat("333.222abc"));
console.log(parseFloat("abc333.33"));

let str_from_num = num_add.toString();
console.log(typeof str_from_num);

// COMPARISON
// Lose Equality (If not the same type, a value can be converted to another type to compare)
console.log(123 == 123); // True
console.log(123 == '123'); // True
console.log('123' == '123'); // True
console.log('abc' == 'xyz'); // False
console.log(' 123 ' == 123); // True
console.log(+0.0 == -0.0);
console.log(null == null); // True
console.log(undefined == undefined); // True
console.log(NaN == NaN); // False

console.log();
// Strict Equality (2 operands must belong to the same type)
console.log(123 === 123);
console.log(123 === '123');
console.log('123' === '123');
console.log('abc' === 'xyz');
console.log(' 123 ' === 123);
console.log(+0.0 === -0.0);
console.log(null === null); // True
console.log(undefined === undefined); // True
console.log(NaN === NaN); // False

console.log();
// Same-value => Use `Object.is()` method

// BIT-WISE OPERATORS
let bitAnd = 123 & 321;
console.log(bitAnd);
let bitOr = 123 | 312;
console.log(bitOr);
let bitNeg = ~123;
console.log(bitNeg);
let bitXor = 123 ^ 321;
console.log(bitXor);
let bitLShift = 123 << 12; // Max shift is 64
console.log(bitLShift);
let bitRShift = -123 >> 1; // Max shift is 64
console.log(bitRShift);
let bitURShift = -123 >>> 1; // Max shift is 64
console.log(bitURShift);

// ASSIGNMENT OPERATORS
let me = 123;
me += 333;
me -= 222;
me *= 333;
me /= 222;
me %= 111;
me |= 3123;
me &= 2312;
me ^= 1233;

// TRICKS
// Convert decimal to binary
console.log((123 >>> 0).toString(2));
console.log((-123 >>> 0).toString(2));
