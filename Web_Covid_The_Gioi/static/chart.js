google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

var data = google.visualization.arrayToDataTable([
    ['Status', 'Quantity'],
    ['Confirmed', 905477],
    ['Deaths', 21910],
    ['Recovered', 813963]
]);

var options = {
    title: 'COVID CHART',
    titleTextStyle: {
    fontSize: 25
    },
    pieStartAngle: 270,
    chartArea:{
    left: 200,
    width: 1500
}
};

var chart = new google.visualization.PieChart(document.getElementById('chart_covid'));

chart.draw(data, options);
}