function validateage() {
    var userAge = document.getElementsByTagName("input")[0].value;

    if (isNaN(userAge)) {
        alert("Not a number");
    } else if (userAge >= 13) {
        alert("You are old enough. Happy learning!");
    } else {
        alert("Sorry, but you have to be at least 13 years old.");
    }
}
