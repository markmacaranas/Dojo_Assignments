function arrayRotate(arr,shiftBy){

for (var i = 0; i < arr.length; i++){
	arr[i + shiftBy] = arr[i];

	}
		console.log(arr);

}
arrayRotate([1,3,5],1);
