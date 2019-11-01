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
    Newcell1.innerHTML = '<td><Button>' + filename + '</Button></td>'
    Newcell1.vidFile = file
    Newcell1.addEventListener('click', function () {
      playSelectedFile(file)
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
