<?hh

function pra(mixed $par): void {
    echo "<pre>";
    var_dump($par);
    echo "</pre>";
}
//  PRIMITIVE TYPES

//  Boolean
echo "Boolean";
$boolean = true;
pra($boolean);
$boolean = false;
pra($boolean);
$negation = !$boolean;
pra($negation);
$and = $negation && $boolean;
pra($and);
$or = $negation || $boolean;
pra($or);
$xor = $negation xor $boolean;
pra($xor);
$complex_boolean = !($negation || $and) && $or;
pra($complex_boolean);

//  Integer
echo "Integer";
$integer = 10;
pra($integer);
$negation = -$integer;
pra($negation);
$addition = 10 + $integer;
pra($addition);
$subtraction = $integer - 10;
pra($subtraction);
$multiplication = $integer * 99;
pra($multiplication);
$integer_division = intdiv(99, $integer);
pra($integer_division);
$integer_modulo = 99 % $integer;
pra($integer_modulo);
$int_expo = $integer ** 9;
pra($int_expo);

//  Float
echo "Float";
$float = 9.3;
pra($float);
$negation = -$float;
pra($negation);
$addition = $float + 8;
pra($addition);
$subtraction = 36.5 - $addition;
pra($subtraction);
$multiplication = $addition * $subtraction;
pra($multiplication);
$float_division = $multiplication / $negation;
pra($float_division);
$float_expo = $subtraction ** $addition;
pra($float_expo);
//  Using modulo operator on float types result in unexpected value.

//  String (will receive individual chapter on this)
$str = "Hello World";
pra($str);
$cat = "Meow" . $str . "Yup";
pra($cat);

//  TRICKS

//  Get type of a variable:
pra(gettype($str));
pra(gettype($integer));
pra(gettype($float_expo));
pra(gettype($boolean));

//  Self operator
//  a `op`= b is the same as a = a `op` b
$cat .= $str;
pra($cat);
$int_expo += 2;
pra($int_expo);
$float_expo /= 100;
pra($float_expo);