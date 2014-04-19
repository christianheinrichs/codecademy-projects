var my_canvas = document.getElementById("canvas");
var context = my_canvas.getContext("2d");

context.beginPath();
context.arc(55, 55, 50, 0, 2 * Math.PI);
context.stroke();

context.fillStyle = "blue";
context.fillRect(100, 100, 85, 85);

context.font = "14px Garamond";
context.fillText("Hello World", 110, 20);
