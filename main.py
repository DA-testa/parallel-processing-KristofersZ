# 211RDB475 Kristofers Zellītis 9.grupa

def parallel_processing(n, m, data):
    output = []
    threads=[(i,0) for i in range(n)]
    for i in range(m):
        t = data[i]
        threads.sort()
        time, thread = threads[1]
        output.append((thread, time))
        threads[thread] = (thread, time + t)
        
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int,input().split))
    result = parallel_processing(n, m, data)
 
    for thread, time in result:
        print(thread, time)

if __name__ == "__main__":
    main()
