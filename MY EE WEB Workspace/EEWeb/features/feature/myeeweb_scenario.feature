Feature: MyEE_WEB_Scenario

# @ProfileCreation
# Background: Yopmail and Janrain profile creation
#   Given I am on Yopmail page
#   Then I am on yopmail page to create mail with <Mail>
#   Given I am on Janrain login page
#   When Entered the login details as <Username> <Password> and Navigate to Home page
#   Then Create user profile with <BAN> and <ManagedObject> if <RoletType> is LEGAL and Create user profile with <CTN> , <ManagedObject> and <RelatedManagedObject> if <RoleType> is END USER

# Examples:
# | Mail       | Username                     | Password       | BAN       | CTN         | ManagedObject                       | RelatedManagedObject          | RoletType  |
# | "usecase1" | "anant.halyal@capgemini.com" | "sh0wmus@g0on" | 143452001 | 07996705036 | /excalibur/subscribers/447996228906 | /excalibur/accounts/143459038 | LegalOwner |

@testcase1
Scenario Outline: Verify if the system is able to fetch the account information of a Account holder upon logging into MY EE (PAYM)
  Given I Am On Yopmail Page
  Then I Create Yopmil EmailID <Email>
  Then I Am On Janrain Login Page
  Then I Enter The Login Details <Username> <Password> And Navigate To Janrain Home Page
  Then I Create User Profile For Legal Owner <BAN> <RoleType> <RelatedManagedObject> <Email> and Logged Out From Application
  When I Am On My EE Web Login Page
  Then I Am Loged In To The My EE web Application With <Email> <Password2> and Navigate to My EE Web Home Page <CustType>
  # Then I Verify Account Information <BAN>
  # Then I am Logged Out From MY EE Web Application
  Examples:
  | BAN         | CTN           | Email       | Username                     | Password       | ManagedObject                        | RelatedManagedObject            | RoleType     | Password2   | CustType |
  | "143468458" | "07996709676" | "usecase13" | "anant.halyal@capgemini.com" | "sh0wmus@g0on" | "/excalibur/subscribers/07996709676" | "/excalibur/accounts/143468440" | "LegalOwner" | "Password2" | "PAYM"   |

@testcase2
Scenario Outline: Verify if the system is able to fetch the account information of a  Account holder upon logging into MY EE (PAYG) 
  # Given I Am On Yopmail Page
  # Then I Create Yopmil EmailID <Email>
  # Then I Am On Janrain Login Page
  # Then I Enter The Login Details <Username> <Password> And Navigate To Janrain Home Page
  # Then I Create User Profile For Legal Owner <BAN> <RoleType> <RelatedManagedObject> <Mail> and Logged Out From Application
  When I Am On My EE Web Login Page
  Then I Am Loged In To The My EE web Application With <Email> <Password2> and Navigate to My EE Web Home Page <CustType>
  Then I Verify Account Information For PAYG <BAN>
  Then I am Logged Out From MY EE Web Application
  Examples:
  | BAN         | CTN           | Email       | Username                     | Password       | ManagedObject                        | RelatedManagedObject            | RoleType     | Password2   | CustType |
  | "143468886" | "07996709676" | "usecase31" | "anant.halyal@capgemini.com" | "sh0wmus@g0on" | "/excalibur/subscribers/07996709676" | "/excalibur/accounts/143468440" | "LegalOwner" | "Password2" | "PAYG"  |

@testcase3
Scenario Outline: Review the Plan Summery(PAYM)
  # Given I Am On Yopmail Page
  # Then I Create Yopmil EmailID <Email>
  # Then I Am On Janrain Login Page
  # Then I Enter The Login Details <Username> <Password> And Navigate To Janrain Home Page
  # Then I Create User Profile For Legal Owner <BAN> <RoleType> <RelatedManagedObject> <Mail> and Logged Out From Application
  When I Am On My EE Web Login Page
  Then I Am Loged In To The My EE web Application With <Email> <Password2> and Navigate to My EE Web Home Page <CustType>
  Then Review the Plan Summery(PAYM)
  Then I am Logged Out From MY EE Web Application
  Examples:
  | BAN         | CTN           | Email       | Username                     | Password       | ManagedObject                        | RelatedManagedObject            | RoleType     | Password2   | CustType |
  | "143468458" | "07996709676" | "incidentlive12" | "anant.halyal@capgemini.com" | "sh0wmus@g0on" | "/excalibur/subscribers/07996709676" | "/excalibur/accounts/143468440" | "LegalOwner" | "Password2" | "PAYM"   |

