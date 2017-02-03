function max_Min_Avg (arr){
  var max = arr[0];
  var min = arr[0];
  var sum = arr[0];

    for(var i = 1; i < arr.length; i++){
      if(arr[i] > max){
        max = arr[i];

      if(arr[i] < min){
        min = arr[i];

        sum += arr[i];
    }
  }
}
    var avg = sum/arr.length;
    var arrnew = [max,min,avg];
      return arrnew;
}

console.log(max_Min_Avg([1,3,5,7,9]));
