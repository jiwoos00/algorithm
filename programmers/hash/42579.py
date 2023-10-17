def solution(genres, plays):
    songs_dict = {} # 장르별 각 노래의 (재생횟수, 인덱스)
    genre_total_plays = {} # 장르별 재생 횟수

    for idx, genre in enumerate(genres):
        if genre not in songs_dict:
            songs_dict[genre] = []
        songs_dict[genre].append((plays[idx], idx))
        
        if genre not in genre_total_plays:
            genre_total_plays[genre] = 0
        genre_total_plays[genre] += plays[idx]
        
    
    # 장르별 재생 횟수 합계를 기준으로 정렬
    sorted_genres = sorted(genre_total_plays.keys(), key = lambda genre: -genre_total_plays[genre])

    
    result = []
    for genre in sorted_genres:
        # 각 장르별 노래들을 재생 횟수와 인덱스를 기준으로 정렬
        songs_list = sorted(songs_dict[genre], key = lambda song: (-song[0], song[1]))
        
        # 노래 중에서 최대 2개까지 선택
        for _, idx in songs_list[:2]:
            result.append(idx)
    return result