<?php
//test username and password
$testUser = 'user';
$testPass = 'pass';
//get user input from index.php, set to null if none
$user = $POST['user']??null;
$pass = $POST['password']??null;
//check if user and password are correct
if ($user == $testUser && $pass == $testPass){
  //set logged in to true to track status
  $loggedIn=true;
  //allow the user to access the home page
  redirect('Location: rooms');
  exit();   
}
else{
  //set logged in to false to track status
  $loggedIn=False;
  //send or keep user at the login page
  header('Location: index');
  exit();
}
//function to ensure user is logged in
function checkLoggedIn(){
  if($loggedIn=false){
    //send or keep user at the login page
    header('Location: index'););
    exit();
  }
}
?>