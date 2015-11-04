//Made by : Divam

var chokidar = require('chokidar');

var path = require('path')
var childProcess = require('child_process')
var phantomjs = require('phantomjs')
var binPath = phantomjs.path

console.log(binPath);



var isReady = 0;

var watcher = chokidar.watch('.', {
  ignored: /[\/\\]\./,
  persistent: true
});

watcher
  .on('add', function(path) { 
  	if(isReady)
  	{
  		console.log('File', path, 'has been added'); 
  		if (path.indexOf('.html') > 0 )
  		{
  			console.log("html added");
  			generateImgFromHtml(  path , path.replace('.html' , '.png').replace('html_files' , 'image_files'))
  		}
  	}
  

  })
  .on('ready', function() { 
  	console.log('Initial scan complete. Ready for changes.');
  	isReady = 1;
   })



function generateImgFromHtml(htmlPath , imagePath , callback)
{
	var childArgs = [
	  path.join(__dirname, 'phantomjs-script.js'),
	  htmlPath , imagePath
	];

	childProcess.execFile('phantomjs', childArgs, function(err, stdout, stderr) {
	  // handle results 
	  console.log("hh");
	  console.log(err);
	})

}
