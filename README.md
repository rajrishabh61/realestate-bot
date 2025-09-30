<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RealEstate Bot</title>
<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f4f6f8;
        color: #333;
        margin: 20px;
    }
    .container {
        background-color: #fff;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        max-width: 800px;
        margin: auto;
    }
    h1 {
        color: #2c3e50;
        text-align: center;
        font-size: 2.5em;
    }
    h2 {
        color: #34495e;
        margin-top: 25px;
    }
    p {
        line-height: 1.6;
        font-size: 1.1em;
    }
    .feature-list {
        margin: 20px 0;
        padding-left: 20px;
    }
    .feature-list li {
        margin-bottom: 10px;
        font-weight: 500;
    }
    .highlight {
        color: #e74c3c;
        font-weight: bold;
    }
    .button {
        display: inline-block;
        padding: 12px 25px;
        background-color: #3498db;
        color: #fff;
        text-decoration: none;
        border-radius: 8px;
        margin-top: 20px;
        transition: background-color 0.3s ease;
    }
    .button:hover {
        background-color: #2980b9;
    }
</style>
</head>
<body>
<div class="container">
    <h1>🏠 RealEstate Bot</h1>
    <p>Welcome to <span class="highlight">RealEstate Bot</span> – your intelligent property assistant! This Python-based chatbot helps users search for properties effortlessly, providing property details including images, location, price, and BHK configurations.</p>

    <h2>✨ Features</h2>
    <ul class="feature-list">
        <li>Search properties by <span class="highlight">address</span> with fuzzy matching</li>
        <li>View property <span class="highlight">images, BHK, location, and price</span></li>
        <li>Interactive chat interface for <span class="highlight">buy, rent, or sell</span> inquiries</li>
        <li>Fallback options if no properties match your search</li>
        <li>Easy to extend with new features and data</li>
    </ul>

    <h2>⚡ Quick Start</h2>
    <p>1. Place your <strong>RealEstate.csv</strong> file in the project root.<br>
       2. Ensure images are in <strong>static/images/</strong> folder.<br>
       3. Install dependencies:<br>
       <code>pip install -r requirements.txt</code><br>
       4. Run the bot:<br>
       <code>python app.py</code>
    </p>

    <a href="https://github.com/rajrishabh61/realestate-bot" class="button">View on GitHub</a>
</div>
</body>
</html>
