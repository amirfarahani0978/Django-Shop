const cart_data = document.querySelector('.get-cart')
fetch(url)
.then((response)=>{
    for(let i = 0 ; i<response.length ; i++){
        cart_data += `<figure class="product-media">${response[i].name}</figure>`
    }
    throw response.json()
})
.catch(error=>{
    console.log(error)
})
