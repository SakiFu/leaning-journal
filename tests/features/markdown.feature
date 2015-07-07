Feature: Markdown
    Enter text with markdown syntax and desplay it properly
    
    Scenario: Enter text with markdown syntax
        Given I am an authenticated user
        When I enter text with markdown syntax
        Then I see the entry in h1 format

s