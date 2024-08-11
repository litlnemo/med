// ==UserScript==
// @name        MED Open Click
// @description Use this to automatically click the "Show All" button on MED pages
// @match       https://quod.lib.umich.edu/m/middle-english-dictionary/dictionary/*
// @version     1.0
// ==/UserScript==

(function() {	
	document.getElementsByClassName('show-all-button')[0].click()
})();

