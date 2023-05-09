/**
 * Write a JavaScript script that fetches
 *  and prints how to say “Hello” depending on the language
 * You should use this API service:
 *  https://www.fourtonfish.com/hellosalut/hello/
 * The language code will be the value entered
 *  in the tag INPUT#language_code (ex: es, fr, en etc.)
 * The translation must be fetched when the user clicks on INPUT#btn_translate
 *  OR presses ENTER when the focus is on INPUT#language_code
 * The translation of “Hello” must be displayed in the HTML tag DIV#hello
 * You can’t use document.querySelector to select the HTML tag
 * You must use the JQuery API
 * You script must work when imported from the <head> tag
 */

$(document).ready(function () {
  // Get references to the relevant DOM elements
  const languageInput = $('#language_code');
  const translateButton = $('#btn_translate');
  const helloDiv = $('#hello');

  // Add event listeners to the input and button
  languageInput.on('keyup', function (event) {
    if (event.key === 'Enter') {
      fetchTranslation();
    }
  });

  translateButton.on('click', fetchTranslation);

  // Define a function to fetch the translation and update the DOM
  function fetchTranslation () {
    const languageCode = languageInput.val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + languageCode;

    $.get(url, function (data) {
      helloDiv.text(data.hello);
    });
  }
});
