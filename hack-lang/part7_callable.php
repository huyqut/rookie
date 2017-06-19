<?hh

include 'utils.php';

//  CALLABLE
function one_by_one(array<int> $ints,
                    (function(int): int) $callable): array<int> {
    return array_map($callable, $ints);
}

function tenTimes(int $value): int {
    return $value * 10;
}

$input = [1, 2, 3, 4, 5];
//  Closure
pra(one_by_one($input, function(int $value): int {
    return $value * 10;
}));
//  Re-use another function
pra(one_by_one($input, fun('tenTimes')));

class Mather {
    public static function momTenTimes(int $value): int {
        return $value * 10;
    }

    public function myTenTimes(int $value): int {
        return $value * 10;
    }
}

$mather = new Mather();
//  Use a method from an instance
pra(one_by_one($input, inst_meth($mather, 'myTenTimes')));
//  Use a static method from a class
pra(one_by_one($input, class_meth(Mather::class, 'momTenTimes')));
//  Use a method from a class without using any instance (MUST be an empty parameter function)
// pra(one_by_one($input, meth_caller(Mather::class, 'myTenTimes')));
