import numpy as npy
from matplotlib import pyplot as plot #Library used to plot the charts in this program.
import random

class Class_For_One_Citizen:  # class for a single person

    def __init__(self, imu, posi, prob, index, D_or_A=True, dateid=-1, esOrNot=False):
        self.imunity_level = imu  # immunity state
        self.probability = prob  # probability of getting infected
        self.positive_or_not = posi  # infected or not
        self.dead_or_alive = D_or_A  # person alive or not
        self.date_of_infected = dateid  # identified as positive
        self.essential_worker_or_not = esOrNot  # essential worker or not

    def Change_probability(self, value):
        self.probability = value
    def Get_probability_value(self):
        return self.probability
    def set_positive_or_not(self):
        if self.positive_or_not == True:
            self.positive_or_not = False
        else:
            self.positive_or_not = True
    def Change_immuneity(self):
        self.imunity_level = True
    pass

class Class_For_Child(Class_For_One_Citizen):  # class for child
    def __init__(self, prob, i, imun=False, posi=False):
        Class_For_One_Citizen.__init__(self, imun, posi, prob, i)
    pass

class Class_For_Adult(Class_For_One_Citizen): # class for adult
    def __init__(self, prob, i, imun=False, posi=False, essential_worker_or_not=False):
        Class_For_One_Citizen.__init__(self, imun, posi, prob, i, essential_worker_or_not)
    pass

class Class_For_Senior(Class_For_One_Citizen):  # class for seniors
    def __init__(self, prob, i, imu=False, posi=False):
        Class_For_One_Citizen.__init__(self, imu, posi, prob, i)
    pass

class Class_For_Family:  # class for family
    def __init__(self, Family_size, index, members=[], date=-1):
        self.Family_size = Family_size
        self.members = members  # member list
        self.index = index  # index for the family in the list
        self.State_Infected = date  # infected State

    def Change_probability_all(self):
        for i in range(len(self.members)):
            Ran = random.randint(40, 80)
            self.members[i].Change_probability(Ran)
    pass

#Declaring variables
Population_of_the_country = 1000000
total_children_count = random.randint(200000, 210000)  # about 20% are children
remain_children_count = total_children_count  # randomly assign child into family
total_senior_count = random.randint(300000, 310000)  # about 30% are seniors
remain_senior_count = total_senior_count
total_adults_count = Population_of_the_country - (total_children_count + total_senior_count)  # total adults
total_family_members = 0  # live together as a family
total_single_adults = 0  # total single adults
single_seniors = 0
child_count = 0
senior_count = 0
essential_workers = 40000  # variable for essential workers
remain_essential_workers = essential_workers
total_family_essential_workers = 0
total_single_essential_workers = 0
Family_count = []  # list for all families
Single_count = []  # people who live alone
essential_worker_families = []
Positive_cases_plot = []  # positive cases by the day
Death_count_plot = [0]  # store deaths for day
Recovered_count_plot = [0]  # recovered people by the day
Hospitalized_plot = []  # hospitalized people by the day

