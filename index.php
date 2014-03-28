<?php

$f3=require('lib/base.php');

$f3->config('config.ini');

$f3->route('GET /',
  function($f3) {
    echo View::instance()->render('layout.php');
  }
);

$f3->route('POST /',
  function($f3) {

    if (empty($_REQUEST['path_to_search'])){
      echo View::instance()->render('layout.php');
      return;
    }

    $success_res = empty($_REQUEST['success_res']) ? $f3->get('success_res') : explode(',', $_REQUEST['success_res']);
    $web_apps = empty($_REQUEST['web_apps']) ? $f3->get('web_apps') : explode(',', $_REQUEST['web_apps']);
    $time_out = empty($_REQUEST['time_out']) ? $f3->get('time_out') : explode(',', $_REQUEST['time_out']);


    $admin_paths_file = $f3->get('data_path') . 'admins.txt';
    $file_content = file_get_contents($admin_paths_file);
    $admin_paths = explode("\n", $file_content);

    $request_options = array(
      'timeout' => 3,
      'ignore_errors'=>TRUE
    );

    foreach ($admin_paths as $path) {
      $path = trim(preg_replace('/\s\s+/', ' ', $path));
      if (strstr($path, '%EXT%')) {
        foreach ($web_apps as $web_app) {
          $replaced_path = str_replace('%EXT%', $web_app, $path);
          $request_url = $_REQUEST['path_to_search'] . '/' . $replaced_path;
          $response = Web::instance()->request($request_url,$request_options);
          $response_header = parse_headers($response['headers']);
          if (! empty($response_header) && in_array($response_header['status_code'], $success_res)){
            dd($request_url . ' STATUS CODE: ' . $response_header['status_code']);
          }
        }
      } else {
        $request_url = $_REQUEST['path_to_search'] . '/' . $path;
        $response = Web::instance()->request($request_url,$request_options);
        $response_header = parse_headers($response['headers']);
        if (! empty($response_header) && in_array($response_header['status_code'], $success_res)){
          dd($request_url . ' STATUS CODE: ' . $response_header['status_code']);
        }
      }
    }

    // parse_headers($response['headers']);

    echo View::instance()->render('layout.php');
  }
);

$f3->run();

function dd($data, $label = NULL) {
  $out = ($label ? $label . ': ' : '') . print_r($data, TRUE) . "\n";

  // The temp directory does vary across multiple simpletest instances.
  $file = './debug.txt';
  if (file_put_contents($file, $out, FILE_APPEND) === FALSE) {
    return FALSE;
  }
}

function parse_headers(array $headers, $header = null) {
  $output = array();

  if (empty($headers))
    return $output;

  if ('HTTP' === substr($headers[0], 0, 4)) {
    list(, $output['status_code'], $output['status_text']) = explode(' ', $headers[0], 3);
    unset($headers[0]);
  }

  foreach ($headers as $v) {
    $h = preg_split('/:\s*/', $v);
    if (count($h) > 1) {
      $output[strtolower($h[0])] = $h[1];
    }
  }

  if (null !== $header) {
    if (isset($output[strtolower($header)])) {
      return $output[strtolower($header)];
    }
    return;
  }

  return $output;
}
