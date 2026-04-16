<!-- BUCC is planning a football game for male and female, you're consulted to develop a system that will determine if a student is qualified to play based on their weight and their level 
The condition are;
If student in 100 lvl and weight is 50-60 kg: qualified to play 
200 lvl and weight 70-80kg: qualified to play 
300 lvl not more than 90
400lvl  not more than 100 kg
Student most be in school of computing -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BUCC Football Game Qualification</title>
</head>
<body>
    <h1>BUCC Football Game Qualification</h1>
    <form action="check_qualification.php" method="post">
        <label for="level">Level:</label>
        <select name="level" id="level" required>
            <option value="100">100</option>
            <option value="200">200</option>
            <option value="300">300</option>
            <option value="400">400</option>
        </select>
        <br><br>
        <label for="weight">Weight (kg):</label>
        <input type="number" name="weight" id="weight" step="0.1" min="0" required>
        <br><br>
        <label for="school">School:</label>
        <select name="school" id="school" required>
            <option value="computing">School of Computing</option>
            <!-- Add other schools if needed -->
        </select>
        <br><br>
        <input type="submit" value="Check Qualification">
    </form>
</body>
</html>