# randomly assign people to families and singles
for i in range(100000):
    family_size = random.randint(2, 7)
    Temperory_family = Class_For_Family(family_size, i)
    family_remain = family_size
    total_family_members += family_size

    if remain_children_count > 0 and family_remain > 0:
        child_count = random.randint(1, family_remain)
        while (child_count > remain_children_count):
            child_count = random.randint(1, family_remain)
        remain_children_count -= child_count
        for j in range(child_count):
            temp_child = Class_For_Child(random.randint(10, 20), i)
            Temperory_family.members.append(temp_child)
            family_remain -= 1

    if remain_senior_count > 0 and family_remain > 0:
        senior_count = random.randint(1, family_remain)
        while (senior_count > remain_senior_count):
            senior_count = random.randint(1, family_remain)
        remain_senior_count -= senior_count
        for j in range(senior_count):
            Temp_senoir = Class_For_Senior(random.randint(35, 60), i)
            Temperory_family.members.append(Temp_senoir)
            family_remain -= 1

    if remain_children_count > family_remain and family_remain > 0 :
        for j in range(family_remain):
            temp_child = Class_For_Child(random.randint(10, 20), i)
            Temperory_family.members.append(temp_child)
            family_remain -= 1
            remain_children_count -= 1
    elif family_remain > 0:
        for j in range(family_remain):
            if remain_essential_workers > 0:
                Essential_Or_Not = random.randint(1, 2)
                if Essential_Or_Not == 2:
                    Temp_adult = Class_For_Adult(random.randint(15, 40), i)
                    Temperory_family.members.append(Temp_adult)
                    family_remain -= 1
                    total_adults_count += 1
                else:
                    Temp_adult = Class_For_Adult(random.randint(15, 40), i, False, False, True)
                    Temperory_family.members.append(Temp_adult)
                    remain_essential_workers -= 1
                    total_family_essential_workers += 1
                    family_remain -= 1
                    total_adults_count += 1
                    essential_worker_families.append(Temperory_family)
            else:
                Temp_adult = Class_For_Adult(random.randint(15, 40), i)
                Temperory_family.members.append(Temp_adult)
                total_adults_count += 1
                family_remain -= 1

    Family_count.append(Temperory_family)  # add created family to the list

for i in range(1000000 - total_family_members):
    if (remain_senior_count > i):
        single_seniors += 1
        temp_senior = Class_For_Senior(random.randint(35, 60), i)
        Single_count.append(temp_senior)
    else:
        if remain_essential_workers > 0:
            Temp_adult = Class_For_Adult(random.randint(15, 40), i, False, False, True)
            Single_count.append(Temp_adult)
            remain_essential_workers -= 1
            total_single_essential_workers += 1
            total_single_adults += 1

        else:
            Temp_adult = Class_For_Adult(random.randint(15, 40), i)
            Single_count.append(Temp_adult)
            total_single_adults += 1

Randomly_Selecting_A_Family = random.randint(1, 2) # 1 families 2 single person
if Randomly_Selecting_A_Family == 2:
    index = random.randint(0, len(Single_count) - 1)
    Single_count[index].set_positive_or_not()
    Single_count[index].date_of_infected = 1
else:
    index = random.randint(0, 99999)  # select random family form 100000 families
    memberindex = random.randint(0, Family_count[index].Family_size - 1)  # pick a random member
    Family_count[index].members[memberindex].set_positive_or_not()
    Family_count[index].State_Infected = 1
    Family_count[index].members[memberindex].date_of_infected = 1
    Family_count[index].Change_probability_all()

Positive_cases_plot.append(1)
hospitalized_total = 1
In_hospital_count_plot = [1]
total_recovered = 0
wear_Masks = False  # varibales for storing details o frestrictions
travel_restrictions = False
print("\n")
print("Give Restrictions")
# get user inputs about restrictions

Travelling_restrictions = input("Travel restrictions (y/n) :")
while Travelling_restrictions != 'y' and Travelling_restrictions != 'n':
    print("Input a valid character")
    Travelling_restrictions = input("Face Masks (y/n) :")
if Travelling_restrictions == 'y':
    travel_restrictions = True

facemask = input("Face Masks (y/n) :")
while facemask != 'y' and facemask != 'n':
    print("Input a valid character")
    facemask = input("Face Masks (y/n) :")
if facemask == 'y':
    wear_Masks = True

dayend = 0
daystart = 0

if travel_restrictions == True or wear_Masks == True:
    daystart = int(input('Enter day that these restriction start :'))
    dayend = int(input('Enter day that these restriction end :'))

    while daystart > 50 or daystart < 0 or dayend > 50 or dayend < 0:  # validation inputs
        print("invalid counts")
        daystart = int(input('Enter day that these restriction start :'))
        dayend = int(input('Enter day that these restriction end :'))
