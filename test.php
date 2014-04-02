<?php

$file_a = file_get_contents('data/admins.txt');
$file_b = file_get_contents('data/admin.txt');
$file_a_paths = explode("\n", $file_a);
$file_b_paths = explode("\n", $file_b);

// echo count($file_a_paths);
// echo '<br />';
// echo count($file_b_paths);


foreach ($file_a_paths as $a){
  $a = trim(preg_replace('/\s\s+/', ' ', $a));

  if (strstr($a, '%EXT%')) {
    $a = str_replace('.%EXT%', '{ext}', $a);
  }

  if (! in_array($a, $file_b_paths))
    file_put_contents('data/admin.txt', $a . "\n", FILE_APPEND);
}
