<?hh

include 'utils.php';

//  `do while` loop
$i = 10;
do {
    pra($i);
    ++$i;
} while ($i < 10);

//  `while` loop
$i = 0;
while ($i < 10) {
    pra($i);
    ++$i;
}

//  `for` loop
for ($j = 0; $j < 3; ++$j) {
    pra($j);
}

//  `continue` and `break` keyword (can be used with `while`, `do while`, `for`, `foreach`)
$a = true;
$b = false;
while ($a) {
    if ($b) {
        $b = false;
        continue;
    } else {
        break;
    }
    ++$i;
}

//  `goto`
//  Use `goto` to replace `while`:
// $i = 0;
// goto condition;
// my_loop:
// pra($i);
// ++$i;
// condition:
// if ($i < 10) {
//     goto my_loop;
// }
