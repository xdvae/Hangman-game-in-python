#this is not the main game code i just use it to mess around and try new things...
import random
import os
RESET = '\033[0m'  # Reset to default
BOLD = '\033[1m'   # Bold
UNDERLINE = '\033[4m'  # Underline

# Foreground colors
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
LIME = '\033[92m'


# Background colors
BLACK_BACKGROUND = '\033[40m'
RED_BACKGROUND = '\033[41m'
GREEN_BACKGROUND = '\033[42m'
YELLOW_BACKGROUND = '\033[43m'
BLUE_BACKGROUND = '\033[44m'
PURPLE_BACKGROUND = '\033[45m'
CYAN_BACKGROUND = '\033[46m'
WHITE_BACKGROUND = '\033[47m'

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
    }, 
    #100 words
    {
        "name": "Fountain",
        "hint_1": "Decorative water feature",
        "hint_2": "Often found in public spaces",
        "hint_3": "Can be large or small"
    },
    {
        "name": "Piano",
        "hint_1": "Musical instrument",
        "hint_2": "Played by pressing keys",
        "hint_3": "Can be acoustic or digital"
    },
    {
        "name": "Snowflake",
        "hint_1": "Delicate ice crystal",
        "hint_2": "Forms in cold weather",
        "hint_3": "Unique and fragile"
    },
    {
        "name": "Lighthouse",
        "hint_1": "Tower guiding ships",
        "hint_2": "Found on coastlines",
        "hint_3": "Has a light at the top"
    },
    {
        "name": "Butterfly",
        "hint_1": "Colorful insect",
        "hint_2": "Has wings and antennae",
        "hint_3": "Undergoes metamorphosis"
    },
    {
        "name": "Drum",
        "hint_1": "Musical instrument",
        "hint_2": "Played by hitting a surface",
        "hint_3": "Can be loud or soft"
    },
    {
        "name": "Cloud",
        "hint_1": "Collection of water vapor",
        "hint_2": "Found in the sky",
        "hint_3": "Can produce rain or snow"
    },
    {
        "name": "Violin",
        "hint_1": "Stringed musical instrument",
        "hint_2": "Played with a bow",
        "hint_3": "Has four strings"
    },
    {
        "name": "Peacock",
        "hint_1": "Colorful bird",
        "hint_2": "Known for its plumage",
        "hint_3": "Has a distinctive call"
    },
    {
        "name": "Globe",
        "hint_1": "Model of the Earth",
        "hint_2": "Shows countries and oceans",
        "hint_3": "Can be physical or digital"
    },
    {
        "name": "Kangaroo",
        "hint_1": "Australian marsupial",
        "hint_2": "Has a pouch and strong legs",
        "hint_3": "Hops to move around"
    },
    {
        "name": "Harmonica",
        "hint_1": "Small musical instrument",
        "hint_2": "Played by blowing and drawing air",
        "hint_3": "Portable and easy to learn"
    },
    {
        "name": "Fiddle",
        "hint_1": "Stringed musical instrument",
        "hint_2": "Similar to a violin",
        "hint_3": "Often used in folk music"
    },
    {
        "name": "Raccoon",
        "hint_1": "North American mammal",
        "hint_2": "Has a mask-like marking",
        "hint_3": "Omnivorous and adaptable"
    },
    {
        "name": "Saxophone",
        "hint_1": "Brass musical instrument",
        "hint_2": "Played by blowing air",
        "hint_3": "Common in jazz and blues"
    },
    {
        "name": "Turtle",
        "hint_1": "Slow-moving reptile",
        "hint_2": "Has a shell for protection",
        "hint_3": "Found in oceans and freshwater"
    },
    {
        "name": "Banjo",
        "hint_1": "Stringed musical instrument",
        "hint_2": "Has a distinctive twang",
        "hint_3": "Often used in folk and country music"
    },
    {
        "name": "Fjord",
        "hint_1": "Narrow inlet of the sea",
        "hint_2": "Formed by glacial erosion",
        "hint_3": "Found in Norway and other countries"
    },
    {
        "name": "Harp",
        "hint_1": "Stringed musical instrument",
        "hint_2": "Played by plucking strings",
        "hint_3": "Has a distinctive sound"
    },
    {
        "name": "Llama",
        "hint_1": "South American mammal",
        "hint_2": "Has a long neck and soft fur",
        "hint_3": "Often used as a pack animal"
    },
    #125 words!!!! i am gonna stop here too tired for more
        {
        "name": "Ruler",
        "hint_1": "Measuring tool",
        "hint_2": "Has units of length",
        "hint_3": "Used in geometry and design"
    },
    {
        "name": "Flute",
        "hint_1": "Woodwind instrument",
        "hint_2": "Played by blowing air",
        "hint_3": "Often used in orchestras"
    },
    {
        "name": "Rug",
        "hint_1": "Floor covering",
        "hint_2": "Made of fabric or material",
        "hint_3": "Adds warmth and comfort"
    },
    {
        "name": "Saw",
        "hint_1": "Tool for cutting",
        "hint_2": "Has a sharp blade",
        "hint_3": "Used in carpentry and DIY"
    },
    {
        "name": "Tusk",
        "hint_1": "Ivory protrusion",
        "hint_2": "Found on elephants",
        "hint_3": "Valued for its beauty"
    },
    {
        "name": "Vase",
        "hint_1": "Decorative container",
        "hint_2": "Holds flowers or plants",
        "hint_3": "Made of glass, ceramic, or metal"
    },
    {
        "name": "Wok",
        "hint_1": "Cooking vessel",
        "hint_2": "Originated in China",
        "hint_3": "Used for stir-frying and braising"
    },
    {
        "name": "Xylo",
        "hint_1": "Musical instrument",
        "hint_2": "Played by striking keys",
        "hint_3": "Has a bright, ringing sound"
    },
    {
        "name": "Yogurt",
        "hint_1": "Dairy product",
        "hint_2": "High in protein and calcium",
        "hint_3": "Often eaten as a snack"
    },
    {
        "name": "Zest",
        "hint_1": "Outer layer of citrus",
        "hint_2": "Used in cooking and baking",
        "hint_3": "Adds flavor and aroma"
    },
    {
        "name": "Bolt",
        "hint_1": "Fastener",
        "hint_2": "Used in construction",
        "hint_3": "Has a head and a shaft"
    },
    {
        "name": "Cork",
        "hint_1": "Material from trees",
        "hint_2": "Used in wine stoppers",
        "hint_3": "Lightweight and buoyant"
    },
    {
        "name": "Dish",
        "hint_1": "Plate or serving vessel",
        "hint_2": "Made of ceramic or glass",
        "hint_3": "Used for eating and serving"
    },
    {
        "name": "Eel",
        "hint_1": "Slender fish",
        "hint_2": "Found in freshwater and saltwater",
        "hint_3": "Has a snake-like body"
    },
    {
        "name": "Fang",
        "hint_1": "Sharp tooth",
        "hint_2": "Found in animals",
        "hint_3": "Used for biting and piercing"
    },
    {
        "name": "Gnat",
        "hint_1": "Small flying insect",
        "hint_2": "Found near water",
        "hint_3": "Can be a nuisance"
    },
    {
        "name": "Husk",
        "hint_1": "Outer covering",
        "hint_2": "Found on fruits and grains",
        "hint_3": "Protects the inner contents"
    },
    {
        "name": "Iris",
        "hint_1": "Flower or eye part",
        "hint_2": "Has a colorful appearance",
        "hint_3": "Symbolizes hope and wisdom"
    },
    {
        "name": "Jute",
        "hint_1": "Fiber from plants",
        "hint_2": "Used in rope and textiles",
        "hint_3": "Strong and durable"
    },
    {
        "name": "Knot",
        "hint_1": "Tying or fastening",
        "hint_2": "Used in sailing and climbing",
        "hint_3": "Secures ropes and lines"
    },
    {
    "name": "Lid",
    "hint_1": "Cover or top",
    "hint_2": "Fits on a container",
    "hint_3": "Can be made of various materials"
    },
    #150 words
    {
    "name": "Garrulous",
    "hint_1": "Talkative person",
    "hint_2": "Loves to converse",
    "hint_3": "May dominate conversations"
    },
    #175 words
    {
        "name": "Heliotrope",
        "hint_1": "Type of gemstone",
        "hint_2": "Has a blood-red color",
        "hint_3": "Found in metamorphic rocks"
    },
    {
        "name": "Thixotropy",
        "hint_1": "Property of fluids",
        "hint_2": "Becomes less viscous when agitated",
        "hint_3": "Returns to original state when still"
    },
    {
        "name": "Velleity",
        "hint_1": "Mild or slight desire",
        "hint_2": "Not a strong or intense want",
        "hint_3": "May be easily swayed"
    },
    {
        "name": "Selenite",
        "hint_1": "Type of crystal",
        "hint_2": "Has a moon-like appearance",
        "hint_3": "Often used in decorative objects"
    },
    {
        "name": "Cacophony",
        "hint_1": "Harsh, discordant sound",
        "hint_2": "Lack of harmony or rhythm",
        "hint_3": "Can be unpleasant to hear"
    },
    {
        "name": "Chiaroscurist",
        "hint_1": "Artist who specializes",
        "hint_2": "Uses strong contrasts of light",
        "hint_3": "Creates dramatic, three-dimensional effects"
    },
    {
        "name": "Thalassophobia",
        "hint_1": "Fear of the sea",
        "hint_2": "May be triggered by deep water",
        "hint_3": "Can cause anxiety or panic"
    },
    {
        "name": "Gnomon",
        "hint_1": "Vertical rod or pillar",
        "hint_2": "Casts a shadow to indicate time",
        "hint_3": "Used in sundials and astronomy"
    },
    {
        "name": "Sesquipedalian",
        "hint_1": "Given to using long words",
        "hint_2": "May be perceived as pretentious",
        "hint_3": "Loves to show off vocabulary"
    },
    {
        "name": "Tintinnabulation",
        "hint_1": "Ringing or tinkling sound",
        "hint_2": "Often associated with bells",
        "hint_3": "Can be musical or pleasant"
    },
    {
        "name": "Umbra",
        "hint_1": "Shadow or dark area",
        "hint_2": "Caused by blocking light",
        "hint_3": "Can be used in art and design"
    },
    {
        "name": "Vesper",
        "hint_1": "Evening star",
        "hint_2": "Appears in the western sky",
        "hint_3": "Symbolizes hope and guidance"
    },
    {
        "name": "Wamble",
        "hint_1": "To walk or move unsteadily",
        "hint_2": "May be due to weakness or injury",
        "hint_3": "Can be a sign of instability"
    },
    {
        "name": "Xanthosis",
        "hint_1": "Yellowish discoloration",
        "hint_2": "Affects skin or eyes",
        "hint_3": "Can be a sign of liver disease"
    },
    {
        "name": "Yonder",
        "hint_1": "At a distance, either physically or metaphorically",
        "hint_2": "May be used to indicate a goal",
        "hint_3": "Can be a poetic or literary term"
    },
    {
        "name": "Zymurgy",
        "hint_1": "Study of fermentation",
        "hint_2": "Used in brewing and winemaking",
        "hint_3": "Involves chemistry and biology"
    },
    {
        "name": "Abstruse",
        "hint_1": "Difficult to understand",
        "hint_2": "May be complex or obscure",
        "hint_3": "Requires careful thought or study"
    },
    #200 words yay
    {
    "name": "Accretion",
    "hint_1": "Growth or increase",
    "hint_2": "Can occur in astronomy",
    "hint_3": "Involves gradual accumulation"
    },
    {
        "name": "Bougainvillea",
        "hint_1": "Type of flowering vine",
        "hint_2": "Native to South America",
        "hint_3": "Popular in tropical gardens"
    },
    {
        "name": "Cacography",
        "hint_1": "Poor or ungrammatical writing",
        "hint_2": "May be due to lack of skill",
        "hint_3": "Can be embarrassing or unprofessional"
    },
    {
        "name": "Dendrochronology",
        "hint_1": "Study of tree rings",
        "hint_2": "Used in environmental science",
        "hint_3": "Helps date events and climate patterns"
    },
    {
        "name": "Echolocation",
        "hint_1": "Biological sonar system",
        "hint_2": "Used by bats and dolphins",
        "hint_3": "Helps navigate and find prey"
    },
    {
        "name": "Florid",
        "hint_1": "Excessively ornate or flowery",
        "hint_2": "May be used to describe writing",
        "hint_3": "Can be overly elaborate or showy"
    },
    {
        "name": "Gallimaufry",
        "hint_1": " Dish made from leftover food",
        "hint_2": "Can be a mix of different ingredients",
        "hint_3": "May be served as a main course"
    },
    {
        "name": "Heliotropism",
        "hint_1": "Plant movement towards sunlight",
        "hint_2": "Helps with photosynthesis",
        "hint_3": "Can be seen in sunflowers"
    },
    {
        "name": "Insouciant",
        "hint_1": "Carefree or nonchalant",
        "hint_2": "May be used to describe a person",
        "hint_3": "Can be charming or annoying"
    },
    {
        "name": "Jargonelle",
        "hint_1": "Type of pear",
        "hint_2": "Native to Europe",
        "hint_3": "Often eaten fresh or used in cooking"
    },
    {
        "name": "Kibitzer",
        "hint_1": "Person who offers unwanted advice",
        "hint_2": "May be a nuisance or annoyance",
        "hint_3": "Can be found in card games or sports"
    },
    {
        "name": "Liminal",
        "hint_1": "Of or relating to a threshold",
        "hint_2": "May be used in psychology or anthropology",
        "hint_3": "Can describe a transitional state"
    },
    {
        "name": "Mellifluous",
        "hint_1": "Having a smooth, sweet sound",
        "hint_2": "May be used to describe music or voice",
        "hint_3": "Can be pleasing or soothing"
    },
    {
        "name": "Nebulosity",
        "hint_1": "State of being cloudy or foggy",
        "hint_2": "May be used in astronomy or weather",
        "hint_3": "Can affect visibility or observation"
    },
    {
        "name": "Oculus",
        "hint_1": "Eye or eye-like structure",
        "hint_2": "May be used in architecture or anatomy",
        "hint_3": "Can be a decorative feature"
    },
    {
        "name": "Papillon",
        "hint_1": "Type of butterfly",
        "hint_2": "Has a distinctive wing shape",
        "hint_3": "Can be found in tropical regions"
    },
    {
        "name": "Quincunx",
        "hint_1": "Arrangement of five objects",
        "hint_2": "May be used in art or design",
        "hint_3": "Can be a symbol of balance or harmony"
    },
    {
        "name": "Reclusive",
        "hint_1": "Preferring to be alone",
        "hint_2": "May be used to describe a person",
        "hint_3": "Can be a trait of introverts"
    },
    #225 words
    {
    "name": "Reclusive",
    "hint_1": "Preferring to be alone",
    "hint_2": "May be used to describe a person",
    "hint_3": "Can be a trait of introverts"
    },
    {
        "name": "Selenic",
        "hint_1": "Relating to the moon",
        "hint_2": "May be used in astronomy",
        "hint_3": "Can describe a lunar eclipse"
    },
    {
        "name": "Tintinnabulum",
        "hint_1": "Bell or ringing sound",
        "hint_2": "May be used in music or poetry",
        "hint_3": "Can be a symbol of celebration"
    },
    {
        "name": "Uxoricide",
        "hint_1": "Murder of one's wife",
        "hint_2": "May be a crime or a literary theme",
        "hint_3": "Can be a tragic or dramatic event"
    },
    {
        "name": "Velleitarian",
        "hint_1": "Person who has a mild desire",
        "hint_2": "May be used to describe a personality",
        "hint_3": "Can be a trait of indecisiveness"
    },
    {
        "name": "Wamble",
        "hint_1": "To walk or move unsteadily",
        "hint_2": "May be due to weakness or injury",
        "hint_3": "Can be a sign of instability"
    },
    {
        "name": "Xanthosis",
        "hint_1": "Yellowish discoloration",
        "hint_2": "Affects skin or eyes",
        "hint_3": "Can be a sign of liver disease"
    },
    {
        "name": "Yonder",
        "hint_1": "At a distance, either physically or metaphorically",
        "hint_2": "May be used to indicate a goal",
        "hint_3": "Can be a poetic or literary term"
    },
    {
        "name": "Zymosis",
        "hint_1": "Fermentation process",
        "hint_2": "Used in brewing and winemaking",
        "hint_3": "Involves chemical reactions"
    },
    {
        "name": "Abstruse",
        "hint_1": "Difficult to understand",
        "hint_2": "May be complex or obscure",
        "hint_3": "Requires careful thought or study"
    },
    {
        "name": "Callipygian",
        "hint_1": "Having well-shaped buttocks",
        "hint_2": "May be used to describe a person",
        "hint_3": "Can be a term of admiration"
    },
    {
        "name": "Defenestration",
        "hint_1": "Act of throwing someone out a window",
        "hint_2": "May be used in history or politics",
        "hint_3": "Can be a dramatic or violent event"
    },
    {
        "name": "Echolalia",
        "hint_1": "Repetition of words or sounds",
        "hint_2": "May be used in psychology or linguistics",
        "hint_3": "Can be a trait of certain disorders"
    },
    {
        "name": "Fluxion",
        "hint_1": "Mathematical concept of rates of change",
        "hint_2": "Used in calculus and physics",
        "hint_3": "Can be a fundamental principle"
    },
    {
        "name": "Garrulity",
        "hint_1": "Talkativeness or loquacity",
        "hint_2": "May be used to describe a person",
        "hint_3": "Can be a trait of extroverts"
    },
    {
        "name": "Heliography",
        "hint_1": "Study of the sun",
        "hint_2": "May be used in astronomy or meteorology",
        "hint_3": "Can involve solar observations"
    },
    {
        "name": "Infundibuliform",
        "hint_1": "Shaped like a funnel",
        "hint_2": "May be used in anatomy or biology",
        "hint_3": "Can describe a specific structure"
    },
    {
        "name": "Jargogle",
        "hint_1": "To confuse or perplex",
        "hint_2": "May be used in literature or poetry",
        "hint_3": "Can be a verb or a noun"
    },
    #250 words 
    {
    "name": "Kymography",
    "hint_1": "Study of waves or wave-like motions",
    "hint_2": "Used in physics or oceanography",
    "hint_3": "Can involve wave patterns"
    },
    {
        "name": "Lachrymose",
        "hint_1": "Given to tears or crying",
        "hint_2": "May be used to describe a person",
        "hint_3": "Can be a trait of emotional people"
    },
    {
        "name": "Masticate",
        "hint_1": "To chew or grind food",
        "hint_2": "Important for digestion",
        "hint_3": "Can be a slow or deliberate process"
    },
    {
        "name": "Nemesis",
        "hint_1": "Enemy or opponent",
        "hint_2": "May be used in literature or mythology",
        "hint_3": "Can be a powerful or formidable foe"
    },
    {
        "name": "Oculus",
        "hint_1": "Eye or eye-like structure",
        "hint_2": "May be used in architecture or anatomy",
        "hint_3": "Can be a decorative feature"
    },
    {
        "name": "Paprika",
        "hint_1": "Spice made from bell peppers",
        "hint_2": "Used in cooking or seasoning",
        "hint_3": "Can add flavor or color"
    },
    {
        "name": "Quandary",
        "hint_1": "State of uncertainty or doubt",
        "hint_2": "May be used to describe a situation",
        "hint_3": "Can be a difficult or puzzling problem"
    },
    {
        "name": "Reclusiveness",
        "hint_1": "Tendency to avoid social contact",
        "hint_2": "May be a trait of introverts",
        "hint_3": "Can be a preference or a necessity"
        },
    {
        "name": "Sagacious",
        "hint_1": "Having keen discernment or wisdom",
        "hint_2": "May be used to describe a person",
        "hint_3": "Can be a valuable trait"
    },
    {
        "name": "Tintinnabulation",
        "hint_1": "Ringing or tinkling sound",
        "hint_2": "May be used in music or poetry",
        "hint_3": "Can be a pleasant or soothing sound"
    },
    {
        "name": "Umbra",
        "hint_1": "Shadow or dark area",
        "hint_2": "May be used in art or astronomy",
        "hint_3": "Can be a subtle or nuanced effect"
    },
    {
        "name": "Vesper",
        "hint_1": "Evening star or evening prayer",
        "hint_2": "May be used in astronomy or religion",
        "hint_3": "Can be a symbol of hope or guidance"
    },
    {
        "name": "Wattle",
        "hint_1": "Fleshy or loose skin",
        "hint_2": "May be used in anatomy or biology",
        "hint_3": "Can be a characteristic of certain animals"
    },
    {
        "name": "Xanthic",
        "hint_1": "Yellow or yellowish in color",
        "hint_2": "May be used in art or design",
        "hint_3": "Can be a bright or vibrant hue"
    },
    {
        "name": "Yoke",
        "hint_1": "Device for joining two animals",
        "hint_2": "May be used in agriculture or farming",
        "hint_3": "Can be a tool or a symbol"
    },
    {
        "name": "Zestful",
        "hint_1": "Full of enthusiasm or energy",
        "hint_2": "May be used to describe a person",
        "hint_3": "Can be a positive or uplifting trait"
    },
    {
        "name": "Axiom",
        "hint_1": "Self-evident truth or principle",
        "hint_2": "May be used in mathematics or philosophy",
        "hint_3": "Can be a fundamental concept"
    },
    {
        "name": "Bougainville",
        "hint_1": "French explorer or island",
        "hint_2": "May be used in history or geography",
        "hint_3": "Can be a notable figure or place"
    },
    #275 words
    {
    "name": "Cacophony",
    "hint_1": "Harsh or discordant sound",
    "hint_2": "May be used in music or literature",
    "hint_3": "Can be unpleasant or jarring"
    },
    {
        "name": "Dappled",
        "hint_1": "Marked with spots or patches",
        "hint_2": "May be used to describe an animal's coat",
        "hint_3": "Can be a unique or attractive feature"
    },
    {
        "name": "Ephemeral",
        "hint_1": "Lasting for a very short time",
        "hint_2": "May be used to describe a feeling or experience",
        "hint_3": "Can be fleeting or transitory"
    },
    {
        "name": "Flamboyant",
        "hint_1": "Conspicuously dashing or colorful",
        "hint_2": "May be used to describe a person or style",
        "hint_3": "Can be bold or attention-grabbing"
    },
    {
        "name": "Garrulous",
        "hint_1": "Talkative or loquacious",
        "hint_2": "May be used to describe a person",
        "hint_3": "Can be chatty or verbose"
    },
    {
        "name": "Hazy",
        "hint_1": "Lacking clearness or distinctness",
        "hint_2": "May be used to describe the weather",
        "hint_3": "Can be unclear or vague"
    },
    {
        "name": "Insouciant",
        "hint_1": "Carefree or nonchalant",
        "hint_2": "May be used to describe a person's attitude",
        "hint_3": "Can be relaxed or casual"
    },
    {
        "name": "Jocularity",
        "hint_1": "Good humor or jesting",
        "hint_2": "May be used to describe a person's mood",
        "hint_3": "Can be playful or amusing"
    },
    {
        "name": "Kaleidoscopic",
        "hint_1": "Multicolored or constantly changing",
        "hint_2": "May be used to describe a pattern or design",
        "hint_3": "Can be vibrant or dynamic"
    },
    {
        "name": "Lissome",
        "hint_1": "Slender or flexible",
        "hint_2": "May be used to describe a person's physique",
        "hint_3": "Can be agile or graceful"
    },
    {
        "name": "Mellifluous",
        "hint_1": "Having a smooth or sweet sound",
        "hint_2": "May be used to describe music or a voice",
        "hint_3": "Can be pleasant or soothing"
    },
    {
        "name": "Nimble",
        "hint_1": "Quick or light in movement",
        "hint_2": "May be used to describe an athlete or dancer",
        "hint_3": "Can be agile or swift"
    },
    {
        "name": "Opheliac",
        "hint_1": "Relating to Hamlet's Ophelia",
        "hint_2": "May be used in literature or drama",
        "hint_3": "Can be a tragic or romantic figure"
    },
    {
        "name": "Pellucid",
        "hint_1": "Transparent or clear",
        "hint_2": "May be used to describe a liquid or a thought",
        "hint_3": "Can be lucid or easy to understand"
    },
    {
        "name": "Quixotic",
        "hint_1": "Extravagantly chivalrous or romantic",
        "hint_2": "May be used to describe a person's behavior",
        "hint_3": "Can be idealistic or impractical"
    },
    {
        "name": "Rigmarole",
        "hint_1": "Complex or bureaucratic procedure",
        "hint_2": "May be used to describe a process or system",
        "hint_3": "Can be tedious or frustrating"
    },
    {
        "name": "Sesquipedalian",
        "hint_1": "Given to using long words",
        "hint_2": "May be used to describe a person's writing style",
        "hint_3": "Can be pretentious or showy"
    },
    
    #300 words BRUH
    {
    "name": "Tint",
    "hint_1": "A slight or delicate color",
    "hint_2": "May be used in art or design",
    "hint_3": "Can be a subtle or nuanced effect"
    },
    {
        "name": "Ubiquitous",
        "hint_1": "Existing or being everywhere",
        "hint_2": "May be used to describe a phenomenon",
        "hint_3": "Can be widespread or pervasive"
    },
    {
        "name": "Vacillate",
        "hint_1": "To hesitate or waver",
        "hint_2": "May be used to describe a person's decision-making",
        "hint_3": "Can be indecisive or uncertain"
    },
    {
        "name": "Wistful",
        "hint_1": "Feeling a sense of longing or melancholy",
        "hint_2": "May be used to describe a person's mood",
        "hint_3": "Can be nostalgic or sentimental"
    },
    {
        "name": "Xenial",
        "hint_1": "Friendly or hospitable to guests",
        "hint_2": "May be used to describe a person's behavior",
        "hint_3": "Can be welcoming or generous"
    },
    {
        "name": "Yearn",
        "hint_1": "To feel a strong desire or longing",
        "hint_2": "May be used to describe a person's emotions",
        "hint_3": "Can be intense or passionate"
    },
    {
        "name": "Zephyr",
        "hint_1": "A gentle or mild breeze",
        "hint_2": "May be used to describe the weather",
        "hint_3": "Can be refreshing or soothing"
    },
    {
        "name": "Abstruse",
        "hint_1": "Difficult to understand or obscure",
        "hint_2": "May be used to describe a concept or idea",
        "hint_3": "Can be complex or esoteric"
    },
    {
        "name": "Callipygian",
        "hint_1": "Having well-shaped buttocks",
        "hint_2": "May be used to describe a person's physique",
        "hint_3": "Can be a humorous or lighthearted term"
    },
    {
        "name": "Defenestration",
        "hint_1": "The act of throwing someone out a window",
        "hint_2": "May be used in history or politics",
        "hint_3": "Can be a dramatic or violent event"
    },
    {
        "name": "Echolocation",
        "hint_1": "The ability to locate objects by sound",
        "hint_2": "May be used in biology or zoology",
        "hint_3": "Can be a unique or specialized sense"
    },
    {
        "name": "Florid",
        "hint_1": "Excessively ornate or flowery",
        "hint_2": "May be used to describe writing or speech",
        "hint_3": "Can be overly elaborate or pretentious"
    },
    {
        "name": "Garrulity",
        "hint_1": "Talkativeness or loquacity",
        "hint_2": "May be used to describe a person's behavior",
        "hint_3": "Can be chatty or verbose"
    },
    {
        "name": "Heliotropism",
        "hint_1": "The phenomenon of plants turning towards the sun",
        "hint_2": "May be used in botany or biology",
        "hint_3": "Can be a natural or instinctual behavior"
    },
    {
        "name": "Insularity",
        "hint_1": "The state of being isolated or detached",
        "hint_2": "May be used to describe a person's behavior",
        "hint_3": "Can be a psychological or emotional state"
    },
    {
        "name": "Jargonelle",
        "hint_1": "A type of pear or a dialect",
        "hint_2": "May be used in horticulture or linguistics",
        "hint_3": "Can be a specialized or technical term"
    },
    {
        "name": "Kibitzer",
        "hint_1": "A person who offers unwanted or unsolicited advice",
        "hint_2": "May be used in social or cultural contexts",
        "hint_3": "Can be a humorous or satirical term"
    },
    #325 words
    {
    "name": "Liminal",
    "hint_1": "Of or relating to a transitional phase",
    "hint_2": "May be used in psychology or anthropology",
    "hint_3": "Can be a threshold or a turning point"
    },
    {
        "name": "Mandolin",
        "hint_1": "A stringed musical instrument",
        "hint_2": "May be used in music or folk culture",
        "hint_3": "Can be a popular or traditional instrument"
    },
    {
        "name": "Nougat",
        "hint_1": "A type of sweet or candy",
        "hint_2": "May be used in baking or confectionery",
        "hint_3": "Can be a chewy or creamy treat"
    },
    {
        "name": "Oboe",
        "hint_1": "A double-reed woodwind instrument",
        "hint_2": "May be used in classical music or orchestras",
        "hint_3": "Can be a distinctive or haunting sound"
    },
    {
        "name": "Paprika",
        "hint_1": "A spice made from ground bell peppers",
        "hint_2": "May be used in cooking or Hungarian cuisine",
        "hint_3": "Can be sweet or smoky in flavor"
    },
    {
        "name": "Quiche",
        "hint_1": "A type of savory tart or pie",
        "hint_2": "May be used in French cuisine or brunch",
        "hint_3": "Can be a versatile or filling dish"
    },
    {
        "name": "Rucksack",
        "hint_1": "A type of backpack or hiking bag",
        "hint_2": "May be used in outdoor activities or travel",
        "hint_3": "Can be practical or comfortable"
    },
    {
        "name": "Satchel",
        "hint_1": "A type of bag or handbag",
        "hint_2": "May be used in fashion or everyday life",
        "hint_3": "Can be stylish or functional"
    },
    {
        "name": "Tartan",
        "hint_1": "A type of plaid or checked pattern",
        "hint_2": "May be used in Scottish culture or textiles",
        "hint_3": "Can be a traditional or iconic design"
    },
    {
        "name": "Ukelele",
        "hint_1": "A small stringed instrument",
        "hint_2": "May be used in music or Hawaiian culture",
        "hint_3": "Can be a popular or portable instrument"
    },
    {
        "name": "Vesper",
        "hint_1": "A type of evening star or prayer",
        "hint_2": "May be used in astronomy or religion",
        "hint_3": "Can be a beautiful or contemplative concept"
    },
    {
        "name": "Wattle",
        "hint_1": "A type of fence or structure",
        "hint_2": "May be used in construction or gardening",
        "hint_3": "Can be a rustic or natural feature"
    },
    {
        "name": "Xylophone",
        "hint_1": "A type of musical instrument",
        "hint_2": "May be used in music or percussion",
        "hint_3": "Can be a unique or melodic sound"
    },
    {
        "name": "Yogurt",
        "hint_1": "A type of fermented milk product",
        "hint_2": "May be used in cooking or health food",
        "hint_3": "Can be a nutritious or refreshing snack"
    },
    {
        "name": "Zest",
        "hint_1": "The outer layer of a citrus fruit",
        "hint_2": "May be used in cooking or baking",
        "hint_3": "Can be a flavorful or aromatic ingredient"
    },
    {
        "name": "Biscotti",
        "hint_1": "A type of Italian cookie",
        "hint_2": "May be used in baking or coffee culture",
        "hint_3": "Can be crunchy or twice-baked"
    },
    {
        "name": "Cantaloupe",
        "hint_1": "A type of melon or fruit",
        "hint_2": "May be used in cooking or summer recipes",
        "hint_3": "Can be sweet or refreshing"
    },
    {
        "name": "Dumpling",
        "hint_1": "A type of pastry or filled dough",
        "hint_2": "May be used in cooking"
        
    },
    #350
    {
    "name": "Apple",
    "hint_1": "A type of fruit",
    "hint_2": "Often red or green",
    "hint_3": "Eaten as a snack"
    },
    {
        "name": "Bed",
        "hint_1": "A piece of furniture",
        "hint_2": "Used for sleeping",
        "hint_3": "Found in a bedroom"
    },
    {
        "name": "Cake",
        "hint_1": "A type of sweet dessert",
        "hint_2": "Often served at birthdays",
        "hint_3": "Can be chocolate or vanilla"
    },
    {
        "name": "Dog",
        "hint_1": "A type of pet",
        "hint_2": "Often loyal and friendly",
        "hint_3": "Wags its tail"
    },
    {
        "name": "Egg",
        "hint_1": "A type of food",
        "hint_2": "Often eaten for breakfast",
        "hint_3": "Can be scrambled or fried"
    },
    {
        "name": "Fish",
        "hint_1": "A type of animal",
        "hint_2": "Lives in water",
        "hint_3": "Can be eaten as food"
    },
    {
        "name": "Game",
        "hint_1": "An activity for fun",
        "hint_2": "Can be played on a console",
        "hint_3": "Often competitive"
    },
    {
        "name": "Hat",
        "hint_1": "A type of clothing",
        "hint_2": "Worn on the head",
        "hint_3": "Can be stylish or functional"
    },
    {
        "name": "Ice",
        "hint_1": "A type of frozen water",
        "hint_2": "Used in drinks or desserts",
        "hint_3": "Can be cold or refreshing"
    },
    {
        "name": "Jelly",
        "hint_1": "A type of sweet spread",
        "hint_2": "Often eaten on toast",
        "hint_3": "Can be grape or strawberry"
    },
    {
        "name": "Kite",
        "hint_1": "A type of toy",
        "hint_2": "Flies in the air",
        "hint_3": "Often colorful or decorative"
    },
    {
        "name": "Lemon",
        "hint_1": "A type of citrus fruit",
        "hint_2": "Often used in cooking",
        "hint_3": "Can be sour or refreshing"
    },
    {
        "name": "Mouse",
        "hint_1": "A type of small animal",
        "hint_2": "Often found in homes",
        "hint_3": "Can be a pet or pest"
    },
    {
        "name": "Nest",
        "hint_1": "A type of home for birds",
        "hint_2": "Often found in trees",
        "hint_3": "Can be cozy or protective"
    },
    {
        "name": "Ocean",
        "hint_1": "A large body of water",
        "hint_2": "Often blue or salty",
        "hint_3": "Can be calm or stormy"
    },
    {
        "name": "Pencil",
        "hint_1": "A type of writing tool",
        "hint_2": "Often used in school",
        "hint_3": "Can be sharp or dull"
    },
    {
        "name": "Queen",
        "hint_1": "A type of royal title",
        "hint_2": "Often associated with power",
        "hint_3": "Can be regal or majestic"
    },
    {
        "name": "Rabbit",
        "hint_1": "A type of small animal",
        "hint_2": "Often found in gardens",
        "hint_3": "Can be cute or fast"
    },
    {
        "name": "Sun",
        "hint_1": "A type of star",
        "hint_2": "Often shines brightly",
        "hint_3": "Can be warm or hot"
    },
    {
        "name": "Tiger",
        "hint_1": "A type of big cat",
        "hint_2": "Often found in zoos",
        "hint_3": "Can be fierce or majestic"
    },
    {
        "name": "Umbrella",
        "hint_1": "A type of rain protection",
        "hint_2": "Often used on rainy days",
        "hint_3": "Can be colorful or functional"
    },
    #375
    {
    "name": "Vase",
    "hint_1": "A type of decorative container",
    "hint_2": "Often holds flowers",
    "hint_3": "Can be made of glass or ceramic"
    },
    {
        "name": "Water",
        "hint_1": "A type of liquid",
        "hint_2": "Essential for life",
        "hint_3": "Can be drunk or used for washing"
    },
    {
        "name": "Xylo",
        "hint_1": "A type of musical instrument",
        "hint_2": "Often played in schools",
        "hint_3": "Can be a fun or easy instrument"
    },
    {
        "name": "Yellow",
        "hint_1": "A type of bright color",
        "hint_2": "Often associated with sunshine",
        "hint_3": "Can be a happy or cheerful color"
    },
    {
        "name": "Zoo",
        "hint_1": "A place where animals live",
        "hint_2": "Often visited by families",
        "hint_3": "Can be a fun or educational outing"
    },
    {
        "name": "Ball",
        "hint_1": "A type of round object",
        "hint_2": "Often used in sports",
        "hint_3": "Can be bounced or thrown"
    },
    {
        "name": "Book",
        "hint_1": "A type of written material",
        "hint_2": "Often read for entertainment",
        "hint_3": "Can be fiction or non-fiction"
    },
    {
        "name": "Chair",
        "hint_1": "A type of piece of furniture",
        "hint_2": "Often used for sitting",
        "hint_3": "Can be comfortable or stylish"
    },
    {
        "name": "Desk",
        "hint_1": "A type of piece of furniture",
        "hint_2": "Often used for working",
        "hint_3": "Can be cluttered or organized"
    },
    {
        "name": "Ears",
        "hint_1": "A type of body part",
        "hint_2": "Used for hearing",
        "hint_3": "Can be pierced or decorated"
    },
    {
        "name": "Face",
        "hint_1": "A type of body part",
        "hint_2": "Used for expression",
        "hint_3": "Can be happy or sad"
    },
    {
        "name": "Glove",
        "hint_1": "A type of clothing",
        "hint_2": "Worn on the hand",
        "hint_3": "Can be warm or protective"
    },
    {
        "name": "Honey",
        "hint_1": "A type of sweet food",
        "hint_2": "Made by bees",
        "hint_3": "Can be eaten or used in cooking"
    },
    {
        "name": "Igloo",
        "hint_1": "A type of shelter",
        "hint_2": "Made of snow",
        "hint_3": "Can be found in cold climates"
    },
    {
        "name": "Jacket",
        "hint_1": "A type of clothing",
        "hint_2": "Worn on the upper body",
        "hint_3": "Can be warm or stylish"
    },
    {
        "name": "Kite",
        "hint_1": "A type of toy",
        "hint_2": "Flies in the air",
        "hint_3": "Can be colorful or decorative"
    },
    {
        "name": "Lamp",
        "hint_1": "A type of lighting",
        "hint_2": "Used for illumination",
        "hint_3": "Can be table or floor-standing"
    },
    {
        "name": "Milk",
        "hint_1": "A type of liquid",
        "hint_2": "Often drunk for nutrition",
        "hint_3": "Can be whole or skimmed"
    },
    {
        "name": "Nose",
        "hint_1": "A type of body part",
        "hint_2": "Used for smelling",
        "hint_3": "Can be small or large"
    },
    {
        "name": "Oven",
        "hint_1": "A type of kitchen appliance",
        "hint_2": "Used for cooking",
        "hint_3": "Can be electric or gas-powered"
    },
    {
        "name": "Pants",
        "hint_1": "A type of clothing",
        "hint_2": "Worn on the lower body",
        "hint_3": "Can be casual or formal"
    },

