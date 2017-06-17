<?hh

include 'utils.php';

//  Simple `if`
if (true) {
    pra("It must be true");
}
$a = true;
$b = 10;
$c = 9.99;
//  `if` with `else`
if ($a && !($b == 10 || ($c < 100.0 ^ false))) {
    pra("I'm not sure if this is right");
} else {
    pra("Yo! It must be wrong");
}

//  `elseif`
if ($a == false) {
    pra("Not this one");
} elseif ($b < 9) {
    pra("Not this one also");
} else {
    pra("Yup! This is it! Eat this shit!");
}

//  `switch`
switch ($b) {
    case 100:
        pra("Yaya");
        break;
    case 1:
        pra("Papa");
        break;
    default:
        pra("Yolo");
        break;
}
