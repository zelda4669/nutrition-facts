def convert_recipe(list_of_ingredients):
    pass

def lb_to_kg(weight):
    """Convert weight in pounds to weight in kilograms"""
    return weight/2.2046

def ft_to_in(ft, inches):
    """Convert height in feet and inches to inches only"""
    return (ft * 12) + inches

def inches_to_cm(height):
    """Convert height from inches to centimeters"""
    return height * 2.54

def bmi(height, weight):
    """Takes height (in cm) and weight (in kg) and returns bmi"""
    return (weight / (height**2)) * 10000

# good explanation of calculating BMR and TDEE here: https://steelfitusa.com/blogs/health-and-wellness/calculate-tdee
# info on calculating BMR and TDEE during pregnancy/breastfeeding: https://healthyeater.com/pregnancy-breastfeeding-flexible-dieting-iifym


def bmr_no_fat_percentage(sex, age, weight, height):
    """Calculates Basal Metabolic Rate using formulas that do not require body fat percentage.
    Requires weight in kilograms and height in centimeters"""
    base_mifflin = (10 * weight) + (6.25 * height) - (5 * age)
    if sex == 'male':
        mifflin =  base_mifflin + 5
        harris = (13.397 * weight) + (4.799 * height) - (5.677 * age) + 88.362
        return mifflin, harris
    elif sex == 'female':
        mifflin = base_mifflin - 151
        harris = (9.247 * weight) + (3.098 * height) - (4.330 * age) + 447.593
        return mifflin, harris
    else: return 'There has been an input error'

def tdee(bmr, activity):
    """Calculates TDEE for weight maintenance"""
    # definitions:
    # sedentary: no attempt at exercise
    # lightly active: light exercise 1-3 days/week
    # moderately active: moderate exercise 3-5 days/week
    # very active: heavy exercise 6-7 days/week
    # extremely active: professional athlete level
    activity_multipliers = {'sedentary': 1.2,
                            'lightly active': 1.375,
                            'moderately active': 1.55,
                            'very active': 1.725,
                            'extremely active': 1.9}
    return bmr * activity

def macros(tdee, weight):
    """Calculates recommended macronutrient profile based on desired TDEE"""
    # for weight loss subtract approx 20% from base tdee for safe weight loss tdee
    # If you cut 500 cals/day, you will lose about 1 lb/week (approx 3500 calories in a pound)

    # For muscle gain, add no more than 300 cals per day, paired with a strength training regimen
    # For muscle gain, it is recommended that surplus calories come from carbs

    protein = weight * 4
    fat = (weight * 0.4) * 9 # fat multiplier can be between 0.3 and 0.5 depending on whether
    # the person prefers higher fat or higher carb. I'm using the midpoint for the basic version
    # of this app and will refactor when the logic is developed
    carbs = tdee - protein - fat
    return protein, fat, carbs