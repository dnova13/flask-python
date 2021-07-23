import csv

def save_to_file(jobs, word) :
    file = open(f"research_{word}_jobs.csv", mode="w")
    ## mode 파일 형식을 정함. 
    # mode="w" : 쓰기 형식

    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])

    for job in jobs :
        # print(job["title"])
        
        writer.writerow(list(job.values())) 
        # {1:a,2:b,3:c}  딕셔너리 구성으로 저장햇고, value()를 통해 값만 가져옴.
        # list(ex) : ex 를 리스트 형식으로 변환

    return