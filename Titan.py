import streamlit as st 
import random
import math

st.set_page_config(page_title="Titan.com") 
st.title("Titan")
st.header("Helps with Math,Mental health and Fitness")

#Lists!
Healthy_food = ["Hummus","Apple","Banana","Orange","Carrot","Salad"]
Sad_words = ["crying", "hurt", "depressed", "glum", "upset", "dull", "grime", "moody", "sorrowful","heartbroken", "miserable", "gloomy", "unhappy", "hopeless", "weeping","exhausted", "drained", "weary", "heavy", "broken", "worthless", "useless"]
Happy_words = ["happy", "overjoyed", "delighted", "elated", "joyful","blissful","gleeful","jubilant","cheerful", "sunny", "radiant", "beaming", "glowing", "joyous", "lighthearted", "carefree", "bouncy", "peppy", "perky", "playful", "content", "satisfied", "pleased", "gratified", "good-natured", "thrilled", "stoked", "pumped","charmed"]
Excited_words = ["enthusiastic", "eager", "animated", "spirited", "lively", "vibrant", "energetic", "exuberant", "passionate", "zealous", "dynamic", "fired up", "ecstatic", "euphoric", "rhapsodic", "frenzied", "electric", "unstoppable", "triumphant", "victorious"]
Stressed_words = ["stressed", "overwhelmed", "anxious", "panicking", "worried", "pressured", "panicked", "scared", "afraid", "nervous"]
Excited_experiences = ["roller coaster", "theme park", "going to", "beach", "swimming", "pool", "trip", "birthday", "house", "party"]
Fitness_words = ["workout", "exercise", "gym", "run", "fitness", "cardio", "lifting", "training"]
Exercises = [
    "15 Jumping Jacks, 10 Bodyweight Squats, and a 20-second Plank! It gets your blood flowing and boosts your mood instantly.",
    "10 Push-ups, 15 Lunges, and 30 seconds of High Knees! Perfect for building strength right in your room.",
    "5 Burpees, 10 Sit-ups, and a 30-second Wall Sit! This one burns energy fast and builds endurance."
]
Stretches = [
    "The 30-Second Quad Stretch: Stand on one leg, grab your other ankle behind you, and pull it gently toward your glutes. Great for recovery!",
    "The Shoulder Opener: Interlace your fingers behind your back and gently straighten your arms to expand your chest. Takes away all that homework typing tension!",
    "The Cobra Stretch: Lie on your stomach and push your upper body up with your hands while keeping your hips flat. Perfect for relieving back stiffness."
]

if "last_question" not in st.session_state:
    st.session_state.last_question = ""


# 1. Initialize the notebook list
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am Titan!"}
    ]