#400 this is getting tiring i wonder how many words are repeated in it
    {
    "name": "Pillow",
    "hint_1": "A type of bedding",
    "hint_2": "Used for sleeping",
    "hint_3": "Can be soft or firm"
    },
    {
        "name": "Quilt",
        "hint_1": "A type of bedding",
        "hint_2": "Often decorative",
        "hint_3": "Can be handmade or store-bought"
    },
    {
        "name": "Ruler",
        "hint_1": "A type of measuring tool",
        "hint_2": "Used in school or work",
        "hint_3": "Can be plastic or metal"
    },
    {
        "name": "Sand",
        "hint_1": "A type of natural material",
        "hint_2": "Often found on beaches",
        "hint_3": "Can be soft or coarse"
    },
    {
        "name": "Tape",
        "hint_1": "A type of adhesive material",
        "hint_2": "Used for sticking things together",
        "hint_3": "Can be clear or colored"
    },
    {
        "name": "Ukelele",
        "hint_1": "A type of musical instrument",
        "hint_2": "Often played for fun",
        "hint_3": "Can be small or large"
    },
    {
        "name": "Vacuum",
        "hint_1": "A type of cleaning tool",
        "hint_2": "Used for cleaning floors",
        "hint_3": "Can be handheld or upright"
    },
    {
        "name": "Wallet",
        "hint_1": "A type of personal accessory",
        "hint_2": "Used for carrying money",
        "hint_3": "Can be leather or fabric"
    },
    {
        "name": "X-ray",
        "hint_1": "A type of medical imaging",
        "hint_2": "Used for diagnosing injuries",
        "hint_3": "Can be used in hospitals"
    },
    {
        "name": "Yogurt",
        "hint_1": "A type of food",
        "hint_2": "Often eaten for breakfast",
        "hint_3": "Can be sweet or sour"
    },
    {
        "name": "Zipper",
        "hint_1": "A type of clothing fastener",
        "hint_2": "Used for closing or opening",
        "hint_3": "Can be metal or plastic"
    },
    {
        "name": "Bicycle",
        "hint_1": "A type of vehicle",
        "hint_2": "Used for transportation",
        "hint_3": "Can be ridden on roads or trails"
    },
    {
        "name": "Camera",
        "hint_1": "A type of electronic device",
        "hint_2": "Used for taking pictures",
        "hint_3": "Can be digital or film-based"
    },
    {
        "name": "Dictionary",
        "hint_1": "A type of reference book",
        "hint_2": "Used for looking up words",
        "hint_3": "Can be physical or digital"
    },
    {
        "name": "Elevator",
        "hint_1": "A type of transportation device",
        "hint_2": "Used for moving between floors",
        "hint_3": "Can be found in buildings"
    },
    {
        "name": "Flower",
        "hint_1": "A type of plant",
        "hint_2": "Often given as a gift",
        "hint_3": "Can be colorful or fragrant"
    },
    {
        "name": "Guitar",
        "hint_1": "A type of musical instrument",
        "hint_2": "Often played for entertainment",
        "hint_3": "Can be acoustic or electric"
    },
    {
        "name": "Hanger",
        "hint_1": "A type of clothing accessory",
        "hint_2": "Used for hanging clothes",
        "hint_3": "Can be metal or plastic"
    },
    {
        "name": "Ice cream",
        "hint_1": "A type of sweet treat",
        "hint_2": "Often eaten as a dessert",
        "hint_3": "Can be creamy or fruity"
    },
    {
        "name": "Jewelry",
        "hint_1": "A type of personal accessory",
        "hint_2": "Used for decoration",
        "hint_3": "Can be made of gold or silver"
    },
    {
        "name": "Kettle",
        "hint_1": "A type of kitchen appliance",
        "hint_2": "Used for boiling water",
        "hint_3": "Can be electric or non eletric"
    },
    #425 words
    {
        "name": "Luggage",
        "hint_1": "A type of travel accessory",
        "hint_2": "Used for carrying clothes",
        "hint_3": "Can be small or large"
    },
    {
        "name": "Microphone",
        "hint_1": "A type of audio device",
        "hint_2": "Used for speaking or singing",
        "hint_3": "Can be handheld or mounted"
    },
    {
        "name": "Napkin",
        "hint_1": "A type of tableware",
        "hint_2": "Used for wiping hands",
        "hint_3": "Can be paper or cloth"
    },
    {
        "name": "Oboe",
        "hint_1": "A type of musical instrument",
        "hint_2": "Often played in orchestras",
        "hint_3": "Can be made of wood or metal"
    },
    {
        "name": "Pajamas",
        "hint_1": "A type of clothing",
        "hint_2": "Worn for sleeping",
        "hint_3": "Can be soft or comfortable"
    },
    {
        "name": "Quiche",
        "hint_1": "A type of food",
        "hint_2": "Often eaten for breakfast",
        "hint_3": "Can be savory or sweet"
    },
    {
        "name": "Ribbon",
        "hint_1": "A type of decorative material",
        "hint_2": "Used for wrapping gifts",
        "hint_3": "Can be colorful or patterned"
    },
    {
        "name": "Saxophone",
        "hint_1": "A type of musical instrument",
        "hint_2": "Often played in jazz bands",
        "hint_3": "Can be made of brass or metal"
    },
    {
        "name": "Towel",
        "hint_1": "A type of bathroom accessory",
        "hint_2": "Used for drying the body",
        "hint_3": "Can be soft or absorbent"
    },
    {
        "name": "Umbrella",
        "hint_1": "A type of weather accessory",
        "hint_2": "Used for staying dry",
        "hint_3": "Can be compact or large"
    },
    {
        "name": "Vase",
        "hint_1": "A type of decorative container",
        "hint_2": "Often holds flowers",
        "hint_3": "Can be made of glass or ceramic"
    },
    {
        "name": "Wallet",
        "hint_1": "A type of personal accessory",
        "hint_2": "Used for carrying money",
        "hint_3": "Can be leather or fabric"
    },
    {
        "name": "Xylophone",
        "hint_1": "A type of musical instrument",
        "hint_2": "Often played in schools",
        "hint_3": "Can be made of wood or metal"
    },
    {
        "name": "Yarn",
        "hint_1": "A type of crafting material",
        "hint_2": "Used for knitting or crocheting",
        "hint_3": "Can be soft or colorful"
    },
    {
        "name": "Zipper",
        "hint_1": "A type of clothing fastener",
        "hint_2": "Used for closing or opening",
        "hint_3": "Can be metal or plastic"
    },
    {
        "name": "Bicycle",
        "hint_1": "A type of vehicle",
        "hint_2": "Used for transportation",
        "hint_3": "Can be ridden on roads or trails"
    },
    {
        "name": "Calculator",
        "hint_1": "A type of electronic device",
        "hint_2": "Used for math calculations",
        "hint_3": "Can be handheld or desktop"
    },
    {
        "name": "Dishwasher",
        "hint_1": "A type of kitchen appliance",
        "hint_2": "Used for cleaning dishes",
        "hint_3": "Can be electric or gas-powered"
    },
    {
        "name": "Envelope",
        "hint_1": "A type of stationery",
        "hint_2": "Used for sending mail",
        "hint_3": "Can be plain or decorated"
    },
    {
        "name": "Fork",
        "hint_1": "A type of utensil",
        "hint_2": "Used for eating",
        "hint_3": "Can be metal or plastic"
    }, 
    #450 words 
    {
    "name": "Hazard",
    "hint_1": "A type of danger",
    "hint_2": "Can be physical or environmental",
    "hint_3": "Requires caution or warning"
    },
    {
        "name": "Igloo",
        "hint_1": "A type of shelter",
        "hint_2": "Made of snow or ice",
        "hint_3": "Often found in cold climates"
    },
    {
        "name": "Journey",
        "hint_1": "A type of travel",
        "hint_2": "Can be long or short",
        "hint_3": "May involve transportation or walking"
    },
    {
        "name": "Kaleidoscope",
        "hint_1": "A type of toy",
        "hint_2": "Creates colorful patterns",
        "hint_3": "Often used for entertainment"
    },
    {
        "name": "Llama",
        "hint_1": "A type of animal",
        "hint_2": "Found in South America",
        "hint_3": "Has a long neck and soft fur"
    },
    {
        "name": "Meteorite",
        "hint_1": "A type of space rock",
        "hint_2": "Falls to Earth from space",
        "hint_3": "Can be small or large"
    },
    {
        "name": "Nemesis",
        "hint_1": "A type of enemy",
        "hint_2": "Can be a person or thing",
        "hint_3": "Often opposes or rivals"
    },
    {
        "name": "Oculus",
        "hint_1": "A type of eye part",
        "hint_2": "Helps with vision",
        "hint_3": "Can be affected by disease"
    },
    {
        "name": "Paprika",
        "hint_1": "A type of spice",
        "hint_2": "Often used in cooking",
        "hint_3": "Can add flavor or color"
    },
    {
        "name": "Quandary",
        "hint_1": "A type of problem",
        "hint_2": "Can be difficult to solve",
        "hint_3": "May require thought or decision"
    },
    {
        "name": "Rhapsody",
        "hint_1": "A type of music",
        "hint_2": "Often expressive or emotional",
        "hint_3": "Can be performed by an orchestra"
    },
    {
        "name": "Spectrum",
        "hint_1": "A type of range",
        "hint_2": "Can be of colors or frequencies",
        "hint_3": "Often used in science or technology"
    },
    {
        "name": "Tapestry",
        "hint_1": "A type of textile",
        "hint_2": "Often decorative or artistic",
        "hint_3": "Can be hung on a wall"
    },
    {
        "name": "Umbra",
        "hint_1": "A type of shadow",
        "hint_2": "Can be dark or faint",
        "hint_3": "Often cast by an object"
    },
    {
        "name": "Vesper",
        "hint_1": "A type of evening star",
        "hint_2": "Can be seen in the sky",
        "hint_3": "Often associated with twilight"
    },
    {
        "name": "Wisteria",
        "hint_1": "A type of flowering plant",
        "hint_2": "Often fragrant or colorful",
        "hint_3": "Can be grown in gardens"
    },
    {
        "name": "Xanthan",
        "hint_1": "A type of gum or powder",
        "hint_2": "Often used in food or cosmetics",
        "hint_3": "Can be derived from bacteria"
    },
    {
        "name": "Yttrium",
        "hint_1": "A type of chemical element",
        "hint_2": "Often used in technology",
        "hint_3": "Can be found in rare earth minerals"
    },
    {
        "name": "Zymurgy",
        "hint_1": "A type of fermentation science",
        "hint_2": "Often used in brewing or baking",
        "hint_3": "Can involve enzymes or microorganisms"
    },
    {
        "name": "Bougainvillea",
        "hint_1": "A type of flowering vine",
        "hint_2": "Often colorful or thorny",
        "hint_3": "Can be grown in warm climates"
    },  
    #475
    {
    "name": "Basket",
    "hint_1": "A type of container",
    "hint_2": "Used for carrying things",
    "hint_3": "Can be made of wicker or fabric"
    },
    {
        "name": "Cloudy",
        "hint_1": "A type of weather",
        "hint_2": "Often gray or white",
        "hint_3": "Can bring rain or storms"
    },
    {
        "name": "Daisy",
        "hint_1": "A type of flower",
        "hint_2": "Often yellow or white",
        "hint_3": "Can be found in gardens or fields"
    },
    {
        "name": "Eggshell",
        "hint_1": "A type of container",
        "hint_2": "Protects the egg inside",
        "hint_3": "Can be fragile or delicate"
    },
    {
        "name": "Flowerpot",
        "hint_1": "A type of container",
        "hint_2": "Used for holding plants",
        "hint_3": "Can be made of ceramic or plastic"
    },
    {
        "name": "Giggle",
        "hint_1": "A type of laughter",
        "hint_2": "Often happy or playful",
        "hint_3": "Can be contagious or infectious"
    },
    {
        "name": "Honeybee",
        "hint_1": "A type of insect",
        "hint_2": "Often yellow or black",
        "hint_3": "Can make honey or pollinate flowers"
    },
    {
        "name": "Icecream",
        "hint_1": "A type of dessert",
        "hint_2": "Often cold or sweet",
        "hint_3": "Can be eaten in cones or bowls"
    },
    {
        "name": "Jellyfish",
        "hint_1": "A type of sea creature",
        "hint_2": "Often transparent or gelatinous",
        "hint_3": "Can sting or swim in the ocean"
    },
    {
        "name": "Kitten",
        "hint_1": "A type of young animal",
        "hint_2": "Often cute or playful",
        "hint_3": "Can be a pet or grow into a cat"
    },
    {
        "name": "Lollipop",
        "hint_1": "A type of candy",
        "hint_2": "Often sweet or colorful",
        "hint_3": "Can be eaten on a stick"
    },
    {
        "name": "Mitten",
        "hint_1": "A type of clothing",
        "hint_2": "Worn on the hand",
        "hint_3": "Can be warm or fuzzy"
    },
    {
        "name": "Nutmeg",
        "hint_1": "A type of spice",
        "hint_2": "Often used in baking",
        "hint_3": "Can be ground or whole"
    },
    {
        "name": "Oboe",
        "hint_1": "A type of musical instrument",
        "hint_2": "Often played in orchestras",
        "hint_3": "Can be made of wood or metal"
    },
    {
        "name": "Pajamas",
        "hint_1": "A type of clothing",
        "hint_2": "Worn for sleeping",
        "hint_3": "Can be soft or comfortable"
    },
    {
        "name": "Quilt",
        "hint_1": "A type of blanket",
        "hint_2": "Often made of fabric",
        "hint_3": "Can be warm or decorative"
    },
    {
        "name": "Raccoon",
        "hint_1": "A type of animal",
        "hint_2": "Often found in forests",
        "hint_3": "Can be cute or mischievous"
    },
    {
        "name": "Sandcastle",
        "hint_1": "A type of structure",
        "hint_2": "Built on the beach",
        "hint_3": "Can be made of sand or water"
    },
    {
        "name": "Turtle",
        "hint_1": "A type of animal",
        "hint_2": "Often slow or steady",
        "hint_3": "Can have a shell or swim"
    },
    {
        "name": "Umbrella",
        "hint_1": "A type of accessory",
        "hint_2": "Used for staying dry",
        "hint_3": "Can be compact or large"
    },
    {
    "name": "Abstruse",
    "hint_1": "A type of language or concept",
    "hint_2": "Difficult to understand",
    "hint_3": "Often used in academic or technical contexts"
    },
    {
        "name": "Bubblegum",
        "hint_1": "A type of candy",
        "hint_2": "Chewy and sweet",
        "hint_3": "Often pink or blue"
    },
    {
        "name": "Cathode",
        "hint_1": "A type of electrode",
        "hint_2": "Used in electronic devices",
        "hint_3": "Can be negative or positive"
    },
    {
        "name": "Daffodil",
        "hint_1": "A type of flower",
        "hint_2": "Often yellow or trumpet-shaped",
        "hint_3": "Can be found in gardens or fields"
    },
    {
        "name": "Ephemera",
        "hint_1": "A type of transitory thing",
        "hint_2": "Lasting for a short time",
        "hint_3": "Can be fragile or fleeting"
    },
    {
        "name": "Flamenco",
        "hint_1": "A type of music or dance",
        "hint_2": "Originated in Spain",
        "hint_3": "Can be passionate or energetic"
    },
    {
        "name": "Garrulous",
        "hint_1": "A type of talkative person",
        "hint_2": "Often chatty or loquacious",
        "hint_3": "Can be annoying or entertaining"
    },
    {
        "name": "Hypnosis",
        "hint_1": "A type of trance-like state",
        "hint_2": "Induced by suggestion or relaxation",
        "hint_3": "Can be used for therapy or entertainment"
    },
    {
        "name": "Iguana",
        "hint_1": "A type of lizard",
        "hint_2": "Often green or scaly",
        "hint_3": "Can be found in tropical regions"
    },
    {
        "name": "Jester",
        "hint_1": "A type of court entertainer",
        "hint_2": "Often wears a hat or costume",
        "hint_3": "Can be funny or mischievous"
    }
    #500 words holy shit i did not think it would take this long maybe illl stop here or maybe ill come back for 1k idk im tired.
    
]
#use this to check the len of the array anytime
#print(len(Words)) 


