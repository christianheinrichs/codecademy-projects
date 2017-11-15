function showinfos() {
  var firstname = document.getElementsByName("firstname")[0].value;
  var lastname = document.getElementsByName("lastname")[0].value;
  var gender = document.getElementsByName("gender");
  var checkboxes = document.getElementsByName("tracks");
  var feedback = document.getElementsByTagName("textarea")[0].value;
  var selectedGender = "";
  var languages = [];

  for (var i = 0; i < checkboxes.length; i++) {
    if (checkboxes[i].checked) {
      languages.push(checkboxes[i].value);
    }
  }

  for (var i = 0; i < gender.length; i++) {
    if (gender[i].checked) {
      selectedGender = gender[i].value;
    }
  }

  if (firstname !== "" && lastname !== "" && selectedGender !== "" && feedback !== "") {
    alert("Full name: " + firstname + " " + lastname + "\nGender: " + selectedGender + "\nYou have completed the tracks " + languages.join(", ") + "\n" + "And this is what you left as feedback message:\n" + feedback);
  } else {
    alert("Please fill out all fields, before clicking Submit!");
  }
}
