ALFWORLD_STATE ='''You are in the middle of a room. Looking quickly around you, you see a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 3, a diningtable 2, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a sidetable 1, a sinkbasin 1, and a toaster 1. Your task is to: find some apple and put it in sidetable.
State Knowledge: My task is to find an apple and put it in sidetable.
THOUGHT: To solve the task, I need to find and take an apple, then put it in sidetable.First I need to find an apple. An apple is more likely to appear in fridges (1), diningtables (1-3), sidetables (1), countertops (1), sinkbasins (1), garbagecan (1). I can check one by one, starting with fridge 1.ACTION: go to fridge 1
Observation: The fridge 1 is closed. 
State Knowledge: My task is to find an apple and put it in sidetable. I have check no place, and have not found an apple.
ACTION: open fridge 1
Observation: You open the fridge 1.The fridge 1 is open. In it, you see a lettuce 2, a mug 2, a potato 2, and a tomato 1.
State Knowledge: My task is to find an apple and put it in sidetable. I have check fridge 1, and have not found an apple.
ACTION: go to table 1 
Obversation: Nothing happens.
State Knowledge: Error Input because table 1 does not exist, illegal obj.
ACTION: go to diningtable 1
Obversation: On the diningtable 1, you see nothing.
State Knowledge: My task is to find an apple and put it in sidetable. I have check fridge 1,diningtable 1, and have not found an apple.
ACTION: go to garbagecan 1 
Obversation: On the garbagecan 1, you see a apple 3, and a egg 3.
State Knowledge: My task is to find an apple and put it in sidetable. I have check fridge 1, diningtable 1, garbagecan 1, and have found apple 3.
THOUGHT: Now I find an apple (3). Next, I need to take it. ACTION: take apple 3 from garbagecan 1
Obversation: You pick up the apple 3 from the garbagecan 1.
State Knowledge: My task is to find an apple and put it in sidetable. I have check fridge 1, diningtable 1, garbagecan 1, and have found apple 3 and pick it up.
THOUGHT: Now I find an apple (3). Next, I need to put it in/on sidetable 1. ACTION: go to sidetable 1
Obversation: On the sidetable 1, you see nothing.
State Knowledge: My task is to find an apple and put it in sidetable. I have check fridge 1, diningtable 1, garbagecan 1, and have found apple 3 and pick it up.
ACTION: put apple 3 in/on sidetable
Obversation: Nothing happens.
State Knowledge: Error Input because obj sidetable is numbering required。
ACTION: put apple 3 in/on sidetable 1
Obversation: You put the apple 3 in/on the sidetable 1.
State Knowledge: Successfully put an object in/on a location.'''
WEBSHOP_STATE = '''WebShop [SEP] Instruction: [SEP] i need a long clip-in hair extension which is natural looking, and price lower than 40.00 dollars [SEP] Search
State Knowledge: My task is to find a long clip-in hair extension that looks natural and is under $40.00 and buy it
Thought: I need to find a long clip-in hair extension that looks natural and is under $40.00, so I'll start by searching for \"long clip-in hair extension\" to see what options are available.
Action: search[long clip-in hair extension]
Observation: Instruction: [SEP] i need a long clip-in hair extension which is natural looking, and price lower than 40.00 dollars [SEP] Back to Search [SEP] Page 1 (Total results: 50) [SEP] Next > [SEP] B09C337K8S [SEP] Hair Clip Extensions for Women Natural Looking Hair Extensions Clip in Hairpieces Black Synthetic Hair Extensions [SEP] $29.99 [SEP] B093BKWHFK [SEP] MJMOJO Hair Extensions Clip in Human Hair Extensions 120g 7pcs Straight Natural Black Hair Clip in Remy Human Hair Extensions Double Weft (16 inches #NST) [SEP] $63.99 [SEP] B099K9Z9L2 [SEP] Clip in Hair Extensions 20\" Double Weft 100% Remy Human Hair Grade 8A Quality Thick Long Soft Silky Straight 7pcs 16clips for Women 70grams Chocolate Brown/Light Blonde #4/27 Color [SEP] $43.99 [SEP] B08PDYYKSP [SEP] 22 Inch Colored Party Highlights Straight Hair Clip Extension / Colored Clip in Hair Extensions Rainbow Heat-Resistant Synthetic Straight - Cospaly Fashion Party Christmas Gift For Kids Girls (Light Pink (10 Pcs)) [SEP] $12.88 [SEP] B08PF2DJ4T [SEP] 22 Inch Colored Party Highlights Straight Hair Clip Extension / Colored Clip in Hair Extensions Rainbow Heat-Resistant Synthetic Straight - Cospaly Fashion Party Christmas Gift For Kids Girls (Blue (10 Pcs)) [SEP] $12.88 [SEP] B08PF2GZB2 [SEP] 22 Inch Colored Party Highlights Straight Hair Clip Extension / Colored Clip in Hair Extensions Rainbow Heat-Resistant Synthetic Straight - Cospaly Fashion Party Christmas Gift For Kids Girls (Green (10 Pcs)) [SEP] $12.88 [SEP] B08PF47KXT [SEP] 22 Inch Colored Party Highlights Straight Hair Clip Extension / Colored Clip in Hair Extensions Rainbow Heat-Resistant Synthetic Straight - Cospaly Fashion Party Christmas Gift For Kids Girls(Red (10 Pcs)) [SEP] $12.88 [SEP] B09QQLDJ93 [SEP] Lroveb Fashion Long Curly Wig Head Dyed Black Gradient Golden Long Straight Wig African Long Curly Hair Wigs Ladies Gradient Color Chemical Fiber Silk Corn Perm Wig for Women [SEP] $34.89 [SEP] B0851CXM3N [SEP] Beaupretty Long Straight Hair Extensions Hairpieces Wig Clip in Human Hair Extensions for Women Sexy Lady Cosplay Party Accessories [SEP] $10.71 [SEP] B09MYLLBY3 [SEP] DIY hair extension 200pcs 24mm U Shaped Wigs Hair Snap Clips for Hair Extensions accessories 3 Colors Available for Hair Extensions (Color : Blonde) [SEP] $29.76
State Knowledge: My task is to find a long clip-in hair extension that looks natural and is under $40.00 and buy it, and now i have searched for \"long clip-in hair extension\" and found some options.
Thought: There are several options, but I need to find one that looks natural. The first option, B09C337K8S, is within my budget at $29.99 and is described as natural looking, which fits my criteria. I'll check this one out first.
Action: click[b09c337k8s]
Observation: Instruction: [SEP] i need a long clip-in hair extension which is natural looking, and price lower than 40.00 dollars [SEP] Back to Search [SEP] < Prev [SEP] Hair Clip Extensions for Women Natural Looking Hair Extensions Clip in Hairpieces Black Synthetic Hair Extensions [SEP] Price: $29.99 [SEP] Rating: N.A. [SEP] Description [SEP] Features [SEP] Reviews [SEP] Buy Now
State Knowledge: My task is to find a long clip-in hair extension that looks natural and is under $40.00 and buy it, and now i have clicked on the first option, B09C337K8S, which is within my budget at $29.99 and is described as natural looking.
Thought: The product details confirm that these hair extensions are natural looking and the price is right. There are no customer ratings, but the price is within my budget and it seems to match what I'm looking for. I'll go ahead and make the purchase.
Action: click[buy now]
Observation: Instruction: [SEP] i need a long clip-in hair extension which is natural looking, and price lower than 40.00 dollars [SEP] Back to Search [SEP] < Prev [SEP] Hair Clip
State Knowledge: My task is to find a long clip-in hair extension that looks natural and is under $40.00 and buy it, and now i have clicked on the first option, B09C337K8S, which is within my budget at $29.99 and is described as natural looking. I am now trying to buy it.'''
SCIWORLD_STATE = '''Your task is to find a(n) non-living thing. First, focus on the thing. Then, move it to the orange box in the living room.
State Knowledge: My task is to find a non-living thing and move it to the orange box in the living room.
Thought: I need to identify a non-living thing in the bedroom that can be moved to the orange box in the living room. I should look around to see what objects are present here.
Action: look around
Observation: This room is called the bedroom. In it, you see: \n\tthe agent\n\ta substance called air\n\ta bed. On the bed is: a mattress. On the mattress is: a white pillow..\n\ta closet. The closet door is open. In the closet is: nothing.\n\ta painting\n\ta table. On the table is: nothing.\nYou also see:\n\tA door to the hallway (that is open)
State Knowledge: My task is to find a non-living thing and move it to the orange box in the living room. I have checked the bedroom and observed serveral non-living items such as a bed, a mattress, a white pillow, a closet, a painting, and a table.
Thought: After observing the bedroom, I see several non-living items such as a bed, a mattress, a white pillow, a closet, and a painting. The closet is empty, and there's nothing on the table. I need to choose an item that can be moved to the living room.
Action: teleport to living room
Observation: You teleport to the living room.
State Knowledge: My task is to find a non-living thing and move it to the orange box in the living room. I have now teleported to the living room.
Thought: Now that I'm in the living room, I should look around to locate the orange box where I will place the non-living item from the bedroom.
Action: look around
Observation: This room is called the living room. In it, you see: \n\tthe agent\n\ta substance called air\n\ta book shelf (containing A book (Pride and Prejudice) titled Pride and Prejudice by Jane Austen)\n\ta chair. On the chair is: nothing.\n\ta couch. On the couch is: a white pillow.\n\ta desk. On the desk is: a drawer.\n\ta drawing\n\ta orange box (containing nothing)\nYou also see:\n\tA door to the hallway (that is open)
State Knowledge: My task is to find a non-living thing and move it to the orange box in the living room. I have now teleported to the living room and observed various items, including a bookshelf, a chair, a couch, a desk, a drawing, and the orange box.
Thought: I see various items in the living room, including a bookshelf with a book, a chair, a couch with a white pillow, a desk with a drawer, a drawing, and the orange box. I need to decide which item to move to the orange box. The desk seems like a suitable non-living item to focus on.
Action: focus on desk
Observation: You focus on the desk.
State Knowledge: My task is to find a non-living thing and move it to the orange box in the living room. I have now teleported to the living room. I have decided to focus on the desk as the non-living item to move.
Thought: The desk has been identified as the non-living item to move. I will now proceed to move the desk to the orange box as instructed.
Action: move desk to orange box
'''
STATE_KNOWLEDGE= {
    "Instruction" : "You’ll get a segment of a trajectory of a text-based {task} task. Your task is to generate a brief and general state knowledge of the now task state following 'State Knowledge: '. Keep it wise and general for the same task. Here is an example:",
    "Example" : {
        "alfworld":ALFWORLD_STATE,
        "webshop":WEBSHOP_STATE,
        "sciworld":SCIWORLD_STATE
        },
    "Input" : '''Now it's your turn.Here is the trajectory :{Trajectory}. Make sure your output within 128 token and put your answer in this format: 'State Knowledge:...'''
}
TASK_KNOWLEDGE=  {
    "Instruction" : '''I will provide you with an analysis of both a successful trajectory and an explored trajectory for the same task. By comparing the two, we can identify the key factors that contribute to success. Based on this analysis, you need to generate task-related task knowledge to help increase the success rate of future endeavors.''',
    "Input" : '''Success Trajectory:{Success_T}\n Failed Tarjectory:{Failed_T}\nThe task knowledge should specify what to do in what situation in the format of "When .... you should (or should not)... The action workflows are:....".
Here is a task knowledge example:
Example : {Example}
You should make your answer concise.Put your answer in this format: 'Task Knowledge: When .... you should (or should not)... The action workflows are:....'''
}


