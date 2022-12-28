
def tests(filename, ):
    database_tmp = []
    database = []
    print(filename)
    with open(filename, 'r', encoding="utf-8") as file:
        for row in file:
            line = row.strip() # deleting \n
            database_tmp.append(line) # appending 

                
    question_step = 6 # for every question


    for i in range(0, len(database_tmp), question_step):
        question_massive = []
        question_massive.append(database_tmp[i])
        question_massive.append(database_tmp[i+1])
        question_massive.append(database_tmp[i+2])
        question_massive.append(database_tmp[i+3])
        question_massive.append(database_tmp[i+4])
        database.append(question_massive)

    return database
