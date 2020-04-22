<?php
$dbhost = 'db';
$dbuser = 'root';
$dbpass = 'test123';
$dbname = 'countdb';

$c = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname) or 
   die("Unable to Connect to db: " . mysqli_connect_error() . ' (' . mysqli_connect_errno() . ')');

if (mysqli_query($c,'INSERT INTO counter SET data = "dummy"') === TRUE) {
} else {
  echo "Error: " . mysqli_error($c);
}

echo "Counter: ". mysqli_insert_id($c)."\n";
mysqli_close($c);

