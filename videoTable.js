window.onload = function () {
  $('#fileinput').one('click', function () {
    $('#fileinput').change(
      function (e) {
        row(e.target.files[0])
      }
    )
  })

  function row (file) {
    var filename = file.name
    var MyTable =
            document.getElementById('Videos')
    // insert new row.
    var NewRow = MyTable.insertRow(0)
    var Newcell1 = NewRow.insertCell(0)
    var PlayButton = document.createElement('Button')
    PlayButton.innerHTML = '<i class="glyphicon glyphicon-play"/>'
    PlayButton.className = 'iconBtn'
    var DeleteButton = document.createElement('Button')
    DeleteButton.innerHTML = '<i class="glyphicon glyphicon-trash"/>'
    DeleteButton.className = 'iconBtn'
    var ProcessButton = document.createElement('Button')
    ProcessButton.innerHTML = '<i class="glyphicon glyphicon-refresh"> Process</i>'
    ProcessButton.className = 'iconBtn'
    var CoolContainer = document.createElement('div')
    CoolContainer.className = 'button button2'
    Newcell1.innerHTML = '<td></td>'
    var FileName = document.createElement('div')
    FileName.innerHTML = filename
    CoolContainer.appendChild(FileName)
    CoolContainer.appendChild(PlayButton)
    CoolContainer.appendChild(ProcessButton)
    CoolContainer.appendChild(DeleteButton)
    Newcell1.appendChild(CoolContainer)
    Newcell1.vidFile = file
    PlayButton.addEventListener('click', function () {
      playSelectedFile(file)
    })
    DeleteButton.addEventListener('click', function () {
      MyTable.deleteRow(DeleteButton.parentNode.parentNode.rowIndex)
    })
    ProcessButton.addEventListener('click', function () {
      processVideo(Newcell1.vidFile)
    })
  }
  var URL = window.URL || window.webkitURL
  var displayMessage = function (message, isError) {
    var element = document.querySelector('#message')
    element.innerHTML = message
    element.className = isError ? 'error' : 'info'
  }
  var playSelectedFile = function (file) {
    var type = file.type
    var videoNode = document.querySelector('video')
    var canPlay = videoNode.canPlayType(type)
    if (canPlay === '') canPlay = 'no'
    var message = 'Can play type "' + type + '": ' + canPlay
    var isError = canPlay === 'no'
    displayMessage(message, isError)

    if (isError) {
      return
    }
    var fileURL = URL.createObjectURL(file)
    videoNode.src = fileURL
  }
}

function processVideo (file) {
  alert('Processing ' + file.name + '\n')
}
