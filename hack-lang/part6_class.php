<?hh

include 'utils.php';

class HackLang {
    //  Constants (currently not supported access modifers: public, private, protected)
    const string HELLO = "Hello";
    //  Static Properties - All static properties must be initialized by assignment
    public static int $integer = 10;
    private static string $document = "Hello World";

    //  Static methods: can be called by `Class::method([arguments])`
    public static function from(): string {
        return "Facebook";
    }

    //  Properties - All properties must be initialized in constructor
    public $ids;
    private bool $yes;
    private float $ratio;

    //  Constructor
    public function __construct(int $yep) {
        // `this` refers to current instance
        $this->ids = function() {
            return [1, 2, 3, 4];
        };
        $this->yes = true;
        $this->ratio = 0.375;
        pra($yep);
    }

    //  Public methods: can be invoked as ""
    public function getRatio(): float {
        return $this->ratio;
    }

    public function setRatio(float $ratio) {
        $this->ratio = $ratio;
    }
}

pra(HackLang::HELLO);
pra(HackLang::$integer);
pra(HackLang::from());
$lang = new HackLang(10); // Create new instance
pra($lang->getRatio());
pra(($lang->ids)()); // Property

//  `instanceof` operator: check if an instance belongs to a class
$dummy = 99;
pra($dummy instanceof HackLang);
pra($lang instanceof HackLang);

//  `class` operator: Name of a class
pra(HackLang::class);

//  Object in Hack is a reference-type object. The object only stores the address to the real object.
//  This model does NOT apply to primitive types: int, bool, float, string
$another = $lang;  // $another does NOT create a new object. It refers to the same object as $lang.
pra($another->getRatio());
$lang->setRatio(99.99); // $lang changes => $another changes (They refer to the same thing).
pra($another->getRatio());
pra($another == $lang); // 2 objects equal if their properties are equal
pra($another === $lang); // 2 objects refer to the same thing

//  Reference variable - $ref and $lang is the same object, just different name.
$ref = &$lang;
pra($another->getRatio());
pra($ref->getRatio());
$lang = null;
pra($another->getRatio()); // $another is OK because it stills point to the same object that $lang left.
pra($ref); // $ref is also null right now because $lang is set to null.

//  Cloning - a new object is cloned
$other = clone $another;
pra($other->getRatio());
$another->setRatio(13.13);
pra($other->getRatio());
pra($other == $another);
pra($other === $another);

class Replicant {
    public HackLang $anotherLang;
    public function __construct() {
        $this->anotherLang = new HackLang(1);
    }
    public function __clone() {
        //  Force deep copy
        $this->anotherLang = clone $this->anotherLang;
    }
}

$rep1 = new Replicant();
$rep2 = clone $rep1;
pra($rep2->anotherLang->getRatio());
$rep1->anotherLang->setRatio(11.11);
pra($rep2->anotherLang->getRatio()); // 0.375. Without __clone(), it would be 11.11.

//  INHERITANCE
class BaseClass {
    const string MR_X = "xXx";
    public int $age;
    private string $name;
    protected float $credit;

    public function __construct() {
        pra("Base Class");
        $this->age = 11;
        $this->name = "Huy Tran";
        $this->credit = 13.99;
    }

    public function getData() { // To be overriden
        return "From Parents with Love";
    }

    public final function blockChild() { // NOT to be overriden
        return "Block all inheritance";
    }

    public function parentVisible() {
        pra($this->age);
        pra($this->name);
        pra($this->credit);
    }

    public function playWith(BaseClass $temp) {
        // An instance can access to another instance of the same class
        $temp->name = "HoeHoeHoe";
    }
}

class SubFirst extends BaseClass { // `extends` keyword is used to inherit 
    public function __construct() {
        parent::__construct();
        pra("Sub First");
    }

    public function getData() { // Override parent method
        return "From First Child with Love";
    }

    //  Compile Error: the parent's method declared as `final`
    // public function blockChild() {
    //     return "Sup Yo?";
    // }
}

class SubSecond extends BaseClass { // Allow multiple inheritance too
    const string MR_X = "XxX";  // Constants can also be overriden
    public function getData() { // Call parent's method
        return parent::getData() . " and the 2nd Child";
    }

    public function childVisible() {
        pra($this->age); // Fine
        //pra($this->name); // Error
        pra($this->credit); // Fine
    }
}

final class FinalWord {

}

// class AfterFinalWord extends FinalWord {} => Error: Cannot extend final class

$base = new BaseClass();  // BaseClass->__construct()
$sub_first = new SubFirst(); // BaseClass->__construct() && SubFirst->__construct()
$sub_second = new SubSecond(); // BaseClass->__construct()

//  Access modifiers: The same rule is applied for both properties and methods
pra($base->getData());
pra($sub_first->getData());
pra($sub_second->getData());

$base->parentVisible(); // Fine - Everything is visible to parent
$sub_second->parentVisible(); // Fine - Child uses method from parent so it can access parent's properties
$sub_second->childVisible(); // Only see public and protected

pra($base::MR_X);
pra($sub_second::MR_X);

//  Abstract classes
abstract class AbstractClass {
    abstract public function shout();
    abstract protected function dodo();
    // abstract private function lolo(); => Error: children cannot see `private` parts of parents
    // so they cannot override them.

    public function shutUp() {
        pra("Hello");
    }
}

class ConcreteClass extends AbstractClass {
    public function __construct() {}
    public function shout() {
        return "Peep";
    }

    protected function dodo() {
        return "Oops";
    }
}

function testAbstract(AbstractClass $cls) {
    pra($cls->shout());
}

//testAbstract(new AbstractClass()); => Error: Abstract class cann create instance.
testAbstract(new ConcreteClass());

// Interface

interface PresidentSafety {
    const ALERT = "Yellow"; // Interface can declare constants
    //protected int $yes; => Error: Interface cannot contain variables
    public function prepareLimousine(); // Can only declare public interface
}

interface FBI {
    public function yolo();
}

interface MayorSafety extends PresidentSafety, FBI { // Allow multiple inheritance too
    public function yala();
}

class SecretService implements PresidentSafety {
    public function prepareLimousine() {
        pra("Safe car");
    }
}

class PublicService implements MayorSafety {
    public function yolo() {
        pra("Yolo");
    }

    public function yala() {
        pra("Yala");
    }

    public function prepareLimousine() {
        pra("Mayor dooms");
    }
}

function testSingleInterface(PresidentSafety $ss) {
    $ss->prepareLimousine();
    pra($ss::ALERT);
}

function testFBI(FBI $fbi) {
    $fbi->yolo();
}

function testMayorSafety(MayorSafety $ms) {
    $ms->prepareLimousine();
    $ms->yolo();
    $ms->yala();
}

testSingleInterface(new SecretService());
testFBI(new PublicService());
testMayorSafety(new PublicService());

trait Executive {
    // Must have at least 1 require
    require extends ConcreteClass;
    require implements FBI;

    public function power() {
        $this->shutUp();
        pra($this->dodo());
        $this->yolo();
    }
}

class Traitor extends ConcreteClass implements FBI {
    use Executive; // Allow to use multiple traits

    public function yolo() {
        pra("Yup and Nope");
    }
}

$traitor = new Traitor();
$traitor->power();
