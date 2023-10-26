var mousePressed = false;
    var lastX, lastY;
    var ctx;
    
    function getRndInteger(min, max) {
        return Math.floor(Math.random() * (max - min) ) + min;
    }
    
    function InitThis() {
        ctx = document.getElementById('myCanvas').getContext("2d");
        
        numero = getRndInteger(0, 10);
        letra = ['triangulo', 'cuadrado', 'circulo', 'rombo'];
        color = ['verde', 'azul', 'amarillo', 'rojo'];
        random = Math.floor(Math.random() * letra.length);
        randomC = Math.floor(Math.random() * color.length);
        aleatorio = letra[random] + ' ' + color[randomC];

        document.getElementById('mensaje').innerHTML  = 'Dibuja un ' + aleatorio;
        document.getElementById('numero').value = aleatorio;

        $('#myCanvas').mousedown(function (e) {
            mousePressed = true;
            Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, false);
        });

        $('#myCanvas').mousemove(function (e) {
            if (mousePressed) {
                Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, true);
            }
        });

        $('#myCanvas').mouseup(function (e) {
            mousePressed = false;
        });
            $('#myCanvas').mouseleave(function (e) {
            mousePressed = false;
        });
    }

    function changeStrokeColor(color){
        ctx.strokeStyle = color;
    }

    function Draw(x, y, isDown) {
        if (isDown) {
            ctx.beginPath();
            ctx.lineWidth = 11;
            ctx.lineJoin = "round";
            ctx.moveTo(lastX, lastY);
            ctx.lineTo(x, y);
            ctx.closePath();
            ctx.stroke();
        }
        lastX = x; lastY = y;
    }

    function clearArea() {
        // Use the identity matrix while clearing the canvas
        ctx.setTransform(1, 0, 0, 1, 0, 0);
        ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
    }

    //https://www.askingbox.com/tutorial/send-html5-canvas-as-image-to-server
    function prepareImg() {
        var canvas = document.getElementById('myCanvas');
        document.getElementById('myImage').value = canvas.toDataURL();
    }