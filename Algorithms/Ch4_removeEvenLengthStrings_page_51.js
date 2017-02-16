function removeEvenLengthStrings (arr){
var i = 0;
while(i < arr.length){
	var temp = arr[i].split("");
	if(temp.length % 2 === 0 ){
		for(var x = i; x < arr.length-1; x++){
			arr[x] = arr[x + 1];
			}
			arr.pop();
		}
	else {
		i++;
	}
	}
			return arr;
}

console.log(removeEvenLengthStrings(["Nope!","Its","four","Kris","starting","time","with","K!","hi"]));
