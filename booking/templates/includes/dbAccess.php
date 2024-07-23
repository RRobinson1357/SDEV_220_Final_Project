<?php
//locate the database
define('DB_DRIVER','sqlite');
define('DB_PATH', $_SERVER['DOCUMENT_ROOT'] . '/db.sqlite3');
//set the database name
$dsn = DB_DRIVER . ':' . DB_PATH;
//create new pdo object
$db = new PDO($dsn);