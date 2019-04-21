// Check On/Off Specific Todos by Clicking
$("ul").on("click", "li", function() {
    $(this).toggleClass("completed");  
})

// Cick on X to Delete Todo
$("ul").on("click", "span", function(event){
    event.stopPropagation();
    $(this).parent().fadeOut(500,function(){
        $(this).remove();
    });
})

// Make a New Todo
$("input[type='text']").keypress(function(event){
    if (event.which === 13 && $(this).val() != ""){
        // Grabbing New Todo Text from Input
        var todoText = $(this).val();
        //Clears Input
        $(this).val("");
        //Create a New Li to the Ul
        $("ul").append("<li><span><i class='fa fa-trash-alt'></i></span> " + todoText + "</li>")
    }
})

// Toggle New Item
$(".fa-plus").click(function() {
    $("input[type='text']").fadeToggle();
})