# 2. Loop for chat history to stay visible on screen 
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 3. Handle new inputs
if user_text := st.chat_input("Talk to Titan"):
    # Display the user's message right now
    with st.chat_message("user"):
        st.write(user_text)
    
    # Save the user's message to the notebook
    st.session_state.messages.append({"role": "user", "content": user_text})



    # Chat logic
    with st.chat_message("assistant"):
        if any(word in user_text.lower() for word in Stressed_words):
            response = "Take a break and settle down it should help."

        elif "good" in user_text.lower():
            response = "That is Magnificent!"

        elif "hungry" in user_text.lower():
            snack = random.choice(Healthy_food)
    
    # Macro facts lookup logic
            if snack == "Hummus":
                macro_info = "packed with healthy plant-based protein and fiber to keep your energy steady!"
            elif snack in ["Apple", "Banana", "Orange"]:
                macro_info = "full of natural carbohydrates and vitamins to give your muscles a fast, clean energy boost!"
            elif snack == "Carrot":
                macro_info = "low in calories but packed with Vitamin A and antioxidants for excellent eye and skin health!"
            else:  # Salad
                macro_info = "loaded with essential micronutrients and hydration to help your body recover!"
        
            response = (
                f"How about eating some **{snack}**! It is amazing for you!\n\n"
                f"**Titan Macro Breakdown:** This snack is {macro_info}\n\n"
                "Eating clean fuels both your brain for math and your body for fitness. Let me know if you want another option!"
    )


        elif "tired" in user_text.lower():
            response = "Go to sleep don't use a phone 30 minutes before bed time."

        elif any(word in user_text.lower() for word in Sad_words) or "sad" in user_text.lower():
            response = "I hear you, and it is completely okay if you don't have the energy for much right now. We don't have to fix anything today I'm just here if you need a quiet space to process things."

        elif any(word in user_text.lower() for word in Happy_words) or "great" in user_text.lower():
            response = "That is Great especially if your starting out like this you may not need me anymore! or you're fixing your mental health which is great!"

        elif "hi!" in user_text.lower() or "hello" in user_text.lower():
            response = "Hello!"

        elif "ok" in user_text.lower() or "okay" in user_text.lower():
            response = "Alright then!"

        elif "wow" in user_text.lower():
            response = "Yeah I know right!"

        elif any(word in user_text.lower() for word in Excited_words) or "excited" in user_text.lower():
            response = "That is Amazing! What is making you excited?"

        elif any(word in user_text.lower() for word in Excited_experiences):
            response = "Wow Have fun there!"

        elif any(word in user_text.lower() for word in Fitness_words) or "workout" in user_text.lower():
            workout_routine = random.choice(Exercises)
            response = (
            "Moving your body releases endorphins, which helps both your physical strength and your mental health!\n\n"
            f"**Here is your Titan Quick Workout:**\n"
            f"👉 {workout_routine}\n\n"
            "Remember to stay hydrated! Do you want another quick routine or a specific stretch? Type **Yes Strech** if you want to stretch!"
    )
            
        # 2. The explicit stretch routine trigger (Completely safe from accidental "yes" triggers!)
        elif "stretch" in user_text.lower() or "yes stretch" in user_text.lower() or "cool down" in user_text.lower():
            routine_stretch = random.choice(Stretches)
            response = (
                "Let's get limber! Stretching improves flexibility and relaxes your nervous system.\n\n"
                f"**Your Quick Stretch:**\n"
                f"👉 {routine_stretch}\n\n"
                "How does that feel? Type **'more stretch'** for another one, or ask me a math question to jump back to studying!"
    )

        # 3. Trigger for a second stretch
        elif "more stretch" in user_text.lower() or "another stretch" in user_text.lower():
            routine_stretch = random.choice(Stretches)
            response = (
                "You got it! Here is another great movement for your muscles:\n\n"
                f"👉 {routine_stretch}\n\n"
                "Keep breathing deeply. Let me know what we are tackling next!"
    )
 
        elif "percent" in user_text.lower() or "discount" in user_text.lower():
            response = (
        "I can help you learn percentages! Let's say you want to find 20% of $50.\n\n"
        "Step 1: Turn the percentage into a decimal by moving the dot two times to the left. So, 20% becomes 0.20 \n\n"
        "Step 2: Multiply that decimal by your total number. 0.20 times 50 equals 10!\n\n"
        "So, 20% of $50 is $10. Try it with your numbers and let me know if you get stuck!"
    )
        elif "area" in user_text.lower() or "geometry" in user_text.lower():
            response = (
                "Let's learn some Geometry! To find the Area of a Rectangle, use the formula: Length times Width.\n\n"
                "For example: If your box is 5 inches long and 4 inches wide, you multiply 5 x 4. The total area is 20 square inches!\n\n"
                "What shape are you working on right now?"
            )

        # Algebra Calculator
        elif "=" in user_text.lower():
            try:
                eq = user_text.lower().replace(" ", "")
                left, right = eq.split("=")
                total = int(right)
                
                if "+" in left:
                    number = int(left.replace("x", "").replace("+", ""))
                    answer = total - number
                    response = f"Titan Solver: I solved it for you! x = {answer}"

                    
                elif "-" in left and left.startswith("x"):
                    number = int(left.replace("x", "").replace("-", ""))
                    answer = total + number
                    response = f"Titan: I solved it for you! x = {answer}"
            except:
                pass

        elif ("solve for" in user_text.lower() or "equation" in user_text.lower() or "algebra" in user_text.lower()) and "=" not in user_text.lower():
            response = (
                "Algebra is just a puzzle! Think of the equals sign (=) like a balanced scale. Whatever you do to one side, you must do to the other.\n\n"
                "Example: If you have 'x + 5 = 12', you want 'x' all by itself. To get rid of the +5, you do the opposite: subtract 5 from both sides!\n\n"
                "12 minus 5 leaves you with 7. So, x = 7! Want to try one together?"
            )

        elif "calculus" in user_text.lower() or "derivative" in user_text.lower():
            response = (
                "Wow, advanced 12th-grade math! In Calculus, a derivative just tells you how fast something is changing at an exact moment.\n\n"
                "Think of it like a speedometer in a car. It doesn't tell you how far you traveled; it tells you exactly how fast you are moving right now!\n\n"
                "What calculus concept are you reading about?"
            )

        elif "pemdas" in user_text.lower() or "exponent" in user_text.lower() or "order of operations" in user_text.lower():
            response = (
                "Let's master 6th-grade PEMDAS!\n\n"
                "First, an **Exponent** tells you how many times to multiply a number by itself. For example, 2³ means 2 x 2 x 2, which equals 8!\n\n"
                "When solving a big math problem, follow the PEMDAS order:\n"
                "1. **P**arentheses ( )\n"
                "2. **E**xponents (like 2³)\n"
                "3. **M**ultiplication & **D**ivision (left to right)\n"
                "4. **A**ddition & **S**ubtraction (left to right)\n\n"
                "Want to type a PEMDAS problem and break it down together?"
            )
        elif "integer" in user_text.lower() or "negative number" in user_text.lower():
            response = (
                "Let's master 7th-grade Integers! Negative numbers can look weird, but here is the trick for adding them:\n\n"
                "Think of positive numbers as **money you have**, and negative numbers as **money you owe**.\n\n"
                "Example: If you have `-5 + 3`, it means you owe 5 dollars, but you pay back 3. You still owe 2 dollars! So, `-5 + 3 = -2`.\n\n"
                "What integer problem are you working on? We can break it down!"
            )

        elif "slope" in user_text.lower() or "y=mx+b" in user_text.lower() or "linear" in user_text.lower():
            response = (
                "Let's learn 8th-grade Graphing and Slope!\n\n"
                "When you see the formula **y = mx + b**, don't panic! It just describes a straight line on a graph.\n"
                "- **m** is the **Slope** (how steep the hill is).\n"
                "- **b** is the **Y-intercept** (where the line crosses the starting line).\n\n"
                "Example: If a taxi charges $3 per mile plus a flat $5 fee, the equation is `y = 3x + 5`!\n\n"
                "Are you working on finding the slope or graphing a line right now?"
            )
    
        elif "place value" in user_text.lower() or "decimals" in user_text.lower():
            response = (
                "Welcome to 5th Grade Unit 1: Place Value & Decimals!\n\n"
                "Here is the secret trick for multiplying or dividing decimals by 10, 100, or 1,000:\n"
                "- **Multiplying?** Slide the decimal dot to the **RIGHT** for every zero. (Example: `4.52 x 100` has two zeros, so it becomes `452`).\n"
                "- **Dividing?** Slide the decimal dot to the **LEFT** for every zero. (Example: `73.5 / 10` has one zero, so it becomes `7.35`).\n\n"
                "Try shifting the dot on your homework problem and let me know what you get!"
            )
        elif "division" in user_text.lower() or "multiply" in user_text.lower() or "multiplication" in user_text.lower():
            response = (
                "Welcome to 5th Grade Unit 2: Multiplication & Long Division!\n\n"
                "When you are dividing by big two-digit numbers, the secret trick is **Estimation**.\n\n"
                "Example: Imagine you need to solve `132 divided by 24`.\n"
                "1. Round the numbers to friendly terms in your head: think of it as `120 divided by 20`.\n"
                "2. Since `12 divided by 2` is 6, you know your answer will be close to 6!\n"
                "3. Multiply `24 x 5` or `24 x 6` on the side to find the exact match.\n\n"
                "Are you working on a long division puzzle or a massive multiplication problem right now?"
            )

        elif "fraction" in user_text.lower() or "denominator" in user_text.lower():
            response = (
                "Welcome to 5th Grade Unit 3: Adding & Subtracting Fractions!\n\n"
                "The golden rule is: You cannot add or subtract fractions until the **bottom numbers (denominators) match**!\n\n"
                "Example: Let's solve `1/2 + 1/3`.\n"
                "1. Find a number that both 2 and 3 can multiply into. Let's use 6!\n"
                "2. Change `1/2` into sixths by multiplying top and bottom by 3. It becomes `3/6`.\n"
                "3. Change `1/3` into sixths by multiplying top and bottom by 2. It becomes `2/6`.\n"
                "4. Now add the top numbers together: `3/6 + 2/6 = 5/6`!\n\n"
                "Type your fractions here and we can find your matching bottom number together!"
            )
            
        elif "volume" in user_text.lower() or "measurement" in user_text.lower() or "3d" in user_text.lower():
            response = (
                "Welcome to 5th Grade Unit 4: Volume & Measurement!\n\n"
                "To find the **Volume** of a 3D box (how much space is inside), you just multiply three numbers together using this formula:\n"
                "👉 **Length × Width × Height**\n\n"
                "Example: Imagine a tissue box that is 10 inches long, 5 inches wide, and 4 inches tall.\n"
                "1. Multiply Length × Width: `10 × 5 = 50`.\n"
                "2. Multiply that by the Height: `50 × 4 = 200`.\n"
                "So, the total volume is 200 cubic inches!\n\n"
                "Tell me the three measurements of your box, and let's multiply them together!"
            )
        elif "unit rate" in user_text.lower() or "ratio" in user_text.lower() or "proportion" in user_text.lower():
            response = (
                "Welcome to 7th Grade Ratio's and Proportions! \n\n"
                "A **Unit Rate** compares a quantity to exactly ONE unit of another quantity (like miles per hour).\n"
                        "Example: If you drive 120 miles in 2 hours, your unit rate is 120 ÷ 2 = **60 miles per hour**.\n\n"
                        "What ratio or rate problem are you working on right now?"
    )

        elif "pythagorean" in user_text.lower() or "triangle" in user_text.lower() or "hypotenuse" in user_text.lower():
                response = (
        "Welcome to 8th Grade Geometry: The Pythagorean Theorem!\n\n"
        "This formula only works on **right triangles** (triangles with a 90-degree corner).\n"
        "The formula is: **a² + b² = c²**\n"
        "  - **a** and **b** are the short legs, and **c** is the longest side (the hypotenuse).\n\n"
                "Example: If legs are 3 and 4, then 3² + 4² = 9 + 16 = 25. Since √25 = 5, the hypotenuse is 5!"
    )

        elif "quadratic" in user_text.lower() or "factoring" in user_text.lower() or "foil" in user_text.lower():
            response = (
        "Welcome to 9th Grade Algebra 1: Quadratic Equations!\n\n"
                "Quadratic equations have a variable raised to the second power, like **ax² + bx + c = 0**.\n"
                        "To solve them, we look for factors, or use the **Quadratic Formula**: x = (-b ± √(b² - 4ac)) / 2a\n\n"
        "Do you need help factoring an expression, or finding the roots using the formula?"
    )

        elif "inequality" in user_text.lower() or "greater than" in user_text.lower() or "less than" in user_text.lower():
            response = (
            "Welcome to 9th Grade Algebra 1: Inequalities!\n\n"
            "Solving inequalities is just like solving regular equations, with one golden rule you must remember:\n"
            "👉 **If you multiply or divide both sides by a NEGATIVE number, you must FLIP the sign!**\n\n"
            "Example: If you have `-2x < 6`, divide both sides by `-2` and flip the `<` to a `>`. Your answer is `x > -3`!\n\n"
            "Do you have an inequality problem you want to try together?"
    )

        elif "logarithm" in user_text.lower() or " log " in user_text.lower() or "compound interest" in user_text.lower():
            response = (
        "Welcome to 11th Grade Algebra 2: Logarithms & Finance!\n\n"
        "A **Logarithm** answers the question: 'To what power do I raise this base to get this number?'\n"
        "**Compound Interest** calculates money earned over time using the formula: **A = P(1 + r/n)^(nt)**.\n\n"
        "Would you like to solve a logarithm problem or calculate compound interest?"
    )
            
        elif "root" in user_text.lower():
            response = (" Welcome to 9th Grade Algebra 1: Roots! \n\n"
            "What are Roots? Roots are simply the exact places where that U-shaped curve crosses the flat x-axis line (where y = 0). An equation can cross twice, touch exactly once, or miss the axis completely\n")

        elif "trig" in user_text.lower():
            response = ("Welcome to 10th Grade Geometry: Trigonometry! \n\n"
            "What is Trigonometry? Trigonometry is simply the study of relationships between a triangle's angles and its sides. Remember SOH-CAH-TOA: Sine is opposite over hypotenuse, Cosine is adjacent over hypotenuse, and Tangent is opposite over adjacent!\n")

        elif "circle" in user_text.lower() or "radius" in user_text.lower() or "circumference" in user_text.lower():
            response = (
                "Welcome to 10th Grade Geometry: Circles!\n\n"
                "Here are the two essential formulas you need to master:\n"
                "- **Area** (space inside): `π × r²` (Pi times the radius squared)\n"
                "- **Circumference** (distance around the outside): `2 × π × r` (2 times Pi times the radius)\n\n"
                "Example: If your circle has a radius of 5, the area is `3.14 × 25 = 78.5`, and the circumference is `2 × 3.14 × 5 = 31.4`!\n\n"
                "What circle dimensions are you trying to calculate right now?"
    )
    
        elif "midpoint" in user_text.lower() or "middle point" in user_text.lower():
            response = (
            "Welcome to 11th Grade Algebra 2: The Midpoint Formula!\n\n"
            "When you need to find the exact middle spot between two points on a graph, just average their coordinates!\n"
            "👉 **Formula: ( (x₁ + x₂) / 2 , (y₁ + y₂) / 2 )**\n\n"
            "Example: If Point A is at `(1, 2)` and Point B is at `(5, 6)`:\n"
            "1. Add the x values: `1 + 5 = 6`. Divide by 2 to get **3**.\n"
            "2. Add the y values: `2 + 6 = 8`. Divide by 2 to get **4**.\n"
            "So, your exact middle point is `(3, 4)`!\n\n"
            "Give me your two coordinate points, and let's find the middle together!"
    )

        elif "quotient rule" in user_text.lower():
            response = (
            "Welcome to 12th Grade Calculus: The Quotient Rule!\n\n"
            "When you need to find the derivative (slope) of two equations stuck in a fraction like `f(x) / g(x)`, teachers use a famous rhyming trick:\n\n"
            "👉 **'Low d-High minus High d-Low, over the square of what's below!'**\n\n"
            "Breaking it down:\n"
            "- **Low**: The bottom equation\n"
            "- **d-High**: The derivative of the top equation\n"
            "- **High**: The top equation\n"
            "- **d-Low**: The derivative of the bottom equation\n"
            "- **What's below squared**: The bottom equation raised to the power of 2\n\n"
            "Are you working through a tough fraction derivative right now?"
    )

        #Normal calculator
        elif any(op in user_text.lower() for op in ["+", "-", "*", "/"]) and "=" not in user_text.lower():
            try:
                # First, swap human text symbols for programming symbols
                clean_text = user_text.lower()
                # Second, strip out everything except valid numbers and operators
                math_ready = "".join(c for c in clean_text if c in "0123456789+-*/.()")
                # Finally, pass the fixed string to eval()
                response = f"I calculated that for you! The answer is {eval(math_ready)}"
            except ZeroDivisionError:
                response = "Nice try, but you can't divide by zero! You'll break the universe."
            except:
                response = "I could not calculate that! Please check your math formatting."

        
        else:
            response = "I don't know what your saying!"

        #SAVE ASSISTANT RESPONSE
        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

