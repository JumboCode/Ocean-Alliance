// OpenCV test code, from 
// https://www.npmjs.com/package/opencv4nodejs#quick-start
var cv = require('opencv4nodejs');
var Console = require('console');

const pngPrefix = 'data:image/jpeg;base64,';
const jpgPrefix = 'data:image/png;base64,';

function decodeImageFromBase64(base64String) {
    var base64Data = base64String.replace(pngPrefix, '').replace(jpgPrefix, '');
    var buffer = Buffer.from(base64Data, 'base64');
    return cv.imdecode(buffer);
}

function renderImage(img, canvas) { 
    var matRGBA = img.channels === 1 ? img.cvtColor(cv.COLOR_GRAY2RGBA) : img.cvtColor(cv.COLOR_BGR2RGBA);
    canvas.height = img.rows;
    canvas.width = img.cols;
    var imgData = new ImageData(
        new Uint8ClampedArray(matRGBA.getData()),
        img.cols,
        img.rows
    );
    var ctx = canvas.getContext('2d');
    ctx.putImageData(imgData, 0, 0);
}

function onImageSelected(e) {
    selectedFile = e.target.files[0];

    var reader = new FileReader();
    reader.onload = function (re) {
        var selectedImgBGR = decodeImageFromBase64(re.target.result).resizeToMax(500);
        renderImage(
            selectedImgBGR,
            document.getElementById('input')
        );
    };
    reader.readAsDataURL(selectedFile);
}