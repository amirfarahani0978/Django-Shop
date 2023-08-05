let btns = document.querySelectorAll(".product-form button")
btns.forEach(btn=>{
    btn.addEventListener("click", addToCart)
})
function addToCart(e){
    let product_id = e.target.value
    console.log('amir')
    let url = '/order/cart/add/'
    let data = {id:product_id}
    fetch(url ,{
        method:"POST",
        headers:{"Content-Type":"application/Json" , 'X-CSRFToken': csrftoken},
        body:JSON.stringify(data),
    })
    .then(res=>res.json())
    .then(data=>{
        console.log(data)
    })
    .catch(error=>console.log(error))
}
// function addToCart(e) {
//     let product_id = e.target.value;
//     console.log('amir');
//     let url = '/order/cart/add/';
//     let data = {id: product_id};

//     $.ajax({
//         url: url,
//         type: 'POST',
//         headers: {
//             "Content-Type": "application/json",
//             'X-CSRFToken': csrftoken
//         },
//         data: JSON.stringify(data),
//         success: function(data) {
//             console.log(data);
//         },
//         error: function(error) {
//             console.log(error);
//         }
//     });
// }