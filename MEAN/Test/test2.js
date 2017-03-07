//declarations get hoisted
var hello;
function example() {
  var hello;
  hello = "hi";
  console.log(hello);
}
//assignments and invocation maintain order
hello = "interesting";
example();
console.log(hello);
