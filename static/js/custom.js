$(document).ready(function(){
$('.increment-btn').click(function(e){
e.preventDefault();
var inc_value=$(this).closest('.product_data').find('.qty-input').val();
var value=parseInt(inc_value,10);
value=isNaN(value)?0:value;
if(value<10){
value++;
$(this).closest('.product_data').find('.qty-input').val(value)}
});


$('.decrement-btn').click(function(e){
e.preventDefault();
var dec_value=$(this).closest('.product_data').find('.qty-input').val();
var value=parseInt(dec_value,10);
value=isNaN(value)?0:value;
if(value>1){
value--;
$(this).closest('.product_data').find('.qty-input').val(value)}
});

$('.addToCartBtn').click(function(e){
    e.preventDefault();

    var product_id = $(this).closest('.product_data').find('.product_id').val();
    console.log(product_id);
    var product_qty = $(this).closest('.product_data').find('.qty-input').val();
    var token = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
        type: "POST",
        url: '/add-to-cart',
        data: {
            'product_id': product_id,
            'product_qty': product_qty,
            'csrfmiddlewaretoken': token
        },
        'Content-Type': "application/json",
        success: function(response){
            console.log(response);

            alertify.success(response.status);
        }

    });
});

$('.changeQuantity').click(function(e){
    e.preventDefault();

    var product_id = $(this).closest('.product_data').find('.prod_id').val();
    console.log(product_id);
    var product_qty = $(this).closest('.product_data').find('.qty-input').val();
    var token = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
        type: "POST",
        url: '/update-cart',
        data: {
            'product_id': product_id,
            'product_qty': product_qty,
            'csrfmiddlewaretoken': token
        },
        'Content-Type': "application/json",
        success: function(response){
            console.log(response);

            alertify.success(response.status);
        }

    });
});

$('.delete-cart-item').click(function(e){
e.preventDefault();
var product_id=$(this).closest('.product_data').find('.prod_id').val();
var token = $('input[name=csrfmiddlewaretoken]').val();
$.ajax({
        type: "POST",
        url: '/delete-cart-item',
        data: {
            'product_id': product_id,

            'csrfmiddlewaretoken': token
        },
        'Content-Type': "application/json",
        success: function(response){
            console.log(response);

            alertify.success(response.status)

            $('.cart').load(location.href+" .cart")
        }

    });
});

$(document).ready(function(){
$('.increment-btn').click(function(e){
e.preventDefault();
var inc_value=$(this).closest('.chinese_product_data').find('.qty-input').val();
var value=parseInt(inc_value,10);
value=isNaN(value)?0:value;
if(value<10){
value++;
$(this).closest('.chinese_product_data').find('.qty-input').val(value)}
});


$('.decrement-btn').click(function(e){
e.preventDefault();
var dec_value=$(this).closest('.chinese_product_data').find('.qty-input').val();
var value=parseInt(dec_value,10);
value=isNaN(value)?0:value;
if(value>1){
value--;
$(this).closest('.chinese_product_data').find('.qty-input').val(value)}
});


//$('.chineseAddToCartBtn').click(function(e){
//    e.preventDefault();
//    console.log("click");
//
//    var product_id = $(this).closest('.chinese_product_data').find('.product_id').val();
//    console.log(product_id);
//    var product_qty = $(this).closest('.chinese_product_data').find('.qty-input').val();
//    var token = $('input[name=csrfmiddlewaretoken]').val();
//
//    $.ajax({
//        type: "POST",
//        url: '/chinese-add-to-cart',
//        data: {
//            'product_id': product_id,
//            'product_qty': product_qty,
//            'csrfmiddlewaretoken': token
//        },
//        'Content-Type': "application/json",
//        success: function(response){
//            console.log(response);
//
//            alertify.success(response.status);
//        }
//
//    });
//});

$('.chinesechangeQuantity').click(function(e){
    e.preventDefault();

    var product_id = $(this).closest('.product_data').find('.prod_id').val();
    console.log(product_id);
    var product_qty = $(this).closest('.product_data').find('.qty-input').val();
    var token = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
        type: "POST",
        url: '/chinese-update-cart',
        data: {
            'product_id': product_id,
            'product_qty': product_qty,
            'csrfmiddlewaretoken': token
        },
        'Content-Type': "application/json",
        success: function(response){
            console.log(response);

            alertify.success(response.status);
        }

    });
});

$('.chinese-delete-cart-item').click(function(e){
e.preventDefault();
var product_id=$(this).closest('.product_data').find('.prod_id').val();
var token = $('input[name=csrfmiddlewaretoken]').val();
$.ajax({
        type: "POST",
        url: '/chinese-delete-cart-item',
        data: {
            'product_id': product_id,

            'csrfmiddlewaretoken': token
        },
        'Content-Type': "application/json",
        success: function(response){
            console.log(response);

            alertify.success(response.status)

            $('.cart').load(location.href+" .cart")
        }

    });
})
});