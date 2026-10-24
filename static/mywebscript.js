"use strict";

function RunSentimentAnalysis() {
  const textToAnalyze = document.getElementById("textToAnalyze").value;
  const output = document.getElementById("system_response");
  const request = new XMLHttpRequest();

  output.textContent = "Analyzing...";
  request.onreadystatechange = function () {
    if (request.readyState === XMLHttpRequest.DONE) {
      output.textContent = request.responseText;
    }
  };
  request.open(
    "GET",
    "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze),
    true
  );
  request.send();
}
