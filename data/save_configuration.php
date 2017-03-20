<?php

  // load config
  require("config.php");
  
  // retrieve data from POST
  $data = $_REQUEST["plugs"];
  if (null !== $data && (null !== ($data = json_decode($data)))) {
  
    // override configuration plugs array
    if (sizeof($data) === sizeof($config_data["plugs"])) {

      // set names
      for ($i = 0; $i < sizeof($data); $i++) {
        $config_data["plugs"][$i]["name"] = $data[$i];
      }
      
      // jsonify, save to data.json and send back to web-app
      $config_data = json_encode($config_data);
      $file = "/var/www/html/smartplugs/data/data.json";
      if (file_put_contents($file, $config_data)) {
        echo $config_data;
      } else {
        // send error 500 back to web-app
        header($_SERVER['SERVER_PROTOCOL'] . ' 500 Internal Server Error', true, 500);
      }
      
    } else {
      // send error 500 back to web-app
      header($_SERVER['SERVER_PROTOCOL'] . ' 500 Internal Server Error', true, 500);
    }
    
  } else {
    // send error 500 back to web-app
    header($_SERVER['SERVER_PROTOCOL'] . ' 500 Internal Server Error', true, 500);
  }
