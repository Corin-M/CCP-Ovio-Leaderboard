"""
CCP Final project code: takes data on Ovio users and allows for the organization &
display of leaderboards and profiles.
Last edited: 4/2/2019 by Corin Magee

Useful functions to remember:
    find_index(username) --> takes a string username and tells you what the reference 
                             index is for that user (which is needed for all functions)
    create_new_user() --> walks you through entering new data
    [leaderboard].printTop5()--> prints the top 5 users in the leaderboard called with
    username_list[reference index].full_profile() --> prints the profile of the user
                                                      whose reference index is used
"""


"""First we start with importing and organizing all of the data given"""
import pandas as pd
#import all of the data from the csv file partially given by Ovios partially generated
individual_data= pd.read_csv("New_CCP_Data.csv")
#extracts list of usernames from the csv file (this will later be converted to objects)
username_list = []
for i in individual_data["Name"]: username_list.append(i)
#extracts list of total commits in same order as usernames so indexes line up 
commits_list = []
for i in individual_data["Commits"]: commits_list.append(i)
#extracts list of python commits in same order as usernames so indexes line up
python_list = []
for i in individual_data["Python"]: python_list.append(i)
#extracts list of java commits in same order as usernames so indexes line up
java_list = []
for i in individual_data["Java"]: java_list.append(i)
#extracts list of html commits in same order as usernames so indexes line up
html_list = []
for i in individual_data["HTML"]: html_list.append(i)

    
"""This section has the declarations of object types and their features"""

#creates user object
class User(object):
    #all users must be declared with a usernamename and their corresponding list index. 
    def __init__(self, username, index):
        self.username = username
        self.index = index
        #every user also has a list of all the languages they use
        self.langNames = self.getLangs(index)[0]
        #and a corresponding list of their commits in that language (indexes align) 
        self.langNums = self.getLangs(index)[1]
        #and total number of commits
        self.commits = commits_list[index]
        
    #searches through the csv file to return what languages this User uses (not 0) and their values
    def getLangs(self,index):
        langs = []
        values = []
        if python_list[index] != 0:
            langs.append("Python")
            values.append(python_list[index])
        if java_list[index] != 0:
            langs.append("Java")
            values.append(java_list[index])
        if html_list[index] != 0:
            langs.append("HTML")
            values.append(html_list[index])
        #returns a list of language names (langs) and their values(values) w/ matching indexes
        return langs, values
            
    #prints a profile of an individual 
    #includes username, overall rank & commits, and rank & commits by lang           
    def full_profile(self):
        #prints username
        print("Username: "+ str(self.username))
        #finds and prints overall rank and commits
        rank = commits_board.find_rank(self)
        print("#" +str(rank)+ " in overall commits: " + str(self.commits))
        #finds relevant ranks and prints commits for languages
        for i in range(len(self.langNames)):
            if "Python" == self.langNames[i]:
                rank = python_board.find_rank(self)
            if "Java" == self.langNames[i]:
                rank = java_board.find_rank(self)
            if "HTML" == self.langNames[i]:
                rank = html_board.find_rank(self)
            print("#" + str(rank) + " in "+ str(self.langNames[i])  + " commits: " + str(self.langNums[i]) )

    pass


#creates leaderboard object
class Leaderboard():
    #each leaderboard must be initialized with a name and data list
    def __init__(self, name, base_list):
        self.name = name
        self.source = base_list
        #they will also both start with a blank members & values list w/ matching indexes
        self.members = []
        self.values = []
        #they will update their members and values list when created
        self.update_list()

    #returns the rank of a member within the list or if the member is not in the list
    def find_rank(self, member):
        #looks to see if the member is in the list. returns index if found, -1 if not
        try: rank = self.members.index(member)
        except ValueError:
            rank = -1
        #if it is in the list then add one to index to get rank
        if rank != -1:
            return rank +1
        else:
            return str(member.username) + " not found in this leaderboard"
    
    #adds a member to the leaderboard 
    def add_member(self, new_member):
        #if the board is empty the member is automatically added
        if len(self.members) == 0:
            self.members.append(new_member)
            self.values.append(self.source[new_member.index])
        #if not empty then it checks to see if the member is in the board
        try: self.members.index(new_member)
        except ValueError:
            #if the member isn't in teh board already it adds the member in ascending value order
            for counter in range(len(self.values)):
                  #looks to see where in the list the value should be added 
                  #it is placed before any value smaller than the new value               
                  if self.values[counter] < self.source[new_member.index]:
                    self.members.insert(counter, new_member)
                    self.values.insert(counter, self.source[new_member.index])
                    return
            #if it is the smallest it is added to the end
            self.members.append(new_member)
            self.values.append(self.source[new_member.index])
            return
                        
    #adds every member of the source list that has a value not 0 to the board
    def update_list(self):
        #goes through parent list
        for i in range(len(self.source)):
             #checks the value is not 0 
             if self.source[i] != 0:
               #calls to add it to the list
               self.add_member(username_list[i])
                    
    #prints top 5 members of the board with their rank and value
    def printTop5(self):
        print(self.name, " Leaderboard:")
        print("#1: ", self.members[0].username, "\t", self.values[0])
        print("#2: ", self.members[1].username, "\t", self.values[1])
        print("#3: ", self.members[2].username, "\t", self.values[2])
        print("#4: ", self.members[3].username, "\t", self.values[3])
        print("#5: ", self.members[4].username, "\t", self.values[4])
    pass
    
"""This section has all of the non-object functions to be used later"""
#replaces all string usernames with a User object with the same username
def convert_username_list():
    for i in range(len(username_list)):
        if type(username_list[i]) == str:
            username_list[i] = User(username_list[i], username_list.index(username_list[i]))

#walks the user through the creation of a new entry of data. 
#Creates user object and fills in all necessary lists
def create_new_user():
    #fills in all lists
    username_list.append(str(input("Enter Username: ")))
    commits_list.append(int(input("Total commits: ")))
    python_list.append(int(input("Python commits: ")))
    java_list.append(int(input("Java commits: ")))
    html_list.append(int(input("HTML commits: ")))
    #converts username entry to a User object
    username_list[-1] = User(username_list[-1], username_list.index(username_list[-1]))
    #updates all leaderboards with new user if applicable
    commits_board.update_list()
    python_board.update_list()
    java_board.update_list()
    html_board.update_list()

#inputs a string and returns the reference index of that user
def find_user_index(searching_username):
    #looks for a matching username
    for i in range(len(username_list)):
        if username_list[i].username == searching_username:
           #returns index if found
           return username_list[i].index
    #otherwise tells returns not found
    return "User not found"
    
""" This section now calls the prior code and initializes all of the data"""
#gets username_list to carry Users not strings
convert_username_list()

#creates and updates all of the leaderboards
commits_board = Leaderboard("Commits", commits_list)    
python_board = Leaderboard( "Python", python_list)    
java_board = Leaderboard("Java", java_list)
html_board = Leaderboard("HTML", html_list)

"""This is the section you should play with to see what the code does"""
#prints python leaderboard
python_board.printTop5()

#create a user. I tend to write
    #username: contechtions
    #Commits: 900
    #Python: 600
    #Java: 300
    #HTML: 0
create_new_user()

#prints board again to see if new user changes anything
python_board.printTop5()

#prints the user index of a random name (feel free to change)
print("User profile: "+ str(find_user_index("mohsenansari")))
#pulls up mohsenansari's profile
try: username_list[find_user_index("mohsenansari")].full_profile()
except:
    print("No user found")