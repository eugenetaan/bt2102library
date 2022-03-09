Create Database library;

-- if tables alrdy exists then drop
DROP TABLE IF EXISTS fine;
DROP TABLE IF EXISTS borrowed;
DROP TABLE IF EXISTS returned;
DROP TABLE IF EXISTS reservation;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS members;

REATE TABLE members (
  memberID varchar(10) NOT NULL UNIQUE,
  memberName varchar(50) NOT NULL,
  faculty varchar(50) NOT NULL,
  phoneNumber bigint UNSIGNED NOT NULL,
  emailAddress varchar(50) NOT NULL,
  PRIMARY KEY (memberID) 
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE books (
  bookAN varchar(10) NOT NULL UNIQUE,
  title varchar(80) NOT NULL,
  authors varchar(150) NOT NULL,
  ISBN bigint UNSIGNED NOT NULL,
  publisher varchar(50) NOT NULL,
  publicationYear year NOT NULL,
  PRIMARY KEY (bookAN)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE reservation (
  bookAN varchar(10) NOT NULL,
  reservingMemberID varchar(10) NOT NULL,
  reservedDate date NOT NULL,
  PRIMARY KEY (bookAN, reservingMemberID),
  FOREIGN KEY (reservingMemberID) REFERENCES members(memberID) ON DELETE CASCADE
  FOREIGN KEY (bookAN) REFERENCES books(bookAN) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE borrowed (
  bookAN varchar(10) NOT NULL,
  memberID varchar(10) NOT NULL,
  borrowedDate date NOT NULL,
  dueDate date NOT NULL,
  PRIMARY KEY (bookAN),
  FOREIGN KEY (memberID) REFERENCES members(memberID) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE fine (
  memberID varchar(10) NOT NULL,
  paymentDate date,
  paymentAmount decimal NOT NULL,
  PRIMARY KEY (memberID),
  FOREIGN KEY (memberID) REFERENCES members(memberID) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



