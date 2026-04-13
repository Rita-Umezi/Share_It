<?php
if(isset($_POST['name']) && isset($_POST['height']) && isset($_POST['weight'])) {
    $name = $_POST['name'];
    $height = $_POST['height'];
    $weight = $_POST['weight'];
    
    // Calculate BMI
    $bmi = $weight / ($height * $height);

    if ($weight >= 25 && $weight <= 30) {
        echo "Recommended food: Rice and fish";
    } elseif ($weight > 30 && $weight <= 45) {
        echo "Recommended food: Boiled yam and cereal";
    } elseif ($weight > 45 && $weight <= 60) {
        echo "Recommended food: Amala and ogunfe";
    } elseif ($weight > 60 && $weight <= 70) {
        echo "Recommended food: Egg, cereal, milk";
    } elseif ($weight > 70 && $weight <= 90) {
        echo "Recommended food: Beans, moinmoin, watermelon";
    } else {
        echo "Recommended food: Vineless seed grape";
    }
}
?>
