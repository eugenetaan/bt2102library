from distutils.util import execute
from tkinter import Y
from venv import create
from connectors import *
import datetime

borrowLimit = 2



############################# FINE


def getFineAmount(memberID):
    query = f"select * from fine where memberID = '{memberID}'"
    result = readQuery(connection, query)
    if result == []:
        return 0
    else:
        return result[0][2]

def addFine(memberID, fineAmount):
    query = "insert into fine (memberID, fineAmount) values ('%s','%d')" %(memberID, fineAmount)
    executeQuery(connection, query)
    if getFineAmount(memberID) == fineAmount:
        return({"status" : "sucess"})
    else:
        return {"status" : "failed"}


def payFine(memberID):
    if getFineAmount(memberID) == 0:
        return {"status" : "failed", "error" : "User has no outstanding fines"}
    
    query = f"delete from fine where memberID = '{memberID}'"
    executeQuery(connection, query)
    if getFineAmount(memberID) == 0:
        return({"status" : "sucess"})
    else:
        return {"status" : "failed"}


#################### MEMBERS

#id must be string
def getMemberDetails(ID = None):
    if ID != None:
        query = f"select * from members where memberID = '{ID}'"
    else:
        query = "select * from members"
    a = readQuery(connection, query)
    return a
    
#print(getMemberDetails())

def createNewMember(memberData):
    memberID = memberData["memberID"]
    name = memberData["memberName"]
    faculty = memberData["faculty"]    
    phone = memberData["phoneNumber"]
    email = memberData["emailAddress"]
    query = "INSERT INTO members (memberID, memberName, faculty, phoneNumber, emailAddress) VALUES ('%s','%s','%s','%d','%s')" %(memberID,name,faculty,phone,email)
    executeQuery(connection, query)
    if getMemberDetails(memberID) != []:
        return({"status" : "sucess"})
    else:
        return {"status" : "failed"}
    

newMember = {
    "memberID" : "A1234",
    "memberName" : "Maxim",
    "faculty" : "Computing",
    "phoneNumber" : 12345678,
    "emailAddress" : "1234@gmail.com"
}

#print(createNewMember(newMember))

def updateMemberDetails(memberData):
    memberID = memberData["memberID"]
    name = memberData["memberName"]
    faculty = memberData["faculty"]    
    phone = memberData["phoneNumber"]
    email = memberData["emailAddress"]

    if getMemberDetails(memberID) == []:
        return {"status" : "failed", "error" : "member not found"}
    
    query = "update members set memberName = '%s', faculty = '%s', phoneNumber = '%d', emailAddress = '%s' where memberID = '%s'" %(name,faculty,phone,email,memberID)

    executeQuery(connection, query)

newMemberUpdated = {
    "memberID" : "A1234",
    "memberName" : "Maxim",
    "faculty" : "Computing",
    "phoneNumber" : 12345678,
    "emailAddress" : "test@gmail.com"
}    

#print(getMemberDetails("A1234"))
#print(updateMemberDetails(newMemberUpdated))
#print(getMemberDetails("A1234"))     


def deleteMember(memberID):
    if getMemberDetails(memberID) == []:
        return {"status" : "failed", "error" : "member not found"}
    elif getFineAmount(memberID) != 0:
        return {"status" : "failed", "error" : "Member has outstanding fines"}   


    query = f"delete from members where memberID = '{memberID}'"
    executeQuery(connection, query)
    if getMemberDetails(memberID) == []:
        return({"status" : "sucess"})
    else:
        return {"status" : "failed"}
    
#print(deleteMember("A1234"))
    


######################### BOOKS
#
def getBookDetails(AN=None):
    if AN != None:
        query = f"select * from books where bookAN = '{AN}'"
    else:
        query = "select * from books"
    a = readQuery(connection, query)
    return a

#print(getBookDetails("A01"))

def addBook(bookDetails):
    bookAN = bookDetails["bookAN"]
    title = bookDetails["title"]
    ISBN = bookDetails["ISBN"]
    publisher = bookDetails["publisher"]
    year = bookDetails["publicationYear"]
    query = "INSERT INTO books (bookAN, title, ISBN, publisher, publicationYear) VALUES ('%s','%s','%d','%s','%s')" %(bookAN, title, ISBN, publisher, year)
    executeQuery(connection, query)
    if getBookDetails(bookAN) != []:
        return({"status" : "sucess"})
    else:
        return {"status" : "failed"}
    
newBook = {
    "bookAN" : "A999",
    "title" : "1",
    "ISBN" : 23,
    "publisher" : "Test House",
    "publicationYear" : "2022",
}

