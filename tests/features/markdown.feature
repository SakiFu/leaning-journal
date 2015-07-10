Feature: Markdown
    Enter text with markdown syntax
    
    Scenario: Enter text with markdown syntax and desplay it properly
        Given I am an authenticated user
        When I enter text with markdown syntax
        Then I see the entry in h1 format


