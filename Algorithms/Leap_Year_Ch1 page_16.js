function leapYear(i){
  if(i % 4 == 0){
      console.log('Leap Year');
  }
  else if(i % 100 == 0){
      console.log('Not Leap Year');
  }
  else if(i % 400 == 0){
      console.log('Leap Year');
  }
  else {
      console.log('Not Leap Year');
  }
}

leapYear(2000);
