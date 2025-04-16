Feature: login page
  Scenario: User Logs in
    Given I have valid credentials
    When I click on login
    Then I should see error