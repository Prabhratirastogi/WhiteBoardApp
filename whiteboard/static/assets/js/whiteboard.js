
// const canvas = document.getElementById('canvas');

// canvas.width = window.innerWidth;
// canvas.height = window.innerHeight;
// const context = canvas.getContext('2d');
// let drawing = false;

// canvas.addEventListener('mousedown', () => {
//     drawing = true;
// });

// canvas.addEventListener('mouseup', () => {

//     drawing = false;
//     context.beginPath();
// });

// canvas.addEventListener('mousemove', draw);

// function draw(event) {

//     context.lineWidth = 2;
//     context.lineCap = 'round';
//     context.strokeStyle = 'black';

//     context.lineTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
//     context.stroke();
//     context.beginPath();
//     context.moveTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
// }
socketRef.current = new WebSocket('ws://127.0.0.1:8000');

socketRef.current.onopen = e =>{
    console.log('open',e)
}

socketRef.current.onmessage = e =>{
    console.log(e)
}

socketRef.current.onerror = e =>{
    console.log('error', e)
},

window.onload = function () {
    var myCanvas = document.getElementById("myCanvas");
    var ctx = myCanvas.getContext("2d");

    // Fill Window Width and Height
    myCanvas.width = window.innerWidth;
    myCanvas.height = window.innerHeight;

    // Set Background Color
    ctx.fillStyle = "#fff";
    ctx.fillRect(0, 0, myCanvas.width, myCanvas.height);

    // Mouse Event Handlers
    if (myCanvas) {
        var isDown = false;
        var canvasX, canvasY;
        ctx.lineWidth = 5;

        $(myCanvas)
            .mousedown(function (e) {
                isDown = true;
                ctx.beginPath();
                canvasX = e.pageX - myCanvas.offsetLeft;
                canvasY = e.pageY - myCanvas.offsetTop;
                ctx.moveTo(canvasX, canvasY);
            })
            .mousemove(function (e) {
                if (isDown !== false) {
                    canvasX = e.pageX - myCanvas.offsetLeft;
                    canvasY = e.pageY - myCanvas.offsetTop;
                    ctx.lineTo(canvasX, canvasY);
                    ctx.strokeStyle = "#000";
                    ctx.stroke();
                }
            })
            .mouseup(function (e) {
                isDown = false;
                ctx.closePath();
            });
    }

    // Touch Events Handlers
    draw = {
        started: false,
        start: function (evt) {

            ctx.beginPath();
            ctx.moveTo(
                evt.touches[0].pageX,
                evt.touches[0].pageY
            );

            this.started = true;

        },
        move: function (evt) {

            if (this.started) {
                ctx.lineTo(
                    evt.touches[0].pageX,
                    evt.touches[0].pageY
                );

                ctx.strokeStyle = "#000";
                ctx.lineWidth = 5;
                ctx.stroke();
            }

        },
        end: function (evt) {
            this.started = false;
        }
    };

    // Touch Events
    myCanvas.addEventListener('touchstart', draw.start, false);
    myCanvas.addEventListener('touchend', draw.end, false);
    myCanvas.addEventListener('touchmove', draw.move, false);

    // Disable Page Move
    document.body.addEventListener('touchmove', function (evt) {
        // evt.preventDefault();
    }, false);
};