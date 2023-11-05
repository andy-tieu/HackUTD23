<?php
    $dbHost = 'your_instance_connection_name';
    $dbUser = 'your_database_username';
    $dbPass = 'your_database_password';
    $dbName = 'your_database_name';
    
    // Create a connection
    $conn = new mysqli($dbHost, $dbUser, $dbPass, $dbName);

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Retrieve form data using $_POST
        $fName = $_POST["fName"];
        $lName = $_POST["lName"];
        $email = $_POST["email"];
        $creditScore = $_POST["creditScore"];
        $grossIncome = $_POST["grossIncome"];
        $mortgage = $_POST["mortgage"];
        $creditCardPay = $_POST["creditCardPay"];
        $carPay = $_POST["carPay"];
        $studentLoans = $_POST["studentLoans"];
        $password = $_POST["password"];
    }
    
    // Check the connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
?>