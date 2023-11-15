if __name__ == '__main__':
    meals = {
        'breakfast': 'yogurt, granola, and fruit',
        'lunch': 'Cupbop',
        'dinner': 'lasagna and salad'
    }
    food = meals['dinner']
    print(f"I had {food} for dinner.")
    food = meals.get('brunch', 'buttered toast and apple juice')
    print(f"I had {food} for brunch.")
