if __name__ == '__main__':
    meals = {
        'breakfast': 'yogurt, granola, and fruit',
        'lunch': 'Cupbop',
        'dinner': 'lasagna and salad'
    }
    for meal, description in meals.items():
        print(f'For {meal} we are serving {description}. 😋')
