function CarConstructor(name, wheels, passengerNumber, speed){
	if (!(this instanceof CarConstructor)){
		return new CarConstructor(name, wheels, passengerNumber, speed);
	}

	var distanceTraveled = 0;
	var self = this;
	function updateDistanceTraveled(){
		distanceTraveled += self.speed;
		console.log(distanceTraveled);
	}
	this.speed = speed;
	this.name = name || "BMW 325i";
	this.wheels = wheels || 4;
	this.passengerNumber = passengerNumber || 1;

	this.makeNoise = function(noise){
		var noise = noise || "Honk!";
		console.log(noise);
	}
	this.move = function(){
		this.makeNoise();
		updateDistanceTraveled();
	}
	this.checkMiles = function(){
		console.log(distanceTraveled);
	}

}

var car = CarConstructor("car", 4, 2, 40);
car.move();
car.checkMiles();
console.log(car.speed);
