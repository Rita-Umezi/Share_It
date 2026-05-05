<?php

include ('cont.php');

if(isset($_POST['submit'])){

    $name = $_POST['name'];
    $weight = $_POST['weight'];
    $height = $_POST['Height'];
    $bmi = $weight/($height*$height);

    if($bmi>=0.5&& $bmi<=1){
        $food="Rice";
    }
    elseif($bmi>1 && $bmi<=1.5){
        $food ="yam";
    }
    elseif($bmi>1.5 && $bmi<=2){
        $food="Sliming tea";
    }

$sql="INSERT INTO cal_bmi(bmi_id,name,weight,height,food,bmi)
value('0','$name','$weight','$height','$food','$bmi')";

if(mysqli_query($ledor,$sql)){
    header('location:thankyou.php');
}


}
?>