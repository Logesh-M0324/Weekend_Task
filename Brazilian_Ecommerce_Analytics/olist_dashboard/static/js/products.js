new Chart(
    document.getElementById("categorySalesChart"),
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

new Chart(
    document.getElementById("bestProductsChart"),
    {
        type: "bar",
        data: {
            labels: bestProducts.labels,
            datasets: [{
                label: "Units Sold",
                data: bestProducts.values
            }]
        }
    }
);

new Chart(
    document.getElementById("priceChart"),
    {
        type: "line",
        data: {
            labels: priceDistribution.map((_, i) => i + 1),
            datasets: [{
                label: "Price",
                data: priceDistribution
            }]
        }
    }
);

new Chart(
    document.getElementById("popularityChart"),
    {
        type: "pie",
        data: {
            labels: Popularity.labels,
            datasets: [{
                data: Popularity.values
            }]
        }
    }
);