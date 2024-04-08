// Wait for the Google Charts library to load
google.charts.load("current", {packages:["corechart"]});

document.addEventListener('DOMContentLoaded', () => {
    // const points = JSON.parse(localStorage.getItem('gamePoints') || '{}');
    const pointsJson = localStorage.getItem('gamePoints') || '{}';
    const points = JSON.parse(pointsJson);

    displaySummaryAndMessage(points);
    google.charts.setOnLoadCallback(() => drawChart(points));
});

function displaySummaryAndMessage(points) {
    const summaryDiv = document.getElementById('summary');
    const highestCategory = findHighestCategory(points);
    const message = getMessageForCategory(highestCategory, points);

    summaryDiv.innerHTML = `
        
        <p>Academic Points: ${points.Academic || 0}<br>
        Work Points: ${points.Work || 0}<br>
        Well-being Points: ${points['Well-being'] || 0}</p>
        <br>
        <p><strong>${message}</strong></p>
    `;
}

function findHighestCategory(points) {
    let highestCategory = '';
    let highestPoints = 0;
    Object.entries(points).forEach(([category, pts]) => {
        if (pts > highestPoints) {
            highestPoints = pts;
            highestCategory = category;
        }
    });
    // Check if balanced
    const pointValues = Object.values(points);
    const allEqual = pointValues.every(val => val === pointValues[0]);
    return allEqual ? 'Balanced' : highestCategory;
}

function getMessageForCategory(category, points) {
    if (category === 'Balanced') {
        return 'Good job! You have a balanced approach to life!';
    }
    const messages = {
        Academic: 'You have a bright academic future ahead!, but remember to take care of yourself too! ',
        Work: 'Your work ethic will take you far, but your health and studies are important too!',
        'Well-being': 'You know the importance of taking care of yourself. But remember to focus on your studies and work too!',
    };
    return messages[category];
}


// Updated drawChart to directly use 'points' instead of 'pointsJson'
function drawChart(points) {
    const dataArray = [['Category', 'Points']];
    Object.entries(points).forEach(([category, value]) => {
        dataArray.push([category, value]);
    });

    var data = google.visualization.arrayToDataTable(dataArray);
    var options = {
        is3D: true,
        backgroundColor: 'transparent', 
        chartArea: {width: '80%', height: '80%'}, // Example to adjust the chart area
        legend: {position: 'right', textStyle: {color: 'blue', fontSize: 12}}, // Customize legend
        
    };
    var chart = new google.visualization.PieChart(document.getElementById('piechart_3d'));
    chart.draw(data, options);
}

function restartGame() {
    localStorage.removeItem('gamePoints');
    window.location.href = 'index.html';
}