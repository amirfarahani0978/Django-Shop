let btns = document.querySelectorAll(".product-form button")
btns.forEach(btn=>{
    btn.addEventListener("click", addToCart)
})
function addToCart(e){
    let product_id = e.target.value
    console.log(product_id)
}