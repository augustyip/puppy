<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="favicon.ico">

    <title>Starter Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">

    <!-- Custom styles for this template -->
    <link href="ui/css/style.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <div class="container">
      <div class="well well-lg">
        <form class="form-horizontal" role="form" action="" method="post">
          <div class="form-group">
            <label for="path_to_search" class="col-md-2 control-label">Path to search:</label>
            <div class="col-md-10">
              <input type="text" class="form-control" id="path_to_search" name="path_to_search" placeholder="http://">
            </div>
          </div>
          <div class="form-group">
            <label for="success_res" class="col-md-2 control-label">Success res:</label>
            <div class="col-md-3">
              <input type="text" class="form-control" id="success_res" name="success_res" placeholder="<?php echo implode(',', $success_res); ?>">
            </div>
            <label for="web_apps" class="col-md-2 control-label">Web Apps:</label>
            <div class="col-md-2">
              <input type="text" class="form-control" id="web_apps" name="web_apps" placeholder="<?php echo implode(',', $web_apps); ?>">
            </div>
            <label for="time_out" class="col-md-2 control-label">Time out:</label>
            <div class="col-md-1">
              <input type="text" class="form-control" id="time_out" name="time_out" placeholder="<?php echo $time_out; ?>">
            </div>
          </div>
          <div class="form-group">
            <div class="col-md-10 col-md-offset-2">
              <button type="submit" class="btn btn-default">Search</button>
            </div>
          </div>
        </form>
      </div><!-- /.well .well-lg -->

      <div>
        <?php echo $result; ?>
      </div>
    </div><!-- /.container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
  </body>
</html>
