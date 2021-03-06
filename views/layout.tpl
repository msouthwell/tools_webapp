%from bottle import route, view, template, request, response
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link rel="stylesheet" type="text/css" href="/static/css/bootstrap.min.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
    <script src="/static/js/jquery-1.12.3.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.6.0/js/bootstrap-datepicker.js"></script>
</head>

<body>
    <div class="navbar navbar-inverse navbar-static-top">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a href="/about" class="navbar-brand">Handyman Tools</a>
            </div>
            <div class="nav navbar-nav pull-right">
            %if request.get_cookie('customer_id'):
              <li class="nav-item">
                <a class="nav-link" href="/customer_main_menu">Menu</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/exit">Exit</a>
              </li>
            %elif request.get_cookie('clerk_id'):
              <li class="nav-item">
                <a class="nav-link" href="/clerk_main_menu">Menu</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/exit">Exit</a>
              </li>
            %else:
              <li class="nav-item">
                <a class="nav-link" href="/login">Login</a>
              </li>
            %end
            </div>
        </div>
    </div>

    <div class="container body-content">
        {{!base}}
        <hr />
        <footer>
            <p>Team Corn on the Cobb</p>
        </footer>
    </div>

    <script src="/static/js/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>
    <script src="/static/scripts/material.js"></script>
    <script src="/static/scripts/ripples.js"></script>
</body>
</html>
