Feature: Colorize
    Colorize code block

    Scenario: Colorize code block
        Given I have an entry with code block
        When I go to the detail page 
        Then I see colorized code