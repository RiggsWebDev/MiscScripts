##########################################
#                                        #
#                                        #
#              PowerShell script to      #
#           change all users in a CSV    #
#           to a different description   #
##########################################

Import-Module ActiveDirectory
$Users = Import-csv c:\Users.csv
foreach($User in $Users){
Set-ADUser $User.SamAccountName -Description $User.NewDescription
}

###########################################
#In the CSV use 1 column as SamAccountName#
#               Which is their login      #
#  In the next column use NewDescription  #
###########################################
