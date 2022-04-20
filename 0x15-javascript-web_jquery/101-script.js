/*  script that adds, removes and clears LI elements from a list when the user clicks */
$(document).ready(function () {
  const item = $('<li>Item</li>');
  $('DIV#add_item').click(function () {
    $('UL.my_list').append(item.clone());
  });

  $('DIV#remove_item').click(function () {
    $('li', 'UL.my_list').last().remove();
  });

  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
