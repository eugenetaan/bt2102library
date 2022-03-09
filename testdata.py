from matplotlib.pyplot import title
from connectors import *
import pandas

def insertLibBooksData():
    df = pandas.read_csv('/Users/eugenetan/Desktop/BT2102Proj/LibBooks.csv')
    #df.drop(df.columns[[2,3,4]], axis=1, inplace=True)
    df.fillna(0, inplace= True) 
    for index,row in df.iterrows():
        bookAN = row["Accession Number"]
        title = row["Title"]
        ISBN = row["ISBN"]
        publisher = row["Publisher"]
        author1 = row["Authors"]
        author2 = row[3]
        author3 = row[4] 
        authors = author1
        if author2 != 0 and author3 == 0:
            authors = author1 + ", " + author2
        elif author2 != 0 and author3 != 0: 
            authors = author1 + ", " + author2 + ", " + author3
        year = row["Year"]
        query = "INSERT INTO books (bookAN, title, authors, ISBN, publisher, publicationYear) VALUES ('%s','%s','%s','%d','%s','%s')" %(bookAN, title, authors, ISBN, publisher, year)
        executeQuery(connection, query)


def insertLibMemData():
    df = pandas.read_csv('/Users/eugenetan/Desktop/BT2102Proj/LibMems.csv')
    for index,row in df.iterrows():
        memberID = row["2pememberid"]
        name = row["name"]
        faculty = row["faculty"]
        phone = row["phone number"]
        email = row["email address"]
        query = "INSERT INTO members (memberID, memberName, faculty, phoneNumber, emailAddress) VALUES ('%s','%s','%s','%d','%s')" %(memberID,name,faculty,phone,email)
        executeQuery(connection, query)








# def insertLibBooksData():
#     df = pandas.read_csv('/Users/eugenetan/Desktop/BT2102Proj/LibBooks.csv')
#     #df.drop(df.columns[[2,3,4]], axis=1, inplace=True)
#     df.fillna(0, inplace= True) 
#     for index,row in df.iterrows():
#         # insert into books
#         bookAN = row["Accession Number"]
#         title = row["Title"]
#         ISBN = row["ISBN"]
#         publisher = row["Publisher"]
#         year = row["Year"]

#         query = "INSERT INTO books (bookAN, title, ISBN, publisher, publicationYear) VALUES ('%s','%s','%d','%s','%s')" %(bookAN, title, ISBN, publisher, year)
#         executeQuery(connection, query)

#         # insert into authors
#         for i in range(2,5):
#             if row[i] == 0:
#                 continue

#             # get authorID if already in authors table else create new authorID
#             author = row[i]
#             query = "select authorID from authors where authorName = '%s'" %(author)
#             result = readQuery(connection, query)
#             if result == []:
#                 idNumber = readQuery(connection, "select count(authorID) from authors") + 1
#                 authorID = f"N{idNumber}"
#             else:
#                 authorID = result[0][0]

#             query = "insert into authors (authorID, authorName, bookAN)"
            