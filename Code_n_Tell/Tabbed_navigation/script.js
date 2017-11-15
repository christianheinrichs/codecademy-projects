$(document).ready(function() {
  $(".header").click(function() {
    $(".show").hide();
    $(".header").removeClass("active");
    $(this).stop().animate( {
      color: "#ffffff",
      backgroundColor: "rgb( 35, 44, 49 )"
    }); // Animation is broken
    $(this).addClass('active');
    $("#" + $(this).attr("title")).show();
  });

  $(".tabbed").click(function() {
    $(this).remove();
  });

  $(".header").mouseenter(function() {
    $(this).css("cursor", "pointer");
    $(this).stop().animate( {
      color: "#ffffff",
      backgroundColor: "rgb( 45, 60, 70 )"
    });
  });

  $(".header").mouseleave(function() {
    $(this).stop().animate( {
      color: "#696969",
      backgroundColor: "rgb( 33, 33, 33 )"
    });
  });
});
