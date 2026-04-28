# TIL: Law of Demeter

Today I learned about the Law of Demeter, and it's super handy. Basically, it's a principle that tells your code to "only talk to your immediate friends." No deep dives into an object's friends' friends.

The core idea is simple: an object should only call methods on itself, objects passed in as arguments, objects it creates, or its direct component objects. The big takeaway is to avoid long chains of method calls like `obj.getA().getB().getC()`.

Why does this matter? Because if the internal structure of `A` or `B` changes, your code that calls `obj.getA().getB().getC()` breaks. It makes your code tightly coupled and a nightmare to refactor or debug. Less coupling means easier changes and more robust code.

Here's a quick example of what to watch out for:

```python
# Bad example, breaking the Law of Demeter:
order_total = customer.getCart().getItems().getTotalCost()
```

Instead, `customer` or `cart` should expose the total directly. You'd ideally want to call something like `customer.getCartTotal()` or `cart.getTotalCost()`. This keeps your objects focused and less reliant on knowing the intricate details of other objects. Keep it simple!
