document.addEventListener('DOMContentLoaded', function() {
    // Fetch data from Flask route
    fetch('/api/se1/prices')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Extract relevant data for chart
            const labels = data.map(entry => entry.time_start);
            const prices = data.map(entry => entry.SEK_per_kWh);

            // Create chart
            const ctx = document.getElementById('price-chart').getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'SE1 Electricity Prices',
                        data: prices,
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            // Display error message to the user
            const errorMessage = document.createElement('p');
            errorMessage.textContent = 'Error fetching data. Please try again later.';
            document.body.appendChild(errorMessage);
        });
});



document.addEventListener('DOMContentLoaded', function() {
    // Fetch data from the Flask route
    fetch('/api/data?year=2022&month=11&day=24&price_class=SE1') // Example parameters
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Process the data and create the chart as needed
            console.log(data);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            // Display error message to the user
        });
});
