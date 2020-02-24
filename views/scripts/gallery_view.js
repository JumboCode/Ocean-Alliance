const $ = require('jquery')
var inputFiles = [];
inputFiles[0] = "I am  string";
inputFiles[1] = "I am also a string";

window.onload = function () {
    for (var i = 0; i < inputFiles.length; i++) {
	var string = "div";
        var num = i.toString();
        var row = document.createElement("div");
        row.setAttribute("id", string.concat(num));
	var text = document.createTextNode(inputFiles[i]);
	row.appendChild(text);

	var element = document.getElementById("row");
	document.body.insertBefore(row, element);
    }
}
$(document).ready(function() {
    $ ( "body" ).click(function( event ) {
      $( "#squares" ).html( "clicked: " + event.target.nodeName );
    });
});