#print(addBook(newBook))

def deleteBook(AN):
    if getBookDetails(AN) == []:
        return {"status" : "failed", "error" : "book not found"}
    query = f"delete from books where bookAN = '{AN}'"
    executeQuery(connection, query)
    if getBookDetails(AN) == []:
        return({"status" : "sucess"})
    else:
        return {"status" : "failed"}

#print(deleteBook("A999"))


#def bookSearch(searchTerm)



############### RESERVATION

def getReservationDetailsByBook(bookAN):
    query = f"select * from reservation where bookAN = '{bookAN}'"
    result = readQuery(connection, query)
    return result

def getReservationDetailsByMember(memberID):
    query = f"select * from reservation where reservingMemberID = '{memberID}'"
    result = readQuery(connection, query)
    return result   

def getReservationDetails(bookAN, memberID):
    query = f"select * from reservation where (bookAN, reservingMemberID) = ('{bookAN}', '{memberID}')"
    result = readQuery(connection, query)
    return result           

def newReservation(bookAN, memberID, reserveDate):

    query = "INSERT INTO reservation (bookAN, reservingMemberID, reservedDate) values ('%s', '%s', '%s')" %(bookAN, memberID, reserveDate)
    executeQuery(connection, query)
    if getReservationDetails(bookAN,memberID) != []:
        return({"status" : "sucess"})
    else:
        return {"status" : "failed"}    

# print(newReservation("A01", "A301C", "2017-06-15"))
# print(newReservation("A01", "A201B", "2017-06-15"))

#use strftime to format date
print(getReservationDetailsByBook("A01")[0][2].strftime("%Y-%m-%d"))

def removeReservation(bookAN, memberID):

    if getReservationDetails(bookAN,memberID) == []:
        return {"status" : "failed", "error" : "book reservation by member not found"}

    query = f"delete from reservation where (bookAN, reservingMemberID) = ('{bookAN}', '{memberID}')"
    executeQuery(connection, query)
    if getReservationDetails(bookAN,memberID) == []:
        return {"status" : "sucess"}
    else:
        return {"status" : "failed"}

#print(removeReservation("A01", "A301C"))
    

######################### Borrowed

def checkIfBookIsBorrowed(bookAN):
    query = f"select * from borrowed where bookAN = '{bookAN}'"
    result = readQuery(connection, query)
    if result == []:
        return False
    else:
        return True
    
def checkMemberBorrowed(memberID):
    query = f"select count(bookAN) from borrowed where memberID = {memberID}"
    count = readQuery(connection, query)
    return count

def borrowBook(bookAN, memberID):

    if checkIfBookIsBorrowed(bookAN):
        return {"status" : "failed", "error" : "book is not available"}
    elif getReservationDetailsByBook(bookAN) != []:
        return {"status" : "failed", "error" : "book is reserved"}
    elif checkMemberBorrowed(memberID) >= borrowLimit:
        return {"status" : "failed", "error" : "you have reached the maximum number of books borrowed"}
    elif getFineAmount(memberID) > 0:
        return {"status" : "failed", "error" : "you have an outstanding fine"}
    
    currentBooksBorrowed = checkMemberBorrowed(memberID)

    borrowDate = datetime.datetime.now()
    borrowDateString = borrowDate.strftime("%Y-%m-%d")
    dueDate = borrowDate + datetime.timedelta(days=14)
    dueDateString = dueDate.strftime("%Y-%m-%d")
    query = "insert into borrowed (bookAN, memberID, borrowedDate, dueDate) values ('%s', '%s', '%s', '%s')" %(bookAN, memberID, borrowDateString, dueDateString)
    executeQuery(connection, query)

    if checkIfBookIsBorrowed(bookAN) and checkMemberBorrowed(memberID) == currentBooksBorrowed + 1:
        return {"status" : "sucess"}
    else:
        return {"status" : "failed"}
    

def returnBook(bookAN, memberID):
    
    returnDate = datetime.datetime.now()
    dueDate = readQuery(connection, f"select dueDate from borrowed where bookAN = '{bookAN}'")[0][0]
    
    if returnDate > dueDate:
        delta = returnDate - dueDate
        daysDifference = delta.days
        newFineAmount = daysDifference + getFineAmount(memberID)
        addFine(memberID, newFineAmount)
    
    
    query = f"delete from borrowed where bookAN = '{bookAN}'"
    executeQuery(connection, query)
    if not checkIfBookIsBorrowed(bookAN):
        return {"status" : "sucess"}
    else:
        return {"status" : "failed"}





    































    



