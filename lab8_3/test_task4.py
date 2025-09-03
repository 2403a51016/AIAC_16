import unittest
from task4 import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def test_total_cost_empty_cart(self):
        cart = ShoppingCart()
        self.assertEqual(cart.total_cost(), 0)

    def test_total_cost_single_item(self):
        cart = ShoppingCart()
        cart.add_item("apple", 2.0)
        self.assertEqual(cart.total_cost(), 2.0)

    def test_total_cost_multiple_same_item(self):
        cart = ShoppingCart()
        cart.add_item("banana", 1.5)
        cart.add_item("banana", 1.5)
        self.assertEqual(cart.total_cost(), 3.0)

    def test_total_cost_multiple_different_items(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1.0)
        cart.add_item("banana", 2.0)
        self.assertEqual(cart.total_cost(), 3.0)

    def test_total_cost_after_removal(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1.0)
        cart.add_item("apple", 1.0)
        cart.add_item("banana", 2.0)
        cart.remove_item("apple")
        self.assertEqual(cart.total_cost(), 3.0)  # 1 apple + 1 banana

    def test_total_cost_after_all_items_removed(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1.0)
        cart.remove_item("apple")
        self.assertEqual(cart.total_cost(), 0)

    def test_remove_item_not_in_cart(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1.0)
        cart.remove_item("banana")  # Should not raise
        self.assertEqual(cart.total_cost(), 1.0)

    def test_add_and_remove_multiple_items(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1.0)
        cart.add_item("banana", 2.0)
        cart.add_item("banana", 2.0)
        cart.remove_item("banana")
        self.assertEqual(cart.total_cost(), 3.0)  # 1 apple + 1 banana

    def test_remove_item_until_empty(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1.0)
        cart.add_item("apple", 1.0)
        cart.remove_item("apple")
        cart.remove_item("apple")
        self.assertEqual(cart.total_cost(), 0)

    def test_add_item_with_different_prices(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1.0)
        cart.add_item("apple", 2.0)  # Should only increment quantity, price stays as first
        self.assertEqual(cart.total_cost(), 2.0)

    def test_cart_state_after_removal(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1.0)
        cart.remove_item("apple")
        self.assertNotIn("apple", cart.items)

if __name__ == "__main__":
    unittest.main()