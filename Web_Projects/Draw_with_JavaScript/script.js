var my_canvas = document.getElementById("canvas");
var context = my_canvas.getContext("2d");

// Draw an empty, hollow circle
context.beginPath();
context.arc(55, 55, 50, 0, 2 * Math.PI);
context.stroke();

// Draw a blue rectangle
context.fillStyle = "blue";
context.fillRect(100, 100, 85, 85);

// Draw the string "Hello World"
context.font = "14px Garamond";
context.fillText("Hello World", 110, 20);
