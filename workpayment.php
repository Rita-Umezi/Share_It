<!-- Babcock university consulted you to develop a systen that will calculate the take home of a Software Engineer,
  if he works for 30 days, 52 hours, 45 minutes and 23 seconds,
Print the amount of time the Software Engineer work in seconds. The price per seconds for a Software Engineer to work is 1,000 Naira due to the amount. -->
<?php 

// $number_of_days = 30;
// $hours = 52;
// $minutes = 45;
// $seconds = 23;
// $amount = 1000;

// $day_converter = $number_of_days*24*60*60;
// $hour_converter = $hours*60*60;
// $minutes_converter = $hours*60;

// $total_time = $day_converter+$hour_converter+$minutes_converter + $seconds;

// $workdone_in_seconds = $total_time * $amount;

// echo "<h1>The takehome for the Software Engineer is N". $workdone_in_seconds. " Thank You</h1>";
if (isset($_POST['submit'])) 
  
$name = $_POST['name'];
$gender=($_POST['gender']);
$days=($_POST['days']);
$hours=($_POST['hours']);
$mins=($_POST['mins']);
$secs=($_POST['secs']);
$date=($_POST['date']);

echo "Your name is: ". $name. "<br>";
echo "Your gender is ".$gender."<br>";
?>