#This function is called when the code executes it gives you da option to start the game n stuff
#in main file REMOVE ALL THE USELESS CODE
#I DONT EVEN KNOW WHY I KEEPT IT HERE IN THE FIRST PLACE

def greet():
    input_check = True #Using this to check for correct input set it to True before using
    
    print(RED+"Guess"+YELLOW+" the"+ CYAN+" word"+ PURPLE+" game"+RESET)
    print("Enter 1 to start game.")
    print("Enter 2 to exit exit.")
    
    while True:
        try: #Prevents ValueError's 
            while input_check == True:
                player_inpt = int(input("> "))
                
                if player_inpt == 1 or player_inpt == 2:
                    #print("The code reached here #1") #for testing
                    input_check = False
                    if player_inpt == 1:
                        start()
                        
                    elif player_inpt == 2:
                        print("Exiting...")
                        
                    break
                
                else:
                    print("Please enter 1 or 2.")
                    continue
            break
        except ValueError:
            print("Please enter 1 or 2.")
    
    # if(player_inpt == 1):
    #     start()
        
    # elif (player_inpt == 2):
    #     print("Exiting...")


#This function is called when the game starts anything that has to do after start goes below
def start():
    
    os.system("cls")
    random_index = random.randint(0,400)
    chosen_word = Words[random_index].get("name")
    chosen_word_len = len(chosen_word)
    tries = 10
    empty_str = ["_"] * chosen_word_len
    fmt_empty_str = ' '.join(empty_str)  
    
    #print(chosen_word_len) #for testing to check the length of the word
    #print(chosen_word)#for testing to see the word
    
    def hint_1():
        next_hint_in = 3
        nonlocal tries
        nonlocal fmt_empty_str
        #print("GUESS THE WORD")  #keep these inside the while loop
        # print("Length: "+str(chosen_word_len))
        #print("_ "*chosen_word_len)
        # empty_str = ["_"] * chosen_word_len
        # fmt_empty_str = ' '.join(empty_str)     #formatted string removes [''] <-- these
        #print("Hint 1: "+str(Words[random_index].get("hint_1")))
        
        while next_hint_in > 0:

            print(UNDERLINE+"GUESS THE WORD"+RESET)
            print("Length: "+CYAN+str(chosen_word_len)+RESET+"  Tries: "+LIME+str(tries)+RESET)
            print(fmt_empty_str)
            print(BOLD+"Hint 1: "+str(Words[random_index].get("hint_1"))+RESET)
            player_input = input("> ")
            player_input = player_input.lower()
            player_input = player_input.capitalize()
           # player_input_len = len(player_input)
           

            if player_input == '':
                os.system("cls")
                print(RED + "Answer cannot be empty"+RESET)
            elif(player_input == chosen_word):
                win_or_loose = True
                gameover(win_or_loose,chosen_word)
                break
            
            elif(player_input != chosen_word):
                #nonlocal tries
                tries -= 1
                next_hint_in -=1
                chance_random_letter = random.randrange(1,101)
                # This thing gives a random letter randomly so its a coin flip everytime u get the wrong answer
                # it fills an empty sell (50% chance to do so) 
                if(chance_random_letter > 50):
                    random_letter_index = random.randrange(0,chosen_word_len)
                    random_letter = chosen_word[random_letter_index]
                    empty_str[random_letter_index] = random_letter
                    fmt_empty_str = ' '.join(empty_str)
                    os.system("cls")
                    print(YELLOW+"The word",player_input,"was not the right word!"+RESET+"\nTry again.\n")
                    
                else:
                    os.system("cls")
                    print(YELLOW+"The word",player_input,"was not the right word!"+RESET+"\nTry again.\n")
                    
        if(next_hint_in == 0):
            hint_2()            
                  
        
    def hint_2():
        next_hint_in = 3
        #print("GUESS THE WORD")  #keep these inside the while loop
        # print("Length: "+str(chosen_word_len))
        #print("_ "*chosen_word_len)
        #formatted string removes [''] <-- these
        #print("Hint 1: "+str(Words[random_index].get("hint_1")))
        
        while next_hint_in > 0:
            nonlocal tries
            nonlocal fmt_empty_str
            print(UNDERLINE+"GUESS THE WORD"+RESET)
            print("Length: "+CYAN+str(chosen_word_len)+RESET+"  Tries: "+LIME+str(tries)+RESET)
            print(fmt_empty_str)
            print(BOLD+"Hint 1: "+str(Words[random_index].get("hint_1"))+RESET)
            print(BOLD+"Hint 2: "+str(Words[random_index].get("hint_2"))+RESET)
            player_input = input("> ")
            player_input = player_input.lower()
            player_input = player_input.capitalize()
           # player_input_len = len(player_input)
           
