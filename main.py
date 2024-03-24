import random

history = ""
character = {
    "gender": "",
    "name": "",
    "family": "",
    "merit": "",
    "childhood_activity": "",
    "storylines": ["", "", ""]
}

family = {
    "1": ["The baron's associates", """Your family served faithfully to the local feudal lord. Your father was a 
    personal bodyguard for a powerful baron, protecting his estates and family from enemies and intrigues. He was not 
    only a guard, but also as an adviser to his master, taking part in political debates and battles on the 
    battlefields."""],
    "2": ["City merchants", """Your family was connected with the world of trade and commerce. Your parents were 
    merchants, embarking on dangerous journeys around the world, filling city markets with exotic goods and making 
    significant contributions to the kingdom's economy through trade deals and taxes."""],
    "3": ["Farmers", """Your family owned land and embodied ancient farming traditions. Your parents worked for
    fields, growing grains and fruits that will feed the kingdom. They were the breadwinners of many, and their crops 
    and herds were vital to the well-being of the kingdom."""]
}

merit = {
    "1": ["Leadership qualities", """Since childhood, you have been a leader among your peers. You have always been 
attracted to the role leader, and your comrades always followed your example. In a world where power and strength 
are important, your leadership and the ability to make decisions were indispensable qualities."""],
    "2": ["Attention to detail", """Your gaze always penetrated deeper than most. You paid attention to those
details that many have neglected, and often this will bring you unexpected discoveries. In a world where secrets and
mysteries are hidden down to the smallest detail, your attention to detail was a valuable gift."""],
    "3": ["Mental Abilities", """Your mind was your most powerful weapon. You were gifted with clarity and
analytical thinking that made you a master at solving complex puzzles and mysteries. In a world where magic and 
knowledge play key role, your mental abilities were invaluable."""],
    "4": ["Strength and will of spirit", """Your strength and spirit are unshakable. You have gone through many trials 
and obstacles, but never didn't give up. In a world full of dangers and challenges, your strength and determination 
were your greatest weapons."""],
    "5": ["Love and treatment of animals", """Since childhood, you have had a special gift - the gift of communication 
with animals. Your words and gestures were understandable even to the wildest creatures, and they often became your 
faithful companions and helpers in traveling around the world, where every corner of nature is permeated with 
magic."""],
    "6": ["Luck", """You have always been accompanied by amazing luck, and many of your actions ended in the unexpected
success. In a world where fate and magic are intertwined in unprecedented oddities, your luck was a priceless gift."""]
}

