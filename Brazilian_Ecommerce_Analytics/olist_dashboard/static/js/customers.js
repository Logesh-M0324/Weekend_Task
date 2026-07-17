new Chart(
    document.getElementById("customerDistributionChart"),
    {
        type:"bar",
        data:{
            labels:customerDistribution.labels,
            datasets:[{
            label:"Customers",
            data:customerDistribution.values
            }]
        }
    }
);

new Chart(
    document.getElementById("purchaseFrequencyChart"),
    {
        type:"bar",
        data:{
            labels:purchaseFrequency.labels,
            datasets:[{
            label:"Customers",
            data:purchaseFrequency.values
        }]
    }
    }
);

new Chart(
    document.getElementById("clvChart"),
    {
        type:"line",
        data:{
            labels:customerCLV.labels,
            datasets:[{
            label:"Customer Lifetime Value",
            data:customerCLV.values
            }]
        }
    }
);

new Chart(
    document.getElementById("repeatCustomerChart"),
    {
        type:"pie",
        data:{
            labels:repeatSummary.labels,
            datasets:[{
            data:repeatSummary.values
        }]
    }
    }
);