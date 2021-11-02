google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

var data = google.visualization.arrayToDataTable([
    ['Status', 'Quantity'],
    ['Ca nhiễm', 905477],
    ['Tử Vong', 21910],
    ['Phục hồi', 813963]
]);

var options = {
    title: 'COVID CHART',
    titleTextStyle: {
    fontSize: 25
    },
    pieStartAngle: 270,
    chartArea:{
    left: 200,
    width: 700
}
};

var chart = new google.visualization.PieChart(document.getElementById('chart_covid'));

chart.draw(data, options);
}