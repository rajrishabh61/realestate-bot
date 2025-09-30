
# import random
# from fuzzywuzzy import process
# import csv

# class realestateBot():
#     responses = {
#         'hi, hey, hello': 'greetings',
#         'buy': 'purchase',
#         'rent': 'rent',
#         'sell': 'sell'
#     }

#     response = {
#         'greetings': [
#             "Hi 👋 I’m your Real Estate Assistant. Are you looking to buy, rent, or sell property?",
#             "Hello! 😊 Welcome to our real estate service. Would you like to buy, rent, or sell?",
#             "Hey there 👋 Ready to explore properties? Are you looking to buy, rent, or sell?",
#             "Hi! 👋 I can help you with real estate. Do you want to buy, rent, or sell today?"
#         ],
#         'purchase': [
#             "Great! You want to buy a property 🏡. Can you tell me your preferred location and budget?",
#             "Awesome choice 🙌 Looking to purchase? Please share the location and your budget range.",
#             "Buying a property? Perfect! 🏠 Where would you like to buy, and what’s your budget?",
#             "Nice 👍 You’re interested in buying. Let me know the area and price range you have in mind."
#         ],
#         'rent': [
#             "Looking to rent a property? 🏠 Can you share your preferred location and budget?",
#         ],
#         'sell': [
#             "You want to sell a property? 🏡 Please provide details about your property.",
#         ],
#         'location': [
#             "Great! Please tell me your preferred location 🗺️ and budget 💰."
#         ]
#     }

#     def __init__(self):
#         try:
#             with open('C:/xampp/htdocs/pythonnnnnnnnnnn/realestate/RealEstate.csv', 'r', newline='', encoding='utf-8') as file:
#                 self.dict_reader = list(csv.DictReader(file))
#         except FileNotFoundError:
#             self.dict_reader = []
#             print("⚠️ RealEstate.csv not found. Make sure the file exists.")

#     def get_intent(self, user):
#         match, score = process.extractOne(user, self.responses.keys())
#         if score > 50:
#             return self.responses[match]
#         return None

#     def show_properties(self, location_filter=None):
#         """Return all properties as a formatted string"""
#         if not self.dict_reader:
#             return "⚠️ No property data available."

#         output = "Here are some available properties 🏡:\n"
#         for row in self.dict_reader:  # return all, not just first 5
#             output += f"- {row.get('bedRoom','N/A')} in {row.get('Location','N/A')} || Price: {row.get('price','N/A')}\n"
#         return output

#     def chat(self, user_msg=None):
#         """Process a single user message and return bot reply"""
#         if user_msg is None:
#             return "⚠️ No input provided."

#         user_input = user_msg.lower().strip()
#         intent = self.get_intent(user_input)
        
#         if intent and intent in self.response:
#             bot_msg = random.choice(self.response[intent])
            
#             if intent in ["purchase", "rent", "sell"]:
#                 properties = self.show_properties()
#                 if properties:
#                     bot_msg += "\n\n" + properties
#         else:
#             bot_msg = "Sorry, I didn’t understand 🤔. Could you please rephrase?"
        
#         return bot_msg


# # Run console mode only if executed directly
# if __name__ == "__main__":
#     bot = realestateBot()
#     while True:
#         user_input = input("You: ").strip()
#         if user_input.lower() in ["exit", "quit", "bye"]:
#             print("Bot: Goodbye! 👋 Have a great day!")
#             break
#         print("Bot:", bot.chat(user_input))











































































































# import random
# from fuzzywuzzy import process
# import csv

# class realestateBot:
#     responses = {
#         'hi, hey, hello': 'greetings',
#         'buy': 'purchase',
#         'rent': 'rent',
#         'sell': 'sell',
#     }

#     response = {
#         'greetings': [
#             "Hi 👋 I’m your Real Estate Assistant. Are you looking to buy, rent, or sell property?",
#             "Hello! 😊 Welcome to our real estate service. Would you like to buy, rent, or sell?",
#             "Hey there 👋 Ready to explore properties? Are you looking to buy, rent, or sell?",
#             "Hi! 👋 I can help you with real estate. Do you want to buy, rent, or sell today?"
#         ],
#         'purchase': [
#             "Great! You want to buy a property 🏡. Can you tell me your preferred location and budget?",
#             "Awesome choice 🙌 Looking to purchase? Please share the location and your budget range.",
#             "Buying a property? Perfect! 🏠 Where would you like to buy, and what’s your budget?",
#             "Nice 👍 You’re interested in buying. Let me know the area and price range you have in mind."
#         ],
#         'rent': [
#             "Looking to rent a property? Please share the location and your budget.",
#         ],
#         'sell': [
#             "You want to sell your property? Please provide the location and details.",
#         ]
#     }

#     def __init__(self):
#         try:
#             with open('C:/xampp/htdocs/pythonnnnnnnnnnn/realestate/RealEstate.csv', 'r', newline='', encoding='utf-8') as file:
#                 self.dict_reader = list(csv.DictReader(file))
#         except FileNotFoundError:
#             self.dict_reader = []
#             print("⚠️ RealEstate.csv not found. Make sure the file exists.")

#     def get_intent(self, user):
#         match, score = process.extractOne(user, self.responses.keys())
#         if score > 70:
#             return self.responses[match]
#         return None

#     def show_properties(self, limit=5):
#         """Return properties as string"""
#         if not self.dict_reader:
#             return "⚠️ No property data available."
        
#         props = "\nHere are some available properties 🏡:\n"
#         for row in self.dict_reader[:limit]:
#             props += f"- {row.get('bedRoom', 'N/A')} bedroom in {row.get('location', 'Unknown')} for {row.get('price', 'N/A')}\n"
#         return props

