if (monthlySales && monthlySales.labels) {

    new Chart(
        document.getElementById("monthlySalesChart"),
        {
            type:"line",
            data:{
                labels:monthlySales.labels,
                datasets:[{
                    label:"Revenue",
                    data:monthlySales.values
                }]
            }
        }
    );

}

if (categorySales && categorySales.labels) {

    new Chart(
        document.getElementById("categoryChart"),
        {
            type: "bar",
            data: {
                labels: categorySales.labels,
                datasets: [{
                    label: "Revenue",
                    data: categorySales.values
                }]
            }
        }
    );

}