document.addEventListener("DOMContentLoaded", function() {
    var draw = SVG().addTo('#ne').size('100%', '100%');
    draw.viewbox(0, 0, 100, 100);

    // load the image
    var image = draw.image('static/images/map.svg', 1000, 1000);

    // Resize the image to fit the div
    image.size('100%', '100%');

    // https://www.petercollingridge.co.uk/tutorials/svg/interactive/dragging/
    
});