childhood_activity = {
    "1": {
        "1": ["Training at the Knight's Academy", """You attended classes at the Knight's Academy, where you learned 
swordsmanship, horse riding and military strategy."""],
        "2": ["Games of knights", """With your friends, you organized small tournaments and battles with wooden swords, 
turning into brave knights."""],
        "3": ["Caring for horses", """Your communication with knightly horses began in childhood, and you learned to 
care for them and participate in their care."""]
    },
    "2": {
        "1": ["Help in the market", """As a child, you helped your parents in the marketplace, learning to trade and 
business management."""],
        "2": ["Caravan Travel", """Your parents sometimes took you on caravan trips, where you got acquainted with 
different cultures and goods."""],
        "3": ["Product Research", """You were interested in goods and services that were sold on the market, and studied
supply and demand."""]
    },
    "3": {
        "1": ["Work in the fields", """Your obligatory occupation was helping your parents in the fields, caring for 
animals and harvesting."""],
        "2": ["Study of plants", """You were interested in plants and studied their properties, helping your parents 
looked after the with a cat."""]
    }

}
# m-mission a-action e-end story lane
storylines = {
    "1": {
        "1": [
             {"m": "Select a weapon type for a training battle", "1": "Sword", "2": "Spear", "3": "Bow and arrows",
              "4": "Cudgel"},
             {"m": "Choose a location for a mock battle",
              "1": "Borderlands", "2": "Borders of the Wild Forest", "3": "Fortress on the Border",
              "4": "Dungeon"},
             {"m": "Choose the optimal strategy for the upcoming battle",
              "1": "Attack on the flanks", "2": "Strike to the center", "3": "Defensive tactics",
              "4": "Ambush tactics"},
             {"e1": """\nAfter successfully completing your studies at the Knight Academy, you continue to serve
kingdom as a knight. Through your skills and dedication, you become a respected member of the royal
guard and participate in protecting the kingdom from external threats.\n""",
              "e2": """After successfully completing your studies at the knight academy, you continue to serve the 
kingdom as a knight. Through your skill and dedication, you become a respected member of the royal guard and
actively participate in protecting the kingdom from external threats. Despite the obstacles you face, you continue to 
grow and develop as a warrior and a person, becoming a symbol of hope and justice for the kingdom.\n""",
              "e3": """After completing your studies at the Knight Academy, you were unable to cope with
test on the final exam. Your serious mistake led to tragic consequences, leaving you
expelled from the academy and deprived of the title of knight. Having fallen into despair and disappointment, you are 
faced with difficulties adapting to a new life, having lost the dream of serving the kingdom.\n"""}
         ],
        "2": [
            {"m": "Talk to locals", "1": "Ask about legends and stories associated with the castle",
             "2": "Learn about local customs and superstitions",
             "3": "Try to find out if there are witnesses to strange events",
             "4": "Try to find help or associates among the local residents"},
            {"m": "Preparing for dangers",
             "1": "Check the condition of your own equipment and weapons",
             "2": "Check stocks of provisions and medical supplies",
             "3": "Create an action plan in case of sudden danger",
             "4": "Organize a signaling system for communication with comrades"},
            {"m": "Exploring the old castle",
             "1": "Inspect old books and documents",
             "2": "Check strong walls and secret passages",
             "3": "Listen to the sounds coming from dark corners",
             "4": "Unravel codes in ancient ruins"},
            {"e1": """\nAfter long and dangerous adventures, you rescue the princess, expose the conspiracy and return
to the royal palace to applause and honorary awards. You are greeted like real heroes, and your name fits into the 
history of the kingdom as a symbol of courage and honor.\n""",
             "e2": """You save the princess, but were unable to completely expose the conspiracy. Your courageous gait
is recognized, but the exploits do not receive such brilliance as you hoped. Your participation in events remains in 
people's memory, but without much enthusiasm\n""",
             "e3": """Despite your efforts, you were unable to save the princess and expose the conspiracy. Your actions
have caused further problems for the kingdom and you are viewed with suspicion. Your attempt to be a hero results in 
great disappointment and loss of reputation for you.\n"""}
            ],
        "3": [
             {"m": "Care for the coat and hooves", "1": "Clean the coat from dirt and dust",
              "2": "Clean and trim the hooves thoroughly",
              "3": "Check the condition of the hooves and any damage",
              "4": "Use special products for hair and hoof care"},
             {"m": "Feeding and watering",
              "1": "Prepare fresh hay and feed for horses",
              "2": "Make sure the water in the drinking bowls is clean and fresh",
              "3": "Prepare special feed and additives to improve nutrition",
              "4": "Estimate the amount of feed depending on the activity and condition of the horse"},
             {"m": "Physical activity and training",
              "1": "Let the horses out for a walk or pasture",
              "2": "Warm up and jog to maintain physical fitness",
              "3": "Train basic commands and skills",
              "4": "Allow time for rest and recovery after training"},
             {"e1": """After careful horse care and training, your horse will shine with health and strength. Thanks
Thanks to your efforts, the horse becomes a reliable companion and assistant in various tasks, be it transporting goods 
or conveying important information. You are appreciated as an experienced and responsible rider.\n""",
              "e2": """After caring for the horses, you notice that they look healthy and well-groomed, but without any
significant changes. Although your diligence has not led to any specific successes or failures, the horses remain 
faithful and reliable comrades on your way.\n""",
              "e3": """As a result of insufficient care of the horses, one of them fell ill and became unsuitable for
use. Your negligence has caused serious problems and disruptions in your plans. You feel guilty for what happened and 
are now forced to look for ways to correct the situation and return the horse to health.\n"""}
         ],
    },
    "2": {
        "1": [
            {"m": "Assistance with transporting goods",
             "1": "Offer assistance in carrying heavy or bulky items",
             "2": "Provide your own transportation for delivering goods to the market",
             "3": "Share advice on packaging and protecting goods during transportation",
             "4": "Help organize the arrangement of goods on market stalls"},
            {"m": "Support with attracting customers",
             "1": "Offer help in advertising and promoting products at the market",
             "2": "Share ideas for improving the appearance of stalls and product assortment",
             "3": "Offer assistance in serving customers and addressing their inquiries",
             "4": "Share contacts and attract new potential buyers"},
            {"m": "Financial and accounting support",
             "1": "Offer assistance in accounting and financial management",
             "2": "Help with calculating income and expenses",
             "3": "Share tips on improving financial efficiency and allocating resources rationally",
             "4": "Offer assistance in preparing financial documents for tax reporting"},
            {"e1": """\nYour assistance at the market has led to a significant increase in sales and improved the 
reputation of your business partner. Thanks to your efforts, their products have become more noticeable and in demand 
among customers. You feel satisfaction in contributing to the success of the local market and helping small businesses 
thrive.\n""",
             "e2": """Your assistance at the market was in demand, but the results did not exceed expectations. 
Although sales did not increase significantly, your participation was appreciated and recognized. You remain afloat and 
continue to seek new opportunities to support local entrepreneurs.\n""",
             "e3": """Your attempts to help at the market were unsuccessful due to various circumstances. Despite your 
efforts, the products did not receive enough demand, and your business partner faced financial difficulties. You regret 
that the desired outcome was not achieved, but you are ready to learn from this experience and move forward.\n"""}
        ],
        "2": [
            {"m": "Route Selection and Planning",
             "1": "Choose the safest and most efficient route for the caravan",
             "2": "Plan the schedule and resting spots along the journey",
             "3": "Organize the allocation of resources and supplies for the trip",
             "4": "Coordinate with other caravan members to ensure smooth travel"},
            {"m": "Dealing with Obstacles on the Way",
             "1": "Handle adverse weather conditions such as storms or heavy rain",
             "2": "Manage encounters with hostile creatures or bandits on the road",
             "3": "Navigate unexpected delays or detours due to roadblocks or natural obstacles",
             "4": "Provide assistance to injured or sick caravan members during the journey"},
            {"m": "Making Strategic Decisions During the Journey",
             "1": "Decide whether to push through challenging terrain or take a detour",
             "2": "Determine the best course of action when faced with limited resources or provisions",
             "3": "Address conflicts or disputes among caravan members diplomatically",
             "4": "Adapt plans and strategies based on changing circumstances and unforeseen events"},
            {"e1": """\nYour expertise in caravan travels has led to the successful completion of the journey. You 
delivered the goods on time, overcoming all obstacles, and earned a good profit from the deal. Your skills and 
experience have made you a valuable member of the caravan, and your reputation as a reliable guide has been 
strengthened.\n""",
             "e2": """The journey with the caravan ended without any significant incidents, but the profit was modest, 
and the overall experience was limited. You were satisfied that the journey was safe and uneventful, but you remained 
with a sense that you could have done more to increase profit and travel efficiency.\n""",
             "e3": """Your journey with the caravan ended in failure due to various obstacles and unforeseen 
circumstances. Lost goods, lost roads, and other misfortunes led to losses and dissatisfaction from customers. Your 
reputation suffered, and you were left with feelings of disappointment and regret about the journey that had 
passed.\n"""}
        ],
        "3": [
            {"m": "Goods Exploration",
             "1": "Research the market to identify in-demand goods and potential profit margins",
             "2": "Gather information about suppliers, quality standards, and pricing trends",
             "3": "Evaluate the feasibility and risks associated with transporting specific types of goods",
             "4": "Plan logistics and transportation routes to optimize efficiency and minimize costs"},
            {"m": "Negotiating Deals",
             "1": "Engage in negotiations with suppliers to secure favorable terms and prices for goods",
             "2": "Utilize persuasive communication and bargaining tactics to reach mutually beneficial agreements",
             "3": "Negotiate contracts and agreements that outline terms of purchase, delivery, and payment",
             "4": "Ensure transparency and fairness in all business transactions to build trust and maintain long-term "
                  "relationships"},
            {"m": "Risk Management",
             "1": "Assess potential risks and challenges related to transporting and selling goods",
             "2": "Develop contingency plans to mitigate risks such as theft, damage, or market fluctuations",
             "3": "Implement strategies for insurance coverage, security measures, and emergency response protocols",
             "4": "Monitor market conditions and adapt plans accordingly to minimize losses and maximize profits"},
            {"e1": """\nYour thorough research and strategic negotiations paid off, leading to a successful trade 
venture. You secured lucrative deals, delivered high-quality goods, and earned substantial profits. Your reputation as 
a skilled trader grows, attracting more opportunities for profitable ventures in the future.\n""",
             "e2": """While your trade venture yielded some profits, it fell short of your initial expectations. Despite
facing challenges and unforeseen obstacles, you managed to navigate through them with resilience and adaptability. 
Although the profits were modest, you gained valuable experience and insights to improve future endeavors.\n""",
             "e3": """Unfortunately, your trade venture did not go as planned, resulting in financial losses and 
setbacks. Issues such as supply chain disruptions, price fluctuations, or unexpected competition contributed to the 
unfavorable outcome. Despite your best efforts, circumstances beyond your control led to a disappointing result. 
However, you learn valuable lessons from this experience, which will guide you in future trade endeavors.\n"""}
        ],
    },
    "3": {
        "1": [
            {"m": "Farm Work",
             "1": "Engage in various agricultural tasks such as planting, watering, and harvesting crops",
             "2": "Care for livestock by feeding, grooming, and tending to their health needs",
             "3": "Maintain farm equipment and infrastructure to ensure smooth operations",
             "4": "Collaborate with other workers to maximize efficiency and productivity on the farm"},
            {"m": "Crop Management",
             "1": "Monitor crop growth and health, identifying and addressing any issues or diseases",
             "2": "Implement strategies for pest control and weed management to protect crop yields",
             "3": "Adjust irrigation schedules and fertilizer application to optimize crop growth and quality",
             "4": "Make decisions regarding crop rotation and land management practices to maintain soil fertility and "
                  "sustainability"},
            {"m": "Seasonal Tasks",
             "1": "Adapt farm work according to seasonal demands, such as planting in the spring and harvesting in the "
                  "fall",
             "2": "Prepare fields for planting by tilling soil, applying fertilizers, and planting seeds or seedlings",
             "3": "Harvest crops at the peak of maturity, ensuring proper handling and storage to preserve quality",
             "4": "Participate in seasonal activities such as haymaking, pruning orchards, or preparing for winter "
                  "dormancy"},
            {"e1": """\nYour diligent work on the fields pays off with a bountiful harvest, yielding abundant crops and 
healthy livestock. The farm thrives under your careful management, contributing to food security and prosperity in the 
community. Your efforts bring satisfaction and fulfillment as you witness the fruits of your labor, ensuring a 
prosperous future for the farm.\n""",
             "e2": """While your efforts on the fields result in a moderate harvest, external factors such as weather 
fluctuations and market conditions limit the overall success. Despite facing challenges, you manage to maintain 
stability and sustain the farm's operations. Although the harvest may not meet initial expectations, your perseverance 
and adaptability ensure a decent outcome in the face of adversity.\n""",
             "e3": """Despite your hard work and dedication, the harvest proves disappointing due to unforeseen setbacks
such as drought, pests, or disease outbreaks. The farm suffers losses, impacting both productivity and profitability. 
Despite your best efforts to mitigate risks, circumstances beyond your control lead to a disappointing outcome. However,
you learn valuable lessons from the experience, which will guide your future endeavors on the farm.\n"""}
        ],
        "2": [
            {"m": "Plant Study",
             "1": "Engage in systematic research and observation of various plant species, focusing on their "
                  "characteristics, growth patterns, and ecological roles",
             "2": "Conduct experiments to understand factors influencing plant growth, such as soil composition, "
                  "sunlight exposure, and water availability",
             "3": "Document findings and observations to contribute to scientific knowledge and inform agricultural "
                  "practices",
             "4": "Collaborate with botanists, agricultural scientists, and environmentalists to deepen understanding "
                  "and promote sustainable plant management practices"},
            {"m": "Field Research",
             "1": "Explore diverse ecosystems to study plant diversity and distribution in different habitats",
             "2": "Collect plant specimens for identification, classification, and analysis in laboratory settings",
             "3": "Investigate the interactions between plants and their environment, including relationships with "
                  "pollinators, herbivores, and soil microorganisms",
             "4": "Apply research findings to conservation efforts, ecosystem restoration, and the development of "
                  "resilient agricultural systems"},
            {"m": "Community Education",
             "1": "Share knowledge and enthusiasm for plant science through outreach programs, workshops, and "
                  "educational initiatives",
             "2": "Empower local communities with practical skills and insights into plant identification, cultivation,"
                  " and ecological stewardship",
             "3": "Foster appreciation for the importance of plants in sustaining life, promoting biodiversity, and "
                  "mitigating environmental challenges",
             "4": "Inspire future generations of botanists, ecologists, and conservationists to explore the wonders of "
                  "the plant kingdom and advocate for its preservation"},
            {"e1": """\nYour dedicated study of plants leads to becoming a recognized expert in botanical science. Your 
comprehensive knowledge and research contributions significantly advance understanding in the field. You're sought after
for consultations, research collaborations, and educational endeavors, leaving a lasting impact on plant science and 
conservation efforts.\n""",
             "e2": """Inspired by your studies, you become a passionate advocate for environmental conservation and 
sustainable land management practices. Through activism, education, and community engagement, you raise awareness about 
the importance of protecting plant species and preserving their habitats. Your efforts contribute to positive changes in
policies and attitudes towards environmental stewardship.\n""",
             "e3": """While your journey into plant study may not result in external recognition or significant 
achievements, it fosters personal growth and fulfillment. Immersing yourself in the wonders of the natural world brings 
joy and a deeper appreciation for the interconnectedness of all living beings. Your understanding and respect for plants
 enrich your life and inspire others to cultivate a similar connection with nature.\n"""}
        ],
        "3": [
            {"m": "Animal Caretaker",
             "1": "Dedicate yourself to the well-being of animals, providing attentive care, proper nutrition, and "
                  "medical attention as needed",
             "2": "Develop strong bonds with the animals under your care, fostering trust and companionship through "
                  "regular interaction and positive reinforcement",
             "3": "Ensure clean and comfortable living conditions, maintaining hygiene and sanitation in animal "
                  "enclosures or habitats",
             "4": "Advocate for animal welfare and rights, promoting responsible stewardship and ethical treatment of "
                  "all creatures"},
            {"m": "Wildlife Conservation",
             "1": "Channel your passion for animals into conservation efforts, working to protect endangered species "
                  "and preserve their natural habitats",
             "2": "Collaborate with conservation organizations and wildlife agencies to conduct research, monitor "
                  "populations, and implement conservation initiatives",
             "3": "Educate local communities about the importance of biodiversity and the role of animals in ecosystem "
                  "health and resilience",
             "4": "Engage in habitat restoration projects and wildlife rehabilitation efforts to support the survival "
                  "and recovery of threatened species"},
            {"m": "Animal-Assisted Therapy",
             "1": "Harness the healing power of animals to provide therapy and support to individuals facing physical, "
                  "emotional, or psychological challenges",
             "2": "Facilitate animal-assisted therapy sessions in healthcare facilities, schools, and community "
                  "settings, promoting well-being and improving quality of life for diverse populations",
             "3": "Train and certify therapy animals to work alongside you, fostering connections and facilitating "
                  "therapeutic interventions tailored to each individual's needs",
             "4": "Witness the transformative impact of animal-human interactions, as people find comfort, joy, and "
                  "motivation through their relationships with therapy animals"},
            {"e1": """\nYour dedication to animal welfare leads to the flourishing of the sanctuary. Through careful 
management and compassionate care, the sanctuary becomes a haven for animals in need. Visitors are inspired by the 
stories of rehabilitation and recovery, fostering a community of support for your mission. Your efforts contribute to 
the well-being of countless animals and inspire others to prioritize compassion and empathy towards all living 
beings.\n""",
             "e2": """Despite your best efforts, unforeseen challenges arise, such as funding shortages or regulatory 
hurdles. These obstacles strain resources and impact the sanctuary's operations, leading to difficult decisions and 
compromises. While setbacks test your resolve, you remain determined to persevere, seeking innovative solutions and 
rallying support from the community. Your resilience in the face of adversity inspires others to stand by your side and
overcome obstacles together.\n""",
             "e3": """While the sanctuary may not achieve widespread recognition or financial success, the impact on 
individual animals' lives is profound. Each creature receives the care and attention it deserves, finding safety and 
comfort within the sanctuary's walls. Your work brings joy and fulfillment as you witness the transformations of 
once-neglected animals into thriving, happy beings. Despite challenges, the satisfaction of making a difference in their
 lives fuels your commitment to animal welfare.\n"""}
        ],
    },
}

