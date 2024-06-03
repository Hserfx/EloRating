def estimated_score(players, player):
    est_score = 0

    for p in players:
        if p.userId == player.userId:
            continue
        D = 400
        prob = (1/(1+10**((p.eloPoints-player.eloPoints)/D)))/(len(players)*(len(players)-1)/2)
        est_score += prob


    return est_score




def new_score(player, est_score, N):
    Sp = (N-player.place)/(N*(N-1)/2)
    rating = player.eloPoints + 60*(N-1)*(Sp - est_score)
    return rating




def update_scores(players):
    updated_elo = []

    for player in players:
        est_score = estimated_score(players, player)
        new_elo = round(new_score(player, est_score, len(players)))
        updated_elo.append(new_elo)
    for player, elo in zip(players, updated_elo):
        player.eloPoints = elo

    return players