print("\n\n")

for i in range(49):
    print("----> Day ", i + 1)
    recovered = 0
    positive_count = 0
    death_count = 0
    if  i <= dayend and i >= daystart and (travel_restrictions == True or wear_Masks == True):
        if travel_restrictions == True and wear_Masks == True:  # if travel restrictions and mask on restriction is on

            for j in range(len(Single_count)):
                Infection_reducing_prob = random.randint(5, 10)
                Single_count[j].probability -= Infection_reducing_prob
                if Single_count[j].probability < 0:
                    Single_count[j].probability = 0
                if  Single_count[j].essential_worker_or_not == True and Single_count[j].dead_or_alive == True and Single_count[j].date_of_infected == -1 and Single_count[j].positive_or_not == False and Single_count[j].imunity_level == False:
                    result = npy.random.choice([True, False], 1, p=[Single_count[j].Get_probability_value() / 100, 1 - Single_count[j].Get_probability_value() / 100])
                    if result == True:
                        Single_count[j].set_positive_or_not()
                        Single_count[j].date_of_infected = i + random.randint(0, 5)
                if Single_count[j].positive_or_not == True and Single_count[j].imunity_level == False and Single_count[j].dead_or_alive == True:
                    Dead_or_not = npy.random.choice([True, False], 1, p=[0.001, 0.999])
                    if Dead_or_not == True:
                        death_count += 1
                        Single_count[j].dead_or_alive = False
                if Single_count[j].dead_or_alive == True and Single_count[j].date_of_infected == i:
                    positive_count += 1
                    hospitalized_total += 1
                if Single_count[j].date_of_infected != -1 and Single_count[j].date_of_infected + 10 == i and Single_count[j].dead_or_alive == True:
                    Single_count[j].imunity_level == True
                    Single_count[j].positive_or_not = False
                    recovered += 1
                    total_recovered += 1
                Single_count[j].probability += Infection_reducing_prob
            for j in range(len(Family_count)):
                Infection_reducing_prob = random.randint(5, 10)
                Family_count[j].members[k].probability -= Infection_reducing_prob
                if Family_count[j].members[k].probability < 0:
                    Family_count[j].members[k].probability = 0
                for k in range(Family_count[j].Family_size):
                    if Family_count[j].members[k].positive_or_not == False and Family_count[j].members[k].imunity_level == False and Family_count[j].members[k].dead_or_alive == True and Family_count[j].members[k].date_of_infected == -1:
                        result = npy.random.choice([True, False], 1, p=[Family_count[j].members[k].Get_probability_value() / 100, 1 - Family_count[j].members[k].Get_probability_value() / 100])
                        if result == True:
                            Family_count[j].members[k].set_positive_or_not()
                            Family_count[j].members[k].date_of_infected = i + random.randint(5, 11)
                            Family_count[j].Change_probability_all()
                    if Family_count[j].members[k].positive_or_not == True and Family_count[j].members[k].imunity_level == False and Family_count[j].members[k].dead_or_alive == True:
                        Dead_or_not = npy.random.choice([True, False], 1, p=[0.001, 0.999])
                        if Dead_or_not == True:
                            Family_count[j].members[k].dead_or_alive = False
                            death_count += 1

                    if Family_count[j].members[k].date_of_infected == i and Family_count[j].members[k].dead_or_alive == True:
                        hospitalized_total += 1
                        positive_count += 1

                    if Family_count[j].members[k].date_of_infected + 10 == i and Family_count[j].members[k].dead_or_alive == True and Family_count[j].members[k].date_of_infected != -1:
                        recovered += 1
                        total_recovered += 1
                        Family_count[j].members[k].imunity_level == True
                        Family_count[j].members[k].positive_or_not = False
                    Family_count[j].members[k].probability += Infection_reducing_prob

        elif wear_Masks == True:

            for j in range(len(Single_count)):
                Infection_reducing_prob = random.randint(5, 10)
                Single_count[j].probability -= Infection_reducing_prob
                if Single_count[j].probability < 0:
                    Single_count[j].probability = 0
                if Single_count[j].positive_or_not == False and Single_count[j].imunity_level == False and Single_count[j].dead_or_alive == True and Single_count[j].date_of_infected == -1:
                    result = npy.random.choice([True, False], 1, p=[(Single_count[j].Get_probability_value() / 100), 1 - (Single_count[j].Get_probability_value() / 100)])
                    if result == True:
                        Single_count[j].set_positive_or_not()
                        Single_count[j].date_of_infected = i + random.randint(0, 5)
                if Single_count[j].positive_or_not == True and Single_count[j].imunity_level == False and Single_count[j].dead_or_alive == True:
                    Dead_or_not = npy.random.choice([True,False],1,p=[0.001,0.999])
                    if Dead_or_not == True:
                        Single_count[j].dead_or_alive = False
                        death_count += 1
                if Single_count[j].date_of_infected == i and Single_count[j].dead_or_alive == True:
                    positive_count += 1
                    hospitalized_total += 1
                if Single_count[j].date_of_infected + 10 == i and Single_count[j].dead_or_alive == True and Single_count[
                    j].date_of_infected != -1:  # if person positive and its been 10 days since hospitalize hes marked immune
                    Single_count[j].imunity_level == True
                    Single_count[j].positive_or_not = False
                    recovered += 1
                    total_recovered += 1
                Single_count[j].probability += Infection_reducing_prob

            for j in range(100000):

                for k in range(Family_count[j].Family_size):
                    Infection_reducing_prob = random.randint(5, 10)
                    Family_count[j].members[k].probability -= Infection_reducing_prob
                    if Family_count[j].members[k].positive_or_not == False and Family_count[j].members[k].imunity_level == False and Family_count[j].members[k].dead_or_alive == True and Family_count[j].members[k].date_of_infected == -1:
                        result = npy.random.choice([True, False], 1, p=[Family_count[j].members[k].Get_probability_value() / 100, 1 - Family_count[j].members[k].Get_probability_value() / 100])
                        if result == True:
                            Family_count[j].members[k].set_positive_or_not()
                            Family_count[j].members[k].date_of_infected = i + random.randint(5, 11)
                            Family_count[j].Change_probability_all()

                    if Family_count[j].members[k].positive_or_not == True and Family_count[j].members[k].imunity_level == False and Family_count[j].members[k].dead_or_alive == True:
                        Dead_or_not = npy.random.choice([True, False], 1, p=0.001)
                        if Dead_or_not == True:
                            Family_count[j].members[k].dead_or_alive = False
                            death_count += 1

                    if Family_count[j].members[k].date_of_infected == i and Family_count[j].members[k].dead_or_alive == True:
                        positive_count += 1
                        hospitalized_total += 1

                    if Family_count[j].members[k].date_of_infected + 10 == i and Family_count[j].members[k].dead_or_alive == True and Family_count[j].members[k].date_of_infected != -1:
                        Family_count[j].members[k].imunity_level == True
                        Family_count[j].members[k].positive_or_not = False
                        recovered += 1
                        total_recovered += 1
                    Family_count[j].members[k].probability += Infection_reducing_prob
        elif travel_restrictions == True:

            for j in range(len(Single_count)):

                if Single_count[j].positive_or_not == False and Single_count[j].imunity_level == False and Single_count[j].dead_or_alive == True and Single_count[j].date_of_infected == -1 and Single_count[j].essential_worker_or_not == True:  # check for essential worker
                    result = npy.random.choice([True, False], 1, p=[Single_count[j].Get_probability_value() / 100, 1 - Single_count[j].Get_probability_value() / 100])
                    if result == True:
                        Single_count[j].set_positive_or_not()
                        Single_count[j].date_of_infected = i + random.randint(0, 5)
                if Single_count[j].positive_or_not == True and Single_count[j].imunity_level == False and Single_count[j].dead_or_alive == True:
                    Dead_or_not = npy.random.choice([True, False], 1, p=[0.001, 0.999])
                    if Dead_or_not == True:
                        Single_count[j].dead_or_alive = False
                        death_count += 1

                if Single_count[j].date_of_infected == i and Single_count[j].dead_or_alive == True:
                    positive_count += 1
                    hospitalized_total += 1

                if Single_count[j].date_of_infected + 10 == i and Single_count[j].dead_or_alive == True and Single_count[j].date_of_infected != -1:
                    Single_count[j].imunity_level == True
                    Single_count[j].positive_or_not = False
                    recovered += 1
                    total_recovered += 1
            for j in range(len(Family_count)):

                for k in range(Family_count[j].Family_size):
                    if Family_count[j].members[k].positive_or_not == False and Family_count[j].members[k].imunity_level == False and Family_count[j].members[k].dead_or_alive == True and Family_count[j].members[k].date_of_infected == -1:
                        result = npy.random.choice([True, False], 1, p=[Family_count[j].members[k].Get_probability_value() / 100, 1 - Family_count[j].members[k].Get_probability_value() / 100])
                        if result == True:
                            Family_count[j].members[k].set_positive_or_not()
                            Family_count[j].members[k].date_of_infected = i + random.randint(5, 11)
                            Family_count[j].Change_probability_all()

                    if Family_count[j].members[k].positive_or_not == True and Family_count[j].members[k].imunity_level == False and Family_count[j].members[k].dead_or_alive == True:
                        Dead_or_not = npy.random.choice([True, False], 1, p=[0.001, 0.999])
                        if Dead_or_not == True:
                            Family_count[j].members[k].dead_or_alive = False
                            death_count += 1

                    if Family_count[j].members[k].date_of_infected == i and Family_count[j].members[k].dead_or_alive == True:
                        positive_count += 1
                        hospitalized_total += 1

                    if Family_count[j].members[k].date_of_infected + 10 == i and Family_count[j].members[k].dead_or_alive == True and Family_count[j].members[k].date_of_infected != -1:
                        Family_count[j].members[k].imunity_level == True
                        Family_count[j].members[k].positive_or_not = False
                        recovered += 1
                        total_recovered += 1

    else:  # if there is no restrictions are set to be true

        for j in range(len(Single_count)):
            if Single_count[j].positive_or_not == False and Single_count[j].imunity_level == False and Single_count[j].dead_or_alive == True and Single_count[j].date_of_infected == -1:
                result = npy.random.choice([True, False], 1, p=[Single_count[j].Get_probability_value() / 100, 1 - Single_count[j].Get_probability_value() / 100])
                if result == True:
                    Single_count[j].set_positive_or_not()
                    Single_count[j].date_of_infected = i + random.randint(0, 5)
            if Single_count[j].positive_or_not == True and Single_count[j].imunity_level == False and Single_count[j].dead_or_alive == True:
                Dead_or_not = npy.random.choice([True, False], 1, p=[0.001, 0.999])
                if Dead_or_not == True:
                    Single_count[j].dead_or_alive = False
                    death_count += 1

            if Single_count[j].date_of_infected == i and Single_count[j].dead_or_alive == True:
                positive_count += 1
                hospitalized_total += 1

            if Single_count[j].date_of_infected + 10 == i and Single_count[j].dead_or_alive == True and Single_count[j].date_of_infected != -1:
                Single_count[j].imunity_level == True
                Single_count[j].positive_or_not = False
                recovered += 1
                total_recovered += 1

        for j in range(100000):
            for k in range(Family_count[j].Family_size):
                if Family_count[j].members[k].positive_or_not == False and Family_count[j].members[k].imunity_level == False and Family_count[j].members[k].dead_or_alive == True and Family_count[j].members[k].date_of_infected == -1:
                    result = npy.random.choice([True, False], 1, p=[Family_count[j].members[k].Get_probability_value() / 100, 1 - Family_count[j].members[k].Get_probability_value() / 100])
                    if result == True:
                        Family_count[j].members[k].set_positive_or_not()
                        Family_count[j].members[k].date_of_infected = i + random.randint(5, 11)
                        Family_count[j].Change_probability_all()

                if Family_count[j].members[k].positive_or_not == True and Family_count[j].members[k].imunity_level == False and Family_count[j].members[k].dead_or_alive == True:
                    Dead_or_not = npy.random.choice([True, False], 1, p=[0.001, 0.999])
                    if Dead_or_not == True:
                        Family_count[j].members[k].dead_or_alive = False
                        death_count += 1

                if Family_count[j].members[k].date_of_infected == i and Family_count[j].members[k].dead_or_alive == True:
                    positive_count += 1
                    hospitalized_total += 1

                if Family_count[j].members[k].date_of_infected + 10 == i and Family_count[j].members[k].dead_or_alive == True and Family_count[j].members[k].date_of_infected != -1:
                    Family_count[j].members[k].imunity_level == True
                    Family_count[j].members[k].positive_or_not = False
                    recovered += 1
                    total_recovered += 1


    print("-------------- Daily report ----------------")
    print("Total number of covid positive people -> ", positive_count)
    print("Total number of recovered patients -> ", recovered)
    print("Total number of Deaths recorded -> ", death_count)

    print("\n")

    Positive_cases_plot.append(positive_count)
    In_hospital_count_plot.append(hospitalized_total)
    Recovered_count_plot.append(recovered)
    Death_count_plot.append(death_count)

