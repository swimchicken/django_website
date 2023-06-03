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