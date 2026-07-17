// ================= Payment Method =================

new Chart(
    document.getElementById("paymentMethodChart"),
    {
        type: "pie",
        data: {
            labels: paymentMethods.labels,
            datasets: [{
                data: paymentMethods.values
            }]
        }
    }
);

// ================= Installments =================

new Chart(
    document.getElementById("installmentChart"),
    {
        type: "bar",
        data: {
            labels: Installments.labels,
            datasets: [{
                label: "Orders",
                data: Installments.values
            }]
        }
    }
);

// ================= Review Distribution =================

new Chart(
    document.getElementById("reviewDistributionChart"),
    {
        type: "bar",
        data: {
            labels: reviewDistribution.labels,
            datasets: [{
                label: "Reviews",
                data: reviewDistribution.values
            }]
        }
    }
);

// ================= Review Sentiment =================

new Chart(
    document.getElementById("reviewSentimentChart"),
    {
        type: "pie",
        data: {
            labels: reviewSentiment.labels,
            datasets: [{
                data: reviewSentiment.values
            }]
        }
    }
);

// ================= Monthly Review Trend =================

new Chart(
    document.getElementById("reviewTrendChart"),
    {
        type: "line",
        data: {
            labels: reviewTrend.labels,
            datasets: [{
                label: "Average Review Score",
                data: reviewTrend.values,
                fill: false,
                tension: 0.3
            }]
        }
    }
);

new Chart(
    document.getElementById("satisfactionChart"),
    {
        type: "doughnut",
        data: {
            labels: Satisfaction.labels,
            datasets: [{
                data: Satisfaction.values
            }]
        }
    }
);

new Chart(
    document.getElementById("reviewCategoryChart"),
    {
        type: "bar",
        data: {
            labels: reviewCategory.labels,
            datasets: [{
                label: "Average Rating",
                data: reviewCategory.values
            }]
        }
    }
);