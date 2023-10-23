## Background

This is a small demo of the GetSpace App created using FastAPI.

## Assignment

Create a fork of this repo and for each of the steps below make a code change and commit for each step.

1. Get the application to run locally and create a Makefile to automate the steps.
2. One of the tests is currently failing, fix the code to make the test pass.
3. You need to add a new feature to the code where each question can have a weight
   associated with it. When you return the next question you want to return the question
   that hasn't been responded to with the highest overall weight.

   For example, Question A has weight 2 and Question B has weight 3 and if the user hasn't
   responded to either then the next question they get asked should be Question B.

   If the remaining questions have the same weight return a question at random.

4. For each route in the API add logging of when the request began and when it ended.
5. Describe any changes you would make to this code to make it better. Update the README
   below this step with your description of changes.