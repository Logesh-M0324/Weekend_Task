new Chart(
    document.getElementById("sellerRevenueChart"),
    {
        type: "bar",
        data: {
            labels: sellerRevenue.labels,
            datasets: [{
                label: "Revenue",
                data: sellerRevenue.values
            }]
        }
    }
);

new Chart(
    document.getElementById("sellerPerformanceChart"),
    {
        type: "bar",
        data: {
            labels: sellerPerformance.labels,
            datasets: [{
                label: "Performance Score",
                data: sellerPerformance.values
            }]
        }
    }
);

new Chart(
    document.getElementById("sellerLocationChart"),
    {
        type: "pie",
        data: {
            labels: sellerLocations.labels,
            datasets: [{
                data: sellerLocations.values
            }]
        }
    }
);