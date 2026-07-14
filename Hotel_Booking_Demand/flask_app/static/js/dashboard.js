// Monthly Booking Trend

const monthlyChart = document.getElementById("monthlyChart");

if (monthlyChart) {

    new Chart(monthlyChart, {

        type: "line",

        data: {

            labels: monthly.map(x => x.arrival_date_month),

            datasets: [{

                label: "Bookings",

                data: monthly.map(x => x.bookings)

            }]

        }

    });

}



// Hotel Type

const hotelChart = document.getElementById("hotelChart");

if (hotelChart) {

    new Chart(hotelChart, {

        type: "bar",

        data: {

            labels: hotels.map(x => x.hotel),

            datasets: [{

                label: "Bookings",

                data: hotels.map(x => x.bookings)

            }]

        }

    });

}



// Seasonal Bookings

const seasonChart = document.getElementById("seasonChart");

if (seasonChart) {

    new Chart(seasonChart, {

        type: "pie",

        data: {

            labels: seasons.map(x => x.season),

            datasets: [{

                data: seasons.map(x => x.bookings)

            }]

        }

    });

}



// Lead Time

const leadChart = document.getElementById("leadChart");

if (leadChart) {

    new Chart(leadChart, {

        type: "bar",

        data: {

            labels: leadTime.slice(0,50),

            datasets: [{

                label: "Lead Time",

                data: leadTime.slice(0,50)

            }]

        }

    });

}