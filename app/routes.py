from app import app
from flask import render_template, request, redirect, url_for, session
from flask_login import current_user, login_required
from app.models import Product, Cart
from app.forms import AddToCartForm, RemoveFromCartForm
import requests

@app.route('/')
@app.route('/home')
def homePage():
    return render_template('index.html')

@app.route('/login')
def loginPage():
    return render_template('login.html')


@app.route('/cart')
def cartPage():
    cart = session.get("cart", [])
    total_cost = 0
    for item in cart:
        total_cost += item['price'] *  item['quantity']
    return render_template('cart.html', cart = cart, total_cost = total_cost)


@app.route('/add_to_cart/<product_id>')
@login_required
def add_to_cart(product_id):
    product = get_product(product_id)
    if product:
        cart = session.get("cart", [])
        item = next((item for item in cart if item["id"] == product_id), None)
        if item:
            item["quantity"] += 1
        else:
            cart.append({
                "id": product_id,
                "name": product["name"],
                "price": product["price"],
                "quantity": 1
            })
        session["cart"] = cart
        return redirect(url_for("cartPage"))
    else:
        return redirect(url_for("productsPage"))
    
    
    
@app.route('/remove_from_cart/<product_id>')
@login_required
def remove_from_cart(product_id):
    cart = session.get("cart", [])
    cart = [item for item in cart if item["id"] != product_id]
    session["cart"] = cart
    return redirect(url_for("cartPage"))


@app.route('/clear_cart')
@login_required
def clear_cart():
    session["cart"] = []
    return redirect(url_for("cartPage"))


@app.route('/products')
def productsPage():
    products = get_products()
    return render_template('products.html', products=products)


def get_product(product_id):
    # replace with code to get a product from a database or other source
    return {
        "1": { "name": "product 1", "price": 10.99 },
        "2": { "name": "product 2", "price": 5.99 },
        "3": { "name": "product 3", "price": 15.99 }
    }.get(product_id)

def get_products():
    # replace with code to get a list of products from a database or other source
    return [
        { "id": "1", "name": "product 1", "price": 10.99 },
        { "id": "2", "name": "product 2", "price": 5.99 },
        { "id": "3", "name": "product 3", "price": 6.99 } 
    ]