@testcase4
Scenario Outline: Verify that if Existing EE PayM is able to make his bill payment with new card
  # Given I Am On Yopmail Page
  # Then I Create Yopmil EmailID <Email>
  # Then I Am On Janrain Login Page
  # Then I Enter The Login Details <Username> <Password> And Navigate To Janrain Home Page
  # Then I Create User Profile For Legal Owner <BAN> <RoleType> <RelatedManagedObject> <Mail> and Logged Out From Application
  When I Am On My EE Web Login Page
  Then I Am Loged In To The My EE web Application With <Mail> <Password2> and Navigate to My EE Web Home Page
  Then I go to the Bill Payment option
  Then I Verify EE PAYM Able To Make Bill Payment With Card Details <Amount>
  Then I am Logged Out From MY EE Web Application
  Examples:
  | BAN         | CTN           | Mail        | Username                     | Password       | ManagedObject                        | RelatedManagedObject            | RoleType     | Password2   | Amount |
  | "143468458" | "07996709676" | "usecase12" | "anant.halyal@capgemini.com" | "sh0wmus@g0on" | "/excalibur/subscribers/07996709676" | "/excalibur/accounts/143468440" | "LegalOwner" | "Password2" | "10"     |

@testcase5
Scenario Outline: Verify User is able to perform Upgrade for EE PayM Customer
  # Given I Am On Yopmail Page
  # Then I Create Yopmil EmailID <Email>
  # Then I Am On Janrain Login Page
  # Then I Enter The Login Details <Username> <Password> And Navigate To Janrain Home Page
  # Then I Create User Profile For Legal Owner <BAN> <RoleType> <RelatedManagedObject> <Mail> and Logged Out From Application
  When I Am On My EE Web Login Page
  Then I Am Loged In To The My EE web Application With <Mail> <Password2> and Navigate to My EE Web Home Page
  Then I go to the Upgrade Menu option
  Then I Select Device and Price Plan As Per Requierment And Added Addredss Detials And Account Information <Device> <Plan> <AccountHolderName> <AccountNo> <SortCode>
  Then I am Logged Out From MY EE Web Application
  Examples:
  | BAN         | CTN           | Mail        | Username                     | Password       | ManagedObject                        | RelatedManagedObject            | RoleType     | Password2   | Amount | Device          | Plan                 | AccountHolderName | AccountNo  | SortCode |
  | "143468458" | "07996709676" | "usecase12" | "anant.halyal@capgemini.com" | "sh0wmus@g0on" | "/excalibur/subscribers/07996709676" | "/excalibur/accounts/143468440" | "LegalOwner" | "Password2" | "10"   | "iphone-7-plus" | "1GB Essential Plan" | "Suraj"           | "44360282" | 537011   |

@testcase6
Scenario Outline: Verify User is able to perform Upgrade for EE PayG Customer
  # Given I Am On Yopmail Page
  # Then I Create Yopmil EmailID <Email>
  # Then I Am On Janrain Login Page
  # Then I Enter The Login Details <Username> <Password> And Navigate To Janrain Home Page
  # Then I Create User Profile For Legal Owner <BAN> <RoleType> <RelatedManagedObject> <Mail> and Logged Out From Application
  When I Am On My EE Web Login Page
  Then I Am Loged In To The My EE web Application With <Mail> <Password2> and Navigate to My EE Web Home Page
  Then I go to the Upgrade Menu option
  Then I Select Device and Price Plan As Per Requierment And Added Addredss Detials And Account Information
  Then I am Logged Out From MY EE Web Application
  Examples:
  | BAN         | CTN           | Mail        | Username                     | Password       | ManagedObject                        | RelatedManagedObject            | RoleType     | Password2   | Amount |
  | "143468458" | "07996709676" | "usecase12" | "anant.halyal@capgemini.com" | "sh0wmus@g0on" | "/excalibur/subscribers/07996709676" | "/excalibur/accounts/143468440" | "LegalOwner" | "Password2" | "10"     |