#I wrote this but i'm not even gonna pretend ive a clue what the fuck is going on here.
            if player_input == '':
                os.system("cls")
                print(RED + "Answer cannot be empty"+RESET)
            elif(player_input == chosen_word):
                win_or_loose = True
                gameover(win_or_loose,chosen_word)
                break
            
            elif(player_input != chosen_word):
                #nonlocal tries
                tries -= 1
                next_hint_in -=1
                chance_random_letter = random.randrange(1,101)
                # This thing gives a random letter randomly so its a coin flip everytime u get the wrong answer
                # it fills an empty sell (50% chance to do so) 
                if(chance_random_letter > 50):
                    random_letter_index = random.randrange(0,chosen_word_len)
                    random_letter = chosen_word[random_letter_index]
                    empty_str[random_letter_index] = random_letter
                    os.system("cls")
                    print(YELLOW+"The word",player_input,"was not the right word!"+RESET+"\nTry again.\n")
                    fmt_empty_str = ' '.join(empty_str)
                    
                    
                else:
                    os.system("cls")
                    print(YELLOW+"The word",player_input,"was not the right word!"+RESET+"\nTry again.\n")
                    
        if(next_hint_in == 0):
            hint_3()            
             
    def hint_3():
        
        nonlocal tries
        nonlocal fmt_empty_str
        
       #formatted string removes [''] <-- these
        #print("Hint 1: "+str(Words[random_index].get("hint_1")))
        
        while tries >  0:

            print(UNDERLINE+"GUESS THE WORD"+RESET)
            print("Length: "+CYAN+str(chosen_word_len)+RESET+"  Tries: "+LIME+str(tries)+RESET)
            print(fmt_empty_str)
            print(BOLD+"Hint 1: "+str(Words[random_index].get("hint_1"))+RESET)
            print(BOLD+"Hint 2: "+str(Words[random_index].get("hint_2"))+RESET)
            player_input = input("> ")
            player_input = player_input.lower()
            player_input = player_input.capitalize()
           # player_input_len = len(player_input)
           
