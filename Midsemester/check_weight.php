<?php
include('database.php');

if(isset($_POST['name']) && isset($_POST['height']) && isset($_POST['weight'])) {
    $name = $_POST['name'];
    $height = $_POST['height'];
    $weight = $_POST['weight'];
    
    // Calculate BMI
    $bmi = $weight / ($height * $height);

    if ($bmi >= 0.5&& $bmi<= 1) {
        $food = "Rice and fish";
    } elseif ($bmi > 1 && $bmi <= 1.5) {
        $food = "Boiled yam and cereal";
    } elseif ($bmi > 1.5 && $bmi <= 2) {
        $food ="Sliming Tea";
    }

    $sql = "INSERT INTO calculatebmi(bmi_id, name, weight, height, food, bmi) 
    value('0','$name', '$weight', '$height', '$food', '$bmi')";
    /*this is like assigning the value in the php part to  the value in the database, 
    INSERT INTO is the function, calculatebmi is the name of the databse, 
    what is in the bmi is what is in the database
    what is in the value is what is in the code*/

    if(mysqli_query($conn, $sql)){
        header('Location: thankyou.php');
    }
}
?>
