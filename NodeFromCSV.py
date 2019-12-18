import pandas as pd
from PersonNode import *
from CarNode import *
from PhoneNumberNode import *
from HouseNode import *
from BankAccount import *
########################################################################################################################

# CARS
df_cars = pd.read_csv('data/cars.csv')
df_cars.loc[-1] = list(df_cars.columns)
df_cars.index = df_cars.index + 1
df_cars = df_cars.sort_index()
df_cars = df_cars[[df_cars.columns[0], df_cars.columns[1], df_cars.columns[2], df_cars.columns[3]]]
carsDictionary = {}
for i in range(len(df_cars)):
    car_tmp = CarNode(df_cars.iloc[i][0], df_cars.iloc[i][1], df_cars.iloc[i][2], df_cars.iloc[i][3])
    carsDictionary[df_cars.iloc[i][0]] = car_tmp

########################################################################################################################

# Houses
df_houses = pd.read_csv('data/homes.csv')
df_houses.loc[-1] = list(df_houses.columns)
df_houses.index = df_houses.index + 1
df_houses = df_houses.sort_index()
df_houses = df_houses[[df_houses.columns[2], df_houses.columns[1], df_houses.columns[0], df_houses.columns[3], df_houses.columns[4]]]
houseDictionary = {}
for i in range(len(df_houses)):
    house_tmp = HouseNode(df_houses.iloc[i][0], df_houses.iloc[i][2], df_houses.iloc[i][1], df_houses.iloc[i][3], df_houses.iloc[i][4])
    houseDictionary[df_houses.iloc[i][0]] = house_tmp

########################################################################################################################

# BankAccount
df_bankAccounts = pd.read_csv('data/accounts.csv')
df_bankAccounts.loc[-1] = list(df_bankAccounts.columns)
df_bankAccounts.index = df_bankAccounts.index + 1
df_bankAccounts = df_bankAccounts.sort_index()
df_bankAccounts = df_bankAccounts[[df_bankAccounts.columns[2], df_bankAccounts.columns[1], df_bankAccounts.columns[0], df_bankAccounts.columns[3]]]
bankDictionary = {}
for i in range(len(df_bankAccounts)):
    bank_tmp = BankAccount(df_bankAccounts.iloc[i][0], df_bankAccounts.iloc[i][2], df_bankAccounts.iloc[i][1], df_bankAccounts.iloc[i][3])
    bankDictionary[df_bankAccounts.iloc[i][0]] = bank_tmp

########################################################################################################################

# Persons
df_persons = pd.read_csv('data/people.csv')
df_persons.loc[-1] = list(df_persons.columns)
df_persons.index = df_persons.index + 1
df_persons = df_persons.sort_index()
df_persons = df_persons[[df_persons.columns[2], df_persons.columns[1], df_persons.columns[0], df_persons.columns[3], df_persons.columns[4], df_persons.columns[5], df_persons.columns[6]]]
personDictionary = {}
for i in range(len(df_persons)):
    person_tmp = PersonNode(df_persons.iloc[i][0], df_persons.iloc[i][1], df_persons.iloc[i][2], df_persons.iloc[i][3], df_persons.iloc[i][4], df_persons.iloc[i][5])
    personDictionary[df_persons.iloc[i][0]] = person_tmp

########################################################################################################################

# PhoneNumbers
df_phoneNumbers = pd.read_csv('data/phones.csv')
df_phoneNumbers.loc[-1] = list(df_phoneNumbers.columns)
df_phoneNumbers.index = df_phoneNumbers.index + 1
df_phoneNumbers = df_phoneNumbers.sort_index()
df_phoneNumbers = df_phoneNumbers[[df_phoneNumbers.columns[1], df_phoneNumbers.columns[0], df_phoneNumbers.columns[2]]]
phonesDictionary = {}
for i in range(len(df_phoneNumbers)):
    phone_tmp = PhoneNumberNode(df_phoneNumbers.iloc[i][0], df_phoneNumbers.iloc[i][1], df_phoneNumbers.iloc[i][2])
    phonesDictionary[df_phoneNumbers.iloc[i][0]] = phone_tmp


