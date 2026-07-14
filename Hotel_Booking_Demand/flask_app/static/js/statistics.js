// // =======================================
// // Normality Test Summary
// // =======================================

// const normalityCanvas = document.getElementById("normalityChart");

// if (normalityCanvas) {

//     new Chart(normalityCanvas, {

//         type: "bar",

//         data: {

//             labels: statisticsData.normality.map(item => item.Feature),

//             datasets: [{

//                 label: "P-Value",

//                 data: statisticsData.normality.map(item => item["P-Value"]),

//                 backgroundColor: "#0d6efd"

//             }]

//         },

//         options: {

//             responsive: true,

//             maintainAspectRatio: false,

//             plugins: {

//                 legend: {

//                     display: false

//                 }

//             },

//             scales: {

//                 y: {

//                     beginAtZero: true

//                 }

//             }

//         }

//     });

// }



// // =======================================
// // VIF Chart
// // =======================================

// const vifCanvas = document.getElementById("vifChart");

// if (vifCanvas) {

//     new Chart(vifCanvas, {

//     type: "bar",

//     data: {

//         labels: statisticsData.vif.map(item => item.Feature),

//         datasets: [{

//             label: "VIF",

//             data: statisticsData.vif.map(item => item.VIF),

//             backgroundColor: "#198754"

//         }]

//     },

//     options: {

//         responsive: true,

//         maintainAspectRatio: false,

//         indexAxis: "y"

//     }

// });

// }



// // =======================================
// // Strong Correlations
// // =======================================

// const correlationCanvas = document.getElementById("correlationChart");

// if (correlationCanvas) {

//     new Chart(correlationCanvas, {

//         type: "bar",

//         data: {

//             labels: statisticsData.correlation.map(item =>

//                 item.Feature_1 + " vs " + item.Feature_2

//             ),

//             datasets: [{

//                 label: "Correlation",

//                 data: statisticsData.correlation.map(item => item.Correlation),

//                 backgroundColor: "#ffc107"

//             }]

//         },

//         options: {

//             responsive: true,

//             maintainAspectRatio: false,

//             plugins: {

//                 legend: {

//                     display: false

//                 }

//             },

//             scales: {

//                 y: {

//                     min: -1,

//                     max: 1

//                 }

//             }

//         }

//     });

// }



// // =======================================
// // Independent t-Test Result
// // =======================================

// const ttestCanvas = document.getElementById("ttestChart");

// if (ttestCanvas) {

//     const significant = statisticsData.ttest.filter(

//         item => item.Decision === "Reject Null Hypothesis"

//     ).length;

//     const notSignificant = statisticsData.ttest.length - significant;

//     new Chart(ttestCanvas, {

//         type: "pie",

//         data: {

//             labels: [

//                 "Reject H₀",

//                 "Fail to Reject H₀"

//             ],

//             datasets: [{

//                 data: [

//                     significant,

//                     notSignificant

//                 ],

//                 backgroundColor: [

//                     "#dc3545",

//                     "#198754"

//                 ]

//             }]

//         },

//         options: {

//             responsive: true,

//             maintainAspectRatio: false,

//             plugins: {

//                 legend: {

//                     position: "bottom"

//                 }

//             }

//         }

//     });

// }

const vifCanvas = document.getElementById("vifChart");

if (vifCanvas) {

    const filtered = statisticsData.vif.filter(item => item.VIF !== null);

    new Chart(vifCanvas, {

        type: "bar",

        data: {

            labels: filtered.map(item => item.Feature),

            datasets: [{

                label: "VIF",

                data: filtered.map(item => item.VIF),

                backgroundColor: "#198754"

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            indexAxis: "y",

            plugins: {

                legend: {

                    display: false

                }

            },

            scales: {

                x: {

                    beginAtZero: true

                }

            }

        }

    });

}

// =====================================
// Strong Correlation Chart
// =====================================

const correlationCanvas = document.getElementById("correlationChart");

if (correlationCanvas) {

    new Chart(correlationCanvas, {

        type: "bar",

        data: {

            labels: statisticsData.correlation.map(

                item => item["Variable 1"] + " ↔ " + item["Variable 2"]

            ),

            datasets: [{

                label: "Correlation",

                data: statisticsData.correlation.map(

                    item => item.Correlation

                ),

                backgroundColor: "#0d6efd"

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

                    min: -1,

                    max: 1

                }

            }

        }

    });

}