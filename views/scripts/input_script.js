const { ipcRenderer } = require('electron')
const { dialog } = require('electron').remote
const $ = require('jquery')

let inputPaths, outputPath

$('#sourceFile').click(function(){
    console.log("upload source file")
    

    // TODO support for multiple files at once?
    // returns an array of file path
    inputPaths = dialog.showOpenDialogSync({ properties: ['openFile'] })
    if (inputPaths === undefined){
        console.log('file selection canceled')
    }else{
        console.log(inputPaths)
    
        $('#inputRow').attr('hidden',"")
        $('#outputRow').removeAttr('hidden')
    }
})


$('#sourceFolder').click(function(){
    console.log("upload source folder")
    
    // TODO support for multiple files at once?
    // returns an array of file path
    inputPaths = dialog.showOpenDialogSync({ properties: ['openDirectory'] })
    if (inputPaths === undefined) {
        console.log('folder selection canceled')
    } else {
        console.log(inputPaths)

        $('#inputRow').attr('hidden', "")
        $('#outputRow').removeAttr('hidden')
    }
})

$('#destFolder').click(function(){
    console.log("select destination folder")
    outputPath = dialog.showOpenDialogSync({ properties: ['openDirectory', 'createDirectory', 'promptToCreate'] })
    if(outputPath === undefined) {
        console.log('destination selection canceled')
    }else{
        console.log(outputPath)

        // TODO swap this to sendSync to do error handling?
        ipcRenderer.send('submit-job', {'in': inputPaths, 'out': outputPath})
        $(location).attr('href', 'progress_view.html')

    }
})


// updateBtn.addEventListener('click', function () {
//     ipcRenderer.send('submit-job', document.getElementById('notifyVal').value)
// })