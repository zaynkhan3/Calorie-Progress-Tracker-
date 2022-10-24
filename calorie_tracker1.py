from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt

Calorie_Goal_limit = 3000  # kcal
Protein_goal = 160  # in grams
Fat_goal = 60  # in grams
Carb_goal = 300  # in grams

Food_ate_today = []


@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int


done = False

while not done:
    print(""" 
          (1) Add new food
          (2) Visualize  date
          (3) Quit
          """)

    choice = input("Choose an option ")

    if choice == "1":
        print("Adding a new food")
        name = input("Name: ")
        calories = int(input("Calories: "))
        proteins = int(input("Protein: "))
        fats = int(input("Fats: "))
        carbs = int(input("Carbs: "))
        food = Food(name, calories, proteins, fats, carbs)
        Food_ate_today.append(food)
        print("Successfully added to tracker")

    elif choice == "2":
        calories_sum = sum(food.calories for food in Food_ate_today)
        proteins_sum = sum(food.protein for food in Food_ate_today)
        fats_sum = sum(food.fat for food in Food_ate_today)
        carbs_sum = sum(food.carbs for food in Food_ate_today)

        fig, axs = plt.subplots(2, 2)
        axs[0, 0].pie([proteins_sum, fats_sum, carbs_sum], labels=[
            "Proteins", "Fats", "Carbs"], autopct="%1.1f%%")  # shows distribution of macros

        axs[0, 0].set_title("Macronutrient Distribution")
        axs[0, 1].bar([0, 1, 2], [proteins_sum,
                      fats_sum, carbs_sum], width=0.4)
        axs[0, 1].bar([0.5, 1.5, 2.5], [Protein_goal,
                      Fat_goal, Carb_goal], width=0.4)
        axs[0, 1].set_title("Macronutrient Progress")

        axs[1, 0].pie([calories_sum, Calorie_Goal_limit - calories_sum],
                      labels=["Calories", "Remaining"], autopct="%1.1f%%")
        axs[1, 0].set_title("Calories Goal Progress")

        axs[1, 1].plot(list(range(len(Food_ate_today))), np.cumsum(
            [food.calories for food in Food_ate_today]), label="Calories Eaten")
        axs[1, 1].plot(list(range(len(Food_ate_today))), [
                       Calorie_Goal_limit] * len(Food_ate_today), label="Calorie Goal")
        axs[1, 1].legend()
        axs[1, 1].set_title("Calories Goal Over Time")

        fig.tight_layout
        plt.show()

    elif choice == "q":
        done = True
    else:
        print("Invalid Choice")
