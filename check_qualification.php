<?php
if(isset($_POST['level']) && isset($_POST['weight']) && isset($_POST['school'])) {
    $level = $_POST['level'];
    $weight = $_POST['weight'];
    $school = $_POST['school'];
}
$qualified = false;
if($school === 'computing') {
    if($level == '100' && $weight >= 50 && $weight <= 60) {
        $qualified = true;
    } elseif($level == '200' && $weight >= 70 && $weight <= 80) {
        $qualified = true;
    } elseif($level == '300' && $weight <= 90) {
        $qualified = true;
    } elseif($level == '400' && $weight <= 100) {
        $qualified = true;
    }
}
?>
