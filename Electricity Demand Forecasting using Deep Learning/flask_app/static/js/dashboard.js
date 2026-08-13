const labels = [
    "00:00",
    "04:00",
    "08:00",
    "12:00",
    "16:00",
    "20:00",
    "23:00"
];


const demandData = [
    26000,
    24500,
    28500,
    32000,
    34000,
    35000,
    31500
];


const ctx =
    document
        .getElementById("historicalChart");


new Chart(ctx, {

    type: "line",

    data: {

        labels: labels,

        datasets: [{

            label: "Electricity Demand (MW)",

            data: demandData,

            borderWidth: 2,

            tension: 0.3,

            fill: false

        }]

    },

    options: {

        responsive: true,

        maintainAspectRatio: false,

        plugins: {

            legend: {
                display: true
            }

        },

        scales: {

            y: {

                title: {

                    display: true,

                    text: "Demand (MW)"

                }

            },

            x: {

                title: {

                    display: true,

                    text: "Time"

                }

            }

        }

    }

});