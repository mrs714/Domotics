// Function to update the status container with the ping status
function updatePingStatus() {
    // Fetch the /ping endpoint from your Flask app
    fetch('/ping')
        .then(response => response.json())
        .then(data => {
            // Update the status container with the received data
            const statusContainer = document.getElementById('PC-status-container');
            statusContainer.innerHTML = `Status: ${data.status}<br>IP: ${data.ip}`;
        })
        .catch(error => console.error('Error fetching ping status:', error));
}

function sendWOL() {
    // Fetch the /wol endpoint from your Flask app
    fetch('/wol')
        .then(response => response.json())
        .then(data => {
            // Update the status container with the received data
            const statusContainer = document.getElementById('pc-status');
            statusContainer.innerHTML = `Status: ${data.status}`;
        })
        .catch(error => console.error('Error sending WOL:', error));
}

// Refresh the ping status every x seconds (adjust as needed)
setInterval(updatePingStatus, 1000);

// Run the updatePingStatus function once when the page loads
window.addEventListener('load', updatePingStatus);

// Run the sendWOL function once when the button wol-button is clicked
document.getElementById('wol-button').addEventListener('click', sendWOL);