@testcase7
Scenario Outline: Verify if  user is  able to perform the TOP UP (PAYG)
  # Given I Am On Yopmail Page
  # Then I Create Yopmil EmailID <Email>
  # Then I Am On Janrain Login Page
  # Then I Enter The Login Details <Username> <Password> And Navigate To Janrain Home Page
  # Then I Create User Profile For Legal Owner <BAN> <RoleType> <RelatedManagedObject> <Mail> and Logged Out From Application
  When I Am On My EE Web Login Page
  Then I Am Loged In To The My EE web Application With <Email> <Password2> and Navigate to My EE Web Home Page <CustType>
  Then I go to the TopUp Menu option
  Then I Select Payment Option With Registered Card And Confirm The Topup Ammount <TopUpAmmount>
  Then I Verify Topup Payment Successfull Done
  Then I am Logged Out From MY EE Web Application
  Examples:
  | BAN         | CTN           | Email       | Username                     | Password       | ManagedObject                        | RelatedManagedObject            | RoleType     | Password2   | TopUpAmmount | CustType |
  | "143468458" | "07996709676" | "usecase31" | "anant.halyal@capgemini.com" | "sh0wmus@g0on" | "/excalibur/subscribers/07996709676" | "/excalibur/accounts/143468440" | "LegalOwner" | "Password2" | "10"         | "PAYG"   |

@testcase8
Scenario Outline: Verify Customer is able to see usage of the customer 
  # Given I Am On Yopmail Page
  # Then I Create Yopmil EmailID <Email>
  # Then I Am On Janrain Login Page
  # Then I Enter The Login Details <Username> <Password> And Navigate To Janrain Home Page
  # Then I Create User Profile For Legal Owner <BAN> <RoleType> <RelatedManagedObject> <Mail> and Logged Out From Application
  When I Am On My EE Web Login Page
  Then I Am Loged In To The My EE web Application With <Email> <Password2> and Navigate to My EE Web Home Page <CustType>
  Then I Verify User Is Able To See Data Useage On MY EE Home Page
  Then I am Logged Out From MY EE Web Application
  Examples:
  | BAN         | CTN           | Email       | Username                     | Password       | ManagedObject                        | RelatedManagedObject            | RoleType     | Password2   | Amount | CustType |
  | "143468458" | "07996709676" | "usecase31" | "anant.halyal@capgemini.com" | "sh0wmus@g0on" | "/excalibur/subscribers/07996709676" | "/excalibur/accounts/143468440" | "LegalOwner" | "Password2" | "10"   | "PAYG"     |


@testcase9
Scenario Outline: Verify That user is able to Add-On in the Packs and Addon Section for PayG customer 
  # Given I Am On Yopmail Page
  # Then I Create Yopmil EmailID <Email>
  # Then I Am On Janrain Login Page
  # Then I Enter The Login Details <Username> <Password> And Navigate To Janrain Home Page
  # Then I Create User Profile For Legal Owner <BAN> <RoleType> <RelatedManagedObject> <Mail> and Logged Out From Application
  When I Am On My EE Web Login Page
  Then I Am Loged In To The My EE web Application With <Email> <Password2> and Navigate to My EE Web Home Page <CustType>
  Then I Verify User Is Able To See Data Useage On MY EE Home Page
  Then I am Logged Out From MY EE Web Application
  Examples:
  | BAN         | CTN           | Email       | Username                     | Password       | ManagedObject                        | RelatedManagedObject            | RoleType     | Password2   | Amount | CustType |
  | "143468458" | "07996709676" | "usecase31" | "anant.halyal@capgemini.com" | "sh0wmus@g0on" | "/excalibur/subscribers/07996709676" | "/excalibur/accounts/143468440" | "LegalOwner" | "Password2" | "10"   | "PAYG"     |
