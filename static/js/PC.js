// Function to update the status container with the ping status
function updatePingStatus() {
    // Fetch the /ping endpoint from your Flask app
    fetch('/ping')
        .then(response => response.json())
        .then(data => {
            // Update the status container with the received data
            const statusContainer = document.getElementById('status-container');
            statusContainer.innerHTML = `Status: ${data.status}<br>IP: ${data.ip}, ${data}`;
        })
        .catch(error => console.error('Error fetching ping status:', error));
}

// Refresh the ping status every x seconds (adjust as needed)
setInterval(updatePingStatus, 1000);

// Run the updatePingStatus function once when the page loads
window.addEventListener('load', updatePingStatus);