
var n = 0;
$(document).ready(function () {
    document.body.style.visibility = "visible";
    $('input').focus();
    cursor = window.setInterval(function () {
        if ($('#cursor').css('visibility') === 'visible') {
            $('#cursor').css({
                visibility: 'hidden'
            });
        } else {
            $('#cursor').css({
                visibility: 'visible'
            });
        }
    }, 460);
    cursorReady();
    $(document).keydown(function (e) {
        if (e.keyCode == 13) {
            var command = document.getElementById("s1").innerHTML;
            document.getElementById("command").value = "";
            document.getElementById("logInput").style.display = "block";
            
            if(n == 0){
                document.getElementById("logInput").innerHTML = document.getElementById("logInput").innerHTML + command;
                n = parseInt(n) + 1;    
            }else{
                document.getElementById("logInput").innerHTML = document.getElementById("logInput").innerHTML + "<br>" + command;
                n = parseInt(n) + 1;
            }
            printFaz(whatTheFaz($("#s1").text()));
        }
      });
});