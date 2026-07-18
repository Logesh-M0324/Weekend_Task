new Chart(
    document.getElementById("salesTrendChart"),
    {
        type: "bar",
        data: {
            labels: monthlySales.labels,
            datasets: [{
                label: "Revenue",
                data: monthlySales.values
            }]
        }
    }
);

new Chart(
    document.getElementById("salesCategoryChart"),
    {
        type: "line",
        data: {
            labels: categorySales.labels,
            datasets: [{
                label: "Revenue",
                data: categorySales.values
            }]
        }
    }
);

new Chart(
    document.getElementById("stateRevenueChart"),
    {
        type: "bar",
        data: {
            labels: stateSales.labels,
            datasets: [{
                label: "Revenue",
                data: stateSales.values
            }]
        }
    }
);

document.getElementById("averageOrderValue").innerHTML =
    "₹ " + averageOrderValue.toLocaleString();