//Made by : Divam

var page = require('webpage').create();
var system = require('system');
var args = system.args;

var url = args[1];

//CAPTURE CONSOLE MESSAGES
page.onConsoleMessage = function(msg) {
	console.log("console message: " + msg);
};

page.open(url, function(status) {

	page.evaluate(function() {
		console.log(document.title);
	});
	
	// page.render('image_files/aaaa.png');
	page.render(args[2]);
	phantom.exit();
});