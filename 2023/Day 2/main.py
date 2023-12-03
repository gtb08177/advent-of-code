def is_possible(bag_data):
    return (bag_data['red'] >= 0 and bag_data['blue'] >= 0 and bag_data['green'] >= 0)

input = open(r"input.txt","r")
bag_start = {"red":12,"green":13,"blue":14}
running_sum = 0

lines = input.readlines()
for line in lines: 
    
    game_id_and_reveals = line.split(": ") # e.g. ['Game 1','3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green']
    game_id = int(game_id_and_reveals[0].split(" ")[1]) # e.g. 1
    game_all_reveals = game_id_and_reveals[1].split('; ') # ['3 blue, 4 red','1 red, 2 green','6 blue; 2 green']
    game_is_possible = True
    
    for reveal in game_all_reveals:
        arr_colour_and_count = reveal.split(", ") # ['3 blue', '4 red']
        running_bag_data = bag_start.copy()

        for entry in arr_colour_and_count:
            kv_map = entry.split(" ")
            colour = kv_map[1].strip()
            num_of_colour = int(kv_map[0])
            running_bag_data[colour] = running_bag_data[colour]-num_of_colour

        # scope issue here
        if not is_possible(running_bag_data):
            game_is_possible = False
    
    if game_is_possible:
        running_sum = running_sum + game_id

print(running_sum)
