function flexibleCountdown(lowNum, highNum, mult){

  for (var i = lowNum; i <= highNum; i++){
    if(i % 3 == 0){
      console.log(i);
    }
  }
}

flexibleCountdown(2, 9, 3);
