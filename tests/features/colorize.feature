Feature: Colorize
    Colorize code block

    Scenario: Colorize code block
        Given I am an authenticated user
        When I enter text with codehiliter
        Then I see colorized code