
number_of_games = int(input())
games = []
results = {}
table = []

for i in range(number_of_games):
    games.append(input())

for element in games:
    game = element.split(";")
    if int(game[1]) == int(game[3]):
        temp_result = results.get(game[0])
        if temp_result is None:
            temp_score = [0, 0, 0, 0, 0]
            results[game[0]] = temp_score
        results[game[0]][0] += 1
        results[game[0]][1] += 0
        results[game[0]][2] += 1
        results[game[0]][3] += 0
        results[game[0]][4] += 1

        temp_result = results.get(game[2])
        if temp_result is None:
            temp_score = [0, 0, 0, 0, 0]
            results[game[2]] = temp_score
        results[game[2]][0] += 1
        results[game[2]][1] += 0
        results[game[2]][2] += 1
        results[game[2]][3] += 0
        results[game[2]][4] += 1

    elif int(game[1]) > int(game[3]):
        temp_result = results.get(game[0])
        if temp_result is None:
            temp_score = [0, 0, 0, 0, 0]
            results[game[0]] = temp_score
        results[game[0]][0] += 1
        results[game[0]][1] += 1
        results[game[0]][2] += 0
        results[game[0]][3] += 0
        results[game[0]][4] += 3

        temp_result = results.get(game[2])
        if temp_result is None:
            temp_score = [0, 0, 0, 0, 0]
            results[game[2]] = temp_score
        results[game[2]][0] += 1
        results[game[2]][1] += 0
        results[game[2]][2] += 0
        results[game[2]][3] += 1
        results[game[2]][4] += 0

    elif int(game[1]) < int(game[3]):

        temp_result = results.get(game[0])
        if temp_result is None:
            temp_score = [0, 0, 0, 0, 0]
            results[game[0]] = temp_score
        results[game[0]][0] += 1
        results[game[0]][1] += 0
        results[game[0]][2] += 0
        results[game[0]][3] += 1
        results[game[0]][4] += 0

        temp_result = results.get(game[2])
        if temp_result is None:
            temp_score = [0, 0, 0, 0, 0]
            results[game[2]] = temp_score
        results[game[2]][0] += 1
        results[game[2]][1] += 1
        results[game[2]][2] += 0
        results[game[2]][3] += 0
        results[game[2]][4] += 3

for element in results:
    print(element + ":", results[element][0], results[element][1],
          results[element][2], results[element][3], results[element][4])
