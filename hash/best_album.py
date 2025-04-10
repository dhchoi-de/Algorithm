def solution(genres, plays):
    # 속한 노래가 많이 재생된 장르를 찾기위한 장르별 더하고 정렬하기
    per_count = {genre:0 for genre in set(genres)}
    for idx in range(len(genres)):
        per_count[genres[idx]] += plays[idx]
    per_count = dict(sorted(per_count.items(), key=lambda x: x[1], reverse=True)) 
    
    # 장르별 플레이 횟수로 정렬하기
    genres_playes = {f"{idx}_{genres[idx]}":plays[idx] for idx in range(len(genres))}
    genres_playes = dict(sorted(genres_playes.items(), key=lambda x: x[1], reverse=True))
    
    return genres_playes


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop", "hiphop"]
    plays = [500, 600, 150, 800, 2500, 4500]
    answer = solution(genres, plays)
    