<?hh

include 'utils.php';

//  Array (value only) initialization
$ids = [
    1, 3, 7, 9, 11,
    3, 9, 100, 1000
];
pra($ids);
pra($ids[0]); // Index based 0
pra($ids[3]);
$names = array(
    "Huy", 'Quang', "Tran"
);
pra($names);
pra($names[2]);

//  Array (key-value) initialization
$dict = [
    '1' => 'Huy',
    'Quang' => 3,
    2 => 'Tran'
];
pra($dict);
pra($dict['1']);
pra($dict[2]);
pra($dict['Quang']);

$mapper = array(
    99 => 'damn',
    'x' => 'it' //  MUST NOT set a key string that can be converted to another key int. They are treated the same.
);
pra($mapper);
pra($mapper['99']);
pra($mapper['x']);

//  Number of elements inside an array
pra(count($mapper));

//  Visit every element
//  `for` method
$length = count($names);
for ($i = 0; $i < $length; ++$i) {
    pra($names[$i]);
}

//  `foreach` method
//  Value only
foreach ($dict as $value) {
    pra($value);
}
//  Key-Value pairs
foreach ($dict as $key => $value) {
    pra($key);
    pra($value);
}

//  Check existence of a value inside the array
pra(in_array(7, $ids));
//  Check existence of a key/index inside the array
pra(array_key_exists(98, $mapper));

//  Sorting array by VALUE (indices and values are decoupled after being sorted)
$random_int = [
    9, 7, 3, 5
];
sort($random_int);
pra($random_int);
rsort($random_int);
pra($random_int); // Reverse order of sorting: Descending (default is ascending)
$random_str = [
    'this', 'is', 'sparta'
];
sort($random_str);
pra($random_str);
$mix_int = [
    99, '03', 15, '77',
];
sort($mix_int, SORT_NUMERIC); // values are typecasted to numeric and compared
pra($mix_int);
$mix_str = [
    99, '03', 15, '77',
    'tran', '.', ';', '^'
];
sort($mix_str, SORT_STRING); // values are typecasted to strings and compared
pra($mix_str);
$decoup = [
    '9' => 13,
    'tran' => 7,
    '0' => 14
];
pra($decoup);
sort($decoup);
pra($decoup);

//  Sorting array by KEY (flags of sorting is the same as above)
$dict = [
    '9' => 13,
    'tran' => 7,
    '0' => 14
];
ksort($dict);
pra($dict);
krsort($dict);  // Reverse sorting: Descending (default is ascending)
pra($dict);

//  Association Sorting array by VALUE (indices are still coupled with values after being sorted)
//  (Flags of sorting is the same as above)
$dict = [
    '9' => 13,
    'tran' => 7,
    '0' => 14
];
asort($dict);
pra($dict);
arsort($dict);  // Reverse sorting: Descending (default is ascending)
pra($dict);

//  User-defined sorting
//  compare < 0 => a < b
//  compare = 0 => a = b
//  compare > 0 => a > b
function cmp_int(int $a, int $b): int {
    if ($a < $b) {
        return 1;
    } elseif ($a == $b) {
        return -1;
    } else {
        return 0;
    }
}
usort($dict, cmp_int); // Sort by values
pra($dict);
function cmp_str(string $a, string $b): int {
    $c = count($a);
    $d = count($b);
    if ($c < $d) {
        return 1;
    } elseif ($c == $d) {
        return -1;
    } else {
        return 0;
    }
}
$dict = [
    'quang9' => 13,
    'tran' => 7,
    'huy0' => 14
];
uksort($dict, cmp_str); // Sort by keys
pra($dict);
uasort($dict, cmp_int); // Association sort by values (keys are kept)
pra($dict);

//  Get values only from the array
$values = array_values($dict);
pra($values);

//  Get keys only from the array
$keys = array_keys($dict);
pra($keys);

//  Push (at the end) of an array
$yummy = [ 1, 3, 5, 7, 9];
array_push($yummy, 10);
pra($yummy);
array_push($yummy, 99, 100, 101);
pra($yummy);

//  Pop (at the end) of an array: array_pop($array)
pra(array_pop($yummy));
pra($yummy);

//  Remove duplicates (by values) from the array: array_unique($array)
$dup = [ 1, 1, 2, 3, 4, 3, 2, 1 ];
pra(array_unique($dup));

//  Reverse an array: array_reverse($array)
pra(array_reverse($dup));

//  Copy a portion of the array: array_slice($array, $offset, $length)
pra(array_slice($dup, 0, 3)); // 1 1 2
pra(array_slice($dup, 2, 2)); // 2 3
pra(array_slice($dup, -3, 1)); // 3

//  Remove a portion of the array and replace it with something else
array_splice($dup, 6);
pra($dup); // 1 1 2 3 4 3
array_splice($dup, 1, 3, array(6, 7, 8, 9));
pra($dup); // 1 6 7 8 9 4 3

//  Merge multiple arrays
$merged = array_merge($dict, $dup, $yummy);
pra($merged);

//  Map
function mapper(int $variable) {
    return $variable * 10;
}
$mapped = array_map(mapper, $dup);
pra($mapped);
//  Reduce
function reducer($mixed, $carry) {
    return $mixed + $carry;
}
$reduced = array_reduce($mapped, reducer);
pra($reduced);
