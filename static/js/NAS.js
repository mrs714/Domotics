// Function to update the status container with the ping status
function updateNasStatus() {
    // Fetch the /ping endpoint from your Flask app
    fetch('/nas')
        .then(response => response.json())
        .then(data => {
            // Update the status container with the received data
            const statusContainer = document.getElementById('NAS-status-container');
            statusContainer.innerHTML = `Status: ${data.status}<br>IP: ${data.ip}`;
        })
        .catch(error => console.error('Error fetching NAS status:', error));
}

// Refresh the ping status every x seconds (adjust as needed)
setInterval(updateNasStatus, 1000);

// Run the updateNasStatus function once when the page loads
window.addEventListener('load', updateNasStatus);