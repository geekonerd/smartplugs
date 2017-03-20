<?php

  // load config
  require("config.php");

  // retrieve plugs to activate/deactivate
  $data = $_REQUEST["plugs"];
  $action = $_REQUEST["action"];
  if ((null !== $data && (null !== ($data = json_decode($data))))
    && (in_array($action, $config_actions))) {
    
    $command = "sudo python transmit.py";
    
    // set names
    for ($i = 0; $i < sizeof($data); $i++) {
      $command .= " " . $data[$i] . $action;
    }
    
    // execute command
    $result = exec($command);
    echo '{ "command" : "' . $command . '", "result" : "' . $result . '" }';
    
  } else {
    // send error 500 back to web-app
    header($_SERVER['SERVER_PROTOCOL'] . ' 500 Internal Server Error', true, 500);
  }