#     def chat(self, user_input):
#         """Return bot response as string"""
#         user_input = user_input.lower().strip()
#         if user_input in ["exit", "quit", "bye"]:
#             return "Bot: Goodbye! 👋 Have a great day!"

#         intent = self.get_intent(user_input)
#         if intent and intent in self.response:
#             bot_msg = random.choice(self.response[intent])
            
#             # Show properties if needed
#             if intent in ["purchase", "rent", "sell"]:
#                 bot_msg += "\n" + self.show_properties()
            
#             return bot_msg
#         else:
#             return "Bot: Sorry, I didn’t understand 🤔. Could you please rephrase?"

# # Example usage:
# if __name__ == "__main__":
#     bot = realestateBot()
#     while True:
#         user_msg = input("You: ")
#         reply = bot.chat(user_msg)
#         print(reply)
#         if user_msg.lower() in ["exit", "quit", "bye"]:
#             break









import random
from fuzzywuzzy import process
import csv

class realestateBot:
    responses = {
        'hi, hey, hello': 'greetings',
        'buy': 'purchase',
        'rent': 'rent',
        'sell': 'sell',
    }

    response = {
        'greetings': [
            "Hi 👋 I’m your Real Estate Assistant. Are you looking to buy, rent, or sell property?",
            "Hello! 😊 Welcome to our real estate service. Would you like to buy, rent, or sell?",
            "Hey there 👋 Ready to explore properties? Are you looking to buy, rent, or sell?",
            "Hi! 👋 I can help you with real estate. Do you want to buy, rent, or sell today?"
        ],
        'purchase': [
            "Great! You want to buy a property 🏡. Can you tell me your preferred location?",
            "Awesome choice 🙌 Looking to purchase? Please share the location.",
            "Buying a property? Perfect! 🏠 Where would you like to buy?",
            "Nice 👍 You’re interested in buying. Let me know the area."
        ],
        'rent': [
            "Looking to rent a property? Please share the location and your budget.",
        ],
        'sell': [
            "You want to sell your property? Please provide the location and details. By filling the form",
        ]
    }


    def __init__(self):
        try:
            with open('RealEstate.csv', 'r', newline='', encoding='utf-8') as file:
                self.dict_reader = list(csv.DictReader(file))
        except FileNotFoundError:
            self.dict_reader = []
            print("⚠️ RealEstate.csv not found. Make sure the file exists.")
        
        self.awaiting_location = False  # Flag to track if bot is waiting for city

    def get_intent(self, user):
        match, score = process.extractOne(user, self.responses.keys())
        if score > 50:
            return self.responses[match]
        return None
 
    def show_properties(self, location_filter=None):
        if not self.dict_reader:
            return "⚠️ No property data available."
        
        properties = []
        for row in self.dict_reader[:5]:
            # Use 'address' as location
            location = row.get("address", "Unknown")
            price = row.get("rate", "Unknown")
            if location_filter and location_filter.lower()  not in location.lower():
                continue  # skip if filter doesn't match

            bed = row.get("bedRoom", "N/A")
            price = row.get("price", "N/A")
            images = row.get("images", "pexels-pixabay-164522.jpg")  # fallback image

            properties.append(
                f'<img class="t6deh6hj" src="static/images/{images}" alt="Property Image">'
                f'<p>{bed} BHK</p>'
                f'<p>{location}</p>'
                f'<p>₹{price} Lakh</p>'
            )

        
        if not properties:
            return f"❌ No properties found for '{location_filter}'."
        return "\n".join(properties)



    def chat(self, user_input):
        user_input_lower = user_input.lower().strip()

        if self.awaiting_location:
            self.awaiting_location = False

            # List of addresses
            addresses = [row.get("address", "") for row in self.dict_reader]
            price = [row.get("rate", "") for row in self.dict_reader]
            min_price  = [row.get("address", "") for row in self.dict_reader]
            # Find best match using fuzzy matching
            best_match, score = process.extractOne(user_input_lower, addresses)
            if score > 50:  # threshold
                return self.show_properties(location_filter=best_match)
            else:
                return f"❌ Sorry, I couldn’t find properties in '{user_input.title()}'"

        intent = self.get_intent(user_input_lower)
        if intent and intent in self.response:
            bot_msg = "<p>" + random.choice(self.response[intent]) + "</p>"
            if intent == "sell":
                bot_msg += f'\n<button class="hdghdf">Form</button>'

                

            if intent == "purchase":
                self.awaiting_location = True
                return bot_msg
            elif intent == "rent":
                return self.show_properties()
            # elif intent == "sell":
            #     bot_msg = f"Please Fill this form"

            return bot_msg

        return "Bot: Sorry, I didn’t understand 🤔. Could you please rephrase?"

# Run console mode only if executed directly
if __name__ == "__main__":
    bot = realestateBot()
    while True:
        user_msg = input("You: ")
        reply = bot.chat(user_msg)
        print(reply)
        if user_msg.lower() in ["exit", "quit", "bye"]:
            break








#     # def csv(self):
#     #     # Extract all addresses into a list
#     #     addresses = [row['address'].lower() for row in self.dict_reader]
#     #     # Find best match
#     #     match, score = process.extractOne(self.user, addresses)
#     #     if score > 50:
#     #     # Find the row corresponding to the matched address
#     #         for row in self.dict_reader:
#     #             if row['address'].lower() == match:
#     #                 print(row['bedRoom'] , ' || ' , row['address'])
#     #                 break
#     #     else:
#     #         print("No good match found.")
