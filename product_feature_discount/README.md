# Objective

Implement a simple feature in Odoo's eCommerce module. The task is to
create a Product Discount Feature where a percentage discount can be applied to
specfic products, and the discounted price should be reflected in the product listings
and on the product detail page in the eCommerce store.

# Task Description:


 
# 1. Create a Discount Field for Products:


-  Add a new field called discount_percentage to the
product.template model, which allows the admin to set a discount (in
percentage) for each product

- The discount should be applied to the product’s original price to calculate the discounted price
- If the discount is set to 0, the product should be sold at its regular price.



# 2. Display Discounted Price on the eCommerce Store:

- Modify the product template in the eCommerce website so that the
discounted price (if applicable) is shown alongside the original price.
- If a product has a discount, the original price should be shown as
"strikethrough" and the discounted price should be displayed as the main
price.
- If there is no discount, only the original price should be shown.


# 3. Adjust Cart and Checkout to Reflect Discount:

- Ensure that when a customer adds a discounted product to the cart, the
correct discounted price is reflected.
- Make sure the discount is applied during the checkout process and on the
final invoice.


# Odoo Version:  Odoo 17 .