print("""
Let's create your own story:
You can always stop the narration by entering <Q/q>.
""")

while True:
    terminalText = "unknown error"
    if not character["gender"]:
        terminalText = "Select your character's gender (M/F): "
    elif not character["name"]:
        terminalText = "Select your character's name: "
    elif not character["family"]:
        terminalText = """Choose your family:\n"""
        for key, value in family.items():
            terminalText += f"{key}) {value[0]}\n"
        terminalText += ">"
    elif not character["merit"]:
        terminalText = "Choose your main feature:\n"
        for key, value in merit.items():
            terminalText += f"{key}) {value[0]}\n"
        terminalText += ">"
    elif not character["childhood_activity"]:
        terminalText = "Choose what you did as a child.\n"
        for key, value in childhood_activity[character["family"]].items():
            terminalText += f"{key}) {value[0]}\n"
        terminalText += ">"
    elif "" in character["storylines"]:
        dataArr = storylines[character["family"]][character["childhood_activity"]]
        terminalText = dataArr[character["storylines"].index("")]["m"] + ".\n"
        for key, value in dataArr[character["storylines"].index("")].items():
            if key.isdigit():
                terminalText += f"{key}) {value}\n"
        terminalText += ">"
    elif "" not in character["storylines"]:
        total_result = sum(character["storylines"])
        dataArr = storylines[character["family"]][character["childhood_activity"]][-1]
        if total_result < 0:
            history += " " + dataArr["e3"]
        elif total_result == 0:
            history += " " + dataArr["e2"]
        else:
            history += " " + dataArr["e1"]
        print(history)
        break

    user_input = input(terminalText).upper()
    if user_input == "Q":
        if history:
            print(history)
        else:
            print("Narration stopped.")
        break
    # Success data change when all is OK
    elif not character["gender"] and user_input in ["M", "MALE"]:
        character["gender"] = "M"
    elif not character["gender"] and user_input in ["F", "FEMALE"]:
        character["gender"] = "F"
    elif not character["name"] and not any(char.isdigit() for char in user_input):
        character["name"] = user_input
    elif character["name"]:
        if not character["family"] and user_input in family.keys():
            history += "You were born into a family " + family[user_input][0] + ". " + family[user_input][1]
            character["family"] = user_input
        elif not character["merit"] and user_input in merit.keys():
            history += " " + merit[user_input][1]
            character["merit"] = user_input
        elif not character["childhood_activity"] and user_input in childhood_activity[character["family"]].keys():
            history += " " + childhood_activity[character["family"]][user_input][1]
            character["childhood_activity"] = user_input
        elif "" in character["storylines"]:
            index = str(character["storylines"].index(""))
            randTrueAnswer = random.randint(1, 4)
            if abs(randTrueAnswer - int(user_input)) > 1:
                value_to_assign = 1
            elif abs(randTrueAnswer - int(user_input)) == 1:
                value_to_assign = -1
            else:
                value_to_assign = 0
            character["storylines"][index] = value_to_assign

    # Error message when something wrong
    elif not character["gender"]:
        print("Please enter 'M' for Male or 'F' for Female.")
    elif not character["name"]:
        print("Please enter correct name.")
    elif not character["family"] or not character["merit"]:
        print("Choose the correct option.")