ALFWORLD_EXAMPLES ={
    'pick_and_place': 'When looking for an object, if you want to find a kitchen-related object like a spatula, you should start from the most possible locations. The action workflows are as follow:\n1)go to receptacle\n2)take object from receptacle\n3)go to the place to put the object\n4)put object in/on receptacle',
    'pick_clean_then_place': 'When pick an object, clean it and place, you should first go to the possible locations of the object, then take the object, clean it, and put it in the place. The action workflows are as follow:\n1)go to receptacle\n 2)take object from receptacle\n3)clean object with receptacle\n4)go to the place to put the object\n5)put object in/on receptacle',
    'pick_heat_then_place': 'When pick an object, heat it and place, you should first go to the possible locations of the object, then take the object, heat it with micorwave, and put it in the place. The action workflows are as follow:\n1)go to receptacle\n 2)take object from receptacle\n3)heat object with receptacle\n4)go to the place to put the object\n5)put object in/on receptacle',
    'pick_cool_then_place': 'When pick an object, cool it and place, you should first go to the possible locations of the object, then take the object, cool it with fridge, and put it in the place. The action workflows are as follow:\n1)go to receptacle\n 2)take object from receptacle\n3)cool object with receptacle\n4)go to the place to put the object\n5)put object in/on receptacle',
    'look_at_obj': 'When look at an object to find it, before you open receptacle, you should first go to the possible locations of the object, then open the receptacle to find the object. The action workflows are as follow:\n1)go to receptacle\n 2)open receptacle\n3)take object from receptacle\n4)close receptacle\n5)go to the place to put the object',
    'pick_two_obj': 'When pick two objects, you should pick object one by one, and put them in the place one by one. The action workflows are as follow:\n1)go to receptacle\n 2)take object from receptacle\n3)go to the place to put the object\n4)put object in/on receptacle'
}
WEBSHOP_EXAMPLES = "When looking for an object you want to buy, you should first search with relevant keywords tailored to the product you are looking for, and then click the relevant tag to view the product details, if the description matches the characteristics of the target item, click[buy now].\n The action workflows are as follow:\n1)search with keywords,or example, if you are searching for a laptop, you might search[laptop, 14-inch, Intel Core i7]\n2)click the most relevant tag to view the detailed product page.\n3)check the product details one by one, like color, size, type, price, make sure the price is within budget.\n4)if find the right items,click[buy now] to buy it.\n"
SCIWORLD_EXAMPLES = {
    '0':'''Task Knowledge: When tasked with boiling apple juice, focus on locating the kitchen first. Then, locate the apple juice in the fridge. Activate the stove, pour the apple juice into a metal pot, and move the metal pot to the stove. Monitor the stove until the apple juice reaches a boiling point. Once boiled, remove the pot from the stove.
The action workflows are:
1) teleport to the kitchen.
2) look around to find the apple juice in the fridge.
3) activate the stove.
4) pour apple juice into a metal pot.
5) move the metal pot to the stove.
6) look at stove.
7) examine apple juice to confirm boiling.
8) repeat step 6,7 until apple juice is boiled.
''',
    "1":'''Task Knowledge: When tasked with changing the state of matter of chocolate, focus on locating the chocolate in the fridge first. Then, teleport to the foundry and activate the blast furnace. Move the chocolate to the blast furnace to heat it up.
The action workflows are:
1) Teleport to the kitchen.
2) Pick up the chocolate from the fridge.
3) Focus on the chocolate in your inventory.
4) Teleport to the foundry.
5) Activate the blast furnace.
6) Move the chocolate to the blast furnace.
''',
    "2":'''Task Knowledge: When freezing apple juice in a scientific experiment environment,start by heading to the kitchen and locating the apple juice in the fridge. Pick up the cup containing the juice, then move it to the freezer. Wait for some time, checking periodically to see if it's frozen. Repeat until the juice is fully frozen.
The action workflows are:
1) Teleport to the kitchen.
2) Look around to find apple juice in the fridge.
3) Pick up the cup containing apple juice.
4) Focus on the apple juice in your inventory.
5) Move the cup containing apple juice to the freezer.
6) Look at the freezer to confirm the apple juice is inside.
7) Wait for 10 iterations.
8) Check the freezer to see if the apple juice has frozen.
9) If not frozen, wait for another 10 iterations and repeat steps 7-8 until frozen.
''',
    "3":'''Task Knowledge: When attempting to melt ice, follow these action workflows:
1) look around the current room to identify if ice is present. If ice is not found, teleport to another location where ice might be stored.
2) in the kitchen, locate the ice in the freezer.
3) focus on the ice to interact with it effectively.
4) move the ice to a metal pot to contain it as it melts.
5) pick up the metal pot with the ice to transport it.
6) move the metal pot with the ice to a heat source, such as the blast furnace.
7) activate the blast furnace to provide heat and melt the ice.
8) activate the blast furnace to generate the necessary heat and melt the ice.
9) examine and wait until the ice in the metal pot has melted.
''',
    "4":'''Task Knowledge: When tasked with measuring the melting point of lead, focus on locating the thermometer and lead in the kitchen. Pick up the thermometer and focus on it to ensure it's the correct tool. Move the lead to a suitable container for heating, like the metal pot. Teleport to the foundry and place the metal pot in the blast furnace, activating it. Check the blast furnace and examine the lead. Use the thermometer on the lead to measure its temperature. If the lead turns into a liquid, measure its temperature again. If the temperature is above 10.0 degrees Celsius, focus on the orange box in the kitchen.
The action workflows are:
1) locate thermometer and lead in the kitchen.
2) pick up thermometer and focus on it.
3) move lead to metal pot.
4) teleport to foundry and place metal pot in blast furnace, activating it.
5) check blast furnace and examine lead.
6) use thermometer on lead to measure temperature.
7) if lead turns into liquid, measure temperature again.
8) teleport to kitchen and focus on orange box if temperature is above 10.0 degrees Celsius.''',
    "6":'''Task Knowledge: When tasked with measuring the temperature of an unknown substance B, you should focus on locating the thermometer first.
The action workflows are:
1) teleport to the kitchen.
2) look around to find the thermometer.
3) pick up the thermometer.
4) focus on the thermometer in your inventory.
5) teleport to the possible position where unknown substance B is located.
6) look around to locate unknown substance B.
7) pick up unknown substance B.
8) focus on unknown substance B in your inventory.
9) teleport to the living room.
10) look around to locate the orange and yellow boxes.
11) use the thermometer on unknown substance B.
12) move unknown substance B to the appropriate box based on its temperature.'''
,
    "7":'''Task Knowledge: When tasked with turning on the red light bulb, you should first locate it and then create an electrical circuit to power it on.
The action workflows are:
1) teleport to the workshop.
2) look around to find the red light bulb.
3) pick up the red light bulb.
4) connect battery anode to black wire terminal 1.
5) connect battery cathode to yellow wire terminal 1.
6) connect black wire terminal 2 to cathode in red light bulb.
7) connect yellow wire terminal 2 to anode in red light bulb.
8) focus on red light bulb'''
,
    "8":'''Task Knowledge: When tasked with turning on the red light bulb using a renewable power source, follow these steps:
1) Teleport to the workshop.
2) Look around to locate the red light bulb, solar panel, and wires.
3) Pick up the red light bulb, solar panel, black wire, and orange wire.
4) Teleport to the outside.
5) Drop the red light bulb, solar panel, black wire, and orange wire.
6) Connect the solar panel anode to the black wire terminal 1.
7) Connect the solar panel cathode to the orange wire terminal 1.
8) Connect the black wire terminal 2 to the cathode in the red light bulb.
9) Connect the orange wire terminal 2 to the anode in the red light bulb.
10) Wait to observe if the red light bulb turns on.
'''
,
    "9":'''Task Knowledge: When tasked with determining the electrical conductivity of a paper clip.
The action workflows are:
1) teleport to the living room to locate the paper clip.
2) pick up the paper clip and focus on it.
3) teleport to the workshop.
4) drop the paper clip in the workshop.
5) set up a simple circuit using a battery, wires, and a light bulb.
6) connect the paper clip within the circuit.
7) wait to observe if the light bulb turns on.
8) if the light bulb is on, move the paper clip to the red box; if off, move it to the green box.
'''
,
    "10":'''Task Knowledge: When tasked with determining the electrical conductivity of an unknown substance B in the workshop environment.
The action workflows are::
1) Focus on unknown substance B to ensure correct identification.
2) Pick up unknown substance B from the workshop.
3) Drop unknown substance B in the workshop for testing.
4) Connect battery anode to red wire terminal 1.
5) Connect battery cathode to orange wire terminal 1.
6) Connect red wire terminal 2 to cathode in electric motor.
7) Connect black wire terminal 2 to anode in electric motor.
8) Connect unknown substance B terminal 1 to orange wire terminal 2.
9) Connect unknown substance B terminal 2 to black wire terminal 1.
10) Wait for observations of electrical conductivity.
11) If no signs of conductivity are observed, move unknown substance B to the green box.'''
,
    "11":'''Task Knowledge: When tasked with finding and placing an animal in the red box in the kitchen:
The action workflows are:
1) Start by looking around in the hallway for animals or clues.
2) If no animals are found, teleport to outside and observe surroundings.
3) Focus on potential animals, like eggs, and pick them up.
4) Teleport to the kitchen for efficiency.
5) Move the animal from inventory to the red box.
'''
,
    "12":'''Task Knowledge: When tasked with finding a living thing and moving it to the orange box in the workshop, follow these steps:
1) Teleport to the outside environment.
2) Look around to identify potential living things.
3) Focus on the dove egg.
4) Pick up the dove egg.
5) Teleport to the workshop.
6) Move the dove egg from your inventory to the orange box.
'''
,
    "13":'''Task Knowledge: When tasked with moving a non-living thing to an orange box in the bathroom, first teleport to the bathroom, then identify the non-living thing, focus on it, and move it to the orange box. Here's the action workflow:
1) Teleport to the bathroom.
2) Look around to identify the non-living thing.
3) Focus on the non-living thing.
4) Move the non-living thing to the orange box.'''
,
    "14":'''Task Knowledge: When tasked with finding and relocating a plant, follow these steps:
1) Teleport to the greenhouse.
2) Look around to identify the plant.
3) Focus on the plant.
4) Pick up the plant.
5) Teleport to the workshop.
6) Move the plant to the designated location.'''
,
    "15":'''Task Knowledge: When tasked with growing a banana, follow these steps:
1) Teleport to the living room.
2) Pick up the seed jar containing banana seeds.
3) Teleport to the greenhouse.
4) Plant banana seeds in flower pots 1, 2, and 3.
5) Wait for the plants to grow and reproduce.
6) Check the plants' progress in the greenhouse periodically.
7) Close the doors to maintain a controlled environment.
8) Continue waiting until bananas appear on the plants.
9) Focus on the banana on the reproducing plant to complete the task.'''
,
    "16":'''Task Knowledge: When tasked with growing an apple plant from seed, follow these steps:
1) Teleport to the bathroom.
2) Look around to find the apple seeds.
3) Pick up the seed jar containing the apple seeds.
4) Teleport to the greenhouse.
5) Look around to find a suitable place to plant the seeds.
6) Move one of the apple seeds from the seed jar to a flower pot with soil and water.
7) Focus on the planted apple seed to monitor its growth.
8) Wait for the seed to germinate and grow.
9) Continue waiting until the seed reaches the reproduction life stage.''',
    "17":'''Task Knowledge: When tasked with creating salt water using chemistry, follow these steps:
1) Teleport to the kitchen.
2) Look around to find the glass jar containing sodium chloride.
3) Pick up the glass jar of sodium chloride.
4) Teleport to the glass cup on the table.
5) Pick up the glass cup containing nothing.
6) Teleport to the sink.
7) Activate the sink to fill the glass cup with water.
8) Deactivate the sink once the cup is filled.
9) Pick up the glass cup containing sodium chloride and water.
10) Examine the cup to verify the contents.
11) Mix the sodium chloride and water in the cup.
12) Focus on the resulting salt water in your inventory.''',
    "18":'''Task Knowledge: When tasked with creating green paint using chemistry, begin by exploring the art studio.
Action workflows:
1) Teleport to the art studio.
2) Look around to identify available paint colors.
3) Move a cup containing blue paint from the large cupboard to the table.
4) Pour the cup containing yellow paint into the cup containing blue paint.
5) Mix the paints thoroughly.
6) Focus on the resulting green paint to complete the task.'''
,
    "19":'''Task Knowledge: When tasked with creating yellow-green paint, follow these steps:
1) Teleport to the art studio.
2) Look around to identify available paint colors.
3) Pour blue paint from the cupboard into a wood cup.
4) Pour yellow paint from the cupboard into the same wood cup.
5) Mix the blue and yellow paint in the cup to create green paint.
6) Focus on the green paint in your inventory.
7) Look at the green paint to confirm its color.
8) If necessary, pour more yellow paint into the cup containing green paint.
9) Mix the paints again to achieve the desired yellow-green color.
10) Focus on the yellow-green paint in your inventory.'''
,
    "20":'''Task Knowledge: When tasked with identifying the animal with the longest lifespan, follow these steps:
1) Teleport to the outside.
2) Look around to identify all animals present.
3) Focus on the the animal with the longest lifespan.
'''
,
    "21":'''Task Knowledge: When tasked with finding the animal with the longest and shortest lifespan in the 'outside' location, follow these steps:
1) Teleport to the outside.
2) Look around to identify all animals present.
3) Focus on the crocodile egg to consider it for the longest lifespan.
4) Focus on the baby hedgehog to confirm its typical lifespan.
5) Take note of any other animals present for further assessment.''',

    "22":'''Task Knowledge: When tasked with identifying the animal with the shortest lifespan, follow these steps:
1) Teleport to the outside location.
2) Look around to identify all animals present.
3) Focus on the the animal with the shortest lifespan.''',
    "23":'''Task Knowledge: When tasked with observing the three life stages of a wolf, follow these steps:
1) Teleport to the outside environment.
2) Look around to locate the baby wolf.
3) Focus on the baby wolf.
4) Wait for 10 iterations to observe any changes.
5) Repeat steps 2-4 until the baby wolf matures into a juvenile wolf.
6) Focus on the juvenile wolf.
7) Wait for 10 iterations to observe any changes.
8) Repeat steps 6-7 until the juvenile wolf matures into an adult wolf.
9) Focus on the adult wolf.''',
    "24":'''Task Knowledge: When tasked with observing the life stages of banana plants, follow these steps:
1) Teleport to the outside location.
2) Look around to identify banana plants.
3) Focus on the banana seed in self-watering flower pot 6.
4) Look around again to find the next stage of banana plants.
5) Focus on the banana tree in the seedling stage in self-watering flower pot 8.
6) Repeat the process of looking around and focusing on the banana tree's next state in the adult stage in self-watering flower pot 9.
''',

}

