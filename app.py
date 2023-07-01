import random
import numpy as np

exercise_list = ["отжимания", "планка", "приседания", "скручивания"]
count_base_list = np.arange(10, 60, 10)
multiplier_base_list = np.arange(3, 5.5, 0.5)

# random item from list
exercise_to_do = random.choice(exercise_list)

# random item from list
count_to_do = random.choice(count_base_list) * random.choice(multiplier_base_list) 

general_prompt = f'Сможешь ли ты сделать {exercise_to_do} {count_to_do} раз?'
planck_prompt = f'Сможешь ли ты простоять в планке за один подход в течении {count_to_do} секунд?'

prompt = planck_prompt if exercise_to_do == "планка" else general_prompt
print(prompt)
