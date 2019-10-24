// temp js file to contain front end javascript

const { ipcRenderer } = require('electron')

function onSelectButtonClick () {
  ipcRenderer.send('openFile')
}
