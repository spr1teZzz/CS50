import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}  #names = {name,person_ids}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {} #

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    加载数据到集合中
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    根据source和target person_id 来查找最短路径并返回路径list  没有返回None
    [(1,2),(3,4)]表示 2与源id 主演电影1 , 4和2主演电影3,4是目标id,有多条最小路径任意返回一条
    """
    #如果需要找到最短路径，则需要使用BFS 广度优先算法
    #
    if source == target:
        return []
    #最短路径
    path = list()
    #记录当前节点的上一个节点
    parent = dict()
    #1.找到与源id一起主演的id
    neighbors = neighbors_for_person(source)
    
    neighbors_queue = QueueFrontier()
    visited = [source]
    for neighbor in neighbors:
        #将neighbor 添加至 队列中
        if neighbor[-1] == source:
            #不添加source id
            continue
        #将neighbor中的id放入队列中
        neighbors_queue.add((neighbor[0],neighbor[-1]))
        #添加父节点
        parent[neighbor[-1]] = (0,source)


    #遍历队列中的id
    while neighbors_queue.empty() is False:
        #取出id 
        n = neighbors_queue.remove()
        movie_id = n[0]
        id = n[1]
        if id not in visited:
            if id == target:
                #找到target
                path.append((movie_id,target))
                node = target
                while parent[node][-1] != source:
                    father = parent[node]
                    path.append(father)
                    node = father[-1]
                path.reverse()#反转路径
                return path
            else:
                #当前节点不为target，则获取相邻id添加至队列中
                neighbors = neighbors_for_person(id)
                for neighbor in neighbors:
                    # #将neighbor 添加至 队列中   
                    # if neighbor[-1] == id:
                    #     #不添加source id
                    #     continue
                    #将neighbor中的id放入队列中
                    neighbors_queue.add((neighbor[0],neighbor[-1]))
                    #添加父节点
                    if neighbor[-1] not in parent:
                        parent[neighbor[-1]] = (movie_id,id)
        visited.append(id)
    return None


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    根据name 返回 person_id 若有相同的name 则根据个人信息进行选择
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    #返回所有由person_id主演的电影的所有主演 包含person_id
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
