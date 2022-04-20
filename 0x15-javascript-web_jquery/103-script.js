/* JavaScript script that fetches and prints how to say “Hello” depending on the language
when button/ENTER is pressed */
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const langCode = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + langCode, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
  $('INPUT#language_code').on('keypress', function (e) {
    const langCode = $('INPUT#language_code').val();
    if (e.which === 13) {
      $.get('https://fourtonfish.com/hellosalut/?lang=' + langCode, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
});
