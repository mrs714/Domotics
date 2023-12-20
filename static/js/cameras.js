// List of ips for available cameras
var cameras = ["rtsp://192.168.1.137/ch00_0"];
// Website to look up your camera's RTSP link: https://www.ispyconnect.com/camera/xiaomi (replace xiaomi with your camera's brand)

/*
document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById("cameraCanvas");
    const rtspLink = "rtsp://192.168.1.139/ch00_0"; // Change the RTSP link as needed

    const player = new rtsp_player({
        canvas: canvas,
        url: rtspLink,
    });

    // Wait for the player to connect to the RTSP stream
    player.on(rtsp_player.Events.CONNECTION_ESTABLISHED, function() {
        // Capture a single frame
        const frame = player.snap();

        // Draw the captured frame on the canvas
        const ctx = canvas.getContext("2d");
        ctx.drawImage(frame, 0, 0);

        // Save the frame as an image (optional)
        const dataUrl = canvas.toDataURL("image/png");
        const a = document.createElement("a");
        a.href = dataUrl;
        a.download = "captured_frame.png";
        a.click();
    });

    // Handle errors
    player.on(rtsp_player.Events.CONNECTION_FAILED, function() {
        console.error("Error: Could not connect to the RTSP stream.");
    });
});*/