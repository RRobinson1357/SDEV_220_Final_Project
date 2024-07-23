<?php
//include files from includes folder
include 'includes/header.php';
include 'includes/login.php';
include 'includes/dbAccess.php';
//Ensure the user is logged in
//checkLoggedIn($loggedIn);
//query for data
$sql = "SELECT * FROM ";
//save results
$resultSet = $db->query($sql);
?>
  <!DOCTYPE hmtl>
  <html lang="en">
    <head>
      <title>Rooms</title>
    </head>
      <body onload="load()">
       <!-- display database query results-->
      <?php while ($result = $resultSet->fetch(PDO::FETCH_ASSOC)) : ?>
          <?php endwhile ?>
  </body>
  </html>
</html>