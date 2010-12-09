$(document).ready(function() {
  $("form#sendEvaluation").submit(function() {
    return confirm("Är du säker? (du kan inte ta tillbaka, och du kan inte ändra en utvärdering som är skickad)");
  });
});
