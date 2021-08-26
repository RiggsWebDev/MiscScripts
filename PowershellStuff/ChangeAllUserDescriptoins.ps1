Import-Module ActiveDirectory
##########################################
#                                        #
#                                        #
#        Do not uncomment line 9 and 10  #
#           they are for testing only    #
#                                        #
##########################################
#Set-ADUser -SearchBase "dc=redacted,dc=redacted,dc=redacted,dc=redacted" -Description "Non-Certified" -Filter *
#Get-AdGroup -Filter * -Searchbase "OU=Staff, OU=User Groups, DC=redacted, DC=redacted, DC=redacted, DC=redacted" | Get-ADGroupMember
Get-ADUser -Filter * -SearchBase "dc=redacted,dc=redacted,dc=redacted,dc=redacted" | Set-ADUser -Replace @{description="Non-Certified"}
