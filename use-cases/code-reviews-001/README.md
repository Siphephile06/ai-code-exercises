# Code Reviews with AI

## Overview

This exercise helps you practice using AI to improve your code through different review strategies. You'll work with code examples in Python, JavaScript, and Java to discover how AI can serve different roles in the development process - from independent reviewer to pre-submission polisher to real-time programming partner.

## Exercise Options

Choose one of these code examples:

1. **Python Data Visualization Function**: A data processing and visualization utility with various improvement opportunities
2. **JavaScript User Authentication Utility**: A web application authentication module with several issues
3. **Java File Management Class**: A file utility class with quality and design challenges

## Exercise Instructions

1. Choose one of the provided code examples
2. Apply the prompts from the "Pre-submission Code Review" scenario:
   - Project Standards Alignment
   - Reviewer Perspective Simulation
   - Documentation and Comment Enhancement
3. For each prompt, document:
   - What issues or improvements the AI identified
   - Any unexpected insights
   - What changes you would make based on the feedback
4. Compare the feedback from different strategies
5. Implement at least three key improvements based on the feedback
6. Reflect on how you could incorporate these approaches into your workflow

## Code Examples Detail

### 1. Python Data Visualization Function (src/data_visualization.py)

A dashboard generation function that processes sales data and creates visualizations using Plotly. Issues include:
- Import placement and organization
- Error handling and validation improvements
- Documentation gaps
- Performance optimization opportunities

### 2. JavaScript User Authentication Utility (src/user_auth.js)

A session-based authentication system with token management and password validation. Issues include:
- Security vulnerabilities
- Error handling gaps
- Storage management challenges
- Structure and organization improvements

### 3. Java File Management Class (src/FileManager.java)

A utility class for file operations including reading, writing, and archiving. Issues include:
- Resource management concerns
- Exception handling patterns
- Potential thread safety issues
- Design inconsistencies

## Prompting Strategies

### Pre-submission Code Polishing
- **Prompt 1: Project Standards Alignment** - Ensure code follows project/team standards
- **Prompt 2: Reviewer Perspective Simulation** - Anticipate feedback from different reviewer types
- **Prompt 3: Documentation and Comment Enhancement** - Improve code documentation

## Workshop Worksheet

Use this structure to document your findings during the exercise:

### Code Selection
- Selected code: Python
- Code generates a HTML file which will be a sales dashboard. Specific values are taken and displayed in different graphs. Highlighting is added to those that are higher than the threshold.

### Prompt Results
Problems given by each prompt:
- First Prompt:
   * No loggong.
   * placement of imports.
   * Limited error messages.
- Second Prompt:
   * My Syntax errors
   * My logic after implementing an improvement.
- Third Prompt:
   * Basic Docstrings
   * Comments
- Unexpected insights was silent fails given ny the second prompt.
- Planned improvements
   * Logging
   * place imports at the right place
   * Add error messages
   * Fix my added Errors :)
   * Improve doctsrings and commensts

### Comparison of Prompts
- Most valuable prompt was the second promt as it was able to help me grasp the codebase more clearly.
- Type of issue found by multoiple prompts was empty charts being created.
- Types of issues found by only one prompt was basic docstring.

### Implementation Plan
- Top 3 improvements to implement is the docstrings, the comments on complex code and not creating empty charts.
- How you would prioritize these changes

### Workflow Integration
- I would use AI strategies by asking it to guide me on errors and improvements befor moving on to my next phase of code.
- These might complement human code reviews by thoroughness and intricisies that human code reviews might not have the insight on.
