var inputFiles = [];
inputFiles[0] = "I am  string";
inputFiles[1] = "I am also a string";

window.onload = function () {
    for (var i = 0; i < inputFiles.length; i++) {
	var row = document.createElement("p");
	var text = document.createTextNode(inputFiles[i]);
	row.appendChild(text);

	var element = document.getElementById("row");
	element.appendChild(row);
    }
}
