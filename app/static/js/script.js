// app/static/js/script.js

// Function to set the background image
function setBackgroundImage() {
    var backgroundImage = document.body.getAttribute('data-background') || 'default_background4.png';
    var imageUrl = '/static/images/background_images/' + backgroundImage;
    document.body.style.backgroundImage = 'url("' + imageUrl + '")';
    document.body.style.backgroundSize = 'cover';
    document.body.style.backgroundPosition = 'center';
    document.body.style.backgroundAttachment = 'fixed';
}

// Function to update the modal with weather details
function updateModalContent(data) {

    const celsiusTemp = data.temperature || 'N/A';
    const fahrenheitTemp = celsiusTemp !== 'N/A' ? ((celsiusTemp * 9/5) + 32).toFixed(2) : 'N/A';


    document.getElementById('detail-date').textContent = data.date || 'N/A';
    document.getElementById('detail-temperature').textContent = `${celsiusTemp}°C / ${fahrenheitTemp}°F`;
    document.getElementById('detail-description').textContent = data.description || 'N/A';
    document.getElementById('detail-sea_level').textContent = data.seaLevel || 'N/A';
    document.getElementById('detail-ground_level').textContent = data.groundLevel || 'N/A';
    document.getElementById('detail-humidity').textContent = data.humidity || 'N/A';
    document.getElementById('detail-pressure').textContent = data.pressure || 'N/A';
    document.getElementById('detail-wind_speed').textContent = data.windSpeed || 'N/A';
    document.getElementById('detail-clouds').textContent = data.clouds || 'N/A';
    document.getElementById('detail-visibility').textContent = data.visibility || 'N/A';
    document.getElementById('detail-temp_max').textContent = data.tempMax || 'N/A';
    document.getElementById('detail-temp_min').textContent = data.tempMin || 'N/A';
    document.getElementById('detail-sunrise').textContent = data.sunrise || 'N/A';
    document.getElementById('detail-sunset').textContent = data.sunset || 'N/A';
}

// Function to handle row click event
function handleRowClick(event) {
    const row = event.currentTarget;
    const data = {
        date: row.dataset.date,
        temperature: row.dataset.temperature,
        description: row.dataset.description,
        seaLevel: row.dataset.sea_level,
        groundLevel: row.dataset.ground_level,
        humidity: row.dataset.humidity,
        pressure: row.dataset.pressure,
        windSpeed: row.dataset.wind_speed,
        clouds: row.dataset.clouds,
        visibility: row.dataset.visibility,
        tempMax: row.dataset.temp_max,
        tempMin: row.dataset.temp_min,
        sunrise: row.dataset.sunrise,
        sunset: row.dataset.sunset
    };

    // Update modal content and display modal
    updateModalContent(data);
    document.getElementById('weather-modal').style.display = 'block';
}

// Function to handle modal close
function setupModalClose() {
    const modal = document.getElementById('weather-modal');
    const closeBtn = document.querySelector('.modal .close');

    closeBtn.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
}

// Function to show the loading indicator
function showLoadingIndicator() {
    document.getElementById('loadingSpinner').style.display = 'flex';
}

// Function to hide the loading indicator
function hideLoadingIndicator() {
    document.getElementById('loadingSpinner').style.display = 'none';
}




// Initialization function
function initialize() {
    // Set background image
    setBackgroundImage();

    // Attach event listeners to weather rows
    const weatherRows = document.querySelectorAll('.weather-day');
    if (weatherRows.length > 0) {
        weatherRows.forEach(row => {
            row.addEventListener('click', handleRowClick);
        });
    }

    // Setup modal close functionality
    setupModalClose();


}

// Initialize all functions once the DOM content is loaded
document.addEventListener('DOMContentLoaded', initialize);
