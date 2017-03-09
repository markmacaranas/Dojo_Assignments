function NinjaConstructor(name, prevOccupation) {
  this.name = name;
  this.prevOccupation = prevOccupation;
  this.introduce = function() {
    console.log("Hi my name is " + this.name + ". I used to be a " + this.prevOccupation + " and now I'm a Ninja!");
  }
}
var dylan = new NinjaConstructor('Dylan', 'Construction Worker');
console.log(this);
var nikki = NinjaConstructor('Nikki','Historian');

if (!(this instanceof NinjaConstructor)) {

	return new NinjaConstructor(name, prevOccupation);
}
