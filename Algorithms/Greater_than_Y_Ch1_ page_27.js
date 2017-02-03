function greaterThanY (arr, Y){
  var count = 0;
    for(var i = 0; i < arr.length; i++){
      if(arr[i] > Y){
        arr[i] = 0;
          count++;
    }
   }
      console.log(count);
}
greaterThanY([1,3,5],0);
