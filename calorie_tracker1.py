from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt

# asking user to input kcal limit
Calorie_Goal_limit = int(input("What is your calorie goal "))
# asking user to input protein goal in grams
Protein_goal = int(input("What is your protein goal "))
# asking user to input fat goal in grams
Fat_goal = int(input("What is your fat goal "))
# asking user to input carb goal in grams
Carb_goal = int(input("What is your carb goal "))

Food_ate_today = []


@dataclass
class Food:
    name: str  # so user can input a string
    calories: int  # user can input an integer
    protein: int  # user can input an integer
    fat: int  # user can input an integer
    carbs: int  # user can input an integer


done = False  # so while loop continues to run

while not done:
    print(""" 
          (1) Add new food   
          (2) Visualize  date
          (3) Quit
          """)  # string which will give the user 3 options to choose from.

    choice = input("Choose an option ")  # user chooses an option

    if choice == "1":  # if it == 1 then you add new food
        print("Adding a new food")
        name = input("Name: ")  # name of food
        calories = int(input("Calories: "))  # amount of calories in food
        proteins = int(input("Protein: "))  # amount of protein
        fats = int(input("Fats: "))  # amount Fats
        carbs = int(input("Carbs: "))  # amount carbs
        # calls the Food class with all the arguments passed
        food = Food(name, calories, proteins, fats, carbs)
        Food_ate_today.append(food)  # add food you ate too list
        print("Successfully added to tracker")

    elif choice == "2":  # if it == 2 then you create a visualization
        # sum the calories in food list
        calories_sum = sum(food.calories for food in Food_ate_today)
        # sum the protein in food_ate_today
        proteins_sum = sum(food.protein for food in Food_ate_today)
        # sum the fat in food_ate_today
        fats_sum = sum(food.fat for food in Food_ate_today)
        # sum carbs in food_ate_today
        carbs_sum = sum(food.carbs for food in Food_ate_today)

        fig, axs = plt.subplots(2, 2)  # create a 4 charts so 2 by 2
        axs[0, 0].pie([proteins_sum, fats_sum, carbs_sum], labels=[
            "Proteins", "Fats", "Carbs"], autopct="%1.1f%%")  # shows distribution of macros

        axs[0, 0].set_title("Macronutrient Distribution")  # create title
        axs[0, 1].bar([0, 1, 2], [proteins_sum,
                      fats_sum, carbs_sum], width=0.4)  # creates bar chart keeping track of the sums of all the macronutrients
        axs[0, 1].bar([0.5, 1.5, 2.5], [Protein_goal,
                      Fat_goal, Carb_goal], width=0.4)
        axs[0, 1].set_title("Macronutrient Progress")  # create title

        axs[1, 0].pie([calories_sum, Calorie_Goal_limit - calories_sum],  # creates a pie chart for the calorie limit progress
                      labels=["Calories", "Remaining"], autopct="%1.1f%%")
        axs[1, 0].set_title("Calories Goal Progress")  # create title

        axs[1, 1].plot(list(range(len(Food_ate_today))), np.cumsum(
            [food.calories for food in Food_ate_today]), label="Calories Eaten")
        axs[1, 1].plot(list(range(len(Food_ate_today))), [
                       Calorie_Goal_limit] * len(Food_ate_today), label="Calorie Goal") # creates a line graph to show progress with calories eaten over time
        axs[1, 1].legend() # creates legend
        axs[1, 1].set_title("Calories Goal Over Time") # create title

        fig.tight_layout #adjust padding around and between subplots
        plt.show() # show visualization

    elif choice == "q": 
        done = True # if user inputs q then done = true so while loop ends
    else:
        print("Invalid Choice") #else it's wrong choice
