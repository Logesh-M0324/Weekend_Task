new Chart(
    document.getElementById("deliveryTrendChart"),
    {
        type: "line",
        data: {
            labels: deliveryTrend.labels,
            datasets: [{
                label: "Average Delivery Days",
                data: deliveryTrend.values
            }]
        }
    }
);

new Chart(
    document.getElementById("deliveryStatusChart"),
    {
        type: "pie",
        data: {
            labels: deliveryStatus.labels,
            datasets: [{
                data: deliveryStatus.values
            }]
        }
    }
);

new Chart(
    document.getElementById("shippingPerformanceChart"),
    {
        type: "bar",
        data: {
            labels: shippingPerformance.labels,
            datasets: [{
                label: "Average Shipping Days",
                data: shippingPerformance.values
            }]
        }
    }
);