for i in range(50):
    Temp_plot = Recovered_count_plot[0:i]
    Temp_plot2 = Death_count_plot[0:i]
    Hospitalized_plot.append(In_hospital_count_plot[i] - sum(Temp_plot) - sum(Temp_plot2))

print("-------------- Summary for 50 days ----------------")
print("\nTotal number of infected people for 50 Days -> ", sum(Positive_cases_plot))
print("Total number of recovered patients for 50 Days -> ", hospitalized_total - sum(Death_count_plot))
print("Total number of deaths recorded for 50 Days -> ", sum(Death_count_plot))


Y_value_positive = npy.array(Positive_cases_plot)
Y_value_deaths = npy.array(Death_count_plot)
Y_value_recovered = npy.array(Recovered_count_plot)
Y_value_hospitalized = npy.array(Hospitalized_plot)

X_value = npy.arange(1, 51)

# generate plot for covid positive people
plot1 = plot.figure(1)
plot.xlabel("No. of days")
plot.ylabel("Total number of covid positive people")
plot.title("Total number of covid positive people for 50 days")
plot.scatter(X_value, Y_value_positive, color="green")
plot.plot(X_value, Y_value_positive, color="green")

# generate plot for  hospitalized people
plot4 = plot.figure(2)
plot.xlabel("No. of days")
plot.ylabel("Total number of hospitalized people")
plot.title("Total number of hospitalized people for 50 Days")
plot.scatter(X_value, Y_value_hospitalized, color="black")
plot.plot(X_value, Y_value_hospitalized, color="black")

# generate plot for recovered patients
plot3 = plot.figure(3)
plot.xlabel("No. of days")
plot.ylabel("Total number of recovered patients")
plot.title("Total number of recovered patients for 50 Days")
plot.scatter(X_value, Y_value_recovered, color="blue")
plot.plot(X_value, Y_value_recovered, color="blue")

# generate plot for deaths count
plot2 = plot.figure(4)
plot.xlabel("No. of days")
plot.ylabel("Total number of Deaths recorded")
plot.title("Total number of deaths recorded for 50 Days")
plot.scatter(X_value, Y_value_deaths, color="red")
plot.plot(X_value, Y_value_deaths, color="red")

plot.show()