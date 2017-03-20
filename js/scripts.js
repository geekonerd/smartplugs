// load configuration data from data.json
function loadConfiguration() {
  showLoader("#home");
  $.ajax({
    url: "data/data.json",
    dataType: "json",
  }).done(function(data, textStatus, jqXHR) {
    $("#version").html(data.version);
    populatePlugs(data);
    populateActions(data);
    hideLoader("#home");
  }).fail(function(jqXHR, textStatus, errorThrown) {
    showMessage("Si &egrave; verificato un errore: ["
      + textStatus + "]", "alert-danger");
  });
  jQuery("#menu a").each(function(index) {
    $(this).on("click", function(e) {
      e.preventDefault();
      $(".app-panel").addClass("hidden");
      $($(this).attr("href")).removeClass("hidden");
    });
  });
}

// populate actions
function populateActions(data) {
  $("#save_configuration").on("click", saveConfiguration);
  if (data && data.plugs) {
    $("#home .plugaction button").each(function(index) {
      var i = (!index%2 ? index : Math.floor(index/2));
      var code = data["plugs"][i]["code"];
      var action = (index%2 ? "_off" : "_on");
      $(this).attr("plug-code", code);
      $(this).attr("plug-action", action);
      $(this).on("click", transmit);
    });
  }
}

// populate name of plugs
function populatePlugs(data) {
  if (data && data.plugs) {
    $("#home .plugname").each(function(index) {
      $(this).html(data["plugs"][index]["name"]);
    });
    $("#settings .plugname").each(function(index) {
      $(this).val(data["plugs"][index]["name"]);
      $(this).attr("plug-number", data["plugs"][index]["code"]);
    });
  } else {
    showMessage("Si &egrave; verificato un errore: ["
      + "Impossibile recuperare i nomi delle prese!" + "]", "alert-danger");
  }
}

// save configuration to data.json
function saveConfiguration() {
  showLoader("#settings");
  var data = "[";
  var plugs = $("#settings .plugname");
  for (var i = 0; i < plugs.length; i++) {
    data += '"' + $(plugs[i]).val() + '",';
  }
  data = data.substring(0, data.length - 1) + "]";
  $.ajax({
    url: "data/save_configuration.php",
    method: "GET",
    contentType: 'text/plain; charset=utf-8',
    data: { plugs : data },
    dataType: 'json'
  }).done(function(data, textStatus, jqXHR) {
    showMessage("Configurazione salvata con successo!", "alert-success");
    populatePlugs(data);
  }).fail(function(jqXHR, textStatus, errorThrown) {
    showMessage("Si &egrave; verificato un errore: ["
      + textStatus + "]", "alert-danger");
  }).always(function() {
    hideLoader("#settings");
  });
}

// transmit signal "action" for plug "data"
function transmit() {
  var data = $(this).attr("plug-code");
  var action = $(this).attr("plug-action");
  showLoader("#home");
  if (data === "all") {
    var plugs = $("#settings .plugname");
    data = "[";
    for (var i = 0; i < plugs.length - 1; i++) {
      data += '"' + $(plugs[i]).attr("plug-number") + '",';
    }
    data = data.substring(0, data.length - 1) + "]";
  } else {
    data = '["' + data + '"]';
  }
  $.ajax({
    url: "data/transmit.php",
    method: "GET",
    contentType: 'text/plain; charset=utf-8',
    data: { plugs : data, action : action },
    dataType: 'json'
  }).done(function(data, textStatus, jqXHR) {
    showMessage("Segnale inviato con successo!", "alert-success");
  }).fail(function(jqXHR, textStatus, errorThrown) {
    showMessage("Si &egrave; verificato un errore: ["
      + textStatus + "]", "alert-danger");
  }).always(function() {
    hideLoader("#home");
  });
}

// show loader
function showLoader(page) {
  $("#progress").removeClass("hidden");
  $(page).addClass("hidden");
}

// hide loader
function hideLoader(page) {
  $("#progress").addClass("hidden");
  $(page).removeClass("hidden");
}

// show alert message
function showMessage(msg, status) {
  $("#message").html(msg).removeClass("hidden").addClass(status);
  setTimeout(hideMessage, 6000);
}

// hide alert message
function hideMessage() {
  $("#message").html("").removeClass().addClass("alert hidden");
}

// start!
if (typeof jQuery !== 'undefined') {
  jQuery(window).ready(loadConfiguration);
}
