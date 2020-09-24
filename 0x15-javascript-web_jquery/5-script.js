#!/usr/bin/node
const $ = window.$;
$('#add_item').click(function () {
  const info = $('<li></li>').text('Item');
  $('.my_list').append(info);
});
