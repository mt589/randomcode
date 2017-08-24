var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true;
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false;
  });
}

window.onload = init;

/* ADD YOUR CODE BELOW */
function checkPassword() {
  var input = document.getElementById("pw").value
  for (var i = 0; i<wordsList.length; i++){
    if (input == wordsList[i]){
      console.log("This word is too easy anyone can hack it")
      }
      else {
        console.log("This is a fine password you can always try and make it harder, but this will do.")
      }
    }
  }
