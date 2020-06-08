# Created by Muhammet Safa Güner at 7.06.2020

Feature: My tests

  @login
  Scenario: Success test for login
    * I navigate to login page
    * I enter username="pervenches@harveynaylor.buzz" and password="12345_asd"
    * I click on Submit button
    # * I see user name = "Mordor Test" on home page sahibinden hata veriyor. galiba botları engellemısler

  @login
  Scenario: Failure test for login
    * I navigate to login page
    * I enter username="pervenches@harveynaylor.buzz" and password="12345"
    * I click on Submit button
    * login is unsuccessful

  @sigh_up
  Scenario: Open registration page
    * I navigate to sign up page
    * I see the registration page open

  @search
  Scenario:Search text and check no result screen
    * I search "adsfghsadfghjk asdas"
    * I see the no result page

  @search
  Scenario Outline: Search text and open main category
    * I search "<search_text>"
    * I open main category = "<category>" on search result page

    Examples: data
      | search_text | category                     |
      | Daihatsu    | Vasıta                       |
      | Buzdolabı   | İkinci El ve Sıfır Alışveriş |

