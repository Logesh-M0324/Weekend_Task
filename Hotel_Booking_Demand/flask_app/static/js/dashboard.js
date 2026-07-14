// ================================
// Monthly Booking Trend
// ================================

const monthlyCanvas = document.getElementById("monthlyTrendChart");

if (monthlyCanvas) {

    new Chart(monthlyCanvas, {

        type: "line",

        data: {

            labels: dashboardData.monthly.map(

                item => item.Month

            ),

            datasets: [{

                label: "Bookings",

                data: dashboardData.monthly.map(

                    item => item.Bookings

                ),

                borderColor: "#0d6efd",

                backgroundColor: "rgba(13,110,253,0.15)",

                fill: true,

                tension: 0.4

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false

        }

    });

}

// ================================
// Booking Status
// ================================

const bookingCanvas = document.getElementById("bookingStatusChart");

if (bookingCanvas) {

    new Chart(bookingCanvas, {

        type: "doughnut",

        data: {

            labels: dashboardData.bookingStatus.map(

                item => item.Status

            ),

            datasets: [{

                data: dashboardData.bookingStatus.map(

                    item => item.Count

                )

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false

        }

    });

}
