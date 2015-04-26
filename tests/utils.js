var fs = require('fs'),
	marked = require('marked'),
	cheerio = require('cheerio');

module.exports = (function () {
	var utils = {
		getSelectorObject: function () {
			var html = marked(fs.readFileSync('./README.md', 'utf-8'));
			return cheerio.load(html);
		},

		testList: function (assert, $, list) {
			var self = this;

			list.find('ul').each(function () {
				utils.testList(assert, $, $(this));
				$(this).remove('ul');
			});
			self.testAlphabetical(assert, $, list);
		},

		testAlphabetical: function (assert, $, list) {
			var items = [];
			list.find("li > a:first-child").map(function (i) {
				items.push($(this).text().toLowerCase());
			});

			sorted = items.slice().sort();

			assert.deepEqual(items, sorted, 'Links should be in alphabetical order');
		}
	};

	return utils;
})();