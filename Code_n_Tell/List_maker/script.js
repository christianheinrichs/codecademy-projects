$(document).ready(function() {
    $("#button").click(function() {
        var add = $('input').val();

        if (add === "") {
            alert("Have you entered a note?");
        }
        else {
            $(".list").append('<div class="dummy"><div class="listadd">' + add + '</div>' + '<div class="dlt">' + "Delete entry" + "</div></div>");
        }
        $('input').val("");
    });

    $("#dltall").click(function() {
        if (!$(".dummy").length) {
            alert("No entries to delete");
        }
        $(".dummy").fadeOut("slow", function() {
            $(".dummy").remove();
        });
    });

    $(document).on("click", ".dlt", function() {
        $(this).parent().fadeOut("slow", function() {
            $(this).remove();
        });
    });
});
