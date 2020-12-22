# create data
'''
mutation firstmutation{
  addPerson(Name:"gagan",Email:"gagan@gmail.com",Phone:"8767",Address:"skds"){
    person{
      Name
      Address
      Phone
      Email
    }
  }
}
'''

# read data
'''
{
  allPerson{
   id
    Name
    Phone
    Email
    Address
  }
}
'''

# update data
'''
mutation firstmutation{
  updatePerson(id:1,Name:"Ganguli",Email:"ganguli@gmail.com",Phone:"657667",Address:"anupshahr"){
    person{
      id
      Name
      Address
      Phone
      Email
    }
  }
}
'''


# delete data
'''
mutation firstmutation{
  deletePerson(id:3){
    person{
      id
    }
  }
}
'''
