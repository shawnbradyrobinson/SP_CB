# ALL NEW ITEMS FOR THE GAME SHOULD GET ADDED HERE TO BE ADDED IN TO 
# EACH PERSON AND COMMUNITY INSTANCE!!!! 


class Inventory:
    def __init__(self):
        items = {
            "healthcare": {
                "vapor_rubs": 0,
                "sticky_aids": 0, 
                "cough_syrup": 0,
            },

            "materials": {
                "oak_planks": 0, 
                "bricks": 0, 
                "aluminum": 0, 
                "iron": 0, 
                "copper":  0, 
                "steel": 0, 
                "pvc_pipes": 0, 
            },

            "food": {
                #MEAL TYPES -- USED DIFFERENTLY THAN FOODS --# 
                "malnourshing_meals": 0,
                "protein_heavy_meals": 0,
                "fatty_meals": 0,
                "empty_carb_meals": 0,
                "sweet_satisfying_meals": 0,
                "savory_satisfying_meals": 0,
                "sweet_savory_meals": 0,
                "ultra_nutritious_meals": 0,
                #
                "eggs": 0,
                "beef": 0,
                "pork": 0,
                "veal": 0, 
                "poultry": 0, 
                "kale": 0, 
                "tomatoes": 0, 
                "apples": 0, 
                "oranges": 0, 
                "milk_liters": 0, 
                "spinach": 0, 
                "tea_leaves": 0, 
                "coffee_beans": 0, 
                "water_liters": 0, 

            },

            "scholarship": {
                "geometry_textbook": 0,
                "history_textbook": 0,

            }
        }
    
        pass


    #DOWN HERE IS WHERE WE CAN SET UP QUICK-ADD PRESETS FOR DIFFERENT SITUATIONS 

    def emptyPreset(self):
        pass

    #And so on and so forth...  
    def allFoodPreset(self):
        pass

    def trulyRandomPreset(self):
        pass 
