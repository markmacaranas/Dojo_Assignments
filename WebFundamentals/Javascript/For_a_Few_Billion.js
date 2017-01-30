// There is an old tale about a king who offered a servant $10,000 as a reward.
// The servant instead asked that for 30 days he be given an amount that would double, starting with a penny.
// (1 penny for the first day, 2 for the second, 4 for the third, then 8, 16, 32 pennies, and so on).
function reward30Days(){
var pay = 0.01;
var reward = 0;
for(var i = 1; i <= 30; i++){
    console.log(pay);
    reward += pay;
    pay *= 2;

    console.log(reward);
  }
}
reward30Days();
 // on the 30th day, the servant would get a reward of $10,737,418.23!

// How many days would it take the servant to make $10,000?
function daysTo10000(){
var pay = 0.01;
var reward = 0;
var day = 0;
  while(reward <= 10000){
    reward += pay;
    pay *= 2;
    day++;
      }
      console.log(day);
 }
daysTo10000();
// The servant would make $10,000 in 20 days!

// How many days would it take the servant to make $1,000,000,000?
function daysToBillion(){
var pay = 0.01;
var reward = 0;
var day = 0;
  while(reward <= 1000000000){
    reward += pay;
    pay *= 2;
    day++;
      } 
      console.log(day);
 }
daysToBillion();
// The servant would make $1,000,000,000 in 37 days!

// How many days would it take the servant to have infinite money?
function daysToInfinity(){
var pay = 0.01;
var reward = 0;
var day = 0;
  while(reward<Infinity){
    reward += pay;
    pay *= 2;
    day++;
      }
      console.log(day);
      console.log("testing");
 }
daysToInfinity();
// The servant would make infinity money for 1,031 days!
