<?php
    $dbHost = 'your_instance_connection_name';
    $dbUser = 'your_database_username';
    $dbPass = 'your_database_password';
    $dbName = 'your_database_name';
    
    // Create a connection
    $conn = new mysqli($dbHost, $dbUser, $dbPass, $dbName);
    
    // Check the connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
?>