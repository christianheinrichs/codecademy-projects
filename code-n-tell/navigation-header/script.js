$(document).ready(function() {
  $("#lessons").hover(function() {
    $("#backarrow").css({
      "background-image": "url(back-arrow-hover.png)",
      "cursor": "pointer"
    });
    $("#lessons").css("color", "#14aaf5");
  }, function() {
    $("#backarrow").css("background-image", "url(back-arrow.png");
    $("#lessons").css("color", "#ffffff");
  });

  $("#codecademy").hover(function() {
    $(this).css("cursor", "pointer");
    $(this).stop().fadeTo("fast", 0.5);
  }, function() {
    $(this).stop().fadeTo("fast", 1);
  });

  $(".acc").hover(function() {
    $(this).css("color", "#14aaf5");
  },
    function() {
      $(this).css("color", "#ffffff");
  });
});
