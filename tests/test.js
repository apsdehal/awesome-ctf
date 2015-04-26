var assert = require('chai').assert,
	utils = require('./utils');

var $ = utils.getSelectorObject();

describe('Main module', function () {
	it('should contain a non-duplicate link for all title', function () {
		var links = [];

		$('a').each(function (k) {
			var href = $(this).attr('href');

			assert.isDefined(href, 'Expected href for ' + $(this).html());

			if (links[href]) {
				console.log(href);
				assert.ok(false, 'Duplicate link for ' + $(this).html());
			}

			links[href] = true;
		});
	});

	it('should be sorted alphabetically', function () {
		$('ul').each(function () {
			utils.testList(assert, $, $(this));
		})
	});
})