#I wrote this but i'm not even gonna pretend ive a clue what the fuck is going on here.
            if player_input == '':
                os.system("cls")
                print(RED + "Answer cannot be empty"+RESET)
            elif(player_input == chosen_word):
                win_or_loose = True
                gameover(win_or_loose,chosen_word)
                break
            
            elif(player_input != chosen_word):
                #nonlocal tries
                tries -= 1

                chance_random_letter = random.randrange(1,101)
                # This thing gives a random letter randomly so its a coin flip everytime u get the wrong answer
                # it fills an empty sell (50% chance to do so) 
                if(chance_random_letter > 50):
                    random_letter_index = random.randrange(0,chosen_word_len)
                    random_letter = chosen_word[random_letter_index]
                    empty_str[random_letter_index] = random_letter
                    os.system("cls")
                    print(YELLOW+"The word",player_input,"was not the right word!"+RESET+"\nTry again.\n")
                    fmt_empty_str = ' '.join(empty_str)
                    
                    
                else:
                    os.system("cls")
                    print(YELLOW+"The word",player_input,"was not the right word!"+RESET+"\nTry again.\n")
                    
        if(tries == 0):
            win_or_loose = False
            gameover(win_or_loose, chosen_word)
                     

    hint_1()
    # print("GUESS THE WORD")
    # print("Length: "+str(chosen_word_len))
    # print("_ "*chosen_word_len)
    # while(tries > 0):
        
   
    

def gameover(win_or_loose,chosen_word): # This takes a boolean true or false to decide whats its gonna show to the player.
    if win_or_loose == True: # True if they won.
        os.system("cls")
        print(BOLD+"Congrats! You got it right!")
        print("The word was: ",chosen_word+".")
        print("What would you like to do now\n1. To play again.\n2. To exit.\n")
        while True:
            try:
                choice = int(input("> "))
                break
        
            except ValueError:
                print("Please enter the 1 or 2")
                
  
        if (choice == 1):
            start()
            
        elif (choice == 2):
            print("Exiting...")
            
    elif win_or_loose == False: # False if they lost
        print("Sorry! you lost.")
        print("The word was:",chosen_word+".")
        print("What would you like to do now\n1. To play again.\n2. To exit.\n")
        while True:
            try:
                choice = int(input("> "))
                break
        
            except ValueError:
                print("Please enter the 1 or 2")
                
        # This choice thing does not work!
        # will fix later.
        if (choice == 1):
            start()
            
        elif (choice == 2):
            print(choice,"thic code")
            print("Exiting...")
        
    

os.system("cls")
greet() #calls the start function
