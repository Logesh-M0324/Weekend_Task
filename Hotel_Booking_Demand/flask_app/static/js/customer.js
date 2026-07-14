// Customer Type

new Chart(

document.getElementById("customerTypeChart"),

{

type:"pie",

data:{

labels:customerData.customerTypes.map(x=>x.customer_type),

datasets:[{

data:customerData.customerTypes.map(x=>x.count)

}]

}

}

);


// Market Segment

new Chart(

document.getElementById("marketChart"),

{

type:"bar",

data:{

labels:customerData.marketSegments.map(x=>x.market_segment),

datasets:[{

label:"Bookings",

data:customerData.marketSegments.map(x=>x.count)

}]

}

}

);


// Countries

new Chart(

document.getElementById("countryChart"),

{

type:"bar",

data:{

labels:customerData.countries.map(x=>x.country),

datasets:[{

label:"Bookings",

data:customerData.countries.map(x=>x.count)

}]

}

}

);


// Repeat Guests

new Chart(

document.getElementById("repeatChart"),

{

type:"doughnut",

data:{

labels:["New","Repeated"],

datasets:[{

data:customerData.repeatGuests.map(x=>x.count)

}]

}

}

);