<html>
    <head>
        <meta charset="utf-8">
        <title>Гороскоп на сегодня</title>
        
    </head>
    
    <link 
          rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
          integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
          crossorigin="anonymous">
    
    <script
        src="http://code.jquery.com/jquery-3.3.1.js"
        integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60="
        crossorigin="anonymous">
    </script>
    
    <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
    
    <link
              rel='stylesheet'
              type="text/css"
              href='static/styles.css'
            />
        
    <body>
        
        <div class='container'>
            <div class='row'>
                <div class="col-12">
                    <h1 onclick="log_header_click()" id='header_click'>
                    Что день {{ day }} {{ month }} {{ year }} года готовит?
                    </h1>
                </div>
            </div>
            <div class='row'>
                <div class='col-4' id='col1'>
                    <p id="1">
                        
                    </p>
                </div>
                <div class='col-4' id='col1'>
                    <p id="2">
                        
                    </p>
                </div>
                <div class='col-4' id='col1'>
                    <p id="3">
                        
                    </p>
                </div>
            </div>
            <div class='row'>
                <div class='col-4' id='col1'>
                    <p id="4">
                        
                    </p>
                </div>
                <div class='col-4' id='col1'>
                    <p id="5">
                        
                    </p>
                </div>
                <div class='col-4' id='col1'>
                    <p id="6">
                        
                    </p>
                </div>
            </div>
        </div>
    </body>
    <script
        src="static/header_click.js">
    </script>
    <hr/>
    <a href="about">О реализации</a>
</html>
