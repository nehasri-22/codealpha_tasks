<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Calculator</title>

<style>
body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background: #1e1e2f;
    font-family: Arial;
}

.calculator {
    background: #2c2c3c;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(0,0,0,0.5);
}

#display {
    width: 100%;
    height: 60px;
    font-size: 24px;
    margin-bottom: 10px;
    text-align: right;
    padding: 10px;
    border: none;
    border-radius: 10px;
    background: #000;
    color: #0f0;
}

.buttons {
    display: grid;
    grid-template-columns: repeat(4, 70px);
    gap: 10px;
}

button {
    height: 60px;
    font-size: 20px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    transition: 0.2s;
}

button:hover {
    transform: scale(1.05);
}

/* Colors */
.operator { background: orange; }
.equal { background: green; color: white; }
.clear { background: red; color: white; }
.number { background: #444; color: white; }

@media(max-width: 500px) {
    .buttons {
        grid-template-columns: repeat(4, 60px);
    }
}
</style>
</head>

<body>

<div class="calculator">
    <input type="text" id="display" disabled>

    <div class="buttons">
        <button class="clear" onclick="clearDisplay()">C</button>
        <button onclick="deleteLast()">⌫</button>
        <button class="operator" onclick="append('/')">÷</button>
        <button class="operator" onclick="append('*')">×</button>

        <button class="number" onclick="append('7')">7</button>
        <button class="number" onclick="append('8')">8</button>
        <button class="number" onclick="append('9')">9</button>
        <button class="operator" onclick="append('-')">−</button>

        <button class="number" onclick="append('4')">4</button>
        <button class="number" onclick="append('5')">5</button>
        <button class="number" onclick="append('6')">6</button>
        <button class="operator" onclick="append('+')">+</button>

        <button class="number" onclick="append('1')">1</button>
        <button class="number" onclick="append('2')">2</button>
        <button class="number" onclick="append('3')">3</button>
        <button class="equal" onclick="calculate()">=</button>

        <button class="number" onclick="append('0')">0</button>
        <button class="number" onclick="append('.')">.</button>
    </div>
</div>

<script>
const display = document.getElementById("display");

// Add input
function append(value) {
    display.value += value;
}

// Clear screen
function clearDisplay() {
    display.value = "";
}

// Delete last character
function deleteLast() {
    display.value = display.value.slice(0, -1);
}

// Calculate result
function calculate() {
    try {
        display.value = eval(display.value);
    } catch {
        display.value = "Error";
    }
}

// Keyboard support
document.addEventListener("keydown", (e) => {
    if (!isNaN(e.key) || "+-*/.".includes(e.key)) {
        append(e.key);
    } else if (e.key === "Enter") {
        calculate();
    } else if (e.key === "Backspace") {
        deleteLast();
    } else if (e.key === "Escape") {
        clearDisplay();
    }
});
</script>

</body>
</html>
