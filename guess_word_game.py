import random


#This file contain 102 words that can be used in a guess word game
#GoodLuck
Words = [
    {
        "name": "Apple",
        "hint_2": "It is red in color",
        "hint_2": "It is red in color",
        "hint_3": 'it is considered a fruit' 
    },
    
    {
         "name": "Farrari",
         "hint_1": "It is an italian brand",
         "hint_2": "It is quite famous brand",
         "hint_3": "it is a accociated with cars"
    },
    
    {
        "name": "Sunglasses",
        "hint_1": "You wear it on sunny days",
        "hint_2": "It protects your eyes from UV rays",
        "hint_3": "Often comes in different shades"
    },
    {
        "name": "Camera",
        "hint_1": "It captures still images and videos",
        "hint_2": "Used by photographers",
        "hint_3": "Has lenses and a viewfinder"
    },
    {
        "name": "Bicycle",
        "hint_1": "It has two wheels",
        "hint_2": "You pedal to move forward",
        "hint_3": "A common mode of transportation"
    },
    {
        "name": "Guitar",
        "hint_1": "It has strings",
        "hint_2": "Used to play music",
        "hint_3": "Comes in acoustic and electric types"
    },
    {
        "name": "Telescope",
        "hint_1": "Used to observe distant objects",
        "hint_2": "Often used in astronomy",
        "hint_3": "Has lenses and sometimes mirrors"
    },
    {
        "name": "Laptop",
        "hint_1": "Portable computer",
        "hint_2": "You can type and browse on it",
        "hint_3": "Needs to be charged with a battery"
    },
    {
        "name": "Coffee",
        "hint_1": "Popular morning beverage",
        "hint_2": "Can be black or with milk",
        "hint_3": "Comes from roasted beans"
    },
    {
        "name": "Umbrella",
        "hint_1": "Used to shield from rain or sun",
        "hint_2": "Comes in various sizes and colors",
        "hint_3": "Often made of waterproof material"
    },
    {
        "name": "Map",
        "hint_1": "Shows geographical locations",
        "hint_2": "Used for navigation",
        "hint_3": "Can be paper or digital"
    },
    {
        "name": "Basketball",
        "hint_1": "A sport played with this",
        "hint_2": "You dribble and shoot it into a hoop",
        "hint_3": "Orange and round in shape"
    },
    
    {
        "name": "Binoculars",
        "hint_1": "Used for magnifying distant objects",
        "hint_2": "Has two lenses",
        "hint_3": "Commonly used for bird watching"
    },
    {
        "name": "Chandelier",
        "hint_1": "Hangs from the ceiling",
        "hint_2": "Often adorned with crystals",
        "hint_3": "Provides ambient lighting"
    },
    {
        "name": "Skateboard",
        "hint_1": "Has four wheels",
        "hint_2": "Used for riding and performing tricks",
        "hint_3": "Popular among teenagers"
    },
    {
        "name": "Perfume",
        "hint_1": "Used for fragrance",
        "hint_2": "Comes in bottles",
        "hint_3": "Applied on the skin"
    },
    {
        "name": "Globe",
        "hint_1": "Represents the Earth",
        "hint_2": "Used for geography education",
        "hint_3": "Spins on an axis"
    },
    {
        "name": "Microwave",
        "hint_1": "Used for heating food quickly",
        "hint_2": "Uses electromagnetic waves",
        "hint_3": "Found in kitchens"
    },
    {
        "name": "Backpack",
        "hint_1": "Used for carrying items",
        "hint_2": "Worn on the shoulders",
        "hint_3": "Common among students and travelers"
    },
    {
        "name": "Soccer ball",
        "hint_1": "Used in a popular sport",
        "hint_2": "Round in shape",
        "hint_3": "Kicked by players"
    },
    {
        "name": "Bin",
        "hint_1": "Used for storing waste",
        "hint_2": "Found in kitchens and offices",
        "hint_3": "Can have a lid"
    },
    {
        "name": "Treadmill",
        "hint_1": "Used for indoor running or walking",
        "hint_2": "Has a moving belt",
        "hint_3": "Found in gyms and homes"
    },
    
        {
        "name": "Cucumber",
        "hint_1": "Commonly used in salads",
        "hint_2": "Green in color",
        "hint_3": "Has a refreshing taste"
    },
    {
        "name": "Television",
        "hint_1": "Used for watching programs",
        "hint_2": "Has a screen and speakers",
        "hint_3": "Can be wall-mounted or on a stand"
    },
    {
        "name": "Candle",
        "hint_1": "Provides light",
        "hint_2": "Comes in various scents and sizes",
        "hint_3": "Usually made of wax"
    },
    {
        "name": "Pizza",
        "hint_1": "Popular Italian dish",
        "hint_2": "Has toppings like cheese and pepperoni",
        "hint_3": "Served on a round dough base"
    },
    {
        "name": "Swimming pool",
        "hint_1": "Used for recreation and exercise",
        "hint_2": "Contains water",
        "hint_3": "Often has a deep end and shallow end"
    },
    {
        "name": "Scissors",
        "hint_1": "Used for cutting",
        "hint_2": "Has two sharp blades",
        "hint_3": "Commonly found in offices and households"
    },
    {
        "name": "Chocolate",
        "hint_1": "Sweet treat made from cocoa",
        "hint_2": "Comes in various forms like bars and truffles",
        "hint_3": "Loved by many for its rich flavor"
    },
    {
        "name": "Headphones",
        "hint_1": "Used for listening to audio",
        "hint_2": "Worn over the ears",
        "hint_3": "Can be wired or wireless"
    },
    {
        "name": "Alarm clock",
        "hint_1": "Used to wake up in the morning",
        "hint_2": "Makes a sound or buzzes",
        "hint_3": "Has a snooze button"
    },
    {
        "name": "Banana",
        "hint_1": "Yellow fruit",
        "hint_2": "Has a curved shape",
        "hint_3": "Rich in potassium"
    },
    
        {
        "name": "Saxophone",
        "hint_1": "A musical instrument",
        "hint_2": "Commonly used in jazz",
        "hint_3": "Played by blowing into it"
    },
    {
        "name": "Backpack",
        "hint_1": "Used for carrying items",
        "hint_2": "Worn on the shoulders",
        "hint_3": "Common among students and travelers"
    },
    {
        "name": "Rainbow",
        "hint_1": "Visible in the sky after rain",
        "hint_2": "Consists of colors like red, orange, yellow, etc.",
        "hint_3": "Formed due to refraction and dispersion of light"
    },
    {
        "name": "Bonsai",
        "hint_1": "Miniature tree",
        "hint_2": "Art of growing trees in small containers",
        "hint_3": "Originated in Japan"
    },
    {
        "name": "Trombone",
        "hint_1": "Brass instrument",
        "hint_2": "Has a slide mechanism",
        "hint_3": "Common in orchestras and bands"
    },
    {
        "name": "Fireplace",
        "hint_1": "Used for heating a room",
        "hint_2": "Often has a chimney",
        "hint_3": "Can burn wood or use gas"
    },
    {
        "name": "Sushi",
        "hint_1": "Japanese dish",
        "hint_2": "Usually contains rice and raw fish",
        "hint_3": "Eaten with soy sauce and wasabi"
    },
    {
        "name": "Chess",
        "hint_1": "Board game",
        "hint_2": "Involves strategy and tactics",
        "hint_3": "Played with 16 pieces per player"
    },
    {
        "name": "Kite",
        "hint_1": "Flies in the sky",
        "hint_2": "Tethered with a string",
        "hint_3": "Often shaped like a diamond"
    },
    {
        "name": "Binoculars",
        "hint_1": "Used for magnifying distant objects",
        "hint_2": "Has two lenses",
        "hint_3": "Commonly used for bird watching"
    },
    #this is 40 i believe 
        {
        "name": "Chair",
        "hint_1": "You sit on it",
        "hint_2": "Found in homes and offices",
        "hint_3": "Has a backrest and legs"
    },
    {
        "name": "Book",
        "hint_1": "Contains written or printed pages",
        "hint_2": "Read for information or pleasure",
        "hint_3": "Can be fiction or non-fiction"
    },
    {
        "name": "Watch",
        "hint_1": "Worn on the wrist",
        "hint_2": "Shows time",
        "hint_3": "Can be analog or digital"
    },
    {
        "name": "Shoes",
        "hint_1": "Worn on the feet",
        "hint_2": "Protects your feet while walking",
        "hint_3": "Comes in various styles and sizes"
    },
    {
        "name": "Phone",
        "hint_1": "Communication device",
        "hint_2": "Can make calls and send messages",
        "hint_3": "Has apps for various purposes"
    },
    {
        "name": "Wallet",
        "hint_1": "Used to carry money and cards",
        "hint_2": "Fits into pockets or bags",
        "hint_3": "Can be made of leather or fabric"
    },
    {
        "name": "Bicycle",
        "hint_1": "Has two wheels",
        "hint_2": "You pedal to move forward",
        "hint_3": "A common mode of transportation"
    },
    {
        "name": "Window",
        "hint_1": "Lets light and air into a room",
        "hint_2": "Can be opened and closed",
        "hint_3": "Has a frame and glass"
    },
    {
        "name": "Dog",
        "hint_1": "Common pet",
        "hint_2": "Loyal companion",
        "hint_3": "Barks and wags its tail"
    },
    {
        "name": "Coffee",
        "hint_1": "Popular morning beverage",
        "hint_2": "Can be black or with milk",
        "hint_3": "Comes from roasted beans"
    },
    #this is 50 if the other one was 50
        {
        "name": "Helicopter",
        "hint_1": "Flies in the air",
        "hint_2": "Has rotor blades",
        "hint_3": "Used for transport and rescue"
    },
    {
        "name": "Submarine",
        "hint_1": "Operates underwater",
        "hint_2": "Can dive and resurface",
        "hint_3": "Used by navies and researchers"
    },
    {
        "name": "Accordion",
        "hint_1": "Musical instrument",
        "hint_2": "Has keys and bellows",
        "hint_3": "Produces sound by squeezing"
    },
    {
        "name": "Elevator",
        "hint_1": "Moves people between floors",
        "hint_2": "Found in buildings",
        "hint_3": "Operates with buttons and cables"
    },
    {
        "name": "Firetruck",
        "hint_1": "Used by firefighters",
        "hint_2": "Has hoses and ladders",
        "hint_3": "Red in color"
    },
    {
        "name": "Compass",
        "hint_1": "Navigational tool",
        "hint_2": "Shows directions like north and south",
        "hint_3": "Used in hiking and sailing"
    },
    {
        "name": "Guitar",
        "hint_1": "Has strings",
        "hint_2": "Used to play music",
        "hint_3": "Comes in acoustic and electric types"
    },
    {
        "name": "Telescope",
        "hint_1": "Used to observe distant objects",
        "hint_2": "Often used in astronomy",
        "hint_3": "Has lenses and sometimes mirrors"
    },
    {
        "name": "Microscope",
        "hint_1": "Used for magnifying small objects",
        "hint_2": "Has lenses and a light source",
        "hint_3": "Used in laboratories and research"
    },
    {
        "name": "Refrigerator",
        "hint_1": "Keeps food cold",
        "hint_2": "Has shelves and compartments",
        "hint_3": "Plugs into an electrical outlet"
    },
    #60 words YAY
        {
        "name": "Palindrome",
        "hint_1": "A word, phrase, or sequence that reads the same backward as forward",
        "hint_2": "Examples include 'radar' and 'madam'",
        "hint_3": "Often used in puzzles and word games"
    },
    {
        "name": "Calligraphy",
        "hint_1": "Artistic handwriting",
        "hint_2": "Often done with a pen or brush",
        "hint_3": "Has different styles like italic and copperplate"
    },
    {
        "name": "Paradox",
        "hint_1": "A statement or situation that seems contradictory or absurd but may be true",
        "hint_2": "Examples include the 'liar paradox' and 'Ship of Theseus'",
        "hint_3": "Commonly used in philosophy and logic"
    },
    {
        "name": "Amphitheater",
        "hint_1": "Outdoor venue with a semicircular seating arrangement",
        "hint_2": "Historically used for performances and spectacles",
        "hint_3": "Examples include the Colosseum in Rome"
    },
    {
        "name": "Archipelago",
        "hint_1": "A group or chain of islands",
        "hint_2": "Found in oceans and seas",
        "hint_3": "Examples include the Maldives and the Philippines"
    },
    {
        "name": "Nebula",
        "hint_1": "A cloud of gas and dust in outer space",
        "hint_2": "Formed from the remnants of stars",
        "hint_3": "Can be seen through telescopes"
    },
    {
        "name": "Fahrenheit",
        "hint_1": "A temperature scale",
        "hint_2": "Used primarily in the United States",
        "hint_3": "Water freezes at 32 degrees and boils at 212 degrees on this scale"
    },
    {
        "name": "Circumnavigate",
        "hint_1": "To travel completely around something",
        "hint_2": "Historically done by explorers",
        "hint_3": "Magellan was the first to do this around the world"
    },
    {
        "name": "Mnemonic",
        "hint_1": "A memory aid or technique",
        "hint_2": "Used to remember information",
        "hint_3": "Examples include 'ROYGBIV' for colors of the rainbow"
    },
    {
        "name": "Epiphany",
        "hint_1": "A sudden realization or understanding",
        "hint_2": "Often used in literature and psychology",
        "hint_3": "Celebrated as a Christian feast on January 6th"
    },
    #70 words
        {
        "name": "Ball",
        "hint_1": "Round object used in sports",
        "hint_2": "Can bounce",
        "hint_3": "Comes in different sizes and colors"
    },
    {
        "name": "Sun",
        "hint_1": "Star at the center of our solar system",
        "hint_2": "Provides light and heat",
        "hint_3": "Rises in the east and sets in the west"
    },
    {
        "name": "Book",
        "hint_1": "Contains written or printed pages",
        "hint_2": "Read for information or pleasure",
        "hint_3": "Can be fiction or non-fiction"
    },
    {
        "name": "Chair",
        "hint_1": "Furniture used for sitting",
        "hint_2": "Has a backrest and legs",
        "hint_3": "Found in homes and offices"
    },
    {
        "name": "Tree",
        "hint_1": "Tall plant with a trunk and branches",
        "hint_2": "Provides oxygen",
        "hint_3": "Has leaves or needles"
    },
    {
        "name": "Shoes",
        "hint_1": "Worn on the feet",
        "hint_2": "Protects your feet while walking",
        "hint_3": "Comes in various styles and sizes"
    },
    {
        "name": "Window",
        "hint_1": "Lets light and air into a room",
        "hint_2": "Can be opened and closed",
        "hint_3": "Has a frame and glass"
    },
    {
        "name": "Phone",
        "hint_1": "Communication device",
        "hint_2": "Can make calls and send messages",
        "hint_3": "Has apps for various purposes"
    },
    {
        "name": "Water",
        "hint_1": "Essential liquid for life",
        "hint_2": "Clear and odorless in its pure form",
        "hint_3": "Found in oceans, rivers, and lakes"
    },
    {
        "name": "Pizza",
        "hint_1": "Popular Italian dish",
        "hint_2": "Has toppings like cheese and pepperoni",
        "hint_3": "Served on a round dough base"
    },
    #idk anymore probably 80
        {
        "name": "Table",
        "hint_1": "Furniture used for eating or working",
        "hint_2": "Flat surface with legs",
        "hint_3": "Found in dining rooms and offices"
    },
    {
        "name": "Bird",
        "hint_1": "Feathered animal",
        "hint_2": "Flies in the sky",
        "hint_3": "Builds nests"
    },
    {
        "name": "Cake",
        "hint_1": "Sweet dessert",
        "hint_2": "Often baked for celebrations",
        "hint_3": "Can have frosting and decorations"
    },
    {
        "name": "Chair",
        "hint_1": "Furniture used for sitting",
        "hint_2": "Has a backrest and legs",
        "hint_3": "Found in homes and offices"
    },
    {
        "name": "Carrot",
        "hint_1": "Orange vegetable",
        "hint_2": "Grows underground",
        "hint_3": "Often used in salads and cooking"
    },
    {
        "name": "Television",
        "hint_1": "Electronics device",
        "hint_2": "Displays images and sound",
        "hint_3": "Used for entertainment"
    },
    {
        "name": "Bicycle",
        "hint_1": "Has two wheels",
        "hint_2": "You pedal to move forward",
        "hint_3": "A common mode of transportation"
    },
    {
        "name": "Umbrella",
        "hint_1": "Used to shield from rain or sun",
        "hint_2": "Comes in various sizes and colors",
        "hint_3": "Often made of waterproof material"
    },
    {
        "name": "Candle",
        "hint_1": "Provides light",
        "hint_2": "Often scented",
        "hint_3": "Made of wax"
    },
    {
        "name": "Laptop",
        "hint_1": "Portable computer",
        "hint_2": "You can type and browse on it",
        "hint_3": "Needs to be charged with a battery"
    },
    #90 words!!! LETS GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO THIS IS THE LONGEST FILE IVE EVER MADEEEE WHOOOOOOOOOOOHOOOOOOOOOOOOOOOOOOOO
        {
        "name": "Elephant",
        "hint_1": "Large mammal with a trunk",
        "hint_2": "Found in Africa and Asia",
        "hint_3": "Known for its tusks"
    },
    {
        "name": "Computer",
        "hint_1": "Electronic device",
        "hint_2": "Used for processing data",
        "hint_3": "Has a screen and keyboard"
    },
    {
        "name": "Pineapple",
        "hint_1": "Tropical fruit",
        "hint_2": "Has spiky skin and sweet flesh",
        "hint_3": "Grows on a plant close to the ground"
    },
    {
        "name": "Guitar",
        "hint_1": "Has strings",
        "hint_2": "Used to play music",
        "hint_3": "Comes in acoustic and electric types"
    },
    {
        "name": "Mountains",
        "hint_1": "High landforms",
        "hint_2": "Often covered in snow",
        "hint_3": "Formed through geological processes"
    },
    {
        "name": "Dolphin",
        "hint_1": "Marine mammal",
        "hint_2": "Known for its intelligence",
        "hint_3": "Has a streamlined body and fins"
    },
    {
        "name": "Pizza",
        "hint_1": "Popular Italian dish",
        "hint_2": "Has toppings like cheese and pepperoni",
        "hint_3": "Served on a round dough base"
    },
    {
        "name": "Telescope",
        "hint_1": "Used to observe distant objects",
        "hint_2": "Often used in astronomy",
        "hint_3": "Has lenses and sometimes mirrors"
    },
    {
        "name": "Peninsula",
        "hint_1": "Land surrounded by water on three sides",
        "hint_2": "Connected to a mainland",
        "hint_3": "Examples include Florida and Italy"
    },
    {
        "name": "Camera",
        "hint_1": "Device used to capture images",
        "hint_2": "Can be digital or film",
        "hint_3": "Has lenses and a viewfinder"
    }
    #100 words!!!! i am gonna stop here too tired for more
]
#use this to check the len of the array anytime
#print(len(Words)) 



def greet():
    input_check = True #Using this to check for correct input set it to True before using
    
    print("Guess the word game")
    print("Enter 1 to start game.")
    print("Enter 2 to exit exit.")
    
    while True:
        try: #Prevents ValueError's 
            while input_check == True:
                player_inpt = int(input("> "))
                
                if player_inpt == 1 or player_inpt == 2:
                    #print("The code reached here #1") #for testing
                    input_check = False
                    start()
                    break
                
                else:
                    print("Please enter 1 or 2.")
                    continue
            break
        except ValueError:
            print("Please enter 1 or 2.")
    
    if(player_inpt == 1):
        start()
        
    elif (player_inpt == 2):
        print("Exiting...")

def start():
    pass

def gameover():
    pass


# greet()