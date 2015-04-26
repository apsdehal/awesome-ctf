var fs = require('fs'),
	marked = require('marked'),
	cheerio = require('cheerio');

module.exports = (function () {
	return {
		getSelectorObject: function () {
			var html = marked(fs.readFileSync('../README.md'));
			return cheerio.load(html);
		},
	}
})();