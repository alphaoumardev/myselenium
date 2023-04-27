import csv
import time

from selenium import webdriver

tags = ['Arcade', 'Board', 'Card', 'Beauty', 'Beautiful', 'Makeup', 'Skincare', 'hair', 'vacation', 'Hairstyle',
        'Manicure', 'Fashion', 'Clothing', 'Jewellery', 'Shoes', 'Bags', 'Hats', 'clothing', 'vaping',
        'Consumer+Electronic', 'Consumer', 'Smartphone', 'Camera', 'Computer', 'Game+console', 'Headset',
        'Television', 'smart', 'Smart+Watch', 'Smart+Electronics', 'Power+Banks', 'Vape', 'Lifestyle', 'Travel',
        'Food', 'Fitness', 'Health', 'Sports', 'Pets', 'Kids', 'Toy', 'DIY', 'Outdoor+Sports', 'Gardening',
        'Home+Garden', 'Kitchen,+Dining+Bar', 'Furniture', 'Vehicles', 'Shopping', 'Baby+Care', 'Music',
        'Rock+music', 'Classical+music', 'Electronic+music', 'Hip+Hop', 'Pop+music', 'Entertainment', 'Movie',
        'Cartoon', 'Humor', 'TV+shows', 'Documentary', 'Unboxing', 'ASM', 'Vlog', 'Science+Technology',
        'Education', 'Finance', 'Cooking', 'Baking', 'Grilling', 'Veganism', 'Vegetarianism', 'Fitness',
        'Bodybuilding', 'Weightlifting', 'Running', 'Cycling', 'Yoga', 'Meditation', 'Mindfulness', 'Travel',
        'Adventure', 'Backpacking', 'Hiking', 'Camping', 'Fishing', 'Hunting', 'Gardening', 'Interior+design',
        'Fashion', 'Makeup', 'Beauty', 'Haircare', 'Skincare', 'Health', 'Nutrition', 'Wellness',
        'Self-improvement', 'Self-help', 'Personal+development', 'Business', 'Entrepreneurship', 'Investing',
        'Finance', 'Real+estate', 'Technology', 'Science', 'Education', 'Learning', 'Language+learning', 'Music',
        'Art', 'Photography', 'Videography', 'Gaming', 'Exports', 'Comedy', 'Sketch+comedy', 'Stand-up+comedy',
        'Pranks', 'Reviews', 'Reaction+videos', 'Vlogs', 'vlog', 'Family+vlogs', 'Parenting', 'Marriage',
        'Relationships', 'furniture', 'Social+justice', 'Environmentalism', 'Sustainability',
        'Conspiracy+theories', 'True+crime', 'History', 'Mythology', 'Philosophy', 'Spirituality', 'Horoscopes',
        'Astrology', 'Tarot', 'Fiction+writing', 'Poetry', 'Non-fiction+writing', 'Journalism', 'Sports',
        'Football', 'Basketball', 'Baseball', 'Soccer', 'Tennis', 'Golf', 'Surfing', 'Skateboarding',
        'Snowboarding', 'Skiing', 'Motorsports', 'Cars', 'Motorcycles', 'Boating', 'Aviation', 'DIY',
        'Home+improvement', 'Woodworking', 'Knitting', 'Crochet', 'Sewing', 'Crafts', 'Calligraphy',
        'Bullet+journaling', 'Stationery', 'Productivity', 'Time+management', 'Fashion+design', 'fashion',
        'Graphic+design', 'Web+design', 'Coding', 'code', 'Game+development', 'Mobile+app+development',
        'Cybersecurity', 'Data+science', 'Robotics', 'Virtual+reality', 'Augmented+reality', 'Blockchain',
        'Cryptocurrency', 'Stock+market', 'Options+trading', 'Forex+trading', 'Travel+hacking', 'Budget+travel',
        'Luxury+travel', 'Food+reviews', 'Restaurant+reviews', 'Wine+tasting', 'Beer+Brewing', 'Whiskey+tasting',
        'Rum+tasting', 'Tequila+tasting', 'Cocktail+making', 'Bartending', 'Pub+culture', 'Live+music',
        'Concerts', 'Festivals', 'Theatre', 'Musicals', 'Opera', 'Ballet', 'Dance', 'Circus', 'Magic',
        'Paranormal', 'Cryptozoology', 'Urban+legends', 'Ghost+stories', 'Haunted+places', 'Aliens', 'UFOs',
        'Mythical+creatures', 'Mythological+creatures', 'Cryptic', 'Unsolved+mysteries', 'True+stories',
        'Baking', 'Cooking', 'Comedy', 'Sketch+Comedy', 'Stand-up+comedy', 'Travel+vlog', 'Adventure+travel',
        'Food+reviews', 'Makeup+tutorials', 'Hair+tutorials', 'DIY+home+decor', 'decor', 'home+decor',
        'Product+reviews', 'Gaming+news', 'Horror+movies', 'Science+fiction+movies', 'Action+movies',
        'Romance+movies', 'Crime+dramas', 'Fantasy+movies', 'Medical+dramas', 'Legal+dramas', 'Political+dramas',
        'Family+dramas', 'Cooking+competitions', 'Gardening+tips', 'Home+Renovation', 'Car+reviews',
        'Sports+news', 'Sports+highlights', 'Fitness+workouts', 'Yoga+tutorials', 'Meditation+guides',
        'Motivational+speeches', 'Fashion+trends', 'Fashion+design', 'Jewellery+making', 'Music+videos',
        'Music+reviews', 'Music+documentaries', 'Music+festivals', 'Live+performances', 'Dance+tutorials',
        'Photography+tutorials', 'Photo+editing+tips', 'Art+tutorials', 'Art+history', 'Nature+documentaries',
        'Animal+documentaries', 'Environmental+issues', 'Political+commentary', 'Social+commentary',
        'News+Analysis', 'Historical+documentaries', 'Ancient+history', 'Modern+history', 'Spiritual+teachings',
        'Religious+teachings', 'Cooking+with+cannabis', 'Stand-up+comedy+specials', 'Celebrity+interviews',
        'Celebrity+gossip', 'Conspiracy+theories', 'Action+game', 'Action-adventure', 'Casual+game', 'Music+game',
        'Puzzle+game', 'Racing+game', 'Role-playing+game', 'Simulation+game', 'Sports+game', 'Strategy+game',
        'UFO+sightings', 'Paranormal+investigations', 'Ghost+stories', 'Haunted+places', 'Luxury+lifestyle',
        'Thrift+store+finds', 'Reselling+tips', 'Personal+Finance', 'Entrepreneurship', 'Technology+news',
        'Technology+reviews', 'Space+exploration', 'Astronomy', 'Science+experiments', 'Robotics',
        'Artificial+intelligence', 'Virtual+reality', '3D+printing', 'Life+hacks', 'Productivity+tips',
        'Mindfulness+practices', 'Mental+health+advice', 'Relationship+Advice', 'Parenting+tips', 'Baby+care',
        'Pet+care', 'Travel+tips', 'Budget+travel', 'Luxury+travel', 'Family+travel', 'Road+trips',
        'Train+travel', 'Cruise+travel', 'RV+travel', 'Backpacking', 'Language+learning', 'Cultural+exchange',
        'DIY', 'Fitness', 'Comedy', 'Technology', 'Cooking', 'Travel', 'Science', 'Beauty', 'Gaming', 'History',
        'News', 'Education', 'Music', 'Animals', 'Sports', 'Fashion', 'Art', 'Business', 'Film', 'Kids',
        'Parenting', 'Health', 'Lifestyle', 'Outdoors', 'Food', 'Cars', 'Photography', 'Crafts', 'Gardening',
        'Books', 'Language+learning', 'Finance', 'Politics', 'Fitness+challenges', 'Minimalism', 'Meditation',
        'Self-improvement', 'True+crime', 'Conspiracy+theories', 'Celebrities', 'Interviews', 'Product+reviews',
        'Gaming', 'Movie+reviews', 'Trailer+reactions', 'ASMR', 'Unboxing', 'Hauls', 'Travel+vlogs',
        'Adventure', 'Documentaries', 'Magic', 'Poetry', 'Stand-up+comedy', 'Reaction+videos', 'Travel+tips',
        'Tech+reviews', 'Career+advice', 'Personal+Finance', 'Stock+market+investing', 'Cryptocurrency',
        'Cryptocurrency+trading', 'Real+estate+investing', 'Home+Renovation', 'Interior+design',
        'Fashion+styling', 'Makeup+tutorials', 'Skincare', 'Haircare', 'Productivity', 'Time+management',
        'Bullet+journaling', 'Productivity+hacks', 'Parenting+hacks', 'Home+organization', 'Minimalist+living',
        'Environment', 'Climate+change', 'Wildlife+conservation', 'Astronomy', 'Psychology', 'Neuroscience',
        'Motivation', 'Mindfulness', 'Inspirational+speeches', 'Mental+health', 'Social+justice',
        'Diversity+and+inclusion', 'Feminism', 'Veganism', 'Vegetarianism', 'Meatless+recipes',
        'Low-carb+recipes', 'Gluten-free+recipes', 'Paleo+recipes', 'Vegan+recipes', 'Vegetarian+recipes',
        'Fast+food+challenges', 'Restaurant+reviews']

driver = webdriver.Chrome()

# Open a CSV file to store the results
with open('category.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Tag', 'Channel_username'])

    # Loop through each tag
    for tag in tags:
        # Load the search results page for the current tag
        driver.get(f'https://www.youtube.com/results?search_query={tag}&sp=EgIQAg%253D%253D')
        time.sleep(2)  # Wait for the page to load

        # Scroll down the page to load more channels
        last_height = driver.execute_script('return document.documentElement.scrollHeight')
        while True:
            driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
            time.sleep(2)
            new_height = driver.execute_script('return document.documentElement.scrollHeight')
            if new_height == last_height:
                break
            last_height = new_height

        # Extract the channel names and store them in the CSV file
        channel_elements = driver.find_elements('xpath', '//*[@id="subscribers"]')

        channel_names = [elem.text for elem in channel_elements]
        for channel_name in channel_names:
            writer.writerow([tag, channel_name])
