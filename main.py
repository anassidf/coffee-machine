MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins={
    'quarters' : 0.25,
    'dimes' :0.10 ,
    'nickles': 0.05,
    'pennies' : 0.01
}
profit = 0

proccess = 'on'
while proccess == 'on':

    order = input('What would you like? (espresso/latte/cappuccino): ')
    if order == 'off':
        proccess = 'off'
    if order == 'report':
        for resourceK, resourceV in resources.items():
            print(resourceK, resourceV)
        continue
    #resource check
    if order == 'latte':
        w_state = float(resources['water']) - float(MENU['latte']['ingredients']['water'])
        m_state = float(resources['milk']) - float(MENU['latte']['ingredients']['milk'])
        c_state = float(resources['coffee']) - float(MENU['latte']['ingredients']['coffee'])
        if w_state < 0:
            print('Sorry there is not enough water')
            continue
        elif m_state < 0:
            print('Sorry there is not enough Milk')
            continue
        elif c_state < 0:
            print('Sorry there is not enough Coffee')
            continue
        # money proccess
        else :

            quarters = float(input('how many quarters? '))
            dimes = float(input('how many dimes? '))
            nickles = float(input('how many nickles? '))
            pennies = float(input('how many pennies? '))

            total = coins['quarters'] * quarters + coins['dimes'] * dimes + coins['nickles'] * nickles + coins[
                'pennies'] * pennies
            if total < MENU['latte']['cost']:
                print('Sorry that\'s not enough money. Money refunded')
                continue
            else:
                #update profit and resources
                #calculate the change
                change = total - MENU['latte']['cost']
                if change > 0:
                    print(('Here is ${} dollars in change').format(change))

                profit += MENU['latte']['cost']
                resources["water"] -= MENU['latte']['ingredients']['water']
                resources["milk"] -= MENU['latte']['ingredients']['milk']
                resources["coffee"] -= MENU['latte']['ingredients']['coffee']
                print('Here is your latte. Enjoy')




    elif order == 'espresso':
        w_state = float(resources['water']) - float(MENU['espresso']['ingredients']['water'])
        c_state = float(resources['coffee']) - float(MENU['espresso']['ingredients']['coffee'])
        if w_state < 0:
            print('Sorry there is not enough water')
            continue

        elif c_state < 0:
            print('Sorry there is not enough Coffee')
            continue

        else :
            quarters = float(input('how many quarters? '))
            dimes = float(input('how many dimes? '))
            nickles = float(input('how many nickles? '))
            pennies = float(input('how many pennies? '))

            total = coins['quarters'] * quarters + coins['dimes'] * dimes + coins['nickles'] * nickles + coins[
                'pennies'] * pennies
            if total < MENU['espresso']['cost']:
                print('Sorry that\'s not enough money. Money refunded')
                continue
            else:
                # update profit and resources
                # calculate the change
                change = total -  MENU['espresso']['cost']
                if change > 0:
                    print(('Here is ${} dollars in change').format(change))

                profit +=MENU['espresso']['cost']
                resources["water"] -= MENU['espresso']['ingredients']['water']
                resources["milk"] -= MENU['espresso']['ingredients']['milk']
                resources["coffee"] -= MENU['espresso']['ingredients']['coffee']
                print('Here is your espresso. Enjoy')

    elif order == 'cappuccino':
        w_state = float(resources['water']) - float(MENU['cappuccino']['ingredients']['water'])
        c_state = float(resources['coffee']) - float(MENU['cappuccino']['ingredients']['coffee'])
        m_state = float(resources['milk']) - float(MENU['cappuccino']['ingredients']['milk'])
        if w_state < 0:
            print('Sorry there is not enough water')
            continue

        elif c_state < 0:
            print('Sorry there is not enough Coffee')
            continue
        elif m_state < 0:
            print('Sorry there is not enough Milk')
            continue
        else :
            quarters = float(input('how many quarters? '))
            dimes = float(input('how many dimes? '))
            nickles = float(input('how many nickles? '))
            pennies = float(input('how many pennies? '))

            total = coins['quarters'] * quarters + coins['dimes'] * dimes + coins['nickles'] * nickles + coins[
                'pennies'] * pennies
            if total < MENU['cappuccino']['cost']:
                print('Sorry that\'s not enough money. Money refunded')
                continue
            else:
                # update profit and resources
                # calculate the change
                change = total -  MENU['cappuccino']['cost']
                if change > 0:
                    print(('Here is ${} dollars in change').format(change))

                profit +=MENU['cappuccino']['cost']
                resources["water"] -= MENU['cappuccino']['ingredients']['water']
                resources["milk"] -= MENU['cappuccino']['ingredients']['milk']
                resources["coffee"] -= MENU['cappuccino']['ingredients']['coffee']
                print('Here is your cappuccino. Enjoy')









