/* JavaScript script that fetches and prints how to say “Hello” depending on the language */
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const langCode = $('INPUT#language_code').val();
    console.log(langCode);
    $.get('https://fourtonfish.com/hellosalut/?lang=' + langCode, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
