// ===============================
// Cancellation Status Chart
// ===============================

const statusCanvas = document.getElementById("statusChart");

if (statusCanvas) {

    new Chart(statusCanvas, {

        type: "pie",

        data: {

            labels: cancellationData.status.map(item =>
                item.status === 0 ? "Not Cancelled" : "Cancelled"
            ),

            datasets: [{

                label: "Bookings",

                data: cancellationData.status.map(item => item.count),

                backgroundColor: [
                    "#198754",
                    "#dc3545"
                ],

                borderWidth: 1

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    position: "bottom"

                }

            }

        }

    });

}



// ===============================
// Cancellation by Hotel Type
// ===============================

const hotelCanvas = document.getElementById("hotelChart");

if (hotelCanvas) {

    new Chart(hotelCanvas, {

        type: "bar",

        data: {

            labels: cancellationData.hotels.map(item => item.hotel),

            datasets: [{

                label: "Cancelled Bookings",

                data: cancellationData.hotels.map(item => item.cancelled),

                backgroundColor: "#0d6efd"

            }]

        },

        options: {

            responsive: true,

            scales: {

                y: {

                    beginAtZero: true

                }

            }

        }

    });

}



// ===============================
// Cancellation by Market Segment
// ===============================

const marketCanvas = document.getElementById("marketChart");

if (marketCanvas) {

    new Chart(marketCanvas, {

        type: "bar",

        data: {

            labels: cancellationData.markets.map(item => item.market_segment),

            datasets: [{

                label: "Cancelled Bookings",

                data: cancellationData.markets.map(item => item.cancelled),

                backgroundColor: "#ffc107"

            }]

        },

        options: {

            responsive: true,

            indexAxis: "y",

            scales: {

                x: {

                    beginAtZero: true

                }

            }

        }

    });

}



// ===============================
// Cancellation by Deposit Type
// ===============================

const depositCanvas = document.getElementById("depositChart");

if (depositCanvas) {

    new Chart(depositCanvas, {

        type: "doughnut",

        data: {

            labels: cancellationData.deposits.map(item => item.deposit_type),

            datasets: [{

                data: cancellationData.deposits.map(item => item.cancelled),

                backgroundColor: [

                    "#0d6efd",

                    "#198754",

                    "#dc3545",

                    "#ffc107",

                    "#6f42c1"

                ]

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    position: "bottom"

                }

            }

        }

    });

}



// ===============================
// Average Lead Time by Cancellation
// ===============================

const leadCanvas = document.getElementById("leadTimeChart");

if (leadCanvas) {

    new Chart(leadCanvas, {

        type: "bar",

        data: {

            labels: cancellationData.leadTime.map(item =>
                item.is_canceled === 0
                    ? "Not Cancelled"
                    : "Cancelled"
            ),

            datasets: [{

                label: "Average Lead Time",

                data: cancellationData.leadTime.map(item => item.lead_time),

                backgroundColor: [

                    "#198754",

                    "#dc3545"

                ]

            }]

        },

        options: {

            responsive: true,

            scales: {

                y: {

                    beginAtZero: true

                }

            },

            plugins: {

                legend: {

                    display: false

                }

            }

        }

    });

}