with st.sidebar:
    st.header("Titan's Math Lab 🧪")

    # Grade Level Selector
    grade = st.selectbox(
        "Choose your Grade Level:",
        ["5th Grade", "6th Grade", "7th Grade", "8th Grade", "9th Grade (Algebra 1)", "10th Grade (Geometry)", "11th Grade (Algebra 2)", "12th Grade (Calculus)"]
    )
    
    st.divider()
    
    if grade == "5th Grade":
        st.subheader("Area Calculator 📐")
        side_length = st.number_input("Enter Length", value=1.0, key="side_geo_length")
        side_width = st.number_input("Enter Width", value=1.0, key="side_geo_width")
        st.success(f"Total Area: {side_length * side_width} sq units")

        st.divider()
        st.subheader("Volume Calculator 📦")
        
        # Input boxes for the 3 dimensions
        v_length = st.number_input("Enter Length", value=10.0, key="vol_length")
        v_width = st.number_input("Enter Width", value=5.0, key="vol_width")
        v_height = st.number_input("Enter Height", value=4.0, key="vol_height")
        
        # Calculate the 3D space
        volume_result = v_length * v_width * v_height
        
        st.info(f"Formula: {v_length} × {v_width} × {v_height}")
        st.success(f"Total Volume: **{volume_result:.1f}** cubic units")

    elif grade == "6th Grade":
        st.subheader("Exponet Calculator 🧮")
        base = st.number_input("Enter Base Number:", value=2, key="unique_key_1")
        exponent = st.number_input("Enter Exponent (Power):", value=3, key="unique_key_2")
        st.success(base ** exponent)

        st.divider()

        st.subheader("Percentage Calculator 📊")
        pct_amount = st.number_input("Find what percent? (e.g., 20)", value=20.0, key="pct_val")
        pct_total = st.number_input("Of what total number? (e.g., 50)", value=50.0, key="pct_total_val")
        
        # Calculate percentage
        pct_result = (pct_amount / 100) * pct_total
        st.success(f"{pct_amount}% of {pct_total} is: **{pct_result:.2f}**")

    elif grade == "7th Grade":
        st.subheader("Unit Rate & Ratio Finder 📊")
    
        quantity_1 = st.number_input("Enter First Quantity (e.g., Miles, Dollars)", value=60.0, key="ratio_q1")
        quantity_2 = st.number_input("Enter Second Quantity (e.g., Hours, Ounces)", value=2.0, key="ratio_q2")

        try:
            # 2. Math calculation for unit rate
            unit_rate = quantity_1 / quantity_2
        
                # 3. Clean up display text using simple math reduction logic
            import math
            gcd_val = math.gcd(int(quantity_1), int(quantity_2))
            simplified_1 = int(quantity_1) // gcd_val
            simplified_2 = int(quantity_2) // gcd_val
        
            st.info(f"Simplified Ratio: **{simplified_1} : {simplified_2}**")
            st.success(f"The Unit Rate is: **{unit_rate:.2f}** per 1 unit")
        except:
            st.error("Make sure your inputs are valid and the second quantity is not zero!")
            
            st.divider()
        st.subheader("Integer Counter & Calculator 📈")
        
        # User inputs for negative/positive integers
        num1 = st.number_input("Enter First Integer:", value=0, step=1, key="int_num1")
        num2 = st.number_input("Enter Second Integer:", value=0, step=1, key="int_num2")
        
        # Simple selection box for operations
        int_op = st.selectbox("Choose Operation:", ["Add (+)", "Subtract (-)", "Multiply (*)", "Divide (/)"], key="int_op")
        
        # Perform calculation based on choice
        if int_op == "Add (+)":
            st.success(f"Result: {num1} + ({num2}) = **{num1 + num2}**")
        elif int_op == "Subtract (-)":
            st.success(f"Result: {num1} - ({num2}) = **{num1 - num2}**")
        elif int_op == "Multiply (*)":
            st.success(f"Result: {num1} * ({num2}) = **{num1 * num2}**")
        elif int_op == "Divide (/)":
            if num2 != 0:
                st.success(f"Result: {num1} / ({num2}) = **{num1 / num2:.2f}**")
            else:
                st.error("Cannot divide an integer by zero!")

    elif grade == "8th Grade":
        st.subheader("Slope Finder (y = mx + b) 📉")
        x1 = st.number_input("Enter x1:", value=0.0, step=1.0, key="slope_x1")
        y1 = st.number_input("Enter y1:", value=0.0, step=1.0, key="slope_y1")
        x2 = st.number_input("Enter x2:", value=1.0, step=1.0, key="slope_x2")
        y2 = st.number_input("Enter y2:", value=0.0, step=1.0, key="slope_y2")
        try:
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - (slope * x1)
            st.success(f"Slope (m) = **{slope:.2f}** | y-intercept (b) = **{intercept:.2f}**")
            st.code(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
        except ZeroDivisionError:
            st.error("Vertical line! x1 and x2 cannot be the same value because you cannot divide by zero.")
            st.divider()
        st.subheader("Pythagorean Theorem Calculator 📐")
        pythag_choice = st.selectbox("What are you solving for?", ["Hypotenuse (c)", "Leg (a or b)"], key="pythag_choice")
        if pythag_choice == "Hypotenuse (c)":
            side_a = st.number_input("Enter length of Side a:", value=3.0, min_value=0.1, key="pythag_a")
            side_b = st.number_input("Enter length of Side b:", value=4.0, min_value=0.1, key="pythag_b")
            hypotenuse = (side_a**2 + side_b**2) ** 0.5
            st.success(f"The Hypotenuse (c) length is: **{hypotenuse:.2f}**")


        elif pythag_choice == "Leg (a or b)":
            side_c = st.number_input("Enter length of Hypotenuse c:", value=5.0, min_value=0.1, key="pythag_c")
            known_side = st.number_input("Enter length of Known Side (a or b):", value=3.0, min_value=0.1, key="pythag_known")
            if side_c > known_side:
                missing_side = (side_c**2 - known_side**2) ** 0.5
                st.success(f"The missing leg length is: **{missing_side:.2f}**")
            else:
                st.error("The Hypotenuse (c) must be longer than the known side!")

    elif grade == "9th Grade (Algebra 1)":
        st.subheader("Quadratic Formula Solver 🧬")
        
        # Unique keys prevent 9th grade inputs from conflicting with other sections
        a = st.number_input("Enter coefficient a:", value=1.0, key="quad_a_9th")
        b = st.number_input("Enter coefficient b:", value=0.0, key="quad_b_9th")
        c = st.number_input("Enter coefficient c:", value=0.0, key="quad_c_9th")
        
        if a == 0:
            st.error("The coefficient 'a' cannot be zero in a quadratic equation!")
        else:
            discriminant = b**2 - (4 * a * c)
            if discriminant > 0:
                root1 = (-b + discriminant**0.5) / (2 * a)
                root2 = (-b - discriminant**0.5) / (2 * a)
                st.success(f"Two real roots found: x = **{root1:.2f}** and x = **{root2:.2f}**")
            elif discriminant == 0:
                root = -b / (2 * a)
                st.success(f"One real root found: x = **{root:.2f}**")
            else:
                st.warning("The roots are complex/imaginary (no real number answers).")
                
        st.divider()
        st.subheader("Linear Equation Solver (mx + b = y) 📈")
        
        m = st.number_input("Enter slope m:", value=1.0, key="linear_m_9th")
        b_val = st.number_input("Enter intercept b:", value=0.0, key="linear_b_9th")
        y = st.number_input("Enter value y:", value=0.0, key="linear_y_9th")
        
        if m == 0:
            if y == b_val:
                st.success("Infinite solutions! Since m = 0 and y = b, x can be any number.")
            else:
                st.error("No solution! A slope of 0 cannot reach that y value.")
        else:
            x_answer = (y - b_val) / m
            st.success(f"Solved for x: x = **{x_answer:.2f}**")
 
    elif grade == "10th Grade (Geometry)":
        st.subheader("Trigonometry Solver 📐")
        angle = st.number_input("Enter angle in degrees:", value=30.0, key="trig_angle_10th")
        rad = math.radians(angle)
        
        st.success(f"sin({angle}°) = **{math.sin(rad):.4f}**")
        st.success(f"cos({angle}°) = **{math.cos(rad):.4f}**")
        
        # Guard against undefined tangent values like 90 degrees
        if angle % 90 == 0 and (angle // 90) % 2 != 0:
            st.error(f"tan({angle}°) is Undefined!")
        else:
            st.success(f"tan({angle}°) = **{math.tan(rad):.4f}**")
            
        st.divider()
        st.subheader("Distance Formula Calculator 📍")
        x1 = st.number_input("Enter x1:", value=0.0, key="dist_x1_10th")
        y1 = st.number_input("Enter y1:", value=0.0, key="dist_y1_10th")
        x2 = st.number_input("Enter x2:", value=3.0, key="dist_x2_10th")
        y2 = st.number_input("Enter y2:", value=4.0, key="dist_y2_10th")
        
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        st.success(f"Distance between points = **{distance:.2f}**")

        st.divider()
        st.subheader("Circle Analyzer 🔴")
        radius = st.number_input("Enter Radius of the Circle:", value=5.0, min_value=0.0, key="circle_r_10th")
        circle_area = math.pi * (radius ** 2)
        circumference = 2 * math.pi * radius
        st.success(f"Total Area: **{circle_area:.2f}** sq units")
        st.success(f"Circumference (Perimeter): **{circumference:.2f}** units")


    elif grade == "11th Grade (Algebra 2)":
        st.subheader("Compound Interest Calculator 💰")
        p = st.number_input("Principal investment ($):", value=1000.0, key="finance_p_11th")
        r = st.number_input("Annual interest rate (as %, e.g., 5 for 5%):", value=5.0, key="finance_r_11th")
        t = st.number_input("Time in years:", value=5.0, key="finance_t_11th")
        n = st.number_input("Times compounded per year (e.g., 12=monthly):", value=12.0, min_value=1.0, key="finance_n_11th")
        
        rate_decimal = r / 100
        amount = p * ((1 + (rate_decimal / n)) ** (n * t))
        interest = amount - p
        
        st.success(f"Total Balance (A): **${amount:.2f}**")
        st.info(f"Total Interest Earned: **${interest:.2f}**")
        
        st.divider()
        st.subheader("Logarithm Solver 🔢")
        base_log = st.number_input("Enter Log Base (b):", value=10.0, min_value=0.1, key="log_base_11th")
        x_log = st.number_input("Enter Argument (x):", value=100.0, min_value=0.1, key="log_x_11th")
        
        if base_log == 1:
            st.error("Log base cannot be 1!")
        else:
            log_result = math.log(x_log) / math.log(base_log)
            st.success(f"log_{base_log}({x_log}) = **{log_result:.4f}**")
    
    elif grade == "12th Grade (Calculus)":
        st.subheader("Derivative Solver (Power Rule) 📈")
        st.write("Finds the rate of change for an equation like: f(x) = x²")
        
        # User inputs the point where they want to check the slope
        x_calc = st.number_input("Enter the x value to check the slope at:", value=2.0, key="calc_x_12th")
        # The derivative of x² is 2x, so we multiply the user's x value by 2
        slope_result = 2 * x_calc
        
        st.success(f"The exact slope (derivative) of f(x) = x² at x = {x_calc} is: **{slope_result:.2f}**")

        st.divider()
        st.subheader("Limits Calculator 🛑")
        st.write("Finds the value that a function approaches. Let's look at: f(x) = (x² - 4) / (x - 2)")
        
        # User inputs the target number that x is approaching
        target_x = st.number_input("As x approaches what number?", value=2.0, key="limit_x_12th")
        # Calculate the limit using the simplified form (x + 2)
        limit_result = target_x + 2
        
        st.success(f"As x approaches {target_x}, the limit of the function is: **{limit_result:.2f}**")




# Custom Theme CSS Style
st.markdown(
    """
    <style>
    :root { --primary-color: #FFFFFF; }
    div[data-testid="stChatMessageAvatarAssistant"] { background-color: #FFFFFF !important; color: #000000 !important; }
    div[data-baseweb="textarea"] { border-color: #FFFFFF !important; }
    </style>
    """, 
    unsafe_allow_html=True
)

#streamlit run c:/Users/Shayaan/Titan.py
