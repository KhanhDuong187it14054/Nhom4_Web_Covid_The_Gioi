fetch('../static/model/data.json')
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        for(var i=0; i < data.length; i++) {
            var htmlObj = document.getElementById('info_data');
            htmlObj.innerHTML = htmlObj.innerHTML 
            + "<br>"
            + "<tr>"
            + "<td>"+ data[i].country + "</td>"
            + "<td>"+  data[i].confirmed + "</td>"
            + "<td>"+  data[i].deaths + "</td>"
            + "<td>"+  data[i].recovered + "</td>"
            + "</tr>"
            + "<br>"
            ;
        }
    })
    .catch(function(err){
        console.log(err);
    });