from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
automate_is_on = True

while automate_is_on:
    options = menu.get_items()
    chosen_drink = input(f"What would you like to drink? {options}")
    if chosen_drink == 'report':
        coffee_maker.report()
        money_machine.report()
    elif chosen_drink == 'off':
        automate_is_on = False
    else:
        try:
            drink = menu.find_drink(chosen_drink)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        except:
            pass
