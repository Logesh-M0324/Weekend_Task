// =======================================
// Monthly ADR Trend (Line Chart)
// =======================================

const monthlyAdrCanvas = document.getElementById("monthlyAdrChart");

if (monthlyAdrCanvas) {

    new Chart(monthlyAdrCanvas, {

        type: "line",

        data: {

            labels: revenueData.monthly.map(item => item.arrival_date_month),

            datasets: [{

                label: "Average ADR",

                data: revenueData.monthly.map(item => item.average_daily_rate),

                borderColor: "#0d6efd",

                backgroundColor: "rgba(13,110,253,0.2)",

                fill: true,

                tension: 0.4

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    position: "top"

                }

            },

            scales: {

                y: {

                    beginAtZero: true

                }

            }

        }

    });

}



// =======================================
// Revenue by Hotel Type (Bar Chart)
// =======================================

const hotelRevenueCanvas = document.getElementById("hotelRevenueChart");

if (hotelRevenueCanvas) {

    new Chart(hotelRevenueCanvas, {

        type: "bar",

        data: {

            labels: revenueData.hotels.map(item => item.hotel),

            datasets: [{

                label: "Revenue",

                data: revenueData.hotels.map(item => item.revenue),

                backgroundColor: [

                    "#0d6efd",

                    "#198754"

                ]

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    display: false

                }

            },

            scales: {

                y: {

                    beginAtZero: true

                }

            }

        }

    });

}



// =======================================
// ADR by Market Segment (Horizontal Bar)
// =======================================

const marketCanvas = document.getElementById("marketSegmentChart");

if (marketCanvas) {

    new Chart(marketCanvas, {

        type: "bar",

        data: {

            labels: revenueData.segments.map(item => item.market_segment),

            datasets: [{

                label: "Average ADR",

                data: revenueData.segments.map(item => item.average_daily_rate),

                backgroundColor: "#ffc107"

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            indexAxis: "y",

            scales: {

                x: {

                    beginAtZero: true

                }

            }

        }

    });

}



// =======================================
// Weekend vs Weekday Revenue
// =======================================

const stayCanvas = document.getElementById("stayChart");

if (stayCanvas) {

    new Chart(stayCanvas, {

        type: "bar",

        data: {

            labels: Object.keys(revenueData.stay),

            datasets: [{

                label: "Revenue",

                data: Object.values(revenueData.stay),

                backgroundColor: [

                    "#20c997",

                    "#fd7e14"

                ]

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    display: false

                }

            },

            scales: {

                y: {

                    beginAtZero: true

                }

            }

        }

    });

}



// =======================================
// ADR by Customer Type (Doughnut Chart)
// =======================================

const customerCanvas = document.getElementById("customerAdrChart");

if (customerCanvas) {

    new Chart(customerCanvas, {

        type: "doughnut",

        data: {

            labels: revenueData.customers.map(item => item.customer_type),

            datasets: [{

                label: "Average ADR",

                data: revenueData.customers.map(item => item.average_daily_rate),

                backgroundColor: [

                    "#0d6efd",

                    "#198754",

                    "#ffc107",

                    "#dc3545"

                ]

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    position: "bottom"

                }

            }

        }

    });

}