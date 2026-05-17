<!-- code to check user weight and display food recommendation based on weight range
 25-30: RIce and fish
 30-45: boiled yam
 45-60: amala and ogunfe
 61-70: egg, cereal, milk
 71-90: beans, moinmoin, watermelon
 90 and above: vineless seed grape 
 
 and we want to collect the users height, name and weight-->
<html>
<head>
    <title>Weight Qualification Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #f6f7ff 0%, #e6f0ff 100%);
            margin: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .form-wrapper {
            width: 100%;
            max-width: 420px;
            background: #ffffff;
            border-radius: 14px;
            box-shadow: 0 12px 32px rgba(36, 58, 86, 0.16);
            padding: 28px 24px;
        }
        h1 {
            margin-top: 0;
            margin-bottom: 18px;
            color: #2a3c62;
            font-size: 1.55rem;
            text-align: center;
        }
        label {
            display: block;
            margin-bottom: 6px;
            color: #41507a;
            font-weight: 600;
        }
        input[type="text"],
        input[type="number"] {
            width: 100%;
            padding: 10px 12px;
            border: 1px solid #d0d7ea;
            border-radius: 8px;
            font-size: 0.96rem;
            margin-bottom: 16px;
            box-sizing: border-box;
        }
        input[type="text"]:focus,
        input[type="number"]:focus {
            outline: none;
            border-color: #6889e5;
            box-shadow: 0 0 0 3px rgba(104, 137, 229, 0.2);
        }
        input[type="submit"] {
            width: 100%;
            padding: 11px 14px;
            background: #3f58d8;
            color: #fff;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: 700;
            transition: background-color 0.2s ease, transform 0.1s ease;
        }
        input[type="submit"]:hover {
            background: #334bc3;
            transform: translateY(-1px);
        }
        input[type="submit"]:active {
            transform: translateY(1px);
        }
    </style>
</head>
<body>
    <div class="form-wrapper">
        <h1>Weight Qualification Form</h1>
    <form action="check_weight.php" method="post">
        <label for="name">Enter your name:</label>
        <input type="text" name="name" id="name" required>
        <br><br>
        <label for="height">Enter your height (cm):</label>
        <input type="number" name="height" id="height" step="0.1" min="0" required>
        <br><br>
        <label for="weight">Enter your weight (kg):</label>
        <input type="number" name="weight" id="weight" step="0.1" min="0" required>
        <br><br>
        <input type="hidden" name="mealtype_id" id="mealtype_id" >
        <input type="submit" value="Check Recommendation">
    </form>
        
</body>
</html>