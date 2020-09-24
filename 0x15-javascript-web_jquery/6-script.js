#!/usr/bin/node
const $ = window.$;
$('#update_header').click(function () {
  $('header').replaceWith('New Header!!!');
});
