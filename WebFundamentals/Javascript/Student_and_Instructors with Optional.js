// Given the following array of objects:
//
// var students = [
//      {first_name:  'Michael', last_name : 'Jordan'},
//      {first_name : 'John', last_name : 'Rosales'},
//      {first_name : 'Mark', last_name : 'Guillen'},
//      {first_name : 'KB', last_name : 'Tonel'}
// ]
// Create a program that outputs:
//
// Michael Jordan
// John Rosales
// Mark Guillen
// KB Tonel



var users = {
 'Students': [
     {first_name:  'Michael', last_name : 'Jordan', num: '13'},
     {first_name : 'John', last_name : 'Rosales', num: '11'},
     {first_name : 'Mark', last_name : 'Guillen', num: '11'},
     {first_name : 'KB', last_name : 'Tonel', num: '7'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi', num: '11'},
     {first_name : 'Martin', last_name : 'Puryear', num: '13'}
  ]
 }
      console.log("Students");
          for(var i = 0; i < users.Students.length; i++){
          console.log(i + 1 + ' - ' + users.Students[i].first_name +" "+ users.Students[i].last_name + " - " + users.Students[i].num);
          }
      console.log("Instructors");
          for(var i = 0; i < users.Instructors.length; i++){
          console.log(i + 1 + ' - ' + users.Instructors[i].first_name +" "+ users.Instructors[i].last_name + " - " + users.Students[i].num);
          }
