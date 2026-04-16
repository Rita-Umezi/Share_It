<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Work Info</title>
</head>
<body>
<form action="workpayment.php" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name"><br><br>

<!--gender should be a dropdown menu-->
    <label for="gender">Gender:</label>
    <select id="gender" name="gender">  
        <option value="male">Male</option>
        <option value="female">Female</option>
        <option value="other">Other</option>
    </select><br><br>

       <label for="days">Days Worked:</label>
    <input type="text" id="days" name="days"><br><br>

    <label for="hours">Hours Worked:</label>
    <input type="text" id="hours" name="hours"><br><br>

    <label for="mins">Minutes Worked:</label>
    <input type="text" id="mins" name="mins"><br><br>

    <label for="secs">Seconds Worked:</label>
    <input type="text" id="secs" name="secs"><br><br>

    <label for="date">Date:</label>
    <input type="date" id="date" name="date"><br><br>   
    <input type="submit" value="Calculate Pay" name="submit">

    <button type="reset">Reset</button>

</form>
</body>
</html>