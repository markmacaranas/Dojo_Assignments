function carConstructor(name, wheels, passengerNumber){
	var car = {};

	car.name = name || "BMW 325i";
	car.wheels = wheels || 4;
	car.passengerNumber = passengerNumber || 1;

	car.makeNoise = function(noise){
		var noise = noise || "Honk!";
		console.log(noise);
}
	return car;
}

var car = carConstructor();

var bike = carConstructor("bike", 2, 1);
bike.makeNoise = function(){
	console.log("ring ring!");
}

var sedan = carConstructor("sedan", 4, 5);
sedan.makeNoise = function(){
	console.log("Honk Honk!");
}

var bus = carConstructor("bus", 8, 20);
bus.pickupPassengers = function(newPassengers){
	bus.passengerNumber += newPassengers;
}

console.log(bus.passengerNumber);
bus.pickupPassengers(8);
console.log(bus.passengerNumber);

bike.makeNoise();
