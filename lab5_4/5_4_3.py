# Ethical guidelines: transparency, fairness, and user feedback
# Sample product catalog and user history
products = [
    {"id": 1, "name": "Wireless Mouse", "category": "Electronics"},
    {"id": 2, "name": "Yoga Mat", "category": "Fitness"},
    {"id": 3, "name": "Bluetooth Speaker", "category": "Electronics"},
    {"id": 4, "name": "Cookbook", "category": "Books"},
    {"id": 5, "name": "Running Shoes", "category": "Fitness"},
]

user_history = [
    {"user_id": 101, "purchased": [1, 3]},  # Electronics
    {"user_id": 102, "purchased": [2, 5]},  # Fitness
    {"user_id": 103, "purchased": [4]},     # Books
]

def get_user_history(user_id):
    for user in user_history:
        if user["user_id"] == user_id:
            return user["purchased"]
    return []

def recommend_products(user_id):
    purchased_ids = get_user_history(user_id)
    if not purchased_ids:
        print("No purchase history found. Showing popular products.")
        # Fairness: recommend from all categories if no history
        recommended = products[:3]
    else:
        # Find categories the user likes
        categories = set()
        for pid in purchased_ids:
            for prod in products:
                if prod["id"] == pid:
                    categories.add(prod["category"])
        # Recommend products from those categories not already purchased
        recommended = []
        for prod in products:
            if prod["category"] in categories and prod["id"] not in purchased_ids:
                recommended.append(prod)
        # Fairness: If no new products in those categories, recommend from other categories
        if not recommended:
            recommended = [prod for prod in products if prod["id"] not in purchased_ids][:3]
    # Transparency: Show why these products are recommended
    print("\nRecommended products for you (based on your interests):")
    for prod in recommended:
        print(f"- {prod['name']} (Category: {prod['category']})")
    print("\nTransparency: Recommendations are based on your previous purchases and interests. We avoid favoritism towards any brand or category.")
    print("Fairness: If you feel these recommendations are not relevant, please provide feedback below.")

def get_user_feedback():
    feedback = input("Are these recommendations helpful? (yes/no): ")
    if feedback.lower() == "no":
        print("Thank you for your feedback. We will use it to improve our recommendations.")
    else:
        print("Glad you found them helpful!")

if __name__ == "__main__":
    try:
        user_id = int(input("Enter your user ID: "))
        recommend_products(user_id)
        get_user_feedback()
    except ValueError:
        print("Invalid user ID. Please enter a numeric value.")
