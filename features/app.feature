Feature: demo app


    Scenario: able to retrieve user
        When I retrieve user test
        Then I receive user test

    Scenario: when a github webhook is received a question is returned
        When A GitHub webhook is received for user test
        Then I receive the next question