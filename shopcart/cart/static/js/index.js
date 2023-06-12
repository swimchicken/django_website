let slides = document.querySelectorAll('home .slide');

let index = 0;

function next(){
    slides[index].classList.remove('active');
    index = (index + 1) % slides.length;
    slides[index].classList.add('active');
}
function prev(){
    slides[index].classList.remove('active');
    index = (index - 1 + slides.length) % slides.length;
    slides[index].classList.add('active');
}



let darkmode = document.querySelector('#darkmode-icon');

darkmode.onclick = () => {
    darkmode.classList.toggle('fa-sun-bright');
    document.body.classList.toggle('dark-mode');
}


var cartButton = document.getElementById("cart-button");
var cartPopup = document.getElementById("cart-popup");
var isCartOpen = false;

cartButton.addEventListener("click", function(event) {
  event.preventDefault();
  if (isCartOpen) {
    cartPopup.style.display = "none";
  } else {
    cartPopup.style.display = "block";
  }
  isCartOpen = !isCartOpen;
});

// 添加結帳按鈕的點擊事件處理器
var checkoutButton = document.getElementById("checkout-button");
checkoutButton.addEventListener("click", function(event) {
  // 執行結帳相關的操作
});

// 點擊頁面其他地方時關閉小視窗
document.addEventListener("click", function(event) {
  if (!cartPopup.contains(event.target) && event.target !== cartButton) {
    cartPopup.style.display = "none";
    isCartOpen = false;
  }
});





/* ajax 後端傳輸 */


/*

$(document).ready(function() {
    // 綁定每個"add to cart"按鈕的點擊事件
    $('.add-to-cart').click(function(event) {
        event.preventDefault(); // 防止點擊後跳轉到其他頁面

        var productName = $(this).data('product-name');
        var price = $(this).data('price');

        console.log(productName, price);
        addToCart(productName, price);
    });
});



function addToCart(productName,money){
    $.ajax({
         url: '/add-to-cart/',
         type: 'POST',
         data: {
            'product_name': productName,
            'money': money
         },
         dataType: 'json',
          success: function (response) {
             // 在請求成功的情況下執行的代碼
             console.log('Success:', response);
             alert('Product added to cart successfully.');
          },
          error: function (xhr, textStatus, errorThrown) {
             // 在請求失敗的情況下執行的代碼
             console.log('Error:', errorThrown);
             alert('Failed to add product to cart.');
